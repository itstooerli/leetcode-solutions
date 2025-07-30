import pytest
from solutions.problem_2419_longest_subarray_with_maximum_bitwise_and import Solution

@pytest.mark.parametrize("nums, expected",[
    ([1,2,3,3,2,2], 2),
    ([1,2,3,4], 1),
    ([1,2,3,5,4], 1),
    ([1,2,3,5,1,5], 1),
    ([1,2,3,5,1,5,1,1,1,5,5,5,5,5,2,2,2,2,2], 5)
])
def test_longest_subarray_with_maximum_bitwise_and(nums, expected):
    result = Solution().longestSubarray(nums)
    assert result == expected