import pytest
from solutions.problem_0077_combinations import Solution


@pytest.mark.parametrize("n, k, expected", [
    (1, 1, [[1]]),
    (2, 1, [[1], [2]]),
    (3, 2, [[1,2], [1,3], [2,3]]),
    (4, 2, [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]),
])
def test_combine(n, k, expected):
    result = Solution().combine(n, k)
    assert sorted(result) == sorted(expected)
    ([1], [[1]])
