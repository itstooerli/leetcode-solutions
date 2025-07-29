import pytest
from solutions.problem_2411_smallest_subarrays_with_maximum_bitwise_or import Solution

@pytest.mark.parametrize("nums, expected",[
    ([1,0,2,1,3], [3,3,2,2,1]),
    ([1,2], [2,1]),
    ([1,0,2,3,1], [3,3,2,1,1]),
    ([1,0,0,0,0,2,1,3], [6,6,5,4,3,2,2,1]),
    ([0], [1])
])
def test_smallest_subarrays_with_maximum_bitwise_or(nums, expected):
    result = Solution().smallestSubarrays(nums)
    assert result == expected