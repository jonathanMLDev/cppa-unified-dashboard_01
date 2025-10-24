# Module Merge Recommendations

**Top Recommendations:** 10
**Sorting:** By Edge Reduction (highest first)
**Strategy:** Best merges across all merge counts (2-5 modules)

## Overall Impact
| Metric | Value |
|--------|-------|
| Original total edges | 2764 |
| Reduced total edges | 1999 |
| Edge reduction | 765 |
| Modules merged | 38 |

---

## Rank 1: assert + config + core + throw_exception + type_traits

**Merge Count:** 5 modules

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 491 |
| Internal edges (removed) | 7 |
| Merged edges (unique) | 135 |
| Edge reduction | 356 |

### Individual Module Details

**assert:**
- Edges from this module: 95
- Dependencies Relations: Primary = 1, All = 1
- Dependents Relations: Primary = 94, All = 129

**config:**
- Edges from this module: 137
- Dependencies Relations: Primary = 0, All = 0
- Dependents Relations: Primary = 137, All = 141

**core:**
- Edges from this module: 102
- Dependencies Relations: Primary = 4, All = 4
- Dependents Relations: Primary = 98, All = 115

**throw_exception:**
- Edges from this module: 71
- Dependencies Relations: Primary = 2, All = 2
- Dependents Relations: Primary = 69, All = 122

**type_traits:**
- Edges from this module: 86
- Dependencies Relations: Primary = 2, All = 2
- Dependents Relations: Primary = 84, All = 107

### Summary

After merge, the combined module would have:
- **135** total outgoing edges (reduced from 491)
- Redundancy saved: 5 Dependents, 343 Dependencies
- Edges saved: **356**

---

## Rank 2: iterator + mpl + preprocessor + static_assert + utility

**Merge Count:** 5 modules

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 257 |
| Internal edges (removed) | 6 |
| Merged edges (unique) | 95 |
| Edge reduction | 162 |

### Individual Module Details

**iterator:**
- Edges from this module: 47
- Dependencies Relations: Primary = 10, All = 24
- Dependents Relations: Primary = 37, All = 61

**mpl:**
- Edges from this module: 59
- Dependencies Relations: Primary = 7, All = 10
- Dependents Relations: Primary = 52, All = 76

**preprocessor:**
- Edges from this module: 47
- Dependencies Relations: Primary = 0, All = 0
- Dependents Relations: Primary = 47, All = 94

**static_assert:**
- Edges from this module: 60
- Dependencies Relations: Primary = 1, All = 1
- Dependents Relations: Primary = 59, All = 121

**utility:**
- Edges from this module: 44
- Dependencies Relations: Primary = 7, All = 8
- Dependents Relations: Primary = 37, All = 84

### Summary

After merge, the combined module would have:
- **95** total outgoing edges (reduced from 257)
- Redundancy saved: 9 Dependents, 141 Dependencies
- Edges saved: **162**

---

## Rank 3: function + optional + range + serialization + smart_ptr

**Merge Count:** 5 modules

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 170 |
| Internal edges (removed) | 4 |
| Merged edges (unique) | 78 |
| Edge reduction | 92 |

### Individual Module Details

**function:**
- Edges from this module: 27
- Dependencies Relations: Primary = 5, All = 6
- Dependents Relations: Primary = 22, All = 71

**optional:**
- Edges from this module: 30
- Dependencies Relations: Primary = 5, All = 6
- Dependents Relations: Primary = 25, All = 66

**range:**
- Edges from this module: 39
- Dependencies Relations: Primary = 17, All = 30
- Dependents Relations: Primary = 22, All = 45

**serialization:**
- Edges from this module: 34
- Dependencies Relations: Primary = 23, All = 57
- Dependents Relations: Primary = 11, All = 16

**smart_ptr:**
- Edges from this module: 40
- Dependencies Relations: Primary = 4, All = 5
- Dependents Relations: Primary = 36, All = 64

### Summary

After merge, the combined module would have:
- **78** total outgoing edges (reduced from 170)
- Redundancy saved: 25 Dependents, 59 Dependencies
- Edges saved: **92**

---

## Rank 4: algorithm + concept_check + fusion + tuple

**Merge Count:** 4 modules

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 99 |
| Internal edges (removed) | 3 |
| Merged edges (unique) | 59 |
| Edge reduction | 40 |

### Individual Module Details

**algorithm:**
- Edges from this module: 25
- Dependencies Relations: Primary = 17, All = 33
- Dependents Relations: Primary = 8, All = 36

**concept_check:**
- Edges from this module: 25
- Dependencies Relations: Primary = 4, All = 4
- Dependents Relations: Primary = 21, All = 67

**fusion:**
- Edges from this module: 28
- Dependencies Relations: Primary = 12, All = 21
- Dependents Relations: Primary = 16, All = 67

**tuple:**
- Edges from this module: 21
- Dependencies Relations: Primary = 4, All = 6
- Dependents Relations: Primary = 17, All = 71

### Summary

After merge, the combined module would have:
- **59** total outgoing edges (reduced from 99)
- Redundancy saved: 14 Dependents, 18 Dependencies
- Edges saved: **40**

---

## Rank 5: detail + integer + lexical_cast + numeric~conversion

**Merge Count:** 4 modules

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 81 |
| Internal edges (removed) | 0 |
| Merged edges (unique) | 48 |
| Edge reduction | 33 |

