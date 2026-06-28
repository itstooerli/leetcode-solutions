"""
LeetCode Problem 39: Combination Sum
Solution by Eric Li
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Return all unique combinations of candidates that sum to target."""
        stack = [([], 0, 0)]
        result = []
        while stack:
            currCombo, minIdx, currSum = stack.pop()
            if currSum == target:
                result.append(currCombo)
                continue
            elif currSum > target:
                continue
            for idx in range(minIdx, len(candidates)):
                nextVal = candidates[idx]
                stack.append((currCombo + [nextVal], idx, currSum + nextVal))
        return result