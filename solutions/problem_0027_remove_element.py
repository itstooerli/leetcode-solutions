"""
LeetCode Problem 27: Remove Element
Solution by Eric Li
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all instances of val in-place and return the number of elements left.
        """
        emptyLoc = 0
        for arrVal in nums:
            if arrVal == val:
                continue
            nums[emptyLoc] = arrVal
            emptyLoc += 1
        return emptyLoc