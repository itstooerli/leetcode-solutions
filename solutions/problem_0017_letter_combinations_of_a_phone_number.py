"""
LeetCode Problem 17: Letter Combinations of a Phone Number
Solution by Eric Li
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mappings = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result: List[str] = []
        stack = [("", 0)]
        while stack:
            currStr, currIdx = stack.pop()
            if currIdx >= len(digits):
                result.append(currStr)
                continue
            for char in mappings[digits[currIdx]]:
                newStr = currStr + char
                stack.append((newStr, currIdx + 1))

        return result
