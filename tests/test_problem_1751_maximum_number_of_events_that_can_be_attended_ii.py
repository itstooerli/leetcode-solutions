import pytest
from solutions.problem_1751_maximum_number_of_events_that_can_be_attended_ii import Solution

@pytest.mark.parametrize("events, k, expected",[
    ([[1,2,4],[3,4,3],[2,3,1]], 2, 7),
    ([[1,2,4],[3,4,3],[2,3,10]], 2, 10),
    ([[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3, 9),
    ([[74,91,40]], 1, 40)
])
def test_maximum_number_of_events_ii(events, k, expected):
    result = Solution().maxValue(events, k)
    assert result == expected