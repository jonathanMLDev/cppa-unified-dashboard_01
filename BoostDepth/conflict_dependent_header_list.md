# Boost Headers with Bidirectional Dependencies (Conflicts)

**Generated:** 2025-10-24 22:10:33

## Summary

Total headers with bidirectional dependencies: **181**

**What are bidirectional dependencies?**

Two headers have a bidirectional dependency when they include each other, creating a circular reference. For example:
- Header A includes Header B
- Header B includes Header A

**Impact:**
- These headers are tightly coupled and cannot be relocated independently
- Moving one without the other will break compilation
- Both headers in a circular pair should be moved together, or
- The circular dependency should be refactored before relocation

---

## Headers by Module

### Module: `hana`

**59 header(s) with conflicts**

#### `boost/hana/accessors.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/struct.hpp`

#### `boost/hana/adjust_if.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/functor.hpp`

#### `boost/hana/any_of.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/searchable.hpp`

#### `boost/hana/ap.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/applicative.hpp`

#### `boost/hana/at.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/iterable.hpp`

#### `boost/hana/chain.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/monad.hpp`

#### `boost/hana/concat.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/monad_plus.hpp`

#### `boost/hana/concept/applicative.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/ap.hpp`
- `boost/hana/lift.hpp`

#### `boost/hana/concept/comonad.hpp`

Circular dependencies with 3 header(s):
- `boost/hana/duplicate.hpp`
- `boost/hana/extend.hpp`
- `boost/hana/extract.hpp`

#### `boost/hana/concept/comparable.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/equal.hpp`

#### `boost/hana/concept/constant.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/value.hpp`

#### `boost/hana/concept/euclidean_ring.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/div.hpp`
- `boost/hana/mod.hpp`

#### `boost/hana/concept/foldable.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/fold_left.hpp`
- `boost/hana/unpack.hpp`

#### `boost/hana/concept/functor.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/adjust_if.hpp`
- `boost/hana/transform.hpp`

#### `boost/hana/concept/group.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/minus.hpp`
- `boost/hana/negate.hpp`

#### `boost/hana/concept/hashable.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/hash.hpp`

#### `boost/hana/concept/iterable.hpp`

Circular dependencies with 3 header(s):
- `boost/hana/at.hpp`
- `boost/hana/drop_front.hpp`
- `boost/hana/is_empty.hpp`

#### `boost/hana/concept/logical.hpp`

Circular dependencies with 3 header(s):
- `boost/hana/eval_if.hpp`
- `boost/hana/not.hpp`
- `boost/hana/while.hpp`

#### `boost/hana/concept/monad.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/chain.hpp`
- `boost/hana/flatten.hpp`

#### `boost/hana/concept/monad_plus.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/concat.hpp`
- `boost/hana/empty.hpp`

#### `boost/hana/concept/monoid.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/plus.hpp`
- `boost/hana/zero.hpp`

#### `boost/hana/concept/orderable.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/less.hpp`

#### `boost/hana/concept/product.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/first.hpp`
- `boost/hana/second.hpp`

#### `boost/hana/concept/ring.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/mult.hpp`
- `boost/hana/one.hpp`

#### `boost/hana/concept/searchable.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/any_of.hpp`
- `boost/hana/find_if.hpp`

#### `boost/hana/concept/struct.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/accessors.hpp`

#### `boost/hana/div.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/euclidean_ring.hpp`

#### `boost/hana/drop_front.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/iterable.hpp`

#### `boost/hana/duplicate.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/concept/comonad.hpp`
- `boost/hana/extend.hpp`

#### `boost/hana/empty.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/monad_plus.hpp`

#### `boost/hana/equal.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/comparable.hpp`

#### `boost/hana/eval_if.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/concept/logical.hpp`
- `boost/hana/if.hpp`

#### `boost/hana/extend.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/concept/comonad.hpp`
- `boost/hana/duplicate.hpp`

#### `boost/hana/extract.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/comonad.hpp`

#### `boost/hana/find_if.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/searchable.hpp`

#### `boost/hana/first.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/product.hpp`

#### `boost/hana/flatten.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/monad.hpp`

#### `boost/hana/fold_left.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/foldable.hpp`

#### `boost/hana/hash.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/hashable.hpp`

#### `boost/hana/if.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/eval_if.hpp`

#### `boost/hana/is_empty.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/iterable.hpp`

#### `boost/hana/length.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/unpack.hpp`

#### `boost/hana/less.hpp`

Circular dependencies with 3 header(s):
- `boost/hana/concept/orderable.hpp`
- `boost/hana/less_equal.hpp`
- `boost/hana/lexicographical_compare.hpp`

#### `boost/hana/less_equal.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/less.hpp`

#### `boost/hana/lexicographical_compare.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/less.hpp`

#### `boost/hana/lift.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/applicative.hpp`

#### `boost/hana/minus.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/group.hpp`

#### `boost/hana/mod.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/euclidean_ring.hpp`

#### `boost/hana/mult.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/ring.hpp`

#### `boost/hana/negate.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/group.hpp`

#### `boost/hana/not.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/logical.hpp`

#### `boost/hana/one.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/ring.hpp`

#### `boost/hana/plus.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/monoid.hpp`

#### `boost/hana/second.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/product.hpp`

#### `boost/hana/transform.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/functor.hpp`

#### `boost/hana/unpack.hpp`

Circular dependencies with 2 header(s):
- `boost/hana/concept/foldable.hpp`
- `boost/hana/length.hpp`

#### `boost/hana/value.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/constant.hpp`

#### `boost/hana/while.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/logical.hpp`

#### `boost/hana/zero.hpp`

Circular dependencies with 1 header(s):
- `boost/hana/concept/monoid.hpp`

### Module: `mysql`

**12 header(s) with conflicts**

#### `boost/mysql/field_view.hpp`

Circular dependencies with 1 header(s):
- `boost/mysql/impl/field_view.hpp`

#### `boost/mysql/format_sql.hpp`

Circular dependencies with 1 header(s):
- `boost/mysql/impl/format_sql.hpp`

#### `boost/mysql/impl/field_view.hpp`

Circular dependencies with 1 header(s):
- `boost/mysql/field_view.hpp`

#### `boost/mysql/impl/format_sql.hpp`

Circular dependencies with 1 header(s):
- `boost/mysql/format_sql.hpp`

#### `boost/mysql/impl/pfr.hpp`

Circular dependencies with 1 header(s):
- `boost/mysql/pfr.hpp`

#### `boost/mysql/impl/statement.hpp`

Circular dependencies with 1 header(s):
- `boost/mysql/statement.hpp`

#### `boost/mysql/impl/with_diagnostics.hpp`

Circular dependencies with 1 header(s):
- `boost/mysql/with_diagnostics.hpp`

#### `boost/mysql/impl/with_params.hpp`

Circular dependencies with 1 header(s):
- `boost/mysql/with_params.hpp`

#### `boost/mysql/pfr.hpp`

Circular dependencies with 1 header(s):
- `boost/mysql/impl/pfr.hpp`

#### `boost/mysql/statement.hpp`

Circular dependencies with 1 header(s):
- `boost/mysql/impl/statement.hpp`