### Individual Module Details

**detail:**
- Edges from this module: 22
- Dependencies Relations: Primary = 5, All = 7
- Dependents Relations: Primary = 17, All = 73

**integer:**
- Edges from this module: 26
- Dependencies Relations: Primary = 6, All = 6
- Dependents Relations: Primary = 20, All = 54

**lexical_cast:**
- Edges from this module: 18
- Dependencies Relations: Primary = 4, All = 8
- Dependents Relations: Primary = 14, All = 40

**numeric~conversion:**
- Edges from this module: 15
- Dependencies Relations: Primary = 7, All = 13
- Dependents Relations: Primary = 8, All = 37

### Summary

After merge, the combined module would have:
- **48** total outgoing edges (reduced from 81)
- Redundancy saved: 12 Dependents, 21 Dependencies
- Edges saved: **33**

---

## Rank 6: filesystem + mp11 + predef + system

**Merge Count:** 4 modules

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 86 |
| Internal edges (removed) | 2 |
| Merged edges (unique) | 56 |
| Edge reduction | 30 |

### Individual Module Details

**filesystem:**
- Edges from this module: 23
- Dependencies Relations: Primary = 14, All = 32
- Dependents Relations: Primary = 9, All = 12

**mp11:**
- Edges from this module: 20
- Dependencies Relations: Primary = 0, All = 0
- Dependents Relations: Primary = 20, All = 92

**predef:**
- Edges from this module: 21
- Dependencies Relations: Primary = 0, All = 0
- Dependents Relations: Primary = 21, All = 95

**system:**
- Edges from this module: 22
- Dependencies Relations: Primary = 5, All = 7
- Dependents Relations: Primary = 17, All = 47

### Summary

After merge, the combined module would have:
- **56** total outgoing edges (reduced from 86)
- Redundancy saved: 3 Dependents, 19 Dependencies
- Edges saved: **30**

---

## Rank 7: container + intrusive + move

**Merge Count:** 3 modules

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 43 |
| Internal edges (removed) | 3 |
| Merged edges (unique) | 26 |
| Edge reduction | 17 |

### Individual Module Details

**container:**
- Edges from this module: 14
- Dependencies Relations: Primary = 4, All = 4
- Dependents Relations: Primary = 10, All = 44

**intrusive:**
- Edges from this module: 11
- Dependencies Relations: Primary = 3, All = 3
- Dependents Relations: Primary = 8, All = 47

**move:**
- Edges from this module: 18
- Dependencies Relations: Primary = 1, All = 1
- Dependents Relations: Primary = 17, All = 59

### Summary

After merge, the combined module would have:
- **26** total outgoing edges (reduced from 43)
- Redundancy saved: 4 Dependents, 9 Dependencies
- Edges saved: **17**

---

## Rank 8: function_types + parameter + typeof

**Merge Count:** 3 modules

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 52 |
| Internal edges (removed) | 0 |
| Merged edges (unique) | 35 |
| Edge reduction | 17 |

### Individual Module Details

**function_types:**
- Edges from this module: 15
- Dependencies Relations: Primary = 6, All = 12
- Dependents Relations: Primary = 9, All = 70

**parameter:**
- Edges from this module: 20
- Dependencies Relations: Primary = 10, All = 23
- Dependents Relations: Primary = 10, All = 15

**typeof:**
- Edges from this module: 17
- Dependencies Relations: Primary = 1, All = 1
- Dependents Relations: Primary = 16, All = 72

### Summary

After merge, the combined module would have:
- **35** total outgoing edges (reduced from 52)
- Redundancy saved: 6 Dependents, 10 Dependencies
- Edges saved: **17**

---

## Rank 9: container_hash + type_index + winapi

**Merge Count:** 3 modules

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 51 |
| Internal edges (removed) | 1 |
| Merged edges (unique) | 38 |
| Edge reduction | 13 |

### Individual Module Details

**container_hash:**
- Edges from this module: 23
- Dependencies Relations: Primary = 3, All = 3
- Dependents Relations: Primary = 20, All = 81

**type_index:**
- Edges from this module: 13
- Dependencies Relations: Primary = 3, All = 6
- Dependents Relations: Primary = 10, All = 31

**winapi:**
- Edges from this module: 15
- Dependencies Relations: Primary = 2, All = 2
- Dependents Relations: Primary = 13, All = 58

### Summary

After merge, the combined module would have:
- **38** total outgoing edges (reduced from 51)
- Redundancy saved: 2 Dependents, 9 Dependencies
- Edges saved: **13**

---

## Rank 10: bind + exception

**Merge Count:** 2 modules

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 32 |
| Internal edges (removed) | 0 |
| Merged edges (unique) | 27 |
| Edge reduction | 5 |

### Individual Module Details

**bind:**
- Edges from this module: 17
- Dependencies Relations: Primary = 2, All = 5
- Dependents Relations: Primary = 15, All = 72

**exception:**
- Edges from this module: 15
- Dependencies Relations: Primary = 7, All = 8
- Dependents Relations: Primary = 8, All = 40

### Summary

After merge, the combined module would have:
- **27** total outgoing edges (reduced from 32)
- Redundancy saved: 2 Dependents, 3 Dependencies
- Edges saved: **5**

---

