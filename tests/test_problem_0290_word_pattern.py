import pytest
from solutions.problem_0290_word_pattern import Solution

@pytest.mark.parametrize("pattern, s, expected", [
    ("abba", "dog cat cat dog", True),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat dog", False),
    ("abba", "dog dog dog dog", False),
])
def test_wordPattern(pattern, s, expected):
    result = Solution().wordPattern(pattern, s)
    assert result == expected
