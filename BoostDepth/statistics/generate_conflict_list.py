#!/usr/bin/env python3
"""
Generate a list of all headers with bidirectional dependencies (conflicts).
"""

from boost_dependency_analyzer import BoostDependencyAnalyzer
from header_module_analyzer import HeaderModuleAnalyzer
from datetime import datetime


def generate_conflict_list():
    """Generate conflict_dependent_header_list.md"""
    
    print("Loading dependency data...")
    analyzer = BoostDependencyAnalyzer()
    analyzer.read_csv()
    
    print("Building module mapping...")
    module_analyzer = HeaderModuleAnalyzer(analyzer)
    module_analyzer.build_module_mapping()
    
    # Get conflict headers from analyzer
    conflict_headers = {}
    if hasattr(analyzer, 'header_deps'):
        for header, deps in analyzer.header_deps.items():
            conflict_list = []
            for dep_header, relation in deps.items():
                if relation == 0:  # Bidirectional dependency = conflict
                    conflict_list.append(dep_header)
            if conflict_list:
                conflict_headers[header] = conflict_list
    
    print(f"Found {len(conflict_headers)} headers with conflicts")
    
    # Generate markdown
    content = []
    content.append("# Boost Headers with Bidirectional Dependencies (Conflicts)\n\n")
    content.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    content.append("## Summary\n\n")
    content.append(f"Total headers with bidirectional dependencies: **{len(conflict_headers)}**\n\n")
    
    content.append("**What are bidirectional dependencies?**\n\n")
    content.append("Two headers have a bidirectional dependency when they include each other, ")
    content.append("creating a circular reference. For example:\n")
    content.append("- Header A includes Header B\n")
    content.append("- Header B includes Header A\n\n")
    
    content.append("**Impact:**\n")
    content.append("- These headers are tightly coupled and cannot be relocated independently\n")
    content.append("- Moving one without the other will break compilation\n")
    content.append("- Both headers in a circular pair should be moved together, or\n")
    content.append("- The circular dependency should be refactored before relocation\n\n")
    
    content.append("---\n\n")
    
    # Group by module
    content.append("## Headers by Module\n\n")
    
    # Organize by module
    by_module = {}
    for header, conflicts in conflict_headers.items():
        module = module_analyzer.header_to_module.get(header, 'unknown')
        if module not in by_module:
            by_module[module] = []
        by_module[module].append((header, conflicts))
    
    # Sort modules by number of conflict headers (descending)
    sorted_modules = sorted(by_module.items(), key=lambda x: len(x[1]), reverse=True)
    
    for module, headers in sorted_modules:
        content.append(f"### Module: `{module}`\n\n")
        content.append(f"**{len(headers)} header(s) with conflicts**\n\n")
        
        # Sort headers alphabetically
        sorted_headers = sorted(headers, key=lambda x: x[0])
        
        for header, conflicts in sorted_headers:
            content.append(f"#### `{header}`\n\n")
            content.append(f"Circular dependencies with {len(conflicts)} header(s):\n")
            for conflict in sorted(conflicts):
                content.append(f"- `{conflict}`\n")
            content.append("\n")
    
    content.append("---\n\n")
    
    # Alphabetical list
    content.append("## Complete Alphabetical List\n\n")
    
    sorted_all = sorted(conflict_headers.items(), key=lambda x: x[0])
    
    for i, (header, conflicts) in enumerate(sorted_all, 1):
        module = module_analyzer.header_to_module.get(header, 'unknown')
        content.append(f"{i}. **`{header}`** (Module: `{module}`)\n")
        content.append(f"   - Circular dependencies with {len(conflicts)} header(s):\n")
        for conflict in sorted(conflicts):
            content.append(f"     - `{conflict}`\n")
        content.append("\n")
    
    content.append("---\n\n")
    
    # Statistics by module
    content.append("## Statistics by Module\n\n")
    content.append("| Module | Headers with Conflicts |\n")
    content.append("|--------|------------------------|\n")
    
    for module, headers in sorted_modules:
        content.append(f"| {module} | {len(headers)} |\n")
    
    content.append("\n")
    content.append("---\n\n")
    
    # Self-referencing headers (potential data errors)
    content.append("## Self-Referencing Headers\n\n")
    content.append("These headers appear to reference themselves (may indicate data errors):\n\n")
    
    self_refs = []
    for header, conflicts in sorted(conflict_headers.items()):
        if header in conflicts:
            module = module_analyzer.header_to_module.get(header, 'unknown')
            self_refs.append((header, module))
    
    if self_refs:
        for i, (header, module) in enumerate(self_refs, 1):
            content.append(f"{i}. `{header}` (Module: `{module}`)\n")
    else:
        content.append("*None found*\n")
    
    content.append("\n")
    
    # Write to file
    output_path = "conflict_dependent_header_list.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(content))
    
    print(f"\nConflict list generated: {output_path}")
    print(f"Total: {len(conflict_headers)} headers with bidirectional dependencies")
    print(f"Across {len(by_module)} modules")
    print(f"Self-referencing: {len(self_refs)} headers")


if __name__ == "__main__":
    generate_conflict_list()

