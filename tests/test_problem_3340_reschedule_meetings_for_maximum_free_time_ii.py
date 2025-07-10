import pytest
from solutions.problem_3340_reschedule_meetings_for_maximum_free_time_ii import Solution

@pytest.mark.parametrize("eventTime, startTime, endTime, expected",[
    (5, [1,3], [2,5], 2),
    (10, [0,7,9], [1,8,10], 7),
    (10, [0,3,7,9], [1,4,8,10], 6),
    (5, [0,1,2,3,4], [1,2,3,4,5], 0)
])
def test_reschedule_meetings_for_maximum_free_time_ii(eventTime, startTime, endTime, expected):
    result = Solution().maxFreeTime(eventTime, startTime, endTime)
    assert result == expected