import pytest
from solutions.problem_3487_maximum_unique_subarray_sum_after_deletion import Solution

@pytest.mark.parametrize("nums, expected",[
    ([1,2,3,4,5], 15),
    ([1,1,0,1,1], 1),
    ([1,2,-1,-2,1,0,-1], 3)
])
def test_maximum_unique_subarray_sum_after_deletion(nums, expected):
    result = Solution().maxSum(nums)
    assert result == expected