import pytest
from solutions.problem_0527_word_abbreviation import Solution

@pytest.mark.parametrize("words, expected",[
    (["like","god","internal","me","internet","interval","intension","face","intrusion"], ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]),
    (["aa","aaa"], ["aa","aaa"]),
    (["reallylongword","reallylongwoad"], ["reallylongword","reallylongwoad"]),
    (["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaa"], ["a31a","a18a"]),
    (["abcdefg","abccefg","abcckkg"],["abcd2g","abccefg","abcckkg"])
])
def test_word_abbreviation(words, expected):
    result = Solution().wordsAbbreviation(words)
    assert result == expected