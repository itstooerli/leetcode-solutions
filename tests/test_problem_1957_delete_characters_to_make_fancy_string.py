import pytest
from solutions.problem_1957_delete_characters_to_make_fancy_string import Solution

@pytest.mark.parametrize("s, expected",[
    ("leeetcode", "leetcode"),
    ("aaabaaaa", "aabaa"),
    ("aab", "aab")
])
def test_delete_characters_to_make_fancy_string(s, expected):
    result = Solution().makeFancyString(s)
    assert result == expected