#### `boost/mysql/with_diagnostics.hpp`

Circular dependencies with 1 header(s):
- `boost/mysql/impl/with_diagnostics.hpp`

#### `boost/mysql/with_params.hpp`

Circular dependencies with 1 header(s):
- `boost/mysql/impl/with_params.hpp`

### Module: `math`

**10 header(s) with conflicts**

#### `boost/math/special_functions/beta.hpp`

Circular dependencies with 2 header(s):
- `boost/math/special_functions/binomial.hpp`
- `boost/math/special_functions/detail/ibeta_inverse.hpp`

#### `boost/math/special_functions/binomial.hpp`

Circular dependencies with 1 header(s):
- `boost/math/special_functions/beta.hpp`

#### `boost/math/special_functions/detail/ibeta_inverse.hpp`

Circular dependencies with 1 header(s):
- `boost/math/special_functions/beta.hpp`

#### `boost/math/special_functions/detail/igamma_inverse.hpp`

Circular dependencies with 1 header(s):
- `boost/math/special_functions/gamma.hpp`

#### `boost/math/special_functions/erf.hpp`

Circular dependencies with 1 header(s):
- `boost/math/special_functions/gamma.hpp`

#### `boost/math/special_functions/gamma.hpp`

Circular dependencies with 2 header(s):
- `boost/math/special_functions/detail/igamma_inverse.hpp`
- `boost/math/special_functions/erf.hpp`

#### `boost/math/special_functions/polygamma.hpp`

Circular dependencies with 1 header(s):
- `boost/math/special_functions/trigamma.hpp`

#### `boost/math/special_functions/trigamma.hpp`

Circular dependencies with 1 header(s):
- `boost/math/special_functions/polygamma.hpp`

#### `boost/math/tools/polynomial.hpp`

Circular dependencies with 1 header(s):
- `boost/math/tools/polynomial_gcd.hpp`

#### `boost/math/tools/polynomial_gcd.hpp`

Circular dependencies with 1 header(s):
- `boost/math/tools/polynomial.hpp`

### Module: `predef`

**9 header(s) with conflicts**

#### `boost/predef/architecture/x86.h`

Circular dependencies with 2 header(s):
- `boost/predef/architecture/x86/32.h`
- `boost/predef/architecture/x86/64.h`

#### `boost/predef/architecture/x86/32.h`

Circular dependencies with 1 header(s):
- `boost/predef/architecture/x86.h`

#### `boost/predef/architecture/x86/64.h`

Circular dependencies with 1 header(s):
- `boost/predef/architecture/x86.h`

#### `boost/predef/os/bsd.h`

Circular dependencies with 5 header(s):
- `boost/predef/os/bsd/bsdi.h`
- `boost/predef/os/bsd/dragonfly.h`
- `boost/predef/os/bsd/free.h`
- `boost/predef/os/bsd/net.h`
- `boost/predef/os/bsd/open.h`

#### `boost/predef/os/bsd/bsdi.h`

Circular dependencies with 1 header(s):
- `boost/predef/os/bsd.h`

#### `boost/predef/os/bsd/dragonfly.h`

Circular dependencies with 1 header(s):
- `boost/predef/os/bsd.h`

#### `boost/predef/os/bsd/free.h`

Circular dependencies with 1 header(s):
- `boost/predef/os/bsd.h`

#### `boost/predef/os/bsd/net.h`

Circular dependencies with 1 header(s):
- `boost/predef/os/bsd.h`

#### `boost/predef/os/bsd/open.h`

Circular dependencies with 1 header(s):
- `boost/predef/os/bsd.h`

### Module: `beast`

**8 header(s) with conflicts**

#### `boost/beast/core/buffers_adaptor.hpp`

Circular dependencies with 1 header(s):
- `boost/beast/core/impl/buffers_adaptor.hpp`

#### `boost/beast/core/buffers_generator.hpp`

Circular dependencies with 1 header(s):
- `boost/beast/core/impl/buffers_generator.hpp`

#### `boost/beast/core/impl/buffers_adaptor.hpp`

Circular dependencies with 1 header(s):
- `boost/beast/core/buffers_adaptor.hpp`

#### `boost/beast/core/impl/buffers_generator.hpp`

Circular dependencies with 1 header(s):
- `boost/beast/core/buffers_generator.hpp`

#### `boost/beast/http/impl/message_generator.hpp`

Circular dependencies with 1 header(s):
- `boost/beast/http/message_generator.hpp`

#### `boost/beast/http/impl/read.hpp`

Circular dependencies with 1 header(s):
- `boost/beast/http/read.hpp`

#### `boost/beast/http/message_generator.hpp`

Circular dependencies with 1 header(s):
- `boost/beast/http/impl/message_generator.hpp`

#### `boost/beast/http/read.hpp`

Circular dependencies with 1 header(s):
- `boost/beast/http/impl/read.hpp`

### Module: `fusion`

**7 header(s) with conflicts**

#### `boost/fusion/container/deque/convert.hpp`

Circular dependencies with 1 header(s):
- `boost/fusion/container/deque/detail/convert_impl.hpp`

#### `boost/fusion/container/deque/detail/convert_impl.hpp`

Circular dependencies with 1 header(s):
- `boost/fusion/container/deque/convert.hpp`

#### `boost/fusion/container/vector/detail/next_impl.hpp`

Circular dependencies with 1 header(s):
- `boost/fusion/container/vector/vector_iterator.hpp`

#### `boost/fusion/container/vector/detail/prior_impl.hpp`

Circular dependencies with 1 header(s):
- `boost/fusion/container/vector/vector_iterator.hpp`

#### `boost/fusion/container/vector/vector_iterator.hpp`

Circular dependencies with 2 header(s):
- `boost/fusion/container/vector/detail/next_impl.hpp`
- `boost/fusion/container/vector/detail/prior_impl.hpp`

#### `boost/fusion/sequence/intrinsic/begin.hpp`

Circular dependencies with 1 header(s):
- `boost/fusion/sequence/intrinsic/detail/segmented_begin.hpp`

#### `boost/fusion/sequence/intrinsic/detail/segmented_begin.hpp`

Circular dependencies with 1 header(s):
- `boost/fusion/sequence/intrinsic/begin.hpp`

### Module: `contract`

**6 header(s) with conflicts**

#### `boost/contract/core/exception.hpp`

Circular dependencies with 1 header(s):
- `boost/contract/detail/inlined/core/exception.hpp`

#### `boost/contract/detail/checking.hpp`

Circular dependencies with 1 header(s):
- `boost/contract/detail/inlined/detail/checking.hpp`

#### `boost/contract/detail/inlined/core/exception.hpp`

Circular dependencies with 1 header(s):
- `boost/contract/core/exception.hpp`

#### `boost/contract/detail/inlined/detail/checking.hpp`

Circular dependencies with 1 header(s):
- `boost/contract/detail/checking.hpp`

#### `boost/contract/detail/inlined/old.hpp`

Circular dependencies with 1 header(s):
- `boost/contract/old.hpp`

#### `boost/contract/old.hpp`

Circular dependencies with 1 header(s):
- `boost/contract/detail/inlined/old.hpp`

