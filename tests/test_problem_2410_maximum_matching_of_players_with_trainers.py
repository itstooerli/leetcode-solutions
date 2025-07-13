import pytest
from solutions.problem_2410_maximum_matching_of_players_with_trainers import Solution

@pytest.mark.parametrize("players, trainers, expected",[
    ([4,7,9], [8,2,5,8], 2),
    ([1,1,1], [10], 1),
    ([1,2,3,4,5], [1,2,3,4,5], 5),
])
def test_maximum_matching_of_players_to_trainers(players, trainers, expected):
    result = Solution().matchPlayersAndTrainers(players, trainers)
    assert result == expected