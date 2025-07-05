import pytest
from solutions.problem_3375_minimum_operations_to_mark_array_values_equal_to_k import Solution

@pytest.mark.parametrize("nums, k, expected",[
    ([5,2,5,4,5], 2, 2),
    ([2,1,2], 2, -1),
    ([9,7,5,3], 1, 4)
])
def test_min_operations_to_make_values_equal_k(nums, k, expected):
    result = Solution().minOperations(nums, k)
    assert result == expected