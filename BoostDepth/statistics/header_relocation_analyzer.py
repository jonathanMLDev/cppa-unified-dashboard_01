"""
Header Relocation Analyzer

Suggests optimal module relocations for headers based on their connection patterns.
Uses HeaderModuleAnalyzer to determine if headers should be moved to different modules.
"""

from typing import Dict, List
from collections import defaultdict
from pathlib import Path
import csv

from boost_dependency_analyzer import BoostDependencyAnalyzer
from header_module_analyzer import HeaderModuleAnalyzer


class HeaderRelocationAnalyzer:
    """
    Analyzes headers and suggests relocations to different modules based on
    connection patterns.
    
    A header should be moved if it has significantly more connections to
    another module than to its current module.
    """
    
    def __init__(self, module_analyzer: HeaderModuleAnalyzer):
        """
        Initialize with a HeaderModuleAnalyzer instance.
        
        Args:
            module_analyzer: HeaderModuleAnalyzer with completed analysis
        """
        self.module_analyzer = module_analyzer
        self.relocation_recommendations: List[Dict] = []
        
        # Get conflict and non-existent header info from the underlying analyzer
        self.analyzer = module_analyzer.analyzer
        self.conflict_headers = self._identify_conflict_headers()
        self.no_exist_headers = getattr(self.analyzer, 'no_exist_header_include', {})
    
    def _identify_conflict_headers(self) -> Dict[str, List[str]]:
        """
        Identify headers with bidirectional dependencies (conflicts).
        
        Returns:
            Dictionary mapping headers to list of conflicting headers
        """
        conflicts = {}
        
        if not hasattr(self.analyzer, 'header_deps'):
            return conflicts
        
        for header, deps in self.analyzer.header_deps.items():
            conflict_list = []
            for dep_header, relation in deps.items():
                if relation == 0:  # Bidirectional dependency = conflict
                    conflict_list.append(dep_header)
            
            if conflict_list:
                conflicts[header] = conflict_list
        
        return conflicts
        
    def analyze_relocations(self, 
                          min_external_ratio: float = 0.6,
                          min_total_connections: int = 5,
                          min_improvement_ratio: float = 1.5) -> List[Dict]:
        """
        Analyze headers and suggest relocations.
        
        Args:
            min_external_ratio: Minimum external ratio to consider (0-1)
            min_total_connections: Minimum total connections to analyze
            min_improvement_ratio: Minimum ratio of (target_module_connections / current_module_connections)
                                  to suggest relocation
        
        Returns:
            List of relocation recommendations sorted by priority
        """
        print("Analyzing relocations with criteria:")
        print(f"  - Min external ratio: {min_external_ratio:.0%}")
        print(f"  - Min total connections: {min_total_connections}")
        print(f"  - Min improvement ratio: {min_improvement_ratio}x")
        print()
        
        recommendations = []
        
        for header, analysis in self.module_analyzer.header_analysis.items():
            # Skip if doesn't meet basic criteria
            if analysis['total_count'] < min_total_connections:
                continue
            
            if analysis['external_ratio'] < min_external_ratio:
                continue
            
            # Count connections to each external module
            external_module_counts = defaultdict(int)
            for _, _, target_module in analysis['external_deps']:
                external_module_counts[target_module] += 1
            
            # Find module with most connections
            if not external_module_counts:
                continue
            
            best_target_module = max(external_module_counts.items(), 
                                    key=lambda x: x[1])
            target_module_name = best_target_module[0]
            target_module_count = best_target_module[1]
            
            current_module = analysis['module']
            current_internal_count = analysis['internal_count']
            
            # Skip if target is same as current
            if target_module_name == current_module:
                continue
            
            # Calculate improvement
            # If current_internal_count is 0, any external connections are worth considering
            if current_internal_count == 0:
                improvement_ratio = float('inf') if target_module_count > 0 else 0
            else:
                improvement_ratio = target_module_count / current_internal_count
            
            # Check if improvement is significant enough
            if improvement_ratio < min_improvement_ratio and current_internal_count > 0:
                continue
            
            # Calculate what the new ratios would be after relocation
            # After moving to target module:
            # - connections to target module become internal
            # - connections to current module become external
            new_external = analysis['total_count'] - target_module_count
            new_external_ratio = new_external / analysis['total_count'] if analysis['total_count'] > 0 else 0
            
            # Skip headers with conflicts or non-existent references
            # These will be shown separately as notices, not recommendations
            if header in self.conflict_headers or header in self.no_exist_headers:
                continue
            
            # Calculate benefit score
            benefit_score = (
                (improvement_ratio if improvement_ratio != float('inf') else 100) * 2.0 +
                (analysis['external_ratio'] - new_external_ratio) * 100 +
                target_module_count / analysis['total_count'] * 50
            )
            
            recommendation = {
                'header': header,
                'current_module': current_module,
                'target_module': target_module_name,
                'current_internal': current_internal_count,
                'current_external': analysis['external_count'],
                'target_module_connections': target_module_count,
                'improvement_ratio': improvement_ratio,
                'current_external_ratio': analysis['external_ratio'],
                'new_external_ratio': new_external_ratio,
                'external_ratio_improvement': analysis['external_ratio'] - new_external_ratio,
                'total_connections': analysis['total_count'],
                'benefit_score': benefit_score,
                'other_external_modules': {
                    mod: count for mod, count in external_module_counts.items()
                    if mod != target_module_name
                }
            }
            
            recommendations.append(recommendation)
        
        # Sort by benefit score
        recommendations.sort(key=lambda x: x['benefit_score'], reverse=True)
        
        self.relocation_recommendations = recommendations
        
        print(f"Found {len(recommendations)} relocation candidates")
        
        return recommendations
    
    def print_recommendations(self, top_n: int = 20) -> None:
        """
        Print relocation recommendations.
        
        Args:
            top_n: Number of top recommendations to display
        """
        if not self.relocation_recommendations:
            print("No recommendations yet. Run analyze_relocations() first.")
            return
        
        print("\n" + "=" * 80)
        print(f"TOP {min(top_n, len(self.relocation_recommendations))} RELOCATION RECOMMENDATIONS")
        print("=" * 80)
        
        for i, rec in enumerate(self.relocation_recommendations[:top_n], 1):
            print(f"\n{i}. {rec['header']}")
            print("   " + "─" * 76)
            print(f"   Current module: {rec['current_module']}")
            print(f"   Target module:  {rec['target_module']}")
            print()
            print(f"   Current: {rec['current_internal']} internal, {rec['current_external']} external "
                  f"({rec['current_external_ratio']:.1%} external)")
            print(f"   After move: {rec['target_module_connections']} internal, "
                  f"{rec['total_connections'] - rec['target_module_connections']} external "
                  f"({rec['new_external_ratio']:.1%} external)")
            print()
            print(f"   Improvement: {rec['external_ratio_improvement']:.1%} reduction in external ratio")
            
            if rec['improvement_ratio'] == float('inf'):
                print("   Impact: Currently has NO internal connections!")
            else:
                print(f"   Impact: {rec['improvement_ratio']:.1f}x more connections to target module")
            
            print(f"   Benefit score: {rec['benefit_score']:.1f}")
            
            # Show other significant external connections
            if rec['other_external_modules']:
                top_others = sorted(rec['other_external_modules'].items(), 
                                  key=lambda x: x[1], reverse=True)[:3]
                if top_others:
                    print(f"   Other external: {', '.join(f'{m}({c})' for m, c in top_others)}")
        
        print("\n" + "=" * 80)
    
    def get_relocations_by_module(self, module_name: str) -> List[Dict]:
        """
        Get relocation recommendations for headers currently in a specific module.
        
        Args:
            module_name: Name of the module
            
        Returns:
            List of recommendations for headers in this module
        """
        return [rec for rec in self.relocation_recommendations 
                if rec['current_module'] == module_name]
    
    def get_relocations_to_module(self, module_name: str) -> List[Dict]:
        """
        Get relocation recommendations for headers that should move TO a specific module.
        
        Args:
            module_name: Name of the target module
            
        Returns:
            List of recommendations targeting this module
        """
        return [rec for rec in self.relocation_recommendations 
                if rec['target_module'] == module_name]
    
    def export_to_csv(self, output_file: str = "header_relocation_recommendations.csv") -> str:
        """
        Export relocation recommendations to CSV.
        
        Args:
            output_file: Path to output CSV file
            
        Returns:
            Path to generated file
        """
        if not self.relocation_recommendations:
            print("No recommendations to export. Run analyze_relocations() first.")
            return None
        
        output_path = Path(output_file)
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write header
            writer.writerow([
                'Rank',
                'Header',
                'Current_Module',
                'Target_Module',
                'Current_Internal',
                'Current_External',
                'Target_Module_Connections',
                'Improvement_Ratio',
                'Current_External_Ratio',
                'New_External_Ratio',
                'External_Ratio_Improvement',
                'Benefit_Score'
            ])
            
            # Write data
            for i, rec in enumerate(self.relocation_recommendations, 1):
                improvement_str = 'inf' if rec['improvement_ratio'] == float('inf') else f"{rec['improvement_ratio']:.2f}"
                
                writer.writerow([
                    i,
                    rec['header'],
                    rec['current_module'],
                    rec['target_module'],
                    rec['current_internal'],
                    rec['current_external'],
                    rec['target_module_connections'],
                    improvement_str,
                    f"{rec['current_external_ratio']:.4f}",
                    f"{rec['new_external_ratio']:.4f}",
                    f"{rec['external_ratio_improvement']:.4f}",
                    f"{rec['benefit_score']:.2f}"
                ])
        
        print(f"Recommendations exported to: {output_path.absolute()}")
        return str(output_path.absolute())
    
    def generate_report(self, output_file: str = "header_relocation_report.md") -> str:
        """
        Generate a comprehensive markdown report.
        
        Args:
            output_file: Path to output markdown file
            
        Returns:
            Path to generated file
        """
        if not self.relocation_recommendations:
            print("No recommendations to report. Run analyze_relocations() first.")
            return None
        
        from datetime import datetime
        
        output_path = Path(output_file)
        
        content = []
        content.append("# Header Relocation Recommendations Report\n\n")
        content.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Summary statistics
        total_recs = len(self.relocation_recommendations)
        
        # Count by current module
        by_current_module = defaultdict(int)
        for rec in self.relocation_recommendations:
            by_current_module[rec['current_module']] += 1
        
        # Count by target module
        by_target_module = defaultdict(int)
        for rec in self.relocation_recommendations:
            by_target_module[rec['target_module']] += 1
        
        # ============================================================================
        # SHOW NOTICES AT THE TOP - Pull directly from BoostDependencyAnalyzer
        # These are NOT recommendations, just notices about problematic headers
        # ============================================================================
        if self.conflict_headers or self.no_exist_headers:
            content.append("## ⚠️ NOTICE: Dependency Issues Detected\n\n")
            content.append("**The following headers have dependency issues. These are NOT included in relocation recommendations.**\n\n")
            
            if self.conflict_headers:
                content.append(f"### 🔄 Bidirectional Dependencies (Circular): {len(self.conflict_headers)} Headers\n\n")
                content.append("**Impact**: These headers have mutual dependencies that create circular references.\n\n")
                
                content.append("**Headers with Bidirectional Dependencies:**\n\n")
                
                # Sort alphabetically for consistent output
                sorted_conflict_headers = sorted(self.conflict_headers.items())
                
                for i, (header, conflicts) in enumerate(sorted_conflict_headers, 1):
                    # Get module name from header
                    module = self.module_analyzer.header_to_module.get(header, 'unknown')
                    content.append(f"{i}. **`{header}`** (Module: `{module}`)\n")
                    content.append(f"   - **Circular dependencies with:** {len(conflicts)} header(s)\n")
                    
                    # Show all conflicts for this header
                    for conflict in conflicts:
                        content.append(f"     - `{conflict}`\n")
                    content.append("\n")
                
                content.append("**Recommendation:**\n")
                content.append("- These headers should NOT be relocated individually\n")
                content.append("- Move both headers in a circular pair together, or\n")
                content.append("- Refactor to break circular dependencies before relocation\n")
                content.append("- ⚠️ Similar to MTL library: mutual dependencies require coordinated reorganization\n\n")
            
            if self.no_exist_headers:
                content.append(f"### ❌ Non-Existent Header References: {len(self.no_exist_headers)} Headers\n\n")
                content.append("**Impact**: These headers reference files that don't exist in the codebase.\n\n")
                
                content.append("**Headers Referencing Non-Existent Files:**\n\n")
                
                # Sort alphabetically
                sorted_nonexistent = sorted(self.no_exist_headers.items())
                
                for i, (header, nonexistent) in enumerate(sorted_nonexistent, 1):
                    # Get module name from header
                    module = self.module_analyzer.header_to_module.get(header, 'unknown')
                    content.append(f"{i}. **`{header}`** (Module: `{module}`)\n")
                    content.append(f"   - **References non-existent:** `{nonexistent}`\n")
                    content.append("\n")
                
                content.append("**Possible Causes:**\n")
                content.append("- 📚 **Removed libraries**: References to libraries removed from Boost (e.g., MTL removed 2013-2017)\n")
                content.append("- 🖥️ **Platform-specific**: Conditional includes for platforms not in current build\n")
                content.append("- 📦 **External dependencies**: Headers from libraries outside Boost\n")
                content.append("- ✏️ **Typos or outdated paths**: Incorrect paths or renamed headers\n\n")
                
                content.append("**Recommendation:**\n")
                content.append("- Review and clean up obsolete #include statements\n")
                content.append("- Update paths to renamed or moved headers\n")
                content.append("- Verify platform-specific or conditional includes\n")
                content.append("- Document external dependencies\n\n")
            
            content.append("---\n\n")
        
        content.append("## Summary Statistics\n\n")
        content.append("| Metric | Value |\n")
        content.append("|--------|-------|\n")
        content.append(f"| Total Relocation Recommendations | {total_recs} |\n")
        content.append(f"| Modules Affected (losing headers) | {len(by_current_module)} |\n")
        content.append(f"| Modules Affected (gaining headers) | {len(by_target_module)} |\n")
        content.append(f"| Headers with Bidirectional Dependencies (Notice Only) | {len(self.conflict_headers)} |\n")
        content.append(f"| Headers Referencing Non-Existent Headers (Notice Only) | {len(self.no_exist_headers)} |\n\n")
        
        # Top relocations
        content.append("## Top 50 Relocation Recommendations\n\n")
        content.append("| Rank | Header | From Module | To Module | Current Int | Current Ext | Target Connections | Improvement | Benefit Score |\n")
        content.append("|------|--------|-------------|-----------|-------------|-------------|-------------------|-------------|---------------|\n")
        
        for i, rec in enumerate(self.relocation_recommendations[:50], 1):
            improvement_str = '∞' if rec['improvement_ratio'] == float('inf') else f"{rec['improvement_ratio']:.1f}x"
            content.append(f"| {i} | `{rec['header']}` | {rec['current_module']} | {rec['target_module']} | "
                          f"{rec['current_internal']} | {rec['current_external']} | {rec['target_module_connections']} | "
                          f"{improvement_str} | {rec['benefit_score']:.1f} |\n")
        
        content.append("\n")
        
        # Modules losing most headers
        content.append("## Modules Losing Most Headers\n\n")
        content.append("| Rank | Module | Headers to Relocate |\n")
        content.append("|------|--------|--------------------|\n")
        
        sorted_losers = sorted(by_current_module.items(), key=lambda x: x[1], reverse=True)
        for i, (module, count) in enumerate(sorted_losers[:20], 1):
            content.append(f"| {i} | {module} | {count} |\n")
        
        content.append("\n")
        
        # Modules gaining most headers
        content.append("## Modules Gaining Most Headers\n\n")
        content.append("| Rank | Module | Headers to Receive |\n")
        content.append("|------|--------|--------------------|\n")
        
        sorted_gainers = sorted(by_target_module.items(), key=lambda x: x[1], reverse=True)
        for i, (module, count) in enumerate(sorted_gainers[:20], 1):
            content.append(f"| {i} | {module} | {count} |\n")
        
        content.append("\n")
        
        # Detailed recommendations by module (warnings already shown at top)
        content.append("## Detailed Recommendations by Source Module\n\n")
        
        for module, count in sorted_losers[:10]:
            module_recs = self.get_relocations_by_module(module)
            
            content.append(f"### Module: {module} ({count} headers to relocate)\n\n")
            content.append("| Header | Target Module | Current Internal | Target Connections | Improvement |\n")
            content.append("|--------|---------------|------------------|-------------------|-------------|\n")
            
            for rec in module_recs[:20]:
                improvement_str = '∞' if rec['improvement_ratio'] == float('inf') else f"{rec['improvement_ratio']:.1f}x"
                content.append(f"| `{rec['header']}` | {rec['target_module']} | {rec['current_internal']} | "
                              f"{rec['target_module_connections']} | {improvement_str} |\n")
            
            content.append("\n")
        
        # Write to file
        output_path.write_text(''.join(content), encoding='utf-8')
        print(f"\nReport generated: {output_path.absolute()}")
        
        return str(output_path.absolute())
    
    def print_module_impact(self, top_n: int = 20) -> None:
        """
        Print impact summary by module.
        
        Args:
            top_n: Number of top modules to display
        """
        if not self.relocation_recommendations:
            print("No recommendations yet. Run analyze_relocations() first.")
            return
        
        # Count by current and target module
        by_current = defaultdict(int)
        by_target = defaultdict(int)
        
        for rec in self.relocation_recommendations:
            by_current[rec['current_module']] += 1
            by_target[rec['target_module']] += 1
        
        print("\n" + "=" * 70)
        print(f"MODULE IMPACT SUMMARY (Top {top_n})")
        print("=" * 70)
        
        print("\nModules Losing Headers:")
        print(f"{'Module':<25} {'Headers to Relocate':<20}")
        print("-" * 50)
        
        sorted_losers = sorted(by_current.items(), key=lambda x: x[1], reverse=True)
        for module, count in sorted_losers[:top_n]:
            print(f"{module:<25} {count:<20}")
        
        print("\nModules Gaining Headers:")
        print(f"{'Module':<25} {'Headers to Receive':<20}")
        print("-" * 50)
        
        sorted_gainers = sorted(by_target.items(), key=lambda x: x[1], reverse=True)
        for module, count in sorted_gainers[:top_n]:
            print(f"{module:<25} {count:<20}")
        
        print("=" * 70 + "\n")