### Module: `json`

**6 header(s) with conflicts**

#### `boost/json/array.hpp`

Circular dependencies with 1 header(s):
- `boost/json/value.hpp`

#### `boost/json/impl/array.hpp`

Circular dependencies with 1 header(s):
- `boost/json/value.hpp`

#### `boost/json/impl/object.hpp`

Circular dependencies with 1 header(s):
- `boost/json/value.hpp`

#### `boost/json/object.hpp`

Circular dependencies with 1 header(s):
- `boost/json/value.hpp`

#### `boost/json/value.hpp`

Circular dependencies with 5 header(s):
- `boost/json/array.hpp`
- `boost/json/impl/array.hpp`
- `boost/json/impl/object.hpp`
- `boost/json/object.hpp`
- `boost/json/value_ref.hpp`

#### `boost/json/value_ref.hpp`

Circular dependencies with 1 header(s):
- `boost/json/value.hpp`

### Module: `regex`

**6 header(s) with conflicts**

#### `boost/regex/v5/icu.hpp`

Circular dependencies with 2 header(s):
- `boost/regex/v5/u32regex_iterator.hpp`
- `boost/regex/v5/u32regex_token_iterator.hpp`

#### `boost/regex/v5/perl_matcher.hpp`

Circular dependencies with 2 header(s):
- `boost/regex/v5/perl_matcher_common.hpp`
- `boost/regex/v5/perl_matcher_non_recursive.hpp`

#### `boost/regex/v5/perl_matcher_common.hpp`

Circular dependencies with 1 header(s):
- `boost/regex/v5/perl_matcher.hpp`

#### `boost/regex/v5/perl_matcher_non_recursive.hpp`

Circular dependencies with 1 header(s):
- `boost/regex/v5/perl_matcher.hpp`

#### `boost/regex/v5/u32regex_iterator.hpp`

Circular dependencies with 1 header(s):
- `boost/regex/v5/icu.hpp`

#### `boost/regex/v5/u32regex_token_iterator.hpp`

Circular dependencies with 1 header(s):
- `boost/regex/v5/icu.hpp`

### Module: `spirit`

**6 header(s) with conflicts**

#### `boost/spirit/home/classic/core.hpp`

Circular dependencies with 1 header(s):
- `boost/spirit/home/classic/debug/parser_names.hpp`

#### `boost/spirit/home/classic/debug/parser_names.hpp`

Circular dependencies with 1 header(s):
- `boost/spirit/home/classic/core.hpp`

#### `boost/spirit/home/classic/utility/chset.hpp`

Circular dependencies with 1 header(s):
- `boost/spirit/home/classic/utility/chset_operators.hpp`

#### `boost/spirit/home/classic/utility/chset_operators.hpp`

Circular dependencies with 1 header(s):
- `boost/spirit/home/classic/utility/chset.hpp`

#### `boost/spirit/home/support/utree.hpp`

Circular dependencies with 1 header(s):
- `boost/spirit/home/support/utree/utree_traits.hpp`

#### `boost/spirit/home/support/utree/utree_traits.hpp`

Circular dependencies with 1 header(s):
- `boost/spirit/home/support/utree.hpp`

### Module: `log`

**5 header(s) with conflicts**

#### `boost/log/attributes/attribute.hpp`

Circular dependencies with 1 header(s):
- `boost/log/detail/attribute_get_value_impl.hpp`

#### `boost/log/attributes/attribute_value.hpp`

Circular dependencies with 1 header(s):
- `boost/log/detail/attribute_get_value_impl.hpp`

#### `boost/log/detail/attr_output_impl.hpp`

Circular dependencies with 1 header(s):
- `boost/log/expressions/attr.hpp`

#### `boost/log/detail/attribute_get_value_impl.hpp`

Circular dependencies with 2 header(s):
- `boost/log/attributes/attribute.hpp`
- `boost/log/attributes/attribute_value.hpp`

#### `boost/log/expressions/attr.hpp`

Circular dependencies with 1 header(s):
- `boost/log/detail/attr_output_impl.hpp`

### Module: `process`

**5 header(s) with conflicts**

#### `boost/process/v1/async.hpp`

Circular dependencies with 2 header(s):
- `boost/process/v1/detail/posix/on_exit.hpp`
- `boost/process/v1/detail/windows/on_exit.hpp`

#### `boost/process/v1/detail/config.hpp`

Circular dependencies with 1 header(s):
- `boost/process/v1/exception.hpp`

#### `boost/process/v1/detail/posix/on_exit.hpp`

Circular dependencies with 1 header(s):
- `boost/process/v1/async.hpp`

#### `boost/process/v1/detail/windows/on_exit.hpp`

Circular dependencies with 1 header(s):
- `boost/process/v1/async.hpp`

#### `boost/process/v1/exception.hpp`

Circular dependencies with 1 header(s):
- `boost/process/v1/detail/config.hpp`

### Module: `asio`

**4 header(s) with conflicts**

#### `boost/asio/connect_pipe.hpp`

Circular dependencies with 1 header(s):
- `boost/asio/impl/connect_pipe.hpp`

#### `boost/asio/executor.hpp`

Circular dependencies with 1 header(s):
- `boost/asio/impl/executor.hpp`

#### `boost/asio/impl/connect_pipe.hpp`

Circular dependencies with 1 header(s):
- `boost/asio/connect_pipe.hpp`

#### `boost/asio/impl/executor.hpp`

Circular dependencies with 1 header(s):
- `boost/asio/executor.hpp`

### Module: `chrono`

**4 header(s) with conflicts**

#### `boost/chrono/detail/inlined/process_cpu_clocks.hpp`

Circular dependencies with 1 header(s):
- `boost/chrono/process_cpu_clocks.hpp`

#### `boost/chrono/detail/inlined/thread_clock.hpp`

Circular dependencies with 1 header(s):
- `boost/chrono/thread_clock.hpp`

#### `boost/chrono/process_cpu_clocks.hpp`

Circular dependencies with 1 header(s):
- `boost/chrono/detail/inlined/process_cpu_clocks.hpp`

#### `boost/chrono/thread_clock.hpp`

Circular dependencies with 1 header(s):
- `boost/chrono/detail/inlined/thread_clock.hpp`

### Module: `cobalt`

**4 header(s) with conflicts**

#### `boost/cobalt/channel.hpp`

Circular dependencies with 1 header(s):
- `boost/cobalt/impl/channel.hpp`

#### `boost/cobalt/detail/main.hpp`

Circular dependencies with 1 header(s):
- `boost/cobalt/main.hpp`

#### `boost/cobalt/impl/channel.hpp`

Circular dependencies with 1 header(s):
- `boost/cobalt/channel.hpp`

#### `boost/cobalt/main.hpp`

Circular dependencies with 1 header(s):
- `boost/cobalt/detail/main.hpp`

### Module: `numeric`

**4 header(s) with conflicts**

#### `boost/numeric/odeint/integrate/detail/integrate_adaptive.hpp`

Circular dependencies with 1 header(s):
- `boost/numeric/odeint/integrate/detail/integrate_const.hpp`

