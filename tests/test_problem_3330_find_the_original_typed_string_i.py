import pytest
from solutions.problem_3330_find_the_original_typed_string_i import Solution

@pytest.mark.parametrize("word, expected",[
    ("abbcccc", 5),
    ("abcd", 1),
    ("aaaa", 4)
])
def test_find_original_typed_string_i(word, expected):
    result = Solution().possibleStringCount(word)
    assert result == expected