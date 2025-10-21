# Module Merge Recommendations
**Generated:** 2025-10-21 22:09:49
**Merge Count:** 3 modules per combination
**Top Recommendations:** 10

## Overall Impact
| Metric | Value |
|--------|-------|
| Original total edges | 2764 |
| Reduced total edges | 2322 |
| Edge reduction | 442 (15.99%) |
| Modules merged | 30 |

---

## Rank 1: assert + config + static_assert

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 292 |
| Internal edges (removed) | 4 |
| Merged edges (unique) | 137 |
| Edge reduction | 155 (53.08%) |

### Individual Module Details

**assert:**
- Edges from this module: 95
- Primary Relations: Level 1 = 1, Total = 1
- Reverse Relations: Level 1 = 94, Total = 129

**config:**
- Edges from this module: 137
- Primary Relations: Level 1 = 0, Total = 0
- Reverse Relations: Level 1 = 137, Total = 141

**static_assert:**
- Edges from this module: 60
- Primary Relations: Level 1 = 1, Total = 1
- Reverse Relations: Level 1 = 59, Total = 121

### Merge Metrics

| Metric | Value |
|--------|-------|
| Shared Primary dependencies | 1 |
| Shared Reverse dependencies | 106 |
| Unique Primary dependencies | 1 |
| Unique Reverse dependencies | 139 |
| Redundancy saved (Primary) | 1 |
| Redundancy saved (Reverse) | 151 |
| **Total Merge Damage** | **0.31** |

### Summary

After merge, the combined module would have:
- **137** total outgoing edges (reduced from 292)
- **1** unique Primary dependencies
- **139** unique Reverse dependencies
- Redundancy saved: 1 Primary, 151 Reverse
- Edges saved: **155** (53.08%)

---

## Rank 2: compat + core + type_traits

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 192 |
| Internal edges (removed) | 0 |
| Merged edges (unique) | 113 |
| Edge reduction | 79 (41.15%) |

### Individual Module Details

**compat:**
- Edges from this module: 4
- Primary Relations: Level 1 = 3, Total = 3
- Reverse Relations: Level 1 = 1, Total = 1

**core:**
- Edges from this module: 102
- Primary Relations: Level 1 = 4, Total = 4
- Reverse Relations: Level 1 = 98, Total = 115

**type_traits:**
- Edges from this module: 86
- Primary Relations: Level 1 = 2, Total = 2
- Reverse Relations: Level 1 = 84, Total = 107

### Merge Metrics

| Metric | Value |
|--------|-------|
| Shared Primary dependencies | 4 |
| Shared Reverse dependencies | 74 |
| Unique Primary dependencies | 4 |
| Unique Reverse dependencies | 109 |
| Redundancy saved (Primary) | 5 |
| Redundancy saved (Reverse) | 74 |
| **Total Merge Damage** | **0.47** |

### Summary

After merge, the combined module would have:
- **113** total outgoing edges (reduced from 192)
- **4** unique Primary dependencies
- **109** unique Reverse dependencies
- Redundancy saved: 5 Primary, 74 Reverse
- Edges saved: **79** (41.15%)

---

## Rank 3: detail + mpl + preprocessor

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 128 |
| Internal edges (removed) | 4 |
| Merged edges (unique) | 71 |
| Edge reduction | 57 (44.53%) |

### Individual Module Details

**detail:**
- Edges from this module: 22
- Primary Relations: Level 1 = 5, Total = 7
- Reverse Relations: Level 1 = 17, Total = 73

**mpl:**
- Edges from this module: 59
- Primary Relations: Level 1 = 7, Total = 10
- Reverse Relations: Level 1 = 52, Total = 76

**preprocessor:**
- Edges from this module: 47
- Primary Relations: Level 1 = 0, Total = 0
- Reverse Relations: Level 1 = 47, Total = 94

### Merge Metrics

| Metric | Value |
|--------|-------|
| Shared Primary dependencies | 5 |
| Shared Reverse dependencies | 38 |
| Unique Primary dependencies | 7 |
| Unique Reverse dependencies | 68 |
| Redundancy saved (Primary) | 5 |
| Redundancy saved (Reverse) | 48 |
| **Total Merge Damage** | **1.10** |

### Summary

After merge, the combined module would have:
- **71** total outgoing edges (reduced from 128)
- **7** unique Primary dependencies
- **68** unique Reverse dependencies
- Redundancy saved: 5 Primary, 48 Reverse
- Edges saved: **57** (44.53%)

---

## Rank 4: foreach + mpi + property_map

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 50 |
| Internal edges (removed) | 2 |
| Merged edges (unique) | 24 |
| Edge reduction | 26 (52.00%) |

### Individual Module Details

