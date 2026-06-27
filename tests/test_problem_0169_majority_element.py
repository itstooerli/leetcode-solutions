import pytest
from solutions.problem_0169_majority_element import Solution


@pytest.mark.parametrize("nums, expected", [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([1], 1),
    ([6, 5, 5], 5),
])
def test_majorityElement(nums, expected):
    result = Solution().majorityElement(nums)
    assert result == expected
