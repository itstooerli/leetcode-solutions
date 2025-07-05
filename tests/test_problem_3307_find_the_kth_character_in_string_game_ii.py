import pytest
from solutions.problem_3307_find_the_kth_character_in_string_game_ii import Solution

@pytest.mark.parametrize("k, operations, expected",[
    (5, [0,0,0], "a"),
    (10, [0,1,0,1], "b"),
    (3, [1,0], "a")
])
def test_find_kth_character_in_string_game_ii(k, operations, expected):
    result = Solution().kthCharacter(k, operations)
    assert result == expected