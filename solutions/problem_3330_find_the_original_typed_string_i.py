"""
LeetCode Problem 3330: Find the Original Typed String I
Solution by Eric Li
"""

class Solution:
    def possibleStringCount(self, word: str) -> int:
        output = 1
        for idx in range(1, len(word)):
            if word[idx] == word[idx - 1]:
                output += 1
        return output