import pytest
from solutions.problem_2402_meeting_rooms_iii import Solution

@pytest.mark.parametrize("n, meetings, expected",[
    (2, [[0,10],[1,5],[2,7],[3,4]], 0),
    (3, [[1,20],[2,10],[3,5],[4,9],[6,8]], 1),
    (3, [[1,5],[2,7],[3,4],[0,3]], 0),
    (2, [[0,10],[1,2],[12,14],[13,15]], 0)
])
def test_meeting_rooms_iii(n, meetings, expected):
    result = Solution().mostBooked(n, meetings)
    assert result == expected