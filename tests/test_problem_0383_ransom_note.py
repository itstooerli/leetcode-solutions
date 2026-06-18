import pytest
from solutions.problem_0383_ransom_note import Solution

@pytest.mark.parametrize("ransomNote, magazine, expected",[
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True)
])
def test_can_construct(ransomNote, magazine, expected):
    result = Solution().canConstruct(ransomNote, magazine)
    assert result == expected