"""
LeetCode Problem 1: Two Sum
Solution by Eric Li
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        
        for idx, val in enumerate(nums):
            if val in complements:
                return [idx, complements[val]]
            
            complements[target - val] = idx
        
        return []