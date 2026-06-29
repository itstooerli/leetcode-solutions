import pytest
from solutions.problem_0045_jump_game_ii import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([1], 0),
        ([1, 1, 1, 1], 3),
    ],
)
def test_jump(nums, expected):
    result = Solution().jump(nums)
    assert result == expected
