import pytest
from solutions.problem_3202_find_maximum_length_of_valid_subsequence_ii import Solution

@pytest.mark.parametrize("nums, k, expected",[
    ([1,2,3,4,5], 2, 5),
    ([1,4,2,3,1,4], 3, 4)
])
def test_find_maximum_length_of_valid_subsequence_ii(nums, k, expected):
    result = Solution().maximumLength(nums, k)
    assert result == expected