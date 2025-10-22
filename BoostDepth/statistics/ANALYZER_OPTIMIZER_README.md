# Boost Dependency Analyzer & Merge Optimizer

Two powerful tools for analyzing and optimizing Boost library dependencies.

## Table of Contents
- [Overview](#overview)
- [Boost Dependency Analyzer](#boost-dependency-analyzer)
- [Merge Optimizer](#merge-optimizer)
- [Quick Start](#quick-start)
- [Detailed Usage](#detailed-usage)
- [Output Files](#output-files)

---

## Overview

These tools help analyze Boost module dependencies and identify optimal merge candidates to reduce dependency complexity.

### Boost Dependency Analyzer
Analyzes module and header dependencies from CSV data, providing:
- Module-to-module relation mapping
- Header-to-header relation mapping
- Direct and transitive dependency counting
- Comprehensive statistics reports

### Merge Optimizer
Finds optimal module merge candidates by:
- Calculating merge damage scores
- Identifying shared dependencies
- Computing edge reduction potential
- Generating detailed recommendations

---

## Boost Dependency Analyzer

### Purpose
Analyzes `boost_modules_dependencies.csv` to create relation mappings and statistics for both module-to-module and header-to-header dependencies.

### Key Features

#### 1. Relation Types
- **Primary (1)**: Module A depends on Module B
- **Reverse (-1)**: Module B depends on Module A
- **Both (0)**: Bidirectional dependency

#### 2. Data Structures
```python
# Module relations
module_relation[Module_A][Module_B] = 1 | -1 | 0

# Header relations  
header_relation[Header_from_Module_B][Header_from_Module_A] = 1 | -1 | 0
```

#### 3. Dependency Counts
- **Level 1**: Direct dependencies only
- **Total**: Includes all transitive dependencies (calculated via BFS)

### Running the Analyzer

#### Basic Usage
```bash
python statistics/boost_dependency_analyzer.py
```

This will:
1. Load and process the CSV file
2. Display module and header statistics
3. Show example queries
4. Generate detailed analysis
5. Create `boost_dependency_report.md`

#### Programmatic Usage
```python
from statistics.boost_dependency_analyzer import BoostDependencyAnalyzer

# Initialize and load data
analyzer = BoostDependencyAnalyzer()
analyzer.read_csv()

# Query module relations
relation = analyzer.get_module_relation("module_a", "module_b")
deps = analyzer.get_module_dependencies("module_name")

# Get statistics
module_counts = analyzer.count_negative_relations_by_module()
header_counts = analyzer.count_negative_relations_by_header()

# Generate report
from statistics.boost_dependency_analyzer import generate_statistics_report
generate_statistics_report(analyzer, "my_report.md")
```

### API Reference

#### Class: BoostDependencyAnalyzer

**Constructor**
```python
BoostDependencyAnalyzer(csv_file_path: str = None)
```

**Methods**

| Method | Description | Returns |
|--------|-------------|---------|
| `read_csv()` | Read and process CSV file | None |
| `get_module_relation(module_a, module_b)` | Get relation between two modules | 1, -1, 0, or None |
| `get_header_relation(header_b, header_a)` | Get relation between two headers | 1, -1, 0, or None |
| `get_module_dependencies(module_name)` | Get all dependencies for a module | Dict[str, int] |
| `get_header_dependencies(header_name)` | Get all header dependencies | Dict[str, int] |
| `get_all_modules()` | Get list of all modules | List[str] |
| `get_all_headers()` | Get list of all headers | List[str] |
| `count_negative_relations_by_module()` | Count Primary/Reverse relations for modules | Dict[str, Dict[str, int]] |
| `count_negative_relations_by_header()` | Count Primary/Reverse relations for headers | Dict[str, Dict[str, int]] |
| `print_module_statistics()` | Print module relation statistics | None |
| `print_header_statistics()` | Print header relation statistics | None |

### Generated Report (`boost_dependency_report.md`)

The statistics report includes:

1. **Overall Statistics**
   - Total modules and relations
   - Relation type breakdown (Primary, Reverse, Both)

2. **Top 20 Modules by Primary Dependencies**
   - Modules that depend on the most other modules

3. **Top 20 Modules by Reverse Dependencies**
   - Most depended-upon modules

4. **Top 20 Headers by Primary Dependencies**
   - Headers with most dependencies

5. **Top 20 Headers by Reverse Dependencies**
   - Most used headers

6. **Dependency Distribution**
   - Histogram of Primary dependencies
   - Histogram of Reverse dependencies

---

## Merge Optimizer

### Purpose
Identifies optimal module merge candidates by calculating merge damage and analyzing shared dependencies.

### Key Concepts

#### Merge Damage
A score indicating how well modules fit together for merging:
- **Lower damage** = Better merge candidate (more shared dependencies)
- **Higher damage** = Worse merge candidate (less overlap)

**Formula:**
```
Primary Damage = unshared_primary / (shared_primary + 1)
Reverse Damage = unshared_reverse / (shared_reverse + 1)
Total Damage = Primary Damage + Reverse Damage
```

#### Edge Reduction
When modules are merged, redundant edges are eliminated:
- **Original edges**: Sum of edges from all modules
- **Internal edges**: Edges between modules in the merge group (removed)
- **Merged edges**: Unique edges after merge
- **Edge reduction**: Original - Merged

### Running the Merge Optimizer

#### Basic Usage
```bash
python statistics/merge_optimizer.py
```

#### With Options
```bash
# Merge 2 modules at a time, show top 5
python statistics/merge_optimizer.py --merge-count 2 --top-n 5

# Custom CSV file
python statistics/merge_optimizer.py --csv path/to/file.csv

# Custom output file
python statistics/merge_optimizer.py --output my_merge_results.md

# Skip header analysis (faster)
python statistics/merge_optimizer.py --skip-headers
```

#### All Options
```bash
python statistics/merge_optimizer.py \
  --csv custom_data.csv \
  --merge-count 3 \
  --top-n 10 \
  --output merge_recommendations.md \
  --skip-headers
```

### Command-Line Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--csv` | string | parent dir | Path to CSV file |
| `--merge-count` | int | 3 | Number of modules to merge together |
| `--top-n` | int | 10 | Number of recommendations to display |
| `--output` | string | module_merge_recommendations.md | Output markdown file |
| `--skip-headers` | flag | true | Skip header merge analysis |

### Programmatic Usage

```python
from statistics.boost_dependency_analyzer import BoostDependencyAnalyzer
from statistics.merge_optimizer import MergeOptimizer

# Load dependency data
analyzer = BoostDependencyAnalyzer()
analyzer.read_csv()

# Calculate relation counts
module_counts = analyzer.count_negative_relations_by_module()
header_counts = analyzer.count_negative_relations_by_header()

# Create optimizer
optimizer = MergeOptimizer(
    module_relation=analyzer.module_relation,
    header_relation=analyzer.header_relation,
    module_relation_count=module_counts,
    header_relation_count=header_counts,
    merge_count=3
)

# Get best merge candidates
best_merges = optimizer.get_best_module_merges(10)

# Print recommendations
optimizer.print_module_merge_recommendations(10)

# Export to markdown
optimizer.export_module_merge_to_markdown("output.md", 10)
```

### Console Output Format

```
Rank 1: module_a + module_b
  Edges: 100 → 75 (saved 25, 25.0%)
  Shared: Primary=15, Reverse=40

Rank 2: module_c + module_d
  Edges: 80 → 62 (saved 18, 22.5%)
  Shared: Primary=10, Reverse=35
```

### Generated Report (`module_merge_recommendations.md`)

The markdown report includes for each merge recommendation:

1. **Overall Impact Summary**
   - Total edge reduction across all merges
   - Percentage of edges saved
   - Number of modules merged

2. **For Each Merge:**
   - **Edge Count Impact**: Original, internal, merged, and reduction
   - **Individual Module Details**: Edges and relation counts
   - **Merge Metrics**: Shared dependencies, unique dependencies, redundancy saved
   - **Total Merge Damage**: The optimization score
   - **Summary**: Combined module characteristics

---

## Quick Start

### 1. Analyze Dependencies
```bash
cd BoostDepth
python statistics/boost_dependency_analyzer.py
```
**Output**: Console statistics + `boost_dependency_report.md`

### 2. Find Merge Candidates
```bash
python statistics/merge_optimizer.py --merge-count 2 --top-n 5
```
**Output**: Console summary + `module_merge_recommendations.md`

### 3. Review Results
- Check `boost_dependency_report.md` for overall statistics
- Check `module_merge_recommendations.md` for merge recommendations
- Use the damage scores to prioritize merges

---

## Detailed Usage

### Example Workflow

#### Step 1: Analyze Current State
```python
from statistics.boost_dependency_analyzer import BoostDependencyAnalyzer

analyzer = BoostDependencyAnalyzer()
analyzer.read_csv()

# Check specific module
deps = analyzer.get_module_dependencies("my_module")
print(f"My module has {len(deps)} dependencies")

# Find most depended-upon modules
counts = analyzer.count_negative_relations_by_module()
sorted_modules = sorted(counts.items(), 
                       key=lambda x: x[1]["Reverse_total"], 
                       reverse=True)
print("Top depended-upon modules:", sorted_modules[:5])
```

#### Step 2: Find Merge Opportunities
```python
from statistics.merge_optimizer import MergeOptimizer

optimizer = MergeOptimizer(
    module_relation=analyzer.module_relation,
    header_relation=analyzer.header_relation,
    module_relation_count=counts,
    header_relation_count=analyzer.count_negative_relations_by_header(),
    merge_count=2
)

# Get best 3-way merges
best_merges = optimizer.get_best_module_merges(10)

# Analyze first recommendation
modules, damage = best_merges[0]
print(f"Best merge: {' + '.join(modules)}")
print(f"Damage score: {damage['total_damage']:.2f}")
print(f"Shared Primary: {damage['shared_primary']}")
print(f"Shared Reverse: {damage['shared_reverse']}")
```

#### Step 3: Export for Review
```python
# Generate comprehensive reports
from statistics.boost_dependency_analyzer import generate_statistics_report

generate_statistics_report(analyzer, "analysis.md")
optimizer.export_module_merge_to_markdown("merges.md", 10)
```

### Understanding the Metrics

#### For Modules:
- **Primary_level_1**: Direct dependencies (this module depends on)
- **Primary_total**: All dependencies including transitive
- **Reverse_level_1**: Direct dependents (modules that depend on this)
- **Reverse_total**: All dependents including transitive

#### For Merges:
- **Shared Primary**: Dependencies both modules share
- **Shared Reverse**: Common modules that depend on both
- **Unique Primary**: Total distinct dependencies after merge
- **Redundant Primary**: Dependencies saved by merging
- **Edge Reduction**: Actual edges eliminated

### Interpreting Results

#### Good Merge Candidates (Low Damage):
```
Rank 1: core + type_traits
  Edges: 188 → 113 (saved 75, 39.9%)
  Shared: Primary=2, Reverse=73
  Total Damage: 1.15
```
- High shared reverse dependencies (73) - many modules depend on both
- Significant edge reduction (39.9%)
- Low damage score (1.15)

#### Poor Merge Candidates (High Damage):
```
Rank 50: random_module_a + random_module_b
  Edges: 45 → 44 (saved 1, 2.2%)
  Shared: Primary=0, Reverse=0
  Total Damage: 15.50
```
- No shared dependencies
- Minimal edge reduction
- High damage score

---

## Output Files

### `boost_dependency_report.md`
Comprehensive statistics about the current dependency structure.

**Use Case**: Understanding overall dependency patterns and identifying problematic modules.

### `module_merge_recommendations.md`
Detailed merge recommendations ranked by damage score.

**Use Case**: Planning module consolidation to reduce dependency complexity.

### Console Output
Quick summary for immediate feedback.

**Use Case**: Rapid iteration and testing different merge strategies.

---

## Tips and Best Practices

### 1. Start Small
Begin with `--merge-count 2` to understand pairwise relationships before attempting larger merges.

### 2. Focus on High-Impact Merges
Prioritize merges with:
- Low damage scores (< 2.0)
- High shared reverse dependencies
- Significant edge reduction (> 20%)

### 3. Consider Module Purpose
Damage scores are algorithmic - also consider:
- Functional cohesion
- Logical module boundaries
- Maintenance team structure

### 4. Iterative Approach
After implementing merges:
1. Re-run the analyzer
2. Update CSV with new structure
3. Find next merge opportunities
4. Repeat

### 5. Use Reports for Decision Making
- Share `boost_dependency_report.md` with team
- Discuss `module_merge_recommendations.md` in planning
- Track edge reduction over time

---

## Troubleshooting

### CSV File Not Found
Ensure `boost_modules_dependencies.csv` exists in parent directory or specify path:
```bash
python statistics/boost_dependency_analyzer.py
# OR
python statistics/merge_optimizer.py --csv path/to/file.csv
```

### Performance Issues
For large datasets with header analysis:
```bash
python statistics/merge_optimizer.py --skip-headers
```

### Understanding Output
- Low damage = Good merge candidate
- High edge reduction % = Significant benefit
- High shared dependencies = Strong relationship

---

## License

Part of the BoostDepth project.

