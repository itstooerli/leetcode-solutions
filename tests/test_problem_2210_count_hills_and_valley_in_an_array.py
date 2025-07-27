import pytest
from solutions.problem_2210_count_hills_and_valley_in_an_array import Solution

@pytest.mark.parametrize("nums, expected",[
    ([2,4,1,1,6,5], 3),
    ([6,6,5,5,4,1], 0),
    ([2,2,2,2,4,1,1,6,5], 3)
])
def test_count_hills_and_valley_in_an_array(nums, expected):
    result = Solution().countHillValley(nums)
    assert result == expected