"""
LeetCode Problem 28: Remove Duplicates from Sorted Array
Solution by Eric Li
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates in-place and return the new length.
        """
        prevLoc = 0
        for idx in range(1, len(nums)):
            currVal = nums[idx]
            if currVal == nums[prevLoc]:
                continue
            prevLoc += 1
            nums[prevLoc] = currVal
        return prevLoc + 1