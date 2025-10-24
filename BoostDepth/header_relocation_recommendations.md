# Header Relocation Recommendations Report

**Generated:** 2025-10-24 21:07:28

## ⚠️ NOTICE: Dependency Issues Detected

**The following headers have dependency issues. These are NOT included in relocation recommendations.**

### 🔄 Bidirectional Dependencies (Circular): 219 Headers

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

6. **`boost/beast/core/buffers_generator.hpp`** (Module: `beast`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/beast/core/impl/buffers_generator.hpp`

7. **`boost/beast/core/impl/buffers_adaptor.hpp`** (Module: `beast`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/beast/core/buffers_adaptor.hpp`

8. **`boost/beast/core/impl/buffers_generator.hpp`** (Module: `beast`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/beast/core/buffers_generator.hpp`

9. **`boost/beast/http/impl/message_generator.hpp`** (Module: `beast`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/beast/http/message_generator.hpp`

10. **`boost/beast/http/impl/read.hpp`** (Module: `beast`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/beast/http/read.hpp`

11. **`boost/beast/http/message_generator.hpp`** (Module: `beast`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/beast/http/impl/message_generator.hpp`

12. **`boost/beast/http/read.hpp`** (Module: `beast`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/beast/http/impl/read.hpp`

13. **`boost/callable_traits/add_member_const.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/add_member_const.hpp`

14. **`boost/callable_traits/add_member_cv.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/add_member_cv.hpp`

15. **`boost/callable_traits/add_member_lvalue_reference.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/add_member_lvalue_reference.hpp`

16. **`boost/callable_traits/add_member_rvalue_reference.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/add_member_rvalue_reference.hpp`

17. **`boost/callable_traits/add_member_volatile.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/add_member_volatile.hpp`

18. **`boost/callable_traits/add_noexcept.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/add_noexcept.hpp`

19. **`boost/callable_traits/add_transaction_safe.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/add_transaction_safe.hpp`

20. **`boost/callable_traits/add_varargs.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/add_varargs.hpp`

21. **`boost/callable_traits/apply_member_pointer.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/apply_member_pointer.hpp`

22. **`boost/callable_traits/apply_return.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/apply_return.hpp`

23. **`boost/callable_traits/args.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/args.hpp`

24. **`boost/callable_traits/class_of.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/class_of.hpp`

25. **`boost/callable_traits/function_type.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/function_type.hpp`

26. **`boost/callable_traits/has_member_qualifiers.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/has_member_qualifiers.hpp`

27. **`boost/callable_traits/has_varargs.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/has_varargs.hpp`

28. **`boost/callable_traits/has_void_return.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/has_void_return.hpp`

29. **`boost/callable_traits/is_const_member.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/is_const_member.hpp`

30. **`boost/callable_traits/is_cv_member.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/is_cv_member.hpp`

31. **`boost/callable_traits/is_invocable.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/is_invocable.hpp`

32. **`boost/callable_traits/is_lvalue_reference_member.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/is_lvalue_reference_member.hpp`

33. **`boost/callable_traits/is_noexcept.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/is_noexcept.hpp`

34. **`boost/callable_traits/is_reference_member.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/is_reference_member.hpp`

35. **`boost/callable_traits/is_rvalue_reference_member.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/is_rvalue_reference_member.hpp`

36. **`boost/callable_traits/is_transaction_safe.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/is_transaction_safe.hpp`

37. **`boost/callable_traits/is_volatile_member.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/is_volatile_member.hpp`

38. **`boost/callable_traits/qualified_class_of.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/qualified_class_of.hpp`

39. **`boost/callable_traits/remove_member_const.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/remove_member_const.hpp`

40. **`boost/callable_traits/remove_member_cv.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/remove_member_cv.hpp`

41. **`boost/callable_traits/remove_member_reference.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/remove_member_reference.hpp`

42. **`boost/callable_traits/remove_member_volatile.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/remove_member_volatile.hpp`

43. **`boost/callable_traits/remove_noexcept.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/remove_noexcept.hpp`

44. **`boost/callable_traits/remove_transaction_safe.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/remove_transaction_safe.hpp`

45. **`boost/callable_traits/remove_varargs.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/remove_varargs.hpp`

46. **`boost/callable_traits/return_type.hpp`** (Module: `callable_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/callable_traits/return_type.hpp`

47. **`boost/chrono/detail/inlined/process_cpu_clocks.hpp`** (Module: `chrono`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/chrono/process_cpu_clocks.hpp`

48. **`boost/chrono/detail/inlined/thread_clock.hpp`** (Module: `chrono`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/chrono/thread_clock.hpp`

49. **`boost/chrono/process_cpu_clocks.hpp`** (Module: `chrono`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/chrono/detail/inlined/process_cpu_clocks.hpp`

50. **`boost/chrono/thread_clock.hpp`** (Module: `chrono`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/chrono/detail/inlined/thread_clock.hpp`

51. **`boost/cobalt/channel.hpp`** (Module: `cobalt`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/cobalt/impl/channel.hpp`

52. **`boost/cobalt/detail/main.hpp`** (Module: `cobalt`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/cobalt/main.hpp`

53. **`boost/cobalt/impl/channel.hpp`** (Module: `cobalt`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/cobalt/channel.hpp`

54. **`boost/cobalt/main.hpp`** (Module: `cobalt`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/cobalt/detail/main.hpp`

55. **`boost/contract/core/config.hpp`** (Module: `contract`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/contract/core/config.hpp`

56. **`boost/contract/core/exception.hpp`** (Module: `contract`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/contract/detail/inlined/core/exception.hpp`

57. **`boost/contract/detail/checking.hpp`** (Module: `contract`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/contract/detail/inlined/detail/checking.hpp`

58. **`boost/contract/detail/inlined/core/exception.hpp`** (Module: `contract`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/contract/core/exception.hpp`

59. **`boost/contract/detail/inlined/detail/checking.hpp`** (Module: `contract`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/contract/detail/checking.hpp`

60. **`boost/contract/detail/inlined/old.hpp`** (Module: `contract`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/contract/old.hpp`

61. **`boost/contract/old.hpp`** (Module: `contract`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/contract/detail/inlined/old.hpp`

62. **`boost/function_types/components.hpp`** (Module: `function_types`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/function_types/detail/retag_default_cc.hpp`

63. **`boost/function_types/detail/retag_default_cc.hpp`** (Module: `function_types`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/function_types/components.hpp`

64. **`boost/fusion/container/deque/convert.hpp`** (Module: `fusion`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/fusion/container/deque/detail/convert_impl.hpp`

65. **`boost/fusion/container/deque/detail/convert_impl.hpp`** (Module: `fusion`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/fusion/container/deque/convert.hpp`

66. **`boost/fusion/container/vector/detail/next_impl.hpp`** (Module: `fusion`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/fusion/container/vector/vector_iterator.hpp`

67. **`boost/fusion/container/vector/detail/prior_impl.hpp`** (Module: `fusion`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/fusion/container/vector/vector_iterator.hpp`

68. **`boost/fusion/container/vector/vector_iterator.hpp`** (Module: `fusion`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/fusion/container/vector/detail/next_impl.hpp`
     - `boost/fusion/container/vector/detail/prior_impl.hpp`

69. **`boost/fusion/sequence/intrinsic/begin.hpp`** (Module: `fusion`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/fusion/sequence/intrinsic/detail/segmented_begin.hpp`

70. **`boost/fusion/sequence/intrinsic/detail/segmented_begin.hpp`** (Module: `fusion`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/fusion/sequence/intrinsic/begin.hpp`

71. **`boost/gil/algorithm.hpp`** (Module: `gil`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/gil/image.hpp`

72. **`boost/gil/image.hpp`** (Module: `gil`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/gil/algorithm.hpp`

73. **`boost/graph/detail/read_graphviz_spirit.hpp`** (Module: `graph`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/graph/graphviz.hpp`

74. **`boost/graph/graphviz.hpp`** (Module: `graph`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/graph/detail/read_graphviz_spirit.hpp`

75. **`boost/hana/accessors.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/struct.hpp`

76. **`boost/hana/adjust_if.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/functor.hpp`

77. **`boost/hana/any_of.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/searchable.hpp`

78. **`boost/hana/ap.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/applicative.hpp`

79. **`boost/hana/at.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/iterable.hpp`

80. **`boost/hana/chain.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/monad.hpp`

81. **`boost/hana/concat.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/monad_plus.hpp`

82. **`boost/hana/concept/applicative.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/ap.hpp`
     - `boost/hana/lift.hpp`

83. **`boost/hana/concept/comonad.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 3 header(s)
     - `boost/hana/duplicate.hpp`
     - `boost/hana/extend.hpp`
     - `boost/hana/extract.hpp`

84. **`boost/hana/concept/comparable.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/equal.hpp`

85. **`boost/hana/concept/constant.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/value.hpp`

86. **`boost/hana/concept/euclidean_ring.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/div.hpp`
     - `boost/hana/mod.hpp`

87. **`boost/hana/concept/foldable.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/fold_left.hpp`
     - `boost/hana/unpack.hpp`

88. **`boost/hana/concept/functor.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/adjust_if.hpp`
     - `boost/hana/transform.hpp`

89. **`boost/hana/concept/group.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/minus.hpp`
     - `boost/hana/negate.hpp`

90. **`boost/hana/concept/hashable.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/hash.hpp`

91. **`boost/hana/concept/iterable.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 3 header(s)
     - `boost/hana/at.hpp`
     - `boost/hana/drop_front.hpp`
     - `boost/hana/is_empty.hpp`

92. **`boost/hana/concept/logical.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 3 header(s)
     - `boost/hana/eval_if.hpp`
     - `boost/hana/not.hpp`
     - `boost/hana/while.hpp`

93. **`boost/hana/concept/monad.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/chain.hpp`
     - `boost/hana/flatten.hpp`

94. **`boost/hana/concept/monad_plus.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/concat.hpp`
     - `boost/hana/empty.hpp`

95. **`boost/hana/concept/monoid.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/plus.hpp`
     - `boost/hana/zero.hpp`

96. **`boost/hana/concept/orderable.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/less.hpp`

97. **`boost/hana/concept/product.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/first.hpp`
     - `boost/hana/second.hpp`

98. **`boost/hana/concept/ring.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/mult.hpp`
     - `boost/hana/one.hpp`

99. **`boost/hana/concept/searchable.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/any_of.hpp`
     - `boost/hana/find_if.hpp`

100. **`boost/hana/concept/struct.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/accessors.hpp`

101. **`boost/hana/div.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/euclidean_ring.hpp`

102. **`boost/hana/drop_front.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/iterable.hpp`

103. **`boost/hana/duplicate.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/concept/comonad.hpp`
     - `boost/hana/extend.hpp`

104. **`boost/hana/empty.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/monad_plus.hpp`

105. **`boost/hana/equal.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/comparable.hpp`

106. **`boost/hana/eval_if.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/concept/logical.hpp`
     - `boost/hana/if.hpp`

107. **`boost/hana/extend.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/concept/comonad.hpp`
     - `boost/hana/duplicate.hpp`

108. **`boost/hana/extract.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/comonad.hpp`

109. **`boost/hana/find_if.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/searchable.hpp`

110. **`boost/hana/first.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/product.hpp`

111. **`boost/hana/flatten.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/monad.hpp`

112. **`boost/hana/fold_left.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/foldable.hpp`

113. **`boost/hana/hash.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/hashable.hpp`

114. **`boost/hana/if.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/eval_if.hpp`

115. **`boost/hana/is_empty.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/iterable.hpp`

116. **`boost/hana/length.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/unpack.hpp`

117. **`boost/hana/less.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 3 header(s)
     - `boost/hana/concept/orderable.hpp`
     - `boost/hana/less_equal.hpp`
     - `boost/hana/lexicographical_compare.hpp`

118. **`boost/hana/less_equal.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/less.hpp`

119. **`boost/hana/lexicographical_compare.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/less.hpp`

120. **`boost/hana/lift.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/applicative.hpp`

121. **`boost/hana/minus.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/group.hpp`

122. **`boost/hana/mod.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/euclidean_ring.hpp`

123. **`boost/hana/mult.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/ring.hpp`

124. **`boost/hana/negate.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/group.hpp`

125. **`boost/hana/not.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/logical.hpp`

126. **`boost/hana/one.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/ring.hpp`

127. **`boost/hana/plus.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/monoid.hpp`

128. **`boost/hana/second.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/product.hpp`

129. **`boost/hana/transform.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/functor.hpp`

130. **`boost/hana/unpack.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/hana/concept/foldable.hpp`
     - `boost/hana/length.hpp`

131. **`boost/hana/value.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/constant.hpp`

132. **`boost/hana/while.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/logical.hpp`

133. **`boost/hana/zero.hpp`** (Module: `hana`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/hana/concept/monoid.hpp`

134. **`boost/json/array.hpp`** (Module: `json`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/json/value.hpp`

135. **`boost/json/basic_parser.hpp`** (Module: `json`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/json/basic_parser_impl.hpp`

136. **`boost/json/basic_parser_impl.hpp`** (Module: `json`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/json/basic_parser.hpp`

137. **`boost/json/impl/array.hpp`** (Module: `json`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/json/value.hpp`

138. **`boost/json/impl/object.hpp`** (Module: `json`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/json/value.hpp`

139. **`boost/json/object.hpp`** (Module: `json`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/json/value.hpp`

140. **`boost/json/value.hpp`** (Module: `json`)
   - **Circular dependencies with:** 5 header(s)
     - `boost/json/array.hpp`
     - `boost/json/object.hpp`
     - `boost/json/value_ref.hpp`
     - `boost/json/impl/array.hpp`
     - `boost/json/impl/object.hpp`

141. **`boost/json/value_ref.hpp`** (Module: `json`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/json/value.hpp`

142. **`boost/local_function/aux_/macro/code_/bind.hpp`** (Module: `local_function`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/local_function/aux_/macro/decl.hpp`

143. **`boost/local_function/aux_/macro/code_/functor.hpp`** (Module: `local_function`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/local_function/aux_/macro/decl.hpp`

144. **`boost/local_function/aux_/macro/decl.hpp`** (Module: `local_function`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/local_function/aux_/macro/code_/bind.hpp`
     - `boost/local_function/aux_/macro/code_/functor.hpp`

145. **`boost/log/attributes/attribute.hpp`** (Module: `log`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/log/detail/attribute_get_value_impl.hpp`

146. **`boost/log/attributes/attribute_value.hpp`** (Module: `log`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/log/detail/attribute_get_value_impl.hpp`

147. **`boost/log/detail/attr_output_impl.hpp`** (Module: `log`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/log/expressions/attr.hpp`

148. **`boost/log/detail/attribute_get_value_impl.hpp`** (Module: `log`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/log/attributes/attribute.hpp`
     - `boost/log/attributes/attribute_value.hpp`

149. **`boost/log/expressions/attr.hpp`** (Module: `log`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/log/detail/attr_output_impl.hpp`

150. **`boost/math/special_functions/beta.hpp`** (Module: `math`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/math/special_functions/binomial.hpp`
     - `boost/math/special_functions/detail/ibeta_inverse.hpp`

151. **`boost/math/special_functions/binomial.hpp`** (Module: `math`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/math/special_functions/beta.hpp`

152. **`boost/math/special_functions/detail/ibeta_inverse.hpp`** (Module: `math`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/math/special_functions/beta.hpp`

153. **`boost/math/special_functions/detail/igamma_inverse.hpp`** (Module: `math`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/math/special_functions/gamma.hpp`

154. **`boost/math/special_functions/erf.hpp`** (Module: `math`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/math/special_functions/gamma.hpp`

155. **`boost/math/special_functions/gamma.hpp`** (Module: `math`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/math/special_functions/detail/igamma_inverse.hpp`
     - `boost/math/special_functions/erf.hpp`

156. **`boost/math/special_functions/polygamma.hpp`** (Module: `math`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/math/special_functions/trigamma.hpp`

157. **`boost/math/special_functions/trigamma.hpp`** (Module: `math`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/math/special_functions/polygamma.hpp`

158. **`boost/math/tools/polynomial.hpp`** (Module: `math`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/math/tools/polynomial_gcd.hpp`

159. **`boost/math/tools/polynomial_gcd.hpp`** (Module: `math`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/math/tools/polynomial.hpp`

160. **`boost/msm/front/euml/guard_grammar.hpp`** (Module: `msm`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/msm/front/euml/state_grammar.hpp`

161. **`boost/msm/front/euml/state_grammar.hpp`** (Module: `msm`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/msm/front/euml/guard_grammar.hpp`

162. **`boost/mysql/field_view.hpp`** (Module: `mysql`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/mysql/impl/field_view.hpp`

163. **`boost/mysql/format_sql.hpp`** (Module: `mysql`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/mysql/impl/format_sql.hpp`

164. **`boost/mysql/impl/field_view.hpp`** (Module: `mysql`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/mysql/field_view.hpp`

165. **`boost/mysql/impl/format_sql.hpp`** (Module: `mysql`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/mysql/format_sql.hpp`

166. **`boost/mysql/impl/pfr.hpp`** (Module: `mysql`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/mysql/pfr.hpp`

167. **`boost/mysql/impl/statement.hpp`** (Module: `mysql`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/mysql/statement.hpp`

168. **`boost/mysql/impl/with_diagnostics.hpp`** (Module: `mysql`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/mysql/with_diagnostics.hpp`

169. **`boost/mysql/impl/with_params.hpp`** (Module: `mysql`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/mysql/with_params.hpp`

170. **`boost/mysql/pfr.hpp`** (Module: `mysql`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/mysql/impl/pfr.hpp`

171. **`boost/mysql/statement.hpp`** (Module: `mysql`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/mysql/impl/statement.hpp`

172. **`boost/mysql/with_diagnostics.hpp`** (Module: `mysql`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/mysql/impl/with_diagnostics.hpp`

173. **`boost/mysql/with_params.hpp`** (Module: `mysql`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/mysql/impl/with_params.hpp`

174. **`boost/numeric/odeint/integrate/detail/integrate_adaptive.hpp`** (Module: `numeric`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/numeric/odeint/integrate/detail/integrate_const.hpp`

175. **`boost/numeric/odeint/integrate/detail/integrate_const.hpp`** (Module: `numeric`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/numeric/odeint/integrate/detail/integrate_adaptive.hpp`

176. **`boost/numeric/odeint/iterator/integrate/detail/integrate_adaptive.hpp`** (Module: `numeric`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/numeric/odeint/iterator/integrate/detail/integrate_const.hpp`

177. **`boost/numeric/odeint/iterator/integrate/detail/integrate_const.hpp`** (Module: `numeric`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/numeric/odeint/iterator/integrate/detail/integrate_adaptive.hpp`

178. **`boost/parser/detail/text/transcode_iterator.hpp`** (Module: `parser`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/parser/detail/text/unpack.hpp`

179. **`boost/parser/detail/text/unpack.hpp`** (Module: `parser`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/parser/detail/text/transcode_iterator.hpp`

180. **`boost/predef/architecture/x86.h`** (Module: `predef`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/predef/architecture/x86/32.h`
     - `boost/predef/architecture/x86/64.h`

181. **`boost/predef/architecture/x86/32.h`** (Module: `predef`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/predef/architecture/x86.h`

182. **`boost/predef/architecture/x86/64.h`** (Module: `predef`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/predef/architecture/x86.h`

183. **`boost/predef/hardware/simd.h`** (Module: `predef`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/predef/hardware/simd.h`

184. **`boost/predef/os/bsd.h`** (Module: `predef`)
   - **Circular dependencies with:** 5 header(s)
     - `boost/predef/os/bsd/bsdi.h`
     - `boost/predef/os/bsd/dragonfly.h`
     - `boost/predef/os/bsd/free.h`
     - `boost/predef/os/bsd/open.h`
     - `boost/predef/os/bsd/net.h`

185. **`boost/predef/os/bsd/bsdi.h`** (Module: `predef`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/predef/os/bsd.h`

186. **`boost/predef/os/bsd/dragonfly.h`** (Module: `predef`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/predef/os/bsd.h`

187. **`boost/predef/os/bsd/free.h`** (Module: `predef`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/predef/os/bsd.h`

188. **`boost/predef/os/bsd/net.h`** (Module: `predef`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/predef/os/bsd.h`

189. **`boost/predef/os/bsd/open.h`** (Module: `predef`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/predef/os/bsd.h`

190. **`boost/process/v1/async.hpp`** (Module: `process`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/process/v1/detail/posix/on_exit.hpp`
     - `boost/process/v1/detail/windows/on_exit.hpp`

191. **`boost/process/v1/detail/config.hpp`** (Module: `process`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/process/v1/exception.hpp`

192. **`boost/process/v1/detail/posix/on_exit.hpp`** (Module: `process`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/process/v1/async.hpp`

193. **`boost/process/v1/detail/windows/on_exit.hpp`** (Module: `process`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/process/v1/async.hpp`

194. **`boost/process/v1/exception.hpp`** (Module: `process`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/process/v1/detail/config.hpp`

195. **`boost/property_map/property_map.hpp`** (Module: `property_map`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/property_map/vector_property_map.hpp`

196. **`boost/property_map/vector_property_map.hpp`** (Module: `property_map`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/property_map/property_map.hpp`

197. **`boost/property_tree/detail/exception_implementation.hpp`** (Module: `property_tree`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/property_tree/exceptions.hpp`

198. **`boost/property_tree/detail/ptree_implementation.hpp`** (Module: `property_tree`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/property_tree/ptree.hpp`

199. **`boost/property_tree/exceptions.hpp`** (Module: `property_tree`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/property_tree/detail/exception_implementation.hpp`

200. **`boost/property_tree/ptree.hpp`** (Module: `property_tree`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/property_tree/detail/ptree_implementation.hpp`

201. **`boost/regex/v5/icu.hpp`** (Module: `regex`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/regex/v5/u32regex_iterator.hpp`
     - `boost/regex/v5/u32regex_token_iterator.hpp`

202. **`boost/regex/v5/perl_matcher.hpp`** (Module: `regex`)
   - **Circular dependencies with:** 2 header(s)
     - `boost/regex/v5/perl_matcher_non_recursive.hpp`
     - `boost/regex/v5/perl_matcher_common.hpp`

203. **`boost/regex/v5/perl_matcher_common.hpp`** (Module: `regex`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/regex/v5/perl_matcher.hpp`

204. **`boost/regex/v5/perl_matcher_non_recursive.hpp`** (Module: `regex`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/regex/v5/perl_matcher.hpp`

205. **`boost/regex/v5/u32regex_iterator.hpp`** (Module: `regex`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/regex/v5/icu.hpp`

206. **`boost/regex/v5/u32regex_token_iterator.hpp`** (Module: `regex`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/regex/v5/icu.hpp`

207. **`boost/safe_numerics/concept/safe_numeric.hpp`** (Module: `safe_numerics`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/safe_numerics/concept/safe_numeric.hpp`

208. **`boost/spirit/home/classic/core.hpp`** (Module: `spirit`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/spirit/home/classic/debug/parser_names.hpp`

209. **`boost/spirit/home/classic/debug/parser_names.hpp`** (Module: `spirit`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/spirit/home/classic/core.hpp`

210. **`boost/spirit/home/classic/utility/chset.hpp`** (Module: `spirit`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/spirit/home/classic/utility/chset_operators.hpp`

211. **`boost/spirit/home/classic/utility/chset_operators.hpp`** (Module: `spirit`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/spirit/home/classic/utility/chset.hpp`

212. **`boost/spirit/home/support/utree.hpp`** (Module: `spirit`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/spirit/home/support/utree/utree_traits.hpp`

213. **`boost/spirit/home/support/utree/utree_traits.hpp`** (Module: `spirit`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/spirit/home/support/utree.hpp`

214. **`boost/type_traits/has_trivial_assign.hpp`** (Module: `type_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/type_traits/is_assignable.hpp`

215. **`boost/type_traits/is_assignable.hpp`** (Module: `type_traits`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/type_traits/has_trivial_assign.hpp`

216. **`boost/wave/util/flex_string.hpp`** (Module: `wave`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/wave/wave_config.hpp`

217. **`boost/wave/wave_config.hpp`** (Module: `wave`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/wave/util/flex_string.hpp`

218. **`boost/xpressive/detail/core/results_cache.hpp`** (Module: `xpressive`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/xpressive/match_results.hpp`

219. **`boost/xpressive/match_results.hpp`** (Module: `xpressive`)
   - **Circular dependencies with:** 1 header(s)
     - `boost/xpressive/detail/core/results_cache.hpp`

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