def main():
    """
    Main function demonstrating the HeaderRelocationAnalyzer usage.
    """
    import sys
    # Set UTF-8 encoding for console output (Windows compatibility)
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("=" * 70)
    print("HEADER RELOCATION ANALYSIS")
    print("=" * 70)
    print()
    
    # Step 1: Load dependency data
    print("Step 1: Loading header dependencies...")
    analyzer = BoostDependencyAnalyzer()
    analyzer.read_csv()
    
    # Step 2: Analyze module boundaries
    print("\nStep 2: Analyzing module boundaries...")
    module_analyzer = HeaderModuleAnalyzer(analyzer)
    module_analyzer.build_module_mapping()
    module_analyzer.analyze_header_connections()
    
    # Step 3: Create relocation analyzer
    print("\nStep 3: Analyzing relocations...")
    relocation_analyzer = HeaderRelocationAnalyzer(module_analyzer)
    
    # Step 4: Analyze with different criteria
    relocation_analyzer.analyze_relocations(
        min_external_ratio=0.6,
        min_total_connections=5,
        min_improvement_ratio=2.0
    )
    
    # Step 5: Print results
    print("\nStep 4: Generating recommendations...")
    
    # Print conflict and non-existent header summary from BoostDependencyAnalyzer data
    total_conflicts = len(relocation_analyzer.conflict_headers)
    total_nonexistent = len(relocation_analyzer.no_exist_headers)
    
    if total_conflicts > 0 or total_nonexistent > 0:
        print("\n" + "=" * 70)
        print("⚠️  DEPENDENCY ISSUES DETECTED (Not included in recommendations)")
        print("=" * 70)
        if total_conflicts > 0:
            print(f"\n{total_conflicts} headers have bidirectional dependencies (mutual calls)")
            print("  → These are excluded from relocation recommendations")
            print("  → Fix circular dependencies before considering relocation")
        
        if total_nonexistent > 0:
            print(f"\n{total_nonexistent} headers reference non-existent headers")
            print("  → These are excluded from relocation recommendations")
            print("  → May include removed libraries (e.g., MTL)")
        
        print("=" * 70)
    
    relocation_analyzer.print_recommendations(30)
    relocation_analyzer.print_module_impact(20)
    
    # Step 6: Export results
    print("\nStep 5: Exporting results...")
    relocation_analyzer.export_to_csv("header_relocation_recommendations.csv")
    relocation_analyzer.generate_report("header_relocation_report.md")
    
    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()

