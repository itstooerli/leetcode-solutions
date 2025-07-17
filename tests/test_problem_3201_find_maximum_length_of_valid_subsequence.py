import pytest
from solutions.problem_3201_find_maximum_length_of_valid_subsequence_i import Solution

@pytest.mark.parametrize("nums, expected",[
    ([1,2,3,4], 4),
    ([1,2,1,1,2,1,2], 6),
    ([1,3], 2)
])
def test_find_maximum_length_of_valid_subsequence_i(nums, expected):
    result = Solution().maximumLength(nums)
    assert result == expected