"""
LeetCode Problem 55: Jump Game
Solution by Eric Li
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Determine whether it is possible to reach the last index from the start."""
        latestIdx = len(nums) - 1
        for currIdx in range(len(nums) - 2, -1, -1):
            if currIdx + nums[currIdx] >= latestIdx:
                latestIdx = currIdx
        return latestIdx == 0