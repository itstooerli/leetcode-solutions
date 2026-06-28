"""
LeetCode Problem 22: Generate Parentheses
Solution by Eric Li
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """Generate all combinations of well-formed parentheses with n pairs."""
        stack = [("", n, 0)] # currString, unopened, unclosed
        result = []
        while stack:
            currStr, unopenedCount, unclosedCount = stack.pop()
            if unopenedCount == 0 and unclosedCount == 0:
                result.append(currStr)
                continue
            if unopenedCount > 0:
                stack.append((currStr + "(", unopenedCount - 1, unclosedCount + 1))
            if unclosedCount > 0:
                stack.append((currStr + ")", unopenedCount, unclosedCount - 1))
        return result