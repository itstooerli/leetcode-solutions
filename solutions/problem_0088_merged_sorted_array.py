"""
LeetCode Problem 88: Merge Sorted Array
Solution by Eric Li
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ### Sort array from end first to fill in extra space first ###
        currPtr = m + n - 1
        idx1 = m - 1
        idx2 = n - 1
        while currPtr >= 0 and idx2 >= 0:
            val1 = nums1[idx1] if idx1 >= 0 else float('-inf')
            val2 = nums2[idx2]
            if val1 > val2:
                nums1[currPtr] = val1
                idx1 -= 1
            else:
                nums1[currPtr] = val2
                idx2 -= 1
            currPtr -= 1