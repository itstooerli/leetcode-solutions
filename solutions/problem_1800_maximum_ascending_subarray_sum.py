"""
LeetCode Problem 1800: Maximum Ascending Subarray Sum
Solution by Eric Li
"""

from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        currSum = 0
        for idx in range(len(nums)):
            if idx == 0:
                currSum = nums[idx]
            elif nums[idx] > nums[idx - 1]:
                currSum += nums[idx]
            else:
                currSum = nums[idx]
            maxSum = max(maxSum, currSum)
        return maxSum
