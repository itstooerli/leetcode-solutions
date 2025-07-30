"""
LeetCode Problem 2419: Longest Subarray with Maximum Bitwise AND
Solution by Eric Li
"""

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        Every way you slice it, it seems to only care about the longest
        consecutive of the largest number there is in the array.
        '''
        maxVal = 0
        maxCount = 0
        currCount = 0
        for val in nums:
            if val > maxVal:
                maxVal = val
                maxCount = 1
                currCount = 1
            elif val == maxVal:
                currCount += 1
                maxCount = max(maxCount, currCount)
            else:
                currCount = 0
        return maxCount