#### `boost/numeric/odeint/integrate/detail/integrate_const.hpp`

Circular dependencies with 1 header(s):
- `boost/numeric/odeint/integrate/detail/integrate_adaptive.hpp`

#### `boost/numeric/odeint/iterator/integrate/detail/integrate_adaptive.hpp`

Circular dependencies with 1 header(s):
- `boost/numeric/odeint/iterator/integrate/detail/integrate_const.hpp`

#### `boost/numeric/odeint/iterator/integrate/detail/integrate_const.hpp`

Circular dependencies with 1 header(s):
- `boost/numeric/odeint/iterator/integrate/detail/integrate_adaptive.hpp`

### Module: `property_tree`

**4 header(s) with conflicts**

#### `boost/property_tree/detail/exception_implementation.hpp`

Circular dependencies with 1 header(s):
- `boost/property_tree/exceptions.hpp`

#### `boost/property_tree/detail/ptree_implementation.hpp`

Circular dependencies with 1 header(s):
- `boost/property_tree/ptree.hpp`

#### `boost/property_tree/exceptions.hpp`

Circular dependencies with 1 header(s):
- `boost/property_tree/detail/exception_implementation.hpp`

#### `boost/property_tree/ptree.hpp`

Circular dependencies with 1 header(s):
- `boost/property_tree/detail/ptree_implementation.hpp`

### Module: `local_function`

**3 header(s) with conflicts**

#### `boost/local_function/aux_/macro/code_/bind.hpp`

Circular dependencies with 1 header(s):
- `boost/local_function/aux_/macro/decl.hpp`

#### `boost/local_function/aux_/macro/code_/functor.hpp`

Circular dependencies with 1 header(s):
- `boost/local_function/aux_/macro/decl.hpp`

#### `boost/local_function/aux_/macro/decl.hpp`

Circular dependencies with 2 header(s):
- `boost/local_function/aux_/macro/code_/bind.hpp`
- `boost/local_function/aux_/macro/code_/functor.hpp`

### Module: `function_types`

**2 header(s) with conflicts**

#### `boost/function_types/components.hpp`

Circular dependencies with 1 header(s):
- `boost/function_types/detail/retag_default_cc.hpp`

#### `boost/function_types/detail/retag_default_cc.hpp`

Circular dependencies with 1 header(s):
- `boost/function_types/components.hpp`

### Module: `gil`

**2 header(s) with conflicts**

#### `boost/gil/algorithm.hpp`

Circular dependencies with 1 header(s):
- `boost/gil/image.hpp`

#### `boost/gil/image.hpp`

Circular dependencies with 1 header(s):
- `boost/gil/algorithm.hpp`

### Module: `graph`

**2 header(s) with conflicts**

#### `boost/graph/detail/read_graphviz_spirit.hpp`

Circular dependencies with 1 header(s):
- `boost/graph/graphviz.hpp`

#### `boost/graph/graphviz.hpp`

Circular dependencies with 1 header(s):
- `boost/graph/detail/read_graphviz_spirit.hpp`

### Module: `msm`

**2 header(s) with conflicts**

#### `boost/msm/front/euml/guard_grammar.hpp`

Circular dependencies with 1 header(s):
- `boost/msm/front/euml/state_grammar.hpp`

#### `boost/msm/front/euml/state_grammar.hpp`

Circular dependencies with 1 header(s):
- `boost/msm/front/euml/guard_grammar.hpp`

### Module: `parser`

**2 header(s) with conflicts**

#### `boost/parser/detail/text/transcode_iterator.hpp`

Circular dependencies with 1 header(s):
- `boost/parser/detail/text/unpack.hpp`

#### `boost/parser/detail/text/unpack.hpp`

Circular dependencies with 1 header(s):
- `boost/parser/detail/text/transcode_iterator.hpp`

### Module: `property_map`

**2 header(s) with conflicts**

#### `boost/property_map/property_map.hpp`

Circular dependencies with 1 header(s):
- `boost/property_map/vector_property_map.hpp`

#### `boost/property_map/vector_property_map.hpp`

Circular dependencies with 1 header(s):
- `boost/property_map/property_map.hpp`

### Module: `type_traits`

**2 header(s) with conflicts**

#### `boost/type_traits/has_trivial_assign.hpp`

Circular dependencies with 1 header(s):
- `boost/type_traits/is_assignable.hpp`

#### `boost/type_traits/is_assignable.hpp`

Circular dependencies with 1 header(s):
- `boost/type_traits/has_trivial_assign.hpp`

### Module: `wave`

**2 header(s) with conflicts**

#### `boost/wave/util/flex_string.hpp`

Circular dependencies with 1 header(s):
- `boost/wave/wave_config.hpp`

#### `boost/wave/wave_config.hpp`

Circular dependencies with 1 header(s):
- `boost/wave/util/flex_string.hpp`

### Module: `xpressive`

**2 header(s) with conflicts**

#### `boost/xpressive/detail/core/results_cache.hpp`

Circular dependencies with 1 header(s):
- `boost/xpressive/match_results.hpp`

#### `boost/xpressive/match_results.hpp`

Circular dependencies with 1 header(s):
- `boost/xpressive/detail/core/results_cache.hpp`

### Module: `safe_numerics`

**1 header(s) with conflicts**

#### `boost/safe_numerics/concept/safe_numeric.hpp`

Circular dependencies with 1 header(s):
- `boost/safe_numerics/concept/safe_numeric.hpp`

---

## Complete Alphabetical List

1. **`boost/asio/connect_pipe.hpp`** (Module: `asio`)
   - Circular dependencies with 1 header(s):
     - `boost/asio/impl/connect_pipe.hpp`

2. **`boost/asio/executor.hpp`** (Module: `asio`)
   - Circular dependencies with 1 header(s):
     - `boost/asio/impl/executor.hpp`

3. **`boost/asio/impl/connect_pipe.hpp`** (Module: `asio`)
   - Circular dependencies with 1 header(s):
     - `boost/asio/connect_pipe.hpp`

4. **`boost/asio/impl/executor.hpp`** (Module: `asio`)
   - Circular dependencies with 1 header(s):
     - `boost/asio/executor.hpp`

5. **`boost/beast/core/buffers_adaptor.hpp`** (Module: `beast`)
   - Circular dependencies with 1 header(s):
     - `boost/beast/core/impl/buffers_adaptor.hpp`

6. **`boost/beast/core/buffers_generator.hpp`** (Module: `beast`)
   - Circular dependencies with 1 header(s):
     - `boost/beast/core/impl/buffers_generator.hpp`

7. **`boost/beast/core/impl/buffers_adaptor.hpp`** (Module: `beast`)
   - Circular dependencies with 1 header(s):
     - `boost/beast/core/buffers_adaptor.hpp`

8. **`boost/beast/core/impl/buffers_generator.hpp`** (Module: `beast`)
   - Circular dependencies with 1 header(s):
     - `boost/beast/core/buffers_generator.hpp`

9. **`boost/beast/http/impl/message_generator.hpp`** (Module: `beast`)
   - Circular dependencies with 1 header(s):
     - `boost/beast/http/message_generator.hpp`

