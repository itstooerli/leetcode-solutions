"""
LeetCode Problem 77: Combinations
Solution by Eric Li
"""

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < 1:
            return []

        stack = []
        for initVal in range(1, n + 1):
            stack.append([initVal])
        
        result = []
        while stack:
            currCombo = stack.pop()
            if len(currCombo) == k:
                result.append(currCombo)
                continue
            for nextVal in range(currCombo[-1] + 1, n + 1):
                stack.append(currCombo + [nextVal])
        return result