**foreach:**
- Edges from this module: 10
- Primary Relations: Level 1 = 6, Total = 31
- Reverse Relations: Level 1 = 4, Total = 7

**mpi:**
- Edges from this module: 21
- Primary Relations: Level 1 = 18, Total = 73
- Reverse Relations: Level 1 = 3, Total = 3

**property_map:**
- Edges from this module: 19
- Primary Relations: Level 1 = 15, Total = 32
- Reverse Relations: Level 1 = 4, Total = 7

### Merge Metrics

| Metric | Value |
|--------|-------|
| Shared Primary dependencies | 12 |
| Shared Reverse dependencies | 4 |
| Unique Primary dependencies | 22 |
| Unique Reverse dependencies | 6 |
| Redundancy saved (Primary) | 17 |
| Redundancy saved (Reverse) | 5 |
| **Total Merge Damage** | **1.17** |

### Summary

After merge, the combined module would have:
- **24** total outgoing edges (reduced from 50)
- **22** unique Primary dependencies
- **6** unique Reverse dependencies
- Redundancy saved: 17 Primary, 5 Reverse
- Edges saved: **26** (52.00%)

---

## Rank 5: function + smart_ptr + typeof

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 84 |
| Internal edges (removed) | 0 |
| Merged edges (unique) | 52 |
| Edge reduction | 32 (38.10%) |

### Individual Module Details

**function:**
- Edges from this module: 27
- Primary Relations: Level 1 = 5, Total = 6
- Reverse Relations: Level 1 = 22, Total = 71

**smart_ptr:**
- Edges from this module: 40
- Primary Relations: Level 1 = 4, Total = 5
- Reverse Relations: Level 1 = 36, Total = 64

**typeof:**
- Edges from this module: 17
- Primary Relations: Level 1 = 1, Total = 1
- Reverse Relations: Level 1 = 16, Total = 72

### Merge Metrics

| Metric | Value |
|--------|-------|
| Shared Primary dependencies | 4 |
| Shared Reverse dependencies | 23 |
| Unique Primary dependencies | 5 |
| Unique Reverse dependencies | 47 |
| Redundancy saved (Primary) | 5 |
| Redundancy saved (Reverse) | 27 |
| **Total Merge Damage** | **1.20** |

### Summary

After merge, the combined module would have:
- **52** total outgoing edges (reduced from 84)
- **5** unique Primary dependencies
- **47** unique Reverse dependencies
- Redundancy saved: 5 Primary, 27 Reverse
- Edges saved: **32** (38.10%)

---

## Rank 6: phoenix + proto + uuid

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 38 |
| Internal edges (removed) | 2 |
| Merged edges (unique) | 21 |
| Edge reduction | 17 (44.74%) |

### Individual Module Details

**phoenix:**
- Edges from this module: 17
- Primary Relations: Level 1 = 14, Total = 32
- Reverse Relations: Level 1 = 3, Total = 20

**proto:**
- Edges from this module: 16
- Primary Relations: Level 1 = 10, Total = 31
- Reverse Relations: Level 1 = 6, Total = 22

**uuid:**
- Edges from this module: 5
- Primary Relations: Level 1 = 4, Total = 5
- Reverse Relations: Level 1 = 1, Total = 4

### Merge Metrics

| Metric | Value |
|--------|-------|
| Shared Primary dependencies | 9 |
| Shared Reverse dependencies | 4 |
| Unique Primary dependencies | 17 |
| Unique Reverse dependencies | 6 |
| Redundancy saved (Primary) | 11 |
| Redundancy saved (Reverse) | 4 |
| **Total Merge Damage** | **1.20** |

### Summary

After merge, the combined module would have:
- **21** total outgoing edges (reduced from 38)
- **17** unique Primary dependencies
- **6** unique Reverse dependencies
- Redundancy saved: 11 Primary, 4 Reverse
- Edges saved: **17** (44.74%)

---

## Rank 7: bimap + multi_array + units

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 38 |
| Internal edges (removed) | 0 |
| Merged edges (unique) | 22 |
| Edge reduction | 16 (42.11%) |

### Individual Module Details

**bimap:**
- Edges from this module: 14
- Primary Relations: Level 1 = 13, Total = 30
- Reverse Relations: Level 1 = 1, Total = 7

**multi_array:**
- Edges from this module: 11
- Primary Relations: Level 1 = 10, Total = 26
- Reverse Relations: Level 1 = 1, Total = 1

**units:**
- Edges from this module: 13
- Primary Relations: Level 1 = 12, Total = 37
- Reverse Relations: Level 1 = 1, Total = 1

### Merge Metrics

