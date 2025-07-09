import pytest
from solutions.problem_1353_maximum_number_of_events_that_can_be_attended import Solution

@pytest.mark.parametrize("events, expected",[
    ([[1,2],[2,3],[3,4]], 3),
    ([[1,2],[2,3],[3,4],[1,2]], 4),
    ([[1,3],[1,3],[1,3],[3,4]], 4),
    ([[1,5],[1,5],[1,5],[2,3],[2,3]], 5)
])
def test_maximum_number_of_events(events, expected):
    result = Solution().maxEvents(events)
    assert result == expected