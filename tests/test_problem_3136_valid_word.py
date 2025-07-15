import pytest
from solutions.problem_3136_valid_word import Solution

@pytest.mark.parametrize("word, expected",[
    ("234Adas", True),
    ("b3", False),
    ("a3$e", False),
    ("AhI", True)
])
def test_valid_word(word, expected):
    result = Solution().isValid(word)
    assert result == expected