| Metric | Value |
|--------|-------|
| Shared Primary dependencies | 10 |
| Shared Reverse dependencies | 1 |
| Unique Primary dependencies | 20 |
| Unique Reverse dependencies | 2 |
| Redundancy saved (Primary) | 15 |
| Redundancy saved (Reverse) | 1 |
| **Total Merge Damage** | **1.41** |

### Summary

After merge, the combined module would have:
- **22** total outgoing edges (reduced from 38)
- **20** unique Primary dependencies
- **2** unique Reverse dependencies
- Redundancy saved: 15 Primary, 1 Reverse
- Edges saved: **16** (42.11%)

---

## Rank 8: callable_traits + polygon + qvm

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 4 |
| Internal edges (removed) | 0 |
| Merged edges (unique) | 3 |
| Edge reduction | 1 (25.00%) |

### Individual Module Details

**callable_traits:**
- Edges from this module: 1
- Primary Relations: Level 1 = 0, Total = 0
- Reverse Relations: Level 1 = 1, Total = 1

**polygon:**
- Edges from this module: 2
- Primary Relations: Level 1 = 1, Total = 1
- Reverse Relations: Level 1 = 1, Total = 1

**qvm:**
- Edges from this module: 1
- Primary Relations: Level 1 = 0, Total = 0
- Reverse Relations: Level 1 = 1, Total = 1

### Merge Metrics

| Metric | Value |
|--------|-------|
| Shared Primary dependencies | 0 |
| Shared Reverse dependencies | 1 |
| Unique Primary dependencies | 1 |
| Unique Reverse dependencies | 2 |
| Redundancy saved (Primary) | 0 |
| Redundancy saved (Reverse) | 1 |
| **Total Merge Damage** | **1.50** |

### Summary

After merge, the combined module would have:
- **3** total outgoing edges (reduced from 4)
- **1** unique Primary dependencies
- **2** unique Reverse dependencies
- Redundancy saved: 0 Primary, 1 Reverse
- Edges saved: **1** (25.00%)

---

## Rank 9: graph + property_map_parallel + python

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 83 |
| Internal edges (removed) | 2 |
| Merged edges (unique) | 47 |
| Edge reduction | 36 (43.37%) |

### Individual Module Details

**graph:**
- Edges from this module: 46
- Primary Relations: Level 1 = 42, Total = 71
- Reverse Relations: Level 1 = 3, Total = 6

**property_map_parallel:**
- Edges from this module: 14
- Primary Relations: Level 1 = 13, Total = 74
- Reverse Relations: Level 1 = 1, Total = 1

**python:**
- Edges from this module: 23
- Primary Relations: Level 1 = 21, Total = 72
- Reverse Relations: Level 1 = 2, Total = 5

### Merge Metrics

| Metric | Value |
|--------|-------|
| Shared Primary dependencies | 24 |
| Shared Reverse dependencies | 2 |
| Unique Primary dependencies | 45 |
| Unique Reverse dependencies | 4 |
| Redundancy saved (Primary) | 31 |
| Redundancy saved (Reverse) | 2 |
| **Total Merge Damage** | **1.51** |

### Summary

After merge, the combined module would have:
- **47** total outgoing edges (reduced from 83)
- **45** unique Primary dependencies
- **4** unique Reverse dependencies
- Redundancy saved: 31 Primary, 2 Reverse
- Edges saved: **36** (43.37%)

---

## Rank 10: chrono + property_tree + xpressive

### Edge Count Impact

| Metric | Value |
|--------|-------|
| Original edges (sum) | 58 |
| Internal edges (removed) | 0 |
| Merged edges (unique) | 35 |
| Edge reduction | 23 (39.66%) |

### Individual Module Details

**chrono:**
- Edges from this module: 17
- Primary Relations: Level 1 = 15, Total = 19
- Reverse Relations: Level 1 = 2, Total = 26

**property_tree:**
- Edges from this module: 17
- Primary Relations: Level 1 = 14, Total = 60
- Reverse Relations: Level 1 = 3, Total = 11

**xpressive:**
- Edges from this module: 24
- Primary Relations: Level 1 = 22, Total = 39
- Reverse Relations: Level 1 = 2, Total = 8

### Merge Metrics

| Metric | Value |
|--------|-------|
| Shared Primary dependencies | 13 |
| Shared Reverse dependencies | 3 |
| Unique Primary dependencies | 31 |
| Unique Reverse dependencies | 4 |
| Redundancy saved (Primary) | 20 |
| Redundancy saved (Reverse) | 3 |
| **Total Merge Damage** | **1.54** |

### Summary

After merge, the combined module would have:
- **35** total outgoing edges (reduced from 58)
- **31** unique Primary dependencies
- **4** unique Reverse dependencies
- Redundancy saved: 20 Primary, 3 Reverse
- Edges saved: **23** (39.66%)

---

