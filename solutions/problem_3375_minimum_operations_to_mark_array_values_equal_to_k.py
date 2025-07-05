"""
LeetCode Problem 3375: Minimum Operations to Make Array Values Equal to K
Solution by Eric Li
"""

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        prev_val = None
        ans = 0
        for val in sorted_nums:
            if val < k:
                return -1
            
            if val == k:
                continue

            if prev_val is not None and val == prev_val:
                continue
            
            prev_val = val
            ans += 1

        return ans