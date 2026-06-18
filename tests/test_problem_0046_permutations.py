import pytest
from solutions.problem_0046_permutations import Solution


@pytest.mark.parametrize("nums, expected", [
    ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    ([0,1], [[0,1],[1,0]]),
    ([1], [[1]]),
])
def test_permute(nums, expected):
    result = Solution().permute(nums)
    assert sorted(result) == sorted(expected)