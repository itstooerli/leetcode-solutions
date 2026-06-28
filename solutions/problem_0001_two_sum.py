"""
LeetCode Problem 1: Two Sum
Solution by Eric Li
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Return indices of the two numbers that add up to target."""
        complements = {}
        
        for idx, val in enumerate(nums):
            if val in complements:
                return [idx, complements[val]]
            
            complements[target - val] = idx
        
        return []