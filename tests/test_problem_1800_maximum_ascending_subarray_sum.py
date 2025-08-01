import pytest
from solutions.problem_1800_maximum_ascending_subarray_sum import Solution

@pytest.mark.parametrize("nums, expected",[
    ([10,20,30,5,10,50], 65),
    ([10,20,30,40,50], 150),
    ([12,17,15,13,10,11,12], 33)
])
def test_maximum_ascending_subarray_sum(nums, expected):
    result = Solution().maxAscendingSum(nums)
    assert result == expected