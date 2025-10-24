"""
Header Module Analyzer

This module analyzes header dependencies by module boundaries.
For each header, it calculates:
- Count of connections within the same module (internal)
- Count of connections outside the module (external)
"""

from typing import Dict, List, Tuple
from collections import defaultdict
from pathlib import Path
import csv

from boost_dependency_analyzer import BoostDependencyAnalyzer


class HeaderModuleAnalyzer:
    """
    Analyzes header dependencies across module boundaries.
    
    For each header, tracks:
    - Internal connections: dependencies within the same module
    - External connections: dependencies to other modules
    """
    
    def __init__(self, analyzer: BoostDependencyAnalyzer):
        """
        Initialize the analyzer with a BoostDependencyAnalyzer instance.
        
        Args:
            analyzer: BoostDependencyAnalyzer with loaded header dependency data
        """
        self.analyzer = analyzer
        
        # header -> module name mapping
        self.header_to_module: Dict[str, str] = {}
        
        # header -> {internal_count, external_count, internal_deps, external_deps}
        self.header_analysis: Dict[str, Dict] = {}
        
        # module -> list of headers
        self.module_to_headers: Dict[str, List[str]] = defaultdict(list)
        
    def extract_module_name(self, header_path: str) -> str:
        """
        Extract module name from header path.
        
        Rules:
        - "boost/asio/detail/pop_options.hpp" -> "asio"
        - "boost/asio.hpp" -> "asio"
        - "boost/config.hpp" -> "config"
        
        Args:
            header_path: Full header path
            
        Returns:
            Module name (first directory after "boost/")
        """
        # Normalize path separators
        header_path = header_path.replace('\\', '/')
        
        # Split by '/'
        parts = header_path.split('/')
        
        # Find 'boost' and get the next part
        if len(parts) >= 2 and parts[0] == 'boost':
            module_part = parts[1]
            # Remove file extension if this is a header file (e.g., "asio.hpp" -> "asio")
            if '.' in module_part:
                module_part = module_part.split('.')[0]
            return module_part
        
        # Fallback: return the path as-is if format is unexpected
        return header_path
    
    def build_module_mapping(self) -> None:
        """
        Build mapping of headers to modules.
        """
        print("Building header-to-module mapping...")
        
        if not hasattr(self.analyzer, 'header_deps') or not self.analyzer.header_deps:
            raise ValueError("Analyzer does not have header_deps. Run read_csv() first.")
        
        # Map each header to its module
        for header in self.analyzer.header_deps.keys():
            module = self.extract_module_name(header)
            self.header_to_module[header] = module
            self.module_to_headers[module].append(header)
        
        # Also map headers that appear only as dependencies
        for header, deps in self.analyzer.header_deps.items():
            for dep_header in deps.keys():
                if dep_header not in self.header_to_module:
                    module = self.extract_module_name(dep_header)
                    self.header_to_module[dep_header] = module
                    self.module_to_headers[module].append(dep_header)
        
        print(f"Mapped {len(self.header_to_module)} headers to {len(self.module_to_headers)} modules")
    
    def analyze_header_connections(self) -> None:
        """
        Analyze each header's internal vs external connections.
        
        For each header, counts:
        - Internal connections: dependencies within the same module
        - External connections: dependencies to other modules
        """
        print("Analyzing header connections by module...")
        
        if not self.header_to_module:
            self.build_module_mapping()
        
        for header, deps in self.analyzer.header_deps.items():
            header_module = self.header_to_module.get(header, "unknown")
            
            internal_deps = []
            external_deps = []
            for dep_header, relation in deps.items():
                dep_module = self.header_to_module.get(dep_header, "unknown")
                
                if dep_module == header_module:
                    internal_deps.append((dep_header, relation))
                else:
                    external_deps.append((dep_header, relation, dep_module))
            
            total_count = len(internal_deps) + len(external_deps)
            ext_radio = len(external_deps) / total_count if total_count > 0 else 0
            level = "header"
            
            if header == 'boost/' + header_module + '.hpp':
                level = "module"
                ext_radio = 0
            
            self.header_analysis[header] = {
                'module': header_module,
                'internal_count': len(internal_deps),
                'external_count': len(external_deps),
                'total_count': len(internal_deps) + len(external_deps),
                'internal_deps': internal_deps,
                'external_deps': external_deps,
                'level': level,
                'external_ratio': ext_radio

            }
        
        print(f"Analyzed {len(self.header_analysis)} headers")
    
    def get_header_analysis(self, header: str) -> Dict:
        """
        Get analysis results for a specific header.
        
        Args:
            header: Header file path
            
        Returns:
            Dictionary with internal/external connection counts and details
        """
        return self.header_analysis.get(header, None)
    
    def find_headers_with_high_external_ratio(self, min_ratio: float = 0.5, 
                                              min_total: int = 3) -> List[Tuple[str, Dict]]:
        """
        Find headers with high external dependency ratio.
        
        Args:
            min_ratio: Minimum ratio of external to total connections (0-1)
            min_total: Minimum total connections to consider
            
        Returns:
            List of (header, analysis) tuples sorted by external ratio
        """
        results = []
        
        for header, analysis in self.header_analysis.items():
            if analysis['total_count'] >= min_total and analysis['external_ratio'] >= min_ratio:
                results.append((header, analysis))
        
        # Sort by external ratio descending
        results.sort(key=lambda x: x[1]['external_ratio'], reverse=True)
        
        return results
    
    def find_headers_with_most_external_connections(self, top_n: int = 20) -> List[Tuple[str, Dict]]:
        """
        Find headers with the most external connections.
        
        Args:
            top_n: Number of top headers to return
            
        Returns:
            List of (header, analysis) tuples sorted by external count
        """
        results = [(header, analysis) for header, analysis in self.header_analysis.items()]
        results.sort(key=lambda x: x[1]['external_count'], reverse=True)
        
        return results[:top_n]
    
    def get_module_summary(self, module_name: str) -> Dict:
        """
        Get summary statistics for a module.
        
        Args:
            module_name: Name of the module
            
        Returns:
            Dictionary with module-level statistics
        """
        headers = self.module_to_headers.get(module_name, [])
        
        if not headers:
            return None
        
        total_internal = 0
        total_external = 0
        headers_analyzed = []
        
        for header in headers:
            if header in self.header_analysis:
                analysis = self.header_analysis[header]
                total_internal += analysis['internal_count']
                total_external += analysis['external_count']
                headers_analyzed.append(header)
        
        total_connections = total_internal + total_external
        
        return {
            'module': module_name,
            'header_count': len(headers_analyzed),
            'total_internal': total_internal,
            'total_external': total_external,
            'total_connections': total_connections,
            'external_ratio': total_external / total_connections if total_connections > 0 else 0,
            'avg_internal_per_header': total_internal / len(headers_analyzed) if headers_analyzed else 0,
            'avg_external_per_header': total_external / len(headers_analyzed) if headers_analyzed else 0
        }
    
    def get_all_modules_summary(self) -> List[Dict]:
        """
        Get summary statistics for all modules.
        
        Returns:
            List of module summaries sorted by external ratio
        """
        summaries = []
        
        for module_name in self.module_to_headers.keys():
            summary = self.get_module_summary(module_name)
            if summary and summary['total_connections'] > 0:
                summaries.append(summary)
        
        # Sort by external ratio descending
        summaries.sort(key=lambda x: x['external_ratio'], reverse=True)
        
        return summaries
    
    def print_header_analysis(self, header: str) -> None:
        """
        Print detailed analysis for a specific header.
        
        Args:
            header: Header file path
        """
        analysis = self.get_header_analysis(header)
        
        if not analysis:
            print(f"No analysis found for header: {header}")
            return
        
        print(f"\n{'=' * 70}")
        print(f"HEADER ANALYSIS: {header}")
        print(f"{'=' * 70}")
        print(f"Module: {analysis['module']}")
        print(f"Internal connections: {analysis['internal_count']}")
        print(f"External connections: {analysis['external_count']}")
        print(f"Total connections: {analysis['total_count']}")
        print(f"External ratio: {analysis['external_ratio']:.2%}")
        
        if analysis['internal_deps']:
            print(f"\nInternal dependencies ({len(analysis['internal_deps'])}):")
            for dep_header, relation in sorted(analysis['internal_deps'])[:10]:
                rel_str = "→" if relation == 1 else "←" if relation == -1 else "↔"
                print(f"  {rel_str} {dep_header}")
            if len(analysis['internal_deps']) > 10:
                print(f"  ... and {len(analysis['internal_deps']) - 10} more")
        
        if analysis['external_deps']:
            print(f"\nExternal dependencies ({len(analysis['external_deps'])}):")
            for dep_header, relation, dep_module in sorted(analysis['external_deps'])[:10]:
                rel_str = "→" if relation == 1 else "←" if relation == -1 else "↔"
                print(f"  {rel_str} {dep_header} (module: {dep_module})")
            if len(analysis['external_deps']) > 10:
                print(f"  ... and {len(analysis['external_deps']) - 10} more")
        
        print(f"{'=' * 70}\n")
    
    def print_top_external_headers(self, top_n: int = 20) -> None:
        """
        Print headers with most external connections.
        
        Args:
            top_n: Number of top headers to display
        """
        print(f"\n{'=' * 70}")
        print(f"TOP {top_n} HEADERS BY EXTERNAL CONNECTIONS")
        print(f"{'=' * 70}")
        
        results = self.find_headers_with_most_external_connections(top_n)
        
        print(f"\n{'Rank':<6} {'Internal':<10} {'External':<10} {'Ratio':<8} {'Header':<50}")
        print("-" * 70)
        
        for i, (header, analysis) in enumerate(results, 1):
            print(f"{i:<6} {analysis['internal_count']:<10} {analysis['external_count']:<10} "
                  f"{analysis['external_ratio']:.2%}    {header[:46]}")
        
        print(f"{'=' * 70}\n")
    
    def print_module_summaries(self, top_n: int = 20) -> None:
        """
        Print module-level summaries.
        
        Args:
            top_n: Number of top modules to display
        """
        print(f"\n{'=' * 70}")
        print(f"MODULE SUMMARIES (Top {top_n} by External Ratio)")
        print(f"{'=' * 70}")
        
        summaries = self.get_all_modules_summary()[:top_n]
        
        print(f"\n{'Module':<20} {'Headers':<10} {'Internal':<10} {'External':<10} {'Ext Ratio':<10}")
        print("-" * 70)
        
        for summary in summaries:
            print(f"{summary['module']:<20} {summary['header_count']:<10} "
                  f"{summary['total_internal']:<10} {summary['total_external']:<10} "
                  f"{summary['external_ratio']:.2%}")
        
        print(f"{'=' * 70}\n")
    
    def export_to_csv(self, output_file: str = "header_module_analysis.csv") -> str:
        """
        Export header analysis to CSV file.
        
        Args:
            output_file: Path to output CSV file
            
        Returns:
            Path to generated file
        """
        output_path = Path(output_file)
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write header
            writer.writerow([
                'Header',
                'Module',
                'Internal_Count',
                'External_Count',
                'Total_Count',
                'External_Ratio'
            ])
            
            # Write data sorted by external ratio
            sorted_headers = sorted(
                self.header_analysis.items(),
                key=lambda x: x[1]['external_ratio'],
                reverse=True
            )
            
            for header, analysis in sorted_headers:
                writer.writerow([
                    header,
                    analysis['module'],
                    analysis['internal_count'],
                    analysis['external_count'],
                    analysis['total_count'],
                    f"{analysis['external_ratio']:.4f}"
                ])
        
        print(f"Analysis exported to: {output_path.absolute()}")
        return str(output_path.absolute())
    
    def export_module_summary_to_csv(self, output_file: str = "module_summary.csv") -> str:
        """
        Export module-level summary to CSV file.
        
        Args:
            output_file: Path to output CSV file
            
        Returns:
            Path to generated file
        """
        output_path = Path(output_file)
        
        summaries = self.get_all_modules_summary()
        
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write header
            writer.writerow([
                'Module',
                'Header_Count',
                'Total_Internal',
                'Total_External',
                'Total_Connections',
                'External_Ratio',
                'Avg_Internal_Per_Header',
                'Avg_External_Per_Header'
            ])
            
            # Write data
            for summary in summaries:
                writer.writerow([
                    summary['module'],
                    summary['header_count'],
                    summary['total_internal'],
                    summary['total_external'],
                    summary['total_connections'],
                    f"{summary['external_ratio']:.4f}",
                    f"{summary['avg_internal_per_header']:.2f}",
                    f"{summary['avg_external_per_header']:.2f}"
                ])
        
        print(f"Module summary exported to: {output_path.absolute()}")
        return str(output_path.absolute())
    
    def generate_report(self, output_file: str = "header_module_report.md") -> str:
        """
        Generate a comprehensive markdown report.
        
        Args:
            output_file: Path to output markdown file
            
        Returns:
            Path to generated file
        """
        from datetime import datetime
        
        output_path = Path(output_file)
        
        content = []
        content.append("# Header Module Boundary Analysis Report\n\n")
        content.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Overall statistics
        total_headers = len(self.header_analysis)
        total_modules = len(self.module_to_headers)
        
        total_internal = sum(a['internal_count'] for a in self.header_analysis.values())
        total_external = sum(a['external_count'] for a in self.header_analysis.values())
        total_connections = total_internal + total_external
        
        content.append("## Overall Statistics\n\n")
        content.append("| Metric | Value |\n")
        content.append("|--------|-------|\n")
        content.append(f"| Total Headers Analyzed | {total_headers} |\n")
        content.append(f"| Total Modules | {total_modules} |\n")
        content.append(f"| Total Internal Connections | {total_internal} |\n")
        content.append(f"| Total External Connections | {total_external} |\n")
        content.append(f"| Total Connections | {total_connections} |\n")
        content.append(f"| Overall External Ratio | {total_external / total_connections:.2%} |\n\n")
        
        # Top headers by external connections
        content.append("## Top 30 Headers by External Connections\n\n")
        content.append("| Rank | Header | Module | Internal | External | Total | Ext Ratio |\n")
        content.append("|------|--------|--------|----------|----------|-------|----------|\n")
        
        top_headers = self.find_headers_with_most_external_connections(30)
        for i, (header, analysis) in enumerate(top_headers, 1):
            content.append(f"| {i} | `{header}` | {analysis['module']} | "
                          f"{analysis['internal_count']} | {analysis['external_count']} | "
                          f"{analysis['total_count']} | {analysis['external_ratio']:.2%} |\n")
        content.append("\n")
        
        # Headers with high external ratio
        content.append("## Headers with High External Dependency Ratio (>70%)\n\n")
        content.append("| Header | Module | Internal | External | Total | Ext Ratio |\n")
        content.append("|--------|--------|----------|----------|-------|----------|\n")
        
        high_ratio = self.find_headers_with_high_external_ratio(min_ratio=0.7, min_total=5)
        for header, analysis in high_ratio[:30]:
            content.append(f"| `{header}` | {analysis['module']} | "
                          f"{analysis['internal_count']} | {analysis['external_count']} | "
                          f"{analysis['total_count']} | {analysis['external_ratio']:.2%} |\n")
        content.append("\n")
        
        # Module summaries
        content.append("## Module Summaries (Top 30 by External Ratio)\n\n")
        content.append("| Rank | Module | Headers | Internal | External | Total | Ext Ratio |\n")
        content.append("|------|--------|---------|----------|----------|-------|----------|\n")
        
        summaries = self.get_all_modules_summary()[:30]
        for i, summary in enumerate(summaries, 1):
            content.append(f"| {i} | {summary['module']} | {summary['header_count']} | "
                          f"{summary['total_internal']} | {summary['total_external']} | "
                          f"{summary['total_connections']} | {summary['external_ratio']:.2%} |\n")
        content.append("\n")
        
        # Write to file
        output_path.write_text(''.join(content), encoding='utf-8')
        print(f"\nReport generated: {output_path.absolute()}")
        
        return str(output_path.absolute())


