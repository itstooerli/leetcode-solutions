import pytest
from solutions.problem_3304_find_the_kth_character_in_string_game_i import Solution

@pytest.mark.parametrize("k, expected",[
    (5, "b"),
    (10, "c"),
    (8, "d")
])
def test_find_kth_character_in_string_game_i(k, expected):
    result = Solution().kthCharacter(k)
    assert result == expected