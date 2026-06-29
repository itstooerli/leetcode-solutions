import pytest
from solutions.problem_0055_jump_game import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([1, 0, 0], False),
    ],
)
def test_canJump(nums, expected):
    result = Solution().canJump(nums)
    assert result == expected
