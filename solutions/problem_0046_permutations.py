"""
LeetCode Problem 46: Permutations
Solution by Eric Li
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Return all possible permutations of nums."""
        stack = [([], set())]
        result = []
        while stack:
            currPermu, visited = stack.pop()
            if len(currPermu) == len(nums):
                result.append(currPermu)
                continue
            for nextVal in nums:
                if nextVal in visited:
                    continue
                newPermu = currPermu + [nextVal]
                newSet = set(visited)
                newSet.add(nextVal)
                stack.append((newPermu, newSet))
        return result