10. **`boost/beast/http/impl/read.hpp`** (Module: `beast`)
   - Circular dependencies with 1 header(s):
     - `boost/beast/http/read.hpp`

11. **`boost/beast/http/message_generator.hpp`** (Module: `beast`)
   - Circular dependencies with 1 header(s):
     - `boost/beast/http/impl/message_generator.hpp`

12. **`boost/beast/http/read.hpp`** (Module: `beast`)
   - Circular dependencies with 1 header(s):
     - `boost/beast/http/impl/read.hpp`

13. **`boost/chrono/detail/inlined/process_cpu_clocks.hpp`** (Module: `chrono`)
   - Circular dependencies with 1 header(s):
     - `boost/chrono/process_cpu_clocks.hpp`

14. **`boost/chrono/detail/inlined/thread_clock.hpp`** (Module: `chrono`)
   - Circular dependencies with 1 header(s):
     - `boost/chrono/thread_clock.hpp`

15. **`boost/chrono/process_cpu_clocks.hpp`** (Module: `chrono`)
   - Circular dependencies with 1 header(s):
     - `boost/chrono/detail/inlined/process_cpu_clocks.hpp`

16. **`boost/chrono/thread_clock.hpp`** (Module: `chrono`)
   - Circular dependencies with 1 header(s):
     - `boost/chrono/detail/inlined/thread_clock.hpp`

17. **`boost/cobalt/channel.hpp`** (Module: `cobalt`)
   - Circular dependencies with 1 header(s):
     - `boost/cobalt/impl/channel.hpp`

18. **`boost/cobalt/detail/main.hpp`** (Module: `cobalt`)
   - Circular dependencies with 1 header(s):
     - `boost/cobalt/main.hpp`

19. **`boost/cobalt/impl/channel.hpp`** (Module: `cobalt`)
   - Circular dependencies with 1 header(s):
     - `boost/cobalt/channel.hpp`

20. **`boost/cobalt/main.hpp`** (Module: `cobalt`)
   - Circular dependencies with 1 header(s):
     - `boost/cobalt/detail/main.hpp`

21. **`boost/contract/core/exception.hpp`** (Module: `contract`)
   - Circular dependencies with 1 header(s):
     - `boost/contract/detail/inlined/core/exception.hpp`

22. **`boost/contract/detail/checking.hpp`** (Module: `contract`)
   - Circular dependencies with 1 header(s):
     - `boost/contract/detail/inlined/detail/checking.hpp`

23. **`boost/contract/detail/inlined/core/exception.hpp`** (Module: `contract`)
   - Circular dependencies with 1 header(s):
     - `boost/contract/core/exception.hpp`

24. **`boost/contract/detail/inlined/detail/checking.hpp`** (Module: `contract`)
   - Circular dependencies with 1 header(s):
     - `boost/contract/detail/checking.hpp`

25. **`boost/contract/detail/inlined/old.hpp`** (Module: `contract`)
   - Circular dependencies with 1 header(s):
     - `boost/contract/old.hpp`

26. **`boost/contract/old.hpp`** (Module: `contract`)
   - Circular dependencies with 1 header(s):
     - `boost/contract/detail/inlined/old.hpp`

27. **`boost/function_types/components.hpp`** (Module: `function_types`)
   - Circular dependencies with 1 header(s):
     - `boost/function_types/detail/retag_default_cc.hpp`

28. **`boost/function_types/detail/retag_default_cc.hpp`** (Module: `function_types`)
   - Circular dependencies with 1 header(s):
     - `boost/function_types/components.hpp`

29. **`boost/fusion/container/deque/convert.hpp`** (Module: `fusion`)
   - Circular dependencies with 1 header(s):
     - `boost/fusion/container/deque/detail/convert_impl.hpp`

30. **`boost/fusion/container/deque/detail/convert_impl.hpp`** (Module: `fusion`)
   - Circular dependencies with 1 header(s):
     - `boost/fusion/container/deque/convert.hpp`

31. **`boost/fusion/container/vector/detail/next_impl.hpp`** (Module: `fusion`)
   - Circular dependencies with 1 header(s):
     - `boost/fusion/container/vector/vector_iterator.hpp`

32. **`boost/fusion/container/vector/detail/prior_impl.hpp`** (Module: `fusion`)
   - Circular dependencies with 1 header(s):
     - `boost/fusion/container/vector/vector_iterator.hpp`

33. **`boost/fusion/container/vector/vector_iterator.hpp`** (Module: `fusion`)
   - Circular dependencies with 2 header(s):
     - `boost/fusion/container/vector/detail/next_impl.hpp`
     - `boost/fusion/container/vector/detail/prior_impl.hpp`

34. **`boost/fusion/sequence/intrinsic/begin.hpp`** (Module: `fusion`)
   - Circular dependencies with 1 header(s):
     - `boost/fusion/sequence/intrinsic/detail/segmented_begin.hpp`

35. **`boost/fusion/sequence/intrinsic/detail/segmented_begin.hpp`** (Module: `fusion`)
   - Circular dependencies with 1 header(s):
     - `boost/fusion/sequence/intrinsic/begin.hpp`

36. **`boost/gil/algorithm.hpp`** (Module: `gil`)
   - Circular dependencies with 1 header(s):
     - `boost/gil/image.hpp`

37. **`boost/gil/image.hpp`** (Module: `gil`)
   - Circular dependencies with 1 header(s):
     - `boost/gil/algorithm.hpp`

38. **`boost/graph/detail/read_graphviz_spirit.hpp`** (Module: `graph`)
   - Circular dependencies with 1 header(s):
     - `boost/graph/graphviz.hpp`

39. **`boost/graph/graphviz.hpp`** (Module: `graph`)
   - Circular dependencies with 1 header(s):
     - `boost/graph/detail/read_graphviz_spirit.hpp`

40. **`boost/hana/accessors.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/struct.hpp`

41. **`boost/hana/adjust_if.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/functor.hpp`

42. **`boost/hana/any_of.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/searchable.hpp`

43. **`boost/hana/ap.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/applicative.hpp`

44. **`boost/hana/at.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/iterable.hpp`

45. **`boost/hana/chain.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/monad.hpp`

46. **`boost/hana/concat.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/monad_plus.hpp`

47. **`boost/hana/concept/applicative.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/ap.hpp`
     - `boost/hana/lift.hpp`

48. **`boost/hana/concept/comonad.hpp`** (Module: `hana`)
   - Circular dependencies with 3 header(s):
     - `boost/hana/duplicate.hpp`
     - `boost/hana/extend.hpp`
     - `boost/hana/extract.hpp`

49. **`boost/hana/concept/comparable.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/equal.hpp`

50. **`boost/hana/concept/constant.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/value.hpp`

51. **`boost/hana/concept/euclidean_ring.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/div.hpp`
     - `boost/hana/mod.hpp`

52. **`boost/hana/concept/foldable.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/fold_left.hpp`
     - `boost/hana/unpack.hpp`

53. **`boost/hana/concept/functor.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/adjust_if.hpp`
     - `boost/hana/transform.hpp`

54. **`boost/hana/concept/group.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/minus.hpp`
     - `boost/hana/negate.hpp`

