"""
LeetCode Problem 169: Majority Element
Solution by Eric Li
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Return the majority element that appears more than n/2 times.
        """
        count = 0
        candidate = 0
        for val in nums:
            if count == 0:
                candidate = val
            if val == candidate:
                count += 1
            else:
                count -= 1
        return candidate