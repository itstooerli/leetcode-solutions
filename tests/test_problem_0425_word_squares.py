import pytest
from solutions.problem_0425_word_squares import Solution

@pytest.mark.parametrize("words, expected",[
    (["area","lead","wall","lady","ball"], [["ball","area","lead","lady"],["wall","area","lead","lady"]]),
    (["abat","baba","atan","atal"], [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]),
])
def test_word_search(words, expected):
    result = Solution().wordSquares(words)
    assert sorted(result) == sorted(expected)