55. **`boost/hana/concept/hashable.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/hash.hpp`

56. **`boost/hana/concept/iterable.hpp`** (Module: `hana`)
   - Circular dependencies with 3 header(s):
     - `boost/hana/at.hpp`
     - `boost/hana/drop_front.hpp`
     - `boost/hana/is_empty.hpp`

57. **`boost/hana/concept/logical.hpp`** (Module: `hana`)
   - Circular dependencies with 3 header(s):
     - `boost/hana/eval_if.hpp`
     - `boost/hana/not.hpp`
     - `boost/hana/while.hpp`

58. **`boost/hana/concept/monad.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/chain.hpp`
     - `boost/hana/flatten.hpp`

59. **`boost/hana/concept/monad_plus.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/concat.hpp`
     - `boost/hana/empty.hpp`

60. **`boost/hana/concept/monoid.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/plus.hpp`
     - `boost/hana/zero.hpp`

61. **`boost/hana/concept/orderable.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/less.hpp`

62. **`boost/hana/concept/product.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/first.hpp`
     - `boost/hana/second.hpp`

63. **`boost/hana/concept/ring.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/mult.hpp`
     - `boost/hana/one.hpp`

64. **`boost/hana/concept/searchable.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/any_of.hpp`
     - `boost/hana/find_if.hpp`

65. **`boost/hana/concept/struct.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/accessors.hpp`

66. **`boost/hana/div.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/euclidean_ring.hpp`

67. **`boost/hana/drop_front.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/iterable.hpp`

68. **`boost/hana/duplicate.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/concept/comonad.hpp`
     - `boost/hana/extend.hpp`

69. **`boost/hana/empty.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/monad_plus.hpp`

70. **`boost/hana/equal.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/comparable.hpp`

71. **`boost/hana/eval_if.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/concept/logical.hpp`
     - `boost/hana/if.hpp`

72. **`boost/hana/extend.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/concept/comonad.hpp`
     - `boost/hana/duplicate.hpp`

73. **`boost/hana/extract.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/comonad.hpp`

74. **`boost/hana/find_if.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/searchable.hpp`

75. **`boost/hana/first.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/product.hpp`

76. **`boost/hana/flatten.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/monad.hpp`

77. **`boost/hana/fold_left.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/foldable.hpp`

78. **`boost/hana/hash.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/hashable.hpp`

79. **`boost/hana/if.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/eval_if.hpp`

80. **`boost/hana/is_empty.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/iterable.hpp`

81. **`boost/hana/length.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/unpack.hpp`

82. **`boost/hana/less.hpp`** (Module: `hana`)
   - Circular dependencies with 3 header(s):
     - `boost/hana/concept/orderable.hpp`
     - `boost/hana/less_equal.hpp`
     - `boost/hana/lexicographical_compare.hpp`

83. **`boost/hana/less_equal.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/less.hpp`

84. **`boost/hana/lexicographical_compare.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/less.hpp`

85. **`boost/hana/lift.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/applicative.hpp`

86. **`boost/hana/minus.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/group.hpp`

87. **`boost/hana/mod.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/euclidean_ring.hpp`

88. **`boost/hana/mult.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/ring.hpp`

89. **`boost/hana/negate.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/group.hpp`

90. **`boost/hana/not.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/logical.hpp`

91. **`boost/hana/one.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/ring.hpp`

92. **`boost/hana/plus.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/monoid.hpp`

93. **`boost/hana/second.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/product.hpp`

94. **`boost/hana/transform.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/functor.hpp`

95. **`boost/hana/unpack.hpp`** (Module: `hana`)
   - Circular dependencies with 2 header(s):
     - `boost/hana/concept/foldable.hpp`
     - `boost/hana/length.hpp`

96. **`boost/hana/value.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/constant.hpp`

97. **`boost/hana/while.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/logical.hpp`

98. **`boost/hana/zero.hpp`** (Module: `hana`)
   - Circular dependencies with 1 header(s):
     - `boost/hana/concept/monoid.hpp`

99. **`boost/json/array.hpp`** (Module: `json`)
   - Circular dependencies with 1 header(s):
     - `boost/json/value.hpp`

100. **`boost/json/impl/array.hpp`** (Module: `json`)
   - Circular dependencies with 1 header(s):
     - `boost/json/value.hpp`

101. **`boost/json/impl/object.hpp`** (Module: `json`)
   - Circular dependencies with 1 header(s):
     - `boost/json/value.hpp`

102. **`boost/json/object.hpp`** (Module: `json`)
   - Circular dependencies with 1 header(s):
     - `boost/json/value.hpp`

103. **`boost/json/value.hpp`** (Module: `json`)
   - Circular dependencies with 5 header(s):
     - `boost/json/array.hpp`
     - `boost/json/impl/array.hpp`
     - `boost/json/impl/object.hpp`
     - `boost/json/object.hpp`
     - `boost/json/value_ref.hpp`

104. **`boost/json/value_ref.hpp`** (Module: `json`)
   - Circular dependencies with 1 header(s):
     - `boost/json/value.hpp`

105. **`boost/local_function/aux_/macro/code_/bind.hpp`** (Module: `local_function`)
   - Circular dependencies with 1 header(s):
     - `boost/local_function/aux_/macro/decl.hpp`

106. **`boost/local_function/aux_/macro/code_/functor.hpp`** (Module: `local_function`)
   - Circular dependencies with 1 header(s):
     - `boost/local_function/aux_/macro/decl.hpp`

107. **`boost/local_function/aux_/macro/decl.hpp`** (Module: `local_function`)
   - Circular dependencies with 2 header(s):
     - `boost/local_function/aux_/macro/code_/bind.hpp`
     - `boost/local_function/aux_/macro/code_/functor.hpp`

108. **`boost/log/attributes/attribute.hpp`** (Module: `log`)
   - Circular dependencies with 1 header(s):
     - `boost/log/detail/attribute_get_value_impl.hpp`

109. **`boost/log/attributes/attribute_value.hpp`** (Module: `log`)
   - Circular dependencies with 1 header(s):
     - `boost/log/detail/attribute_get_value_impl.hpp`

110. **`boost/log/detail/attr_output_impl.hpp`** (Module: `log`)
   - Circular dependencies with 1 header(s):
     - `boost/log/expressions/attr.hpp`

111. **`boost/log/detail/attribute_get_value_impl.hpp`** (Module: `log`)
   - Circular dependencies with 2 header(s):
     - `boost/log/attributes/attribute.hpp`
     - `boost/log/attributes/attribute_value.hpp`

112. **`boost/log/expressions/attr.hpp`** (Module: `log`)
   - Circular dependencies with 1 header(s):
     - `boost/log/detail/attr_output_impl.hpp`

113. **`boost/math/special_functions/beta.hpp`** (Module: `math`)
   - Circular dependencies with 2 header(s):
     - `boost/math/special_functions/binomial.hpp`
     - `boost/math/special_functions/detail/ibeta_inverse.hpp`

114. **`boost/math/special_functions/binomial.hpp`** (Module: `math`)
   - Circular dependencies with 1 header(s):
     - `boost/math/special_functions/beta.hpp`

