import pytest
from solutions.problem_1394_find_lucky_integer_in_an_array import Solution

@pytest.mark.parametrize("arr, expected",[
    ([2,2,3,4], 2),
    ([1,2,2,3,3,3], 3),
    ([2,2,2,3,3], -1)
])
def test_find_lucky_integer_in_an_array(arr, expected):
    result = Solution().findLucky(arr)
    assert result == expected