def main():
    """
    Main function demonstrating the HeaderModuleAnalyzer usage.
    """
    print("=" * 70)
    print("HEADER MODULE BOUNDARY ANALYSIS")
    print("=" * 70)
    print()
    
    # Step 1: Load dependency data
    print("Step 1: Loading header dependencies...")
    analyzer = BoostDependencyAnalyzer()
    analyzer.read_csv()
    
    # Step 2: Create module analyzer
    print("\nStep 2: Initializing module analyzer...")
    module_analyzer = HeaderModuleAnalyzer(analyzer)
    
    # Step 3: Build module mapping
    module_analyzer.build_module_mapping()
    
    # Step 4: Analyze connections
    print("\nStep 3: Analyzing header connections...")
    module_analyzer.analyze_header_connections()
    
    # Step 5: Print summaries
    print("\nStep 4: Generating summaries...")
    module_analyzer.print_top_external_headers(20)
    module_analyzer.print_module_summaries(20)
    
    # Step 6: Example header analysis
    print("\nStep 5: Example detailed header analysis...")
    example_headers = ['boost/asio.hpp', 'boost/config.hpp', 'boost/mpl/bool.hpp']
    for header in example_headers:
        if header in module_analyzer.header_analysis:
            module_analyzer.print_header_analysis(header)
            break
    
    # Step 7: Export results
    print("\nStep 6: Exporting results...")
    module_analyzer.export_to_csv("header_module_analysis.csv")
    module_analyzer.export_module_summary_to_csv("module_summary.csv")
    module_analyzer.generate_report("header_module_report.md")
    
    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()

