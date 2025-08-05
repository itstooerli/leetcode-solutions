import pytest
from solutions.problem_3477_fruits_into_baskets_ii import Solution

@pytest.mark.parametrize("fruits, baskets, expected",[
    ([4,2,5], [3,5,4], 1),
    ([3,6,1], [6,4,7], 0),
    ([1,4], [8,1], 1)
])
def test_fruits_into_baskets_ii(fruits, baskets, expected):
    result = Solution().numOfUnplacedFruits(fruits, baskets)
    assert result == expected