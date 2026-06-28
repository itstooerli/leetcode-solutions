"""
LeetCode Problem 3487: Maximum Unique Subarray Sum After Deletion
Solution by Eric Li
"""

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        '''
        This is simply adding up all unique elements since we can delete anything we want.
        Special case of negative numbers should be minimized
        '''
        uniqueElements = set()
        maxNegative = -float('inf')
        for val in nums:
            if val >= 0 and val not in uniqueElements:
                uniqueElements.add(val)
            elif val < 0:
                maxNegative = max(maxNegative, val)
        
        return sum(uniqueElements) if len(uniqueElements) > 0 else maxNegative