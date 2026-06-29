"""
LeetCode Problem 45: Jump Game II
Solution by Eric Li
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """Return the minimum number of jumps required to reach the last index."""
        prevFurthestIdx = 0
        nextFurthestIdx = 0
        numJumps = 0
        for idx in range(len(nums)):
            if prevFurthestIdx >= len(nums) - 1:
                return numJumps
            nextFurthestIdx = max(nextFurthestIdx, idx + nums[idx])
            if idx == prevFurthestIdx:
                prevFurthestIdx = nextFurthestIdx
                numJumps += 1
        return numJumps