115. **`boost/math/special_functions/detail/ibeta_inverse.hpp`** (Module: `math`)
   - Circular dependencies with 1 header(s):
     - `boost/math/special_functions/beta.hpp`

116. **`boost/math/special_functions/detail/igamma_inverse.hpp`** (Module: `math`)
   - Circular dependencies with 1 header(s):
     - `boost/math/special_functions/gamma.hpp`

117. **`boost/math/special_functions/erf.hpp`** (Module: `math`)
   - Circular dependencies with 1 header(s):
     - `boost/math/special_functions/gamma.hpp`

118. **`boost/math/special_functions/gamma.hpp`** (Module: `math`)
   - Circular dependencies with 2 header(s):
     - `boost/math/special_functions/detail/igamma_inverse.hpp`
     - `boost/math/special_functions/erf.hpp`

119. **`boost/math/special_functions/polygamma.hpp`** (Module: `math`)
   - Circular dependencies with 1 header(s):
     - `boost/math/special_functions/trigamma.hpp`

120. **`boost/math/special_functions/trigamma.hpp`** (Module: `math`)
   - Circular dependencies with 1 header(s):
     - `boost/math/special_functions/polygamma.hpp`

121. **`boost/math/tools/polynomial.hpp`** (Module: `math`)
   - Circular dependencies with 1 header(s):
     - `boost/math/tools/polynomial_gcd.hpp`

122. **`boost/math/tools/polynomial_gcd.hpp`** (Module: `math`)
   - Circular dependencies with 1 header(s):
     - `boost/math/tools/polynomial.hpp`

123. **`boost/msm/front/euml/guard_grammar.hpp`** (Module: `msm`)
   - Circular dependencies with 1 header(s):
     - `boost/msm/front/euml/state_grammar.hpp`

124. **`boost/msm/front/euml/state_grammar.hpp`** (Module: `msm`)
   - Circular dependencies with 1 header(s):
     - `boost/msm/front/euml/guard_grammar.hpp`

125. **`boost/mysql/field_view.hpp`** (Module: `mysql`)
   - Circular dependencies with 1 header(s):
     - `boost/mysql/impl/field_view.hpp`

126. **`boost/mysql/format_sql.hpp`** (Module: `mysql`)
   - Circular dependencies with 1 header(s):
     - `boost/mysql/impl/format_sql.hpp`

127. **`boost/mysql/impl/field_view.hpp`** (Module: `mysql`)
   - Circular dependencies with 1 header(s):
     - `boost/mysql/field_view.hpp`

128. **`boost/mysql/impl/format_sql.hpp`** (Module: `mysql`)
   - Circular dependencies with 1 header(s):
     - `boost/mysql/format_sql.hpp`

129. **`boost/mysql/impl/pfr.hpp`** (Module: `mysql`)
   - Circular dependencies with 1 header(s):
     - `boost/mysql/pfr.hpp`

130. **`boost/mysql/impl/statement.hpp`** (Module: `mysql`)
   - Circular dependencies with 1 header(s):
     - `boost/mysql/statement.hpp`

131. **`boost/mysql/impl/with_diagnostics.hpp`** (Module: `mysql`)
   - Circular dependencies with 1 header(s):
     - `boost/mysql/with_diagnostics.hpp`

132. **`boost/mysql/impl/with_params.hpp`** (Module: `mysql`)
   - Circular dependencies with 1 header(s):
     - `boost/mysql/with_params.hpp`

133. **`boost/mysql/pfr.hpp`** (Module: `mysql`)
   - Circular dependencies with 1 header(s):
     - `boost/mysql/impl/pfr.hpp`

134. **`boost/mysql/statement.hpp`** (Module: `mysql`)
   - Circular dependencies with 1 header(s):
     - `boost/mysql/impl/statement.hpp`

135. **`boost/mysql/with_diagnostics.hpp`** (Module: `mysql`)
   - Circular dependencies with 1 header(s):
     - `boost/mysql/impl/with_diagnostics.hpp`

136. **`boost/mysql/with_params.hpp`** (Module: `mysql`)
   - Circular dependencies with 1 header(s):
     - `boost/mysql/impl/with_params.hpp`

137. **`boost/numeric/odeint/integrate/detail/integrate_adaptive.hpp`** (Module: `numeric`)
   - Circular dependencies with 1 header(s):
     - `boost/numeric/odeint/integrate/detail/integrate_const.hpp`

138. **`boost/numeric/odeint/integrate/detail/integrate_const.hpp`** (Module: `numeric`)
   - Circular dependencies with 1 header(s):
     - `boost/numeric/odeint/integrate/detail/integrate_adaptive.hpp`

139. **`boost/numeric/odeint/iterator/integrate/detail/integrate_adaptive.hpp`** (Module: `numeric`)
   - Circular dependencies with 1 header(s):
     - `boost/numeric/odeint/iterator/integrate/detail/integrate_const.hpp`

140. **`boost/numeric/odeint/iterator/integrate/detail/integrate_const.hpp`** (Module: `numeric`)
   - Circular dependencies with 1 header(s):
     - `boost/numeric/odeint/iterator/integrate/detail/integrate_adaptive.hpp`

141. **`boost/parser/detail/text/transcode_iterator.hpp`** (Module: `parser`)
   - Circular dependencies with 1 header(s):
     - `boost/parser/detail/text/unpack.hpp`

142. **`boost/parser/detail/text/unpack.hpp`** (Module: `parser`)
   - Circular dependencies with 1 header(s):
     - `boost/parser/detail/text/transcode_iterator.hpp`

143. **`boost/predef/architecture/x86.h`** (Module: `predef`)
   - Circular dependencies with 2 header(s):
     - `boost/predef/architecture/x86/32.h`
     - `boost/predef/architecture/x86/64.h`

144. **`boost/predef/architecture/x86/32.h`** (Module: `predef`)
   - Circular dependencies with 1 header(s):
     - `boost/predef/architecture/x86.h`

145. **`boost/predef/architecture/x86/64.h`** (Module: `predef`)
   - Circular dependencies with 1 header(s):
     - `boost/predef/architecture/x86.h`

146. **`boost/predef/os/bsd.h`** (Module: `predef`)
   - Circular dependencies with 5 header(s):
     - `boost/predef/os/bsd/bsdi.h`
     - `boost/predef/os/bsd/dragonfly.h`
     - `boost/predef/os/bsd/free.h`
     - `boost/predef/os/bsd/net.h`
     - `boost/predef/os/bsd/open.h`

147. **`boost/predef/os/bsd/bsdi.h`** (Module: `predef`)
   - Circular dependencies with 1 header(s):
     - `boost/predef/os/bsd.h`

148. **`boost/predef/os/bsd/dragonfly.h`** (Module: `predef`)
   - Circular dependencies with 1 header(s):
     - `boost/predef/os/bsd.h`

149. **`boost/predef/os/bsd/free.h`** (Module: `predef`)
   - Circular dependencies with 1 header(s):
     - `boost/predef/os/bsd.h`

150. **`boost/predef/os/bsd/net.h`** (Module: `predef`)
   - Circular dependencies with 1 header(s):
     - `boost/predef/os/bsd.h`

