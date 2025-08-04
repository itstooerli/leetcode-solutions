import pytest
from solutions.problem_0904_fruit_into_baskets import Solution

@pytest.mark.parametrize("fruits, expected",[
    ([1,2,1], 3),
    ([0,1,2,2], 3),
    ([1,1,1,1,2,2,2,3,3,3,3,3,3], 9),
])
def test_fruit_into_baskets(fruits, expected):
    result = Solution().totalFruit(fruits)
    assert result == expected