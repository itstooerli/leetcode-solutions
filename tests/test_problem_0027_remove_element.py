import pytest
from solutions.problem_0027_remove_element import Solution


@pytest.mark.parametrize("nums, val, expected_length, expected_array", [
    ([3, 2, 2, 3], 3, 2, [2, 2]),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
    ([1], 1, 0, []),
    ([1, 2], 2, 1, [1]),
    ([2, 2], 2, 0, []),
])
def test_removeElement(nums, val, expected_length, expected_array):
    result = Solution().removeElement(nums, val)
    assert result == expected_length
    assert nums[:result] == expected_array
