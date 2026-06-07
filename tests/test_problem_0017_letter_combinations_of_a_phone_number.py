import pytest
from solutions.problem_0017_letter_combinations_of_a_phone_number import Solution


@pytest.mark.parametrize("digits, expected", [
    ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ("2", ["a", "b", "c"]),
])
def test_letter_combinations(digits, expected):
    result = Solution().letterCombinations(digits)
    assert sorted(result) == sorted(expected)
