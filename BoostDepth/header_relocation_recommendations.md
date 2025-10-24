# Header Relocation Recommendations Report

**Generated:** 2025-10-24 21:07:28

## ⚠️ NOTICE: Dependency Issues Detected

**The following headers have dependency issues. These are NOT included in relocation recommendations.**

### 🔄 Bidirectional Dependencies (Circular): 219 Headers

#### See file conflict_dependent_header_list.md for a detailed list.

**Impact**: These headers have mutual dependencies that create circular references.

**Headers with Bidirectional Dependencies:**

1. **`boost/asio/connect_pipe.hpp`** (Module: `asio`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/asio/impl/connect_pipe.hpp`

2. **`boost/asio/executor.hpp`** (Module: `asio`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/asio/impl/executor.hpp`

3. **`boost/asio/impl/connect_pipe.hpp`** (Module: `asio`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/asio/connect_pipe.hpp`

4. **`boost/asio/impl/executor.hpp`** (Module: `asio`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/asio/executor.hpp`

5. **`boost/beast/core/buffers_adaptor.hpp`** (Module: `beast`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/beast/core/impl/buffers_adaptor.hpp`
...

**Recommendation:**
- These headers should NOT be relocated individually
- Move both headers in a circular pair together, or
- Refactor to break circular dependencies before relocation
- ⚠️ Similar to MTL library: mutual dependencies require coordinated reorganization

### ❌ Non-Existent Header References: 4 Headers

**Impact**: These headers reference files that don't exist in the codebase.

**Headers Referencing Non-Existent Files:**

1. **`boost/numeric/odeint/external/mtl4/implicit_euler_mtl4.hpp`** (Module: `numeric`)
   - **References non-existent:** `boost/numeric/itl/itl.hpp`

2. **`boost/numeric/odeint/external/mtl4/mtl4_algebra_dispatcher.hpp`** (Module: `numeric`)
   - **References non-existent:** `boost/numeric/mtl/mtl.hpp`

3. **`boost/numeric/odeint/external/mtl4/mtl4_resize.hpp`** (Module: `numeric`)
   - **References non-existent:** `boost/numeric/mtl/matrix/compressed2D.hpp`

4. **`boost/numeric/ublas/functional.hpp`** (Module: `numeric`)
   - **References non-existent:** `boost/numeric/bindings/atlas/cblas.hpp`

**Possible Causes:**
- 📚 **Removed libraries**: References to libraries removed from Boost (e.g., MTL removed 2013-2017)
- 🖥️ **Platform-specific**: Conditional includes for platforms not in current build
- 📦 **External dependencies**: Headers from libraries outside Boost
- ✏️ **Typos or outdated paths**: Incorrect paths or renamed headers

**Recommendation:**
- Review and clean up obsolete #include statements
- Update paths to renamed or moved headers
- Verify platform-specific or conditional includes
- Document external dependencies

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Relocation Recommendations | 437 |
| Modules Affected (losing headers) | 82 |
| Modules Affected (gaining headers) | 66 |
| Headers with Bidirectional Dependencies (Notice Only) | 219 |
| Headers Referencing Non-Existent Headers (Notice Only) | 4 |

## Top 50 Relocation Recommendations

| Rank | Header | From Module | To Module | Current Int | Current Ext | Target Connections | Improvement | Benefit Score |
|------|--------|-------------|-----------|-------------|-------------|-------------------|-------------|---------------|
| 1 | `boost/mpl/vector/aux_/numbered.hpp` | mpl | preprocessor | 0 | 6 | 6 | ∞ | 350.0 |
| 2 | `boost/mpl/vector/aux_/numbered_c.hpp` | mpl | preprocessor | 0 | 6 | 6 | ∞ | 350.0 |
| 3 | `boost/msm/mpl_graph/mpl_utils.hpp` | msm | mpl | 0 | 8 | 8 | ∞ | 350.0 |
| 4 | `boost/polygon/polygon.hpp` | polygon | geometry | 0 | 7 | 7 | ∞ | 350.0 |
| 5 | `boost/preprocessor/tuple/push_back.hpp` | preprocessor | vmd | 0 | 6 | 6 | ∞ | 350.0 |
| 6 | `boost/preprocessor/tuple/replace.hpp` | preprocessor | vmd | 0 | 5 | 5 | ∞ | 350.0 |
| 7 | `boost/preprocessor/tuple/size.hpp` | preprocessor | vmd | 0 | 16 | 16 | ∞ | 350.0 |
| 8 | `boost/pending/indirect_cmp.hpp` | pending | graph | 0 | 18 | 16 | ∞ | 333.3 |
| 9 | `boost/geometry/util/combine_if.hpp` | geometry | mpl | 0 | 8 | 7 | ∞ | 331.2 |
| 10 | `boost/preprocessor/list/adt.hpp` | preprocessor | local_function | 0 | 7 | 6 | ∞ | 328.6 |
| 11 | `boost/detail/algorithm.hpp` | detail | range | 0 | 13 | 11 | ∞ | 326.9 |
| 12 | `boost/concept/requires.hpp` | concept | geometry | 0 | 12 | 10 | ∞ | 325.0 |
| 13 | `boost/detail/interlocked.hpp` | detail | thread | 0 | 6 | 5 | ∞ | 325.0 |
| 14 | `boost/geometry/util/compress_variant.hpp` | geometry | mpl | 0 | 11 | 9 | ∞ | 322.7 |
| 15 | `boost/config/abi_suffix.hpp` | config | thread | 0 | 104 | 84 | ∞ | 321.2 |
| 16 | `boost/core/use_default.hpp` | core | iterator | 0 | 10 | 8 | ∞ | 320.0 |
| 17 | `boost/core/explicit_operator_bool.hpp` | core | log | 0 | 17 | 13 | ∞ | 314.7 |
| 18 | `boost/accumulators/numeric/detail/function_n.hpp` | accumulators | preprocessor | 0 | 16 | 12 | ∞ | 312.5 |
| 19 | `boost/preprocessor/iterate.hpp` | preprocessor | fusion | 0 | 34 | 25 | ∞ | 310.3 |
| 20 | `boost/preprocessor/list/size.hpp` | preprocessor | local_function | 0 | 7 | 5 | ∞ | 307.1 |
| 21 | `boost/preprocessor/logical/bitor.hpp` | preprocessor | vmd | 0 | 13 | 9 | ∞ | 303.8 |
| 22 | `boost/preprocessor/repetition/enum_shifted.hpp` | preprocessor | fusion | 0 | 13 | 9 | ∞ | 303.8 |
| 23 | `boost/concept/detail/concept_def.hpp` | concept | graph | 0 | 6 | 4 | ∞ | 300.0 |
| 24 | `boost/concept/detail/concept_undef.hpp` | concept | graph | 0 | 6 | 4 | ∞ | 300.0 |
| 25 | `boost/detail/compressed_pair.hpp` | detail | type_traits | 0 | 6 | 4 | ∞ | 300.0 |
| 26 | `boost/intrusive/detail/has_member_function_callable_with.hpp` | intrusive | container | 0 | 6 | 4 | ∞ | 300.0 |
| 27 | `boost/pending/container_traits.hpp` | pending | graph | 0 | 9 | 6 | ∞ | 300.0 |
| 28 | `boost/preprocessor/array/size.hpp` | preprocessor | vmd | 0 | 6 | 4 | ∞ | 300.0 |
| 29 | `boost/preprocessor/control/while.hpp` | preprocessor | vmd | 0 | 9 | 6 | ∞ | 300.0 |
| 30 | `boost/preprocessor/logical/bitand.hpp` | preprocessor | vmd | 0 | 15 | 10 | ∞ | 300.0 |
| 31 | `boost/concept/assert.hpp` | concept | graph | 0 | 51 | 33 | ∞ | 297.1 |
| 32 | `boost/preprocessor/variadic/elem.hpp` | preprocessor | vmd | 0 | 19 | 12 | ∞ | 294.7 |
| 33 | `boost/preprocessor/repetition.hpp` | preprocessor | compute | 0 | 16 | 10 | ∞ | 293.8 |
| 34 | `boost/core/ignore_unused.hpp` | core | geometry | 0 | 108 | 67 | ∞ | 293.1 |
| 35 | `boost/preprocessor/comparison/not_equal.hpp` | preprocessor | vmd | 0 | 5 | 3 | ∞ | 290.0 |
| 36 | `boost/preprocessor/list/append.hpp` | preprocessor | local_function | 0 | 5 | 3 | ∞ | 290.0 |
| 37 | `boost/preprocessor/logical/compl.hpp` | preprocessor | vmd | 0 | 12 | 7 | ∞ | 287.5 |
| 38 | `boost/config/abi_prefix.hpp` | config | thread | 1 | 104 | 84 | 84.0x | 287.0 |
| 39 | `boost/preprocessor/enum_shifted_params.hpp` | preprocessor | mpl | 0 | 7 | 4 | ∞ | 285.7 |
| 40 | `boost/preprocessor/comparison/equal.hpp` | preprocessor | vmd | 0 | 41 | 23 | ∞ | 284.1 |
| 41 | `boost/preprocessor/empty.hpp` | preprocessor | fusion | 0 | 9 | 5 | ∞ | 283.3 |
| 42 | `boost/core/checked_delete.hpp` | core | smart_ptr | 0 | 11 | 6 | ∞ | 281.8 |
| 43 | `boost/core/noncopyable.hpp` | core | multi_index | 0 | 22 | 12 | ∞ | 281.8 |
| 44 | `boost/multi_index/indexed_by.hpp` | multi_index | preprocessor | 0 | 8 | 4 | ∞ | 275.0 |
| 45 | `boost/preprocessor/facilities/expand.hpp` | preprocessor | local_function | 0 | 6 | 3 | ∞ | 275.0 |
| 46 | `boost/preprocessor/seq/fold_left.hpp` | preprocessor | parameter | 0 | 8 | 4 | ∞ | 275.0 |
| 47 | `boost/preprocessor/enum_params.hpp` | preprocessor | mpl | 0 | 13 | 6 | ∞ | 269.2 |
| 48 | `boost/preprocessor/facilities/is_empty.hpp` | preprocessor | local_function | 0 | 13 | 6 | ∞ | 269.2 |
| 49 | `boost/preprocessor/dec.hpp` | preprocessor | fusion | 0 | 24 | 11 | ∞ | 268.8 |
| 50 | `boost/preprocessor/repetition/enum_trailing.hpp` | preprocessor | type_erasure | 0 | 9 | 4 | ∞ | 266.7 |

## Modules Losing Most Headers

| Rank | Module | Headers to Relocate |
|------|--------|--------------------|
| 1 | preprocessor | 77 |
| 2 | fusion | 32 |
| 3 | core | 24 |
| 4 | mpl | 20 |
| 5 | spirit | 16 |
| 6 | parameter | 12 |
| 7 | move | 10 |
| 8 | proto | 10 |
| 9 | msm | 8 |
| 10 | pending | 8 |
| 11 | detail | 8 |
| 12 | config | 8 |
| 13 | range | 8 |
| 14 | property_map | 8 |
| 15 | mqtt5 | 8 |
| 16 | type_traits | 8 |
| 17 | multi_index | 7 |
| 18 | algorithm | 7 |
| 19 | utility | 7 |
| 20 | metaparse | 7 |

## Modules Gaining Most Headers

| Rank | Module | Headers to Receive |
|------|--------|--------------------|
| 1 | preprocessor | 68 |
| 2 | mpl | 40 |
| 3 | fusion | 40 |
| 4 | graph | 27 |
| 5 | type_traits | 26 |
| 6 | spirit | 26 |
| 7 | vmd | 15 |
| 8 | asio | 14 |
| 9 | local_function | 12 |
| 10 | parameter | 12 |
| 11 | geometry | 10 |
| 12 | range | 10 |
| 13 | log | 9 |
| 14 | container | 9 |
| 15 | wave | 7 |
| 16 | thread | 6 |
| 17 | proto | 6 |
| 18 | msm | 5 |
| 19 | core | 5 |
| 20 | archive | 5 |

## Detailed Recommendations by Source Module

### Module: preprocessor (77 headers to relocate)

| Header | Target Module | Current Internal | Target Connections | Improvement |
|--------|---------------|------------------|-------------------|-------------|
| `boost/preprocessor/tuple/push_back.hpp` | vmd | 0 | 6 | ∞ |
| `boost/preprocessor/tuple/replace.hpp` | vmd | 0 | 5 | ∞ |
| `boost/preprocessor/tuple/size.hpp` | vmd | 0 | 16 | ∞ |
| `boost/preprocessor/list/adt.hpp` | local_function | 0 | 6 | ∞ |
| `boost/preprocessor/iterate.hpp` | fusion | 0 | 25 | ∞ |
| `boost/preprocessor/list/size.hpp` | local_function | 0 | 5 | ∞ |
| `boost/preprocessor/logical/bitor.hpp` | vmd | 0 | 9 | ∞ |
| `boost/preprocessor/repetition/enum_shifted.hpp` | fusion | 0 | 9 | ∞ |
| `boost/preprocessor/array/size.hpp` | vmd | 0 | 4 | ∞ |
| `boost/preprocessor/control/while.hpp` | vmd | 0 | 6 | ∞ |
| `boost/preprocessor/logical/bitand.hpp` | vmd | 0 | 10 | ∞ |
| `boost/preprocessor/variadic/elem.hpp` | vmd | 0 | 12 | ∞ |
| `boost/preprocessor/repetition.hpp` | compute | 0 | 10 | ∞ |
| `boost/preprocessor/comparison/not_equal.hpp` | vmd | 0 | 3 | ∞ |
| `boost/preprocessor/list/append.hpp` | local_function | 0 | 3 | ∞ |
| `boost/preprocessor/logical/compl.hpp` | vmd | 0 | 7 | ∞ |
| `boost/preprocessor/enum_shifted_params.hpp` | mpl | 0 | 4 | ∞ |
| `boost/preprocessor/comparison/equal.hpp` | vmd | 0 | 23 | ∞ |
| `boost/preprocessor/empty.hpp` | fusion | 0 | 5 | ∞ |
| `boost/preprocessor/facilities/expand.hpp` | local_function | 0 | 3 | ∞ |

### Module: fusion (32 headers to relocate)

| Header | Target Module | Current Internal | Target Connections | Improvement |
|--------|---------------|------------------|-------------------|-------------|
| `boost/fusion/include/at.hpp` | spirit | 2 | 44 | 22.0x |
| `boost/fusion/include/vector.hpp` | spirit | 2 | 41 | 20.5x |
| `boost/fusion/container/list/detail/cpp03/list_forward_ctor.hpp` | preprocessor | 1 | 5 | 5.0x |
| `boost/fusion/container/deque/detail/cpp03/deque_keyed_values_call.hpp` | preprocessor | 1 | 4 | 4.0x |
| `boost/fusion/include/any.hpp` | spirit | 2 | 9 | 4.5x |
| `boost/fusion/include/cons.hpp` | spirit | 2 | 9 | 4.5x |
| `boost/fusion/include/size.hpp` | spirit | 2 | 9 | 4.5x |
| `boost/fusion/container/generation/detail/pp_deque_tie.hpp` | preprocessor | 2 | 6 | 3.0x |
| `boost/fusion/container/generation/detail/pp_list_tie.hpp` | preprocessor | 2 | 6 | 3.0x |
| `boost/fusion/container/generation/detail/pp_vector_tie.hpp` | preprocessor | 2 | 6 | 3.0x |
| `boost/fusion/include/value_at.hpp` | spirit | 2 | 7 | 3.5x |
| `boost/fusion/view/nview/detail/cpp03/nview_impl.hpp` | preprocessor | 2 | 6 | 3.0x |
| `boost/fusion/include/deref.hpp` | spirit | 2 | 5 | 2.5x |
| `boost/fusion/adapted/struct/detail/namespace.hpp` | preprocessor | 3 | 7 | 2.3x |
| `boost/fusion/view/zip_view/detail/equal_to_impl.hpp` | mpl | 4 | 10 | 2.5x |
| `boost/fusion/include/at_key.hpp` | msm | 2 | 7 | 3.5x |
| `boost/fusion/include/as_vector.hpp` | spirit | 2 | 10 | 5.0x |
| `boost/fusion/container/deque/detail/cpp03/deque_initial_size.hpp` | mpl | 2 | 5 | 2.5x |
| `boost/fusion/include/insert_range.hpp` | msm | 2 | 4 | 2.0x |
| `boost/fusion/tuple/detail/tuple_tie.hpp` | preprocessor | 2 | 4 | 2.0x |

### Module: core (24 headers to relocate)

| Header | Target Module | Current Internal | Target Connections | Improvement |
|--------|---------------|------------------|-------------------|-------------|
| `boost/core/use_default.hpp` | iterator | 0 | 8 | ∞ |
| `boost/core/explicit_operator_bool.hpp` | log | 0 | 13 | ∞ |
| `boost/core/ignore_unused.hpp` | geometry | 0 | 67 | ∞ |
| `boost/core/checked_delete.hpp` | smart_ptr | 0 | 6 | ∞ |
| `boost/core/noncopyable.hpp` | multi_index | 0 | 12 | ∞ |
| `boost/core/exchange.hpp` | beast | 0 | 10 | ∞ |
| `boost/core/scoped_enum.hpp` | thread | 0 | 5 | ∞ |
| `boost/core/empty_value.hpp` | beast | 0 | 11 | ∞ |
| `boost/core/bit.hpp` | charconv | 0 | 5 | ∞ |
| `boost/core/cmath.hpp` | lexical_cast | 0 | 2 | ∞ |
| `boost/core/uncaught_exceptions.hpp` | graph | 0 | 2 | ∞ |
| `boost/core/no_exceptions_support.hpp` | multi_index | 0 | 9 | ∞ |
| `boost/core/span.hpp` | mysql | 3 | 30 | 10.0x |
| `boost/core/detail/string_view.hpp` | url | 2 | 28 | 14.0x |
| `boost/core/nvp.hpp` | histogram | 2 | 18 | 9.0x |
| `boost/core/serialization.hpp` | unordered | 1 | 12 | 12.0x |
| `boost/core/allocator_access.hpp` | unordered | 3 | 14 | 4.7x |
| `boost/core/allocator_traits.hpp` | unordered | 1 | 3 | 3.0x |
| `boost/core/pointer_traits.hpp` | unordered | 2 | 6 | 3.0x |
| `boost/core/alloc_construct.hpp` | smart_ptr | 1 | 2 | 2.0x |

### Module: mpl (20 headers to relocate)

| Header | Target Module | Current Internal | Target Connections | Improvement |
|--------|---------------|------------------|-------------------|-------------|
| `boost/mpl/vector/aux_/numbered.hpp` | preprocessor | 0 | 6 | ∞ |
| `boost/mpl/vector/aux_/numbered_c.hpp` | preprocessor | 0 | 6 | ∞ |
| `boost/mpl/aux_/preprocessor/is_seq.hpp` | preprocessor | 1 | 5 | 5.0x |
| `boost/mpl/placeholders.hpp` | accumulators | 4 | 52 | 13.0x |
| `boost/mpl/bool_fwd.hpp` | serialization | 2 | 8 | 4.0x |
| `boost/mpl/aux_/preprocessor/token_equal.hpp` | preprocessor | 1 | 5 | 5.0x |
| `boost/mpl/set.hpp` | msm | 1 | 7 | 7.0x |
| `boost/mpl/equal_to.hpp` | fusion | 3 | 16 | 5.3x |
| `boost/mpl/map.hpp` | msm | 1 | 5 | 5.0x |
| `boost/mpl/int.hpp` | fusion | 11 | 45 | 4.1x |
| `boost/mpl/inherit.hpp` | fusion | 1 | 3 | 3.0x |
| `boost/mpl/end.hpp` | type_erasure | 1 | 5 | 5.0x |
| `boost/mpl/vector.hpp` | bimap | 2 | 20 | 10.0x |
| `boost/mpl/or.hpp` | spirit | 3 | 21 | 7.0x |
| `boost/mpl/begin.hpp` | units | 1 | 3 | 3.0x |
| `boost/mpl/at.hpp` | fusion | 7 | 15 | 2.1x |
| `boost/mpl/list.hpp` | statechart | 1 | 3 | 3.0x |
| `boost/mpl/bool.hpp` | spirit | 17 | 74 | 4.4x |
| `boost/mpl/and.hpp` | icl | 5 | 20 | 4.0x |
| `boost/mpl/identity.hpp` | fusion | 14 | 33 | 2.4x |

### Module: spirit (16 headers to relocate)

| Header | Target Module | Current Internal | Target Connections | Improvement |
|--------|---------------|------------------|-------------------|-------------|
| `boost/spirit/include/classic_assign_actor.hpp` | wave | 1 | 7 | 7.0x |
| `boost/spirit/include/classic_push_back_actor.hpp` | wave | 1 | 7 | 7.0x |
| `boost/spirit/include/classic_core.hpp` | wave | 1 | 9 | 9.0x |
| `boost/spirit/include/classic_parse_tree.hpp` | wave | 1 | 4 | 4.0x |
| `boost/spirit/include/classic_closure.hpp` | wave | 1 | 5 | 5.0x |
| `boost/spirit/home/lex/argument_phoenix.hpp` | phoenix | 1 | 5 | 5.0x |
| `boost/spirit/home/support/algorithm/any.hpp` | fusion | 2 | 6 | 3.0x |
| `boost/spirit/include/classic_confix.hpp` | wave | 1 | 3 | 3.0x |
| `boost/spirit/home/support/algorithm/any_ns.hpp` | fusion | 3 | 6 | 2.0x |
| `boost/spirit/home/support/algorithm/any_ns_so.hpp` | fusion | 3 | 6 | 2.0x |
| `boost/spirit/home/support/detail/as_variant.hpp` | mpl | 1 | 6 | 6.0x |
| `boost/spirit/home/support/nonterminal/expand_arg.hpp` | mpl | 2 | 4 | 2.0x |
| `boost/spirit/home/support/detail/make_cons.hpp` | type_traits | 2 | 4 | 2.0x |
| `boost/spirit/home/support/extended_variant.hpp` | preprocessor | 1 | 2 | 2.0x |
| `boost/spirit/include/classic_multi_pass.hpp` | graph | 1 | 2 | 2.0x |
| `boost/spirit/home/support/utree/detail/utree_detail2.hpp` | type_traits | 1 | 2 | 2.0x |

### Module: parameter (12 headers to relocate)

| Header | Target Module | Current Internal | Target Connections | Improvement |
|--------|---------------|------------------|-------------------|-------------|
| `boost/parameter/aux_/preprocessor/inc_binary_seq.hpp` | preprocessor | 1 | 6 | 6.0x |
| `boost/parameter/aux_/preprocessor/impl/for_each.hpp` | preprocessor | 2 | 11 | 5.5x |
| `boost/parameter/aux_/preprocessor/convert_binary_seq.hpp` | preprocessor | 2 | 8 | 4.0x |
| `boost/parameter/aux_/preprocessor/seq_merge.hpp` | preprocessor | 1 | 4 | 4.0x |
| `boost/parameter/macros.hpp` | preprocessor | 4 | 12 | 3.0x |
| `boost/parameter/aux_/preprocessor/impl/split_args.hpp` | preprocessor | 2 | 6 | 3.0x |
| `boost/parameter/aux_/preprocessor/is_binary.hpp` | preprocessor | 1 | 5 | 5.0x |
| `boost/parameter/aux_/preprocessor/is_nullary.hpp` | preprocessor | 1 | 5 | 5.0x |
| `boost/parameter/aux_/preprocessor/impl/flatten.hpp` | preprocessor | 3 | 8 | 2.7x |
| `boost/parameter/aux_/preprocessor/impl/arity_range.hpp` | preprocessor | 2 | 4 | 2.0x |
| `boost/parameter/keyword.hpp` | log | 9 | 39 | 4.3x |
| `boost/parameter/aux_/maybe.hpp` | type_traits | 2 | 4 | 2.0x |

### Module: move (10 headers to relocate)

| Header | Target Module | Current Internal | Target Connections | Improvement |
|--------|---------------|------------------|-------------------|-------------|
| `boost/move/detail/fwd_macros.hpp` | container | 1 | 20 | 20.0x |
| `boost/move/detail/launder.hpp` | container | 1 | 8 | 8.0x |
| `boost/move/detail/move_helpers.hpp` | container | 3 | 11 | 3.7x |
| `boost/move/core.hpp` | log | 8 | 34 | 4.2x |
| `boost/move/detail/force_ptr.hpp` | container | 1 | 7 | 7.0x |
| `boost/move/detail/iterator_to_raw_pointer.hpp` | container | 6 | 12 | 2.0x |
| `boost/move/detail/to_raw_pointer.hpp` | container | 5 | 12 | 2.4x |
| `boost/move/utility.hpp` | assign | 6 | 12 | 2.0x |
| `boost/move/detail/std_ns_begin.hpp` | container | 1 | 3 | 3.0x |
| `boost/move/detail/std_ns_end.hpp` | container | 1 | 3 | 3.0x |

### Module: proto (10 headers to relocate)

| Header | Target Module | Current Internal | Target Connections | Improvement |
|--------|---------------|------------------|-------------------|-------------|
| `boost/proto/detail/deprecated.hpp` | preprocessor | 2 | 25 | 12.5x |
| `boost/proto/tags.hpp` | spirit | 4 | 32 | 8.0x |
| `boost/proto/detail/remove_typename.hpp` | preprocessor | 1 | 5 | 5.0x |
| `boost/proto/repeat.hpp` | preprocessor | 2 | 7 | 3.5x |
| `boost/proto/functional/fusion/pop_back.hpp` | fusion | 2 | 4 | 2.0x |
| `boost/proto/operators.hpp` | spirit | 7 | 23 | 3.3x |
| `boost/proto/detail/deduce_domain.hpp` | preprocessor | 3 | 8 | 2.7x |
| `boost/proto/functional/fusion/pop_front.hpp` | fusion | 2 | 4 | 2.0x |
| `boost/proto/transform/detail/pack.hpp` | preprocessor | 6 | 12 | 2.0x |
| `boost/proto/context/callable.hpp` | preprocessor | 4 | 9 | 2.2x |

### Module: msm (8 headers to relocate)

| Header | Target Module | Current Internal | Target Connections | Improvement |
|--------|---------------|------------------|-------------------|-------------|
| `boost/msm/mpl_graph/mpl_utils.hpp` | mpl | 0 | 8 | ∞ |
| `boost/msm/mpl_graph/breadth_first_search.hpp` | mpl | 1 | 7 | 7.0x |
| `boost/msm/back/args.hpp` | preprocessor | 2 | 9 | 4.5x |
| `boost/msm/back/metafunctions.hpp` | mpl | 8 | 29 | 3.6x |
| `boost/msm/back11/metafunctions.hpp` | mpl | 5 | 28 | 5.6x |
| `boost/msm/mpl_graph/mpl_graph.hpp` | mpl | 4 | 9 | 2.2x |
| `boost/msm/front/puml/puml.hpp` | fusion | 3 | 7 | 2.3x |
| `boost/msm/front/detail/common_states.hpp` | fusion | 1 | 3 | 3.0x |

### Module: pending (8 headers to relocate)

| Header | Target Module | Current Internal | Target Connections | Improvement |
|--------|---------------|------------------|-------------------|-------------|
| `boost/pending/indirect_cmp.hpp` | graph | 0 | 16 | ∞ |
| `boost/pending/container_traits.hpp` | graph | 0 | 6 | ∞ |
| `boost/pending/bucket_sorter.hpp` | graph | 0 | 2 | ∞ |
| `boost/pending/relaxed_heap.hpp` | graph | 0 | 2 | ∞ |
| `boost/pending/queue.hpp` | graph | 1 | 11 | 11.0x |
| `boost/pending/disjoint_sets.hpp` | graph | 1 | 5 | 5.0x |
| `boost/pending/property_serialize.hpp` | serialization | 1 | 3 | 3.0x |
| `boost/pending/property.hpp` | graph | 2 | 7 | 3.5x |

