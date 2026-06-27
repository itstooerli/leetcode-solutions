import pytest
from solutions.problem_0028_remove_duplicates_from_sorted_array import Solution


@pytest.mark.parametrize("nums, expected_length, expected_array", [
    ([1, 1, 2], 2, [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3], 4, [0, 1, 2, 3]),
    ([1, 2, 3], 3, [1, 2, 3]),
    ([1, 1, 1], 1, [1]),
])
def test_removeDuplicates(nums, expected_length, expected_array):
    result = Solution().removeDuplicates(nums)
    assert result == expected_length
    assert nums[:result] == expected_array
