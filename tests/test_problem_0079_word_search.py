import pytest
from solutions.problem_0079_word_search import Solution

@pytest.mark.parametrize("board, word, expected",[
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False)
])
def test_word_search(board, word, expected):
    result = Solution().exist(board, word)
    assert result == expected