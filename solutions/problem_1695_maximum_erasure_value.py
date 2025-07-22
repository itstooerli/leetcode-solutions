"""
LeetCode Problem 1695: Maximum Erasure Value
Solution by Eric Li
"""

from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        '''
        Two pointer approach - Advance right pointer through array until a duplicate is found,
        then move left pointer until duplicate is removed.
        '''
        leftPtr = 0
        rightPtr = 0
        maxSum = 0
        currSum = 0
        currSet = set()
        while rightPtr < len(nums):
            currSum += nums[rightPtr]
            if nums[rightPtr] not in currSet:
                currSet.add(nums[rightPtr])
            else:
                while nums[leftPtr] != nums[rightPtr]:
                    currSum -= nums[leftPtr]
                    currSet.remove(nums[leftPtr])
                    leftPtr += 1
                currSum -= nums[leftPtr]
                leftPtr += 1
            maxSum = max(maxSum, currSum)
            rightPtr += 1
        return maxSum