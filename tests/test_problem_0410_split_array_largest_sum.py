import pytest
from solutions.problem_0410_split_array_largest_sum import Solution

@pytest.mark.parametrize("nums, k, expected",[
    ([7, 2, 5, 10, 8], 2, 18),
    ([1, 4, 4], 3, 4),
    ([7, 2, 5, 10, 8], 3, 14),
    ([7, 2, 5, 10, 8], 4, 10)
])
def test_split_array(nums, k, expected):
    result = Solution().splitArray(nums, k)
    assert result == expected