151. **`boost/predef/os/bsd/open.h`** (Module: `predef`)
   - Circular dependencies with 1 header(s):
     - `boost/predef/os/bsd.h`

152. **`boost/process/v1/async.hpp`** (Module: `process`)
   - Circular dependencies with 2 header(s):
     - `boost/process/v1/detail/posix/on_exit.hpp`
     - `boost/process/v1/detail/windows/on_exit.hpp`

153. **`boost/process/v1/detail/config.hpp`** (Module: `process`)
   - Circular dependencies with 1 header(s):
     - `boost/process/v1/exception.hpp`

154. **`boost/process/v1/detail/posix/on_exit.hpp`** (Module: `process`)
   - Circular dependencies with 1 header(s):
     - `boost/process/v1/async.hpp`

155. **`boost/process/v1/detail/windows/on_exit.hpp`** (Module: `process`)
   - Circular dependencies with 1 header(s):
     - `boost/process/v1/async.hpp`

156. **`boost/process/v1/exception.hpp`** (Module: `process`)
   - Circular dependencies with 1 header(s):
     - `boost/process/v1/detail/config.hpp`

157. **`boost/property_map/property_map.hpp`** (Module: `property_map`)
   - Circular dependencies with 1 header(s):
     - `boost/property_map/vector_property_map.hpp`

158. **`boost/property_map/vector_property_map.hpp`** (Module: `property_map`)
   - Circular dependencies with 1 header(s):
     - `boost/property_map/property_map.hpp`

159. **`boost/property_tree/detail/exception_implementation.hpp`** (Module: `property_tree`)
   - Circular dependencies with 1 header(s):
     - `boost/property_tree/exceptions.hpp`

160. **`boost/property_tree/detail/ptree_implementation.hpp`** (Module: `property_tree`)
   - Circular dependencies with 1 header(s):
     - `boost/property_tree/ptree.hpp`

161. **`boost/property_tree/exceptions.hpp`** (Module: `property_tree`)
   - Circular dependencies with 1 header(s):
     - `boost/property_tree/detail/exception_implementation.hpp`

162. **`boost/property_tree/ptree.hpp`** (Module: `property_tree`)
   - Circular dependencies with 1 header(s):
     - `boost/property_tree/detail/ptree_implementation.hpp`

163. **`boost/regex/v5/icu.hpp`** (Module: `regex`)
   - Circular dependencies with 2 header(s):
     - `boost/regex/v5/u32regex_iterator.hpp`
     - `boost/regex/v5/u32regex_token_iterator.hpp`

164. **`boost/regex/v5/perl_matcher.hpp`** (Module: `regex`)
   - Circular dependencies with 2 header(s):
     - `boost/regex/v5/perl_matcher_common.hpp`
     - `boost/regex/v5/perl_matcher_non_recursive.hpp`

165. **`boost/regex/v5/perl_matcher_common.hpp`** (Module: `regex`)
   - Circular dependencies with 1 header(s):
     - `boost/regex/v5/perl_matcher.hpp`

166. **`boost/regex/v5/perl_matcher_non_recursive.hpp`** (Module: `regex`)
   - Circular dependencies with 1 header(s):
     - `boost/regex/v5/perl_matcher.hpp`

167. **`boost/regex/v5/u32regex_iterator.hpp`** (Module: `regex`)
   - Circular dependencies with 1 header(s):
     - `boost/regex/v5/icu.hpp`

168. **`boost/regex/v5/u32regex_token_iterator.hpp`** (Module: `regex`)
   - Circular dependencies with 1 header(s):
     - `boost/regex/v5/icu.hpp`

169. **`boost/safe_numerics/concept/safe_numeric.hpp`** (Module: `safe_numerics`)
   - Circular dependencies with 1 header(s):
     - `boost/safe_numerics/concept/safe_numeric.hpp`

170. **`boost/spirit/home/classic/core.hpp`** (Module: `spirit`)
   - Circular dependencies with 1 header(s):
     - `boost/spirit/home/classic/debug/parser_names.hpp`

171. **`boost/spirit/home/classic/debug/parser_names.hpp`** (Module: `spirit`)
   - Circular dependencies with 1 header(s):
     - `boost/spirit/home/classic/core.hpp`

172. **`boost/spirit/home/classic/utility/chset.hpp`** (Module: `spirit`)
   - Circular dependencies with 1 header(s):
     - `boost/spirit/home/classic/utility/chset_operators.hpp`

173. **`boost/spirit/home/classic/utility/chset_operators.hpp`** (Module: `spirit`)
   - Circular dependencies with 1 header(s):
     - `boost/spirit/home/classic/utility/chset.hpp`

174. **`boost/spirit/home/support/utree.hpp`** (Module: `spirit`)
   - Circular dependencies with 1 header(s):
     - `boost/spirit/home/support/utree/utree_traits.hpp`

175. **`boost/spirit/home/support/utree/utree_traits.hpp`** (Module: `spirit`)
   - Circular dependencies with 1 header(s):
     - `boost/spirit/home/support/utree.hpp`

176. **`boost/type_traits/has_trivial_assign.hpp`** (Module: `type_traits`)
   - Circular dependencies with 1 header(s):
     - `boost/type_traits/is_assignable.hpp`

177. **`boost/type_traits/is_assignable.hpp`** (Module: `type_traits`)
   - Circular dependencies with 1 header(s):
     - `boost/type_traits/has_trivial_assign.hpp`

178. **`boost/wave/util/flex_string.hpp`** (Module: `wave`)
   - Circular dependencies with 1 header(s):
     - `boost/wave/wave_config.hpp`

179. **`boost/wave/wave_config.hpp`** (Module: `wave`)
   - Circular dependencies with 1 header(s):
     - `boost/wave/util/flex_string.hpp`

180. **`boost/xpressive/detail/core/results_cache.hpp`** (Module: `xpressive`)
   - Circular dependencies with 1 header(s):
     - `boost/xpressive/match_results.hpp`

181. **`boost/xpressive/match_results.hpp`** (Module: `xpressive`)
   - Circular dependencies with 1 header(s):
     - `boost/xpressive/detail/core/results_cache.hpp`

---

## Statistics by Module

| Module | Headers with Conflicts |
|--------|------------------------|
| hana | 59 |
| mysql | 12 |
| math | 10 |
| predef | 9 |
| beast | 8 |
| fusion | 7 |
| contract | 6 |
| json | 6 |
| regex | 6 |
| spirit | 6 |
| log | 5 |
| process | 5 |
| asio | 4 |
| chrono | 4 |
| cobalt | 4 |
| numeric | 4 |
| property_tree | 4 |
| local_function | 3 |
| function_types | 2 |
| gil | 2 |
| graph | 2 |
| msm | 2 |
| parser | 2 |
| property_map | 2 |
| type_traits | 2 |
| wave | 2 |
| xpressive | 2 |
| safe_numerics | 1 |

---

## Self-Referencing Headers

These headers appear to reference themselves (may indicate data errors):

1. `boost/safe_numerics/concept/safe_numeric.hpp` (Module: `safe_numerics`)

