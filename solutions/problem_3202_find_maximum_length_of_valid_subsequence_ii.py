"""
LeetCode Problem 3202: Find the Maximum Length of Valid Subsequence II
Solution by Eric Li
"""

from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        '''
        Each val as an addend mod will consistently contribute to a specific sum mod
        '''
        ans = 0
        pattern = [[True for _ in range(k)] for _ in range(k)]
        counter = [[0 for _ in range(k)] for _ in range(k)]

        for val in nums:
            patId = val % k
            for idx in range(k):
                # Process row based on True value
                if pattern[patId][idx]:
                    counter[patId][idx] += 1
                    if not patId == idx:
                        pattern[patId][idx] = not pattern[patId][idx]
                
                # Process column based on False value
                if not pattern[idx][patId]:
                    counter[idx][patId] += 1
                    if not patId == idx:
                        pattern[idx][patId] = not pattern[idx][patId]
                
                # Set (val, val) specifically later to avoid accidently entering both conditions
                if patId == idx:
                    pattern[idx][patId] = not pattern[idx][patId]
                
                ans = max(ans, counter[patId][idx], counter[idx][patId])
        return ans
    
        '''
        %3 example

        %=0 - 0, 3, 6, 9, 12, 15, 18  => %=0 + %=0 = 3, 9, 12  (%=0)
        %=1 - 1, 4, 7, 10, 13, 16, 19 => %=1 + %=1 = 5, 11, 17 (%=1)
        %=2 - 2, 5, 8, 11, 14, 17, 20 => %=2 + %=2 = 7, 13, 19 (%=2)

        %=0 + %=1 = 1, 4, 7   = %=1
        %=1 + %=2 = 3,6,9,12  = %=0
        %=0 + %=2 = 2,5,11    = %=2
        %=1 + %=0 =           = %=1
        %=2 + %=1 =           = %=0
        %=2 + %=0 =           = %=2

        [0,0]
        [0,1]
        [0,2]
        [1,0]
        [1,1]
        [1,2]
        [2,0]
        [2,1]
        [2,2]
        '''