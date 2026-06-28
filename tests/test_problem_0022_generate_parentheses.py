import pytest
from solutions.problem_0022_generate_parentheses import Solution


@pytest.mark.parametrize("n, expected", [
    (3, ["((()))","(()())","(())()","()(())","()()()"]),
    (1, ["()"]),
])
def test_generate_parenthesis(n, expected):
    result = Solution().generateParenthesis(n)
    assert sorted(result) == sorted(expected)
