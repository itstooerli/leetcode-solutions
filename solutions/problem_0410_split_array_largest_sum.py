"""
LeetCode Problem 410: Split Array Largest Sum
Solution by Eric Li
"""

from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        prefixSumArr = [0]
        for val in nums:
            prefixSumArr.append(prefixSumArr[-1] + val)

        cache = {}
        def backtrack(prevParts, prevIdx):
            if prevParts == k - 1:
                return prefixSumArr[-1] - prefixSumArr[prevIdx]
            
            result = float('inf')
            for nextIdx in range(prevIdx + 1, len(prefixSumArr)):
                currSum = prefixSumArr[nextIdx] - prefixSumArr[prevIdx]
                if (prevParts + 1, nextIdx) in cache:
                    restMaxSum = cache[(prevParts + 1, nextIdx)]
                else:
                    restMaxSum = backtrack(prevParts + 1, nextIdx)
                    cache[(prevParts + 1, nextIdx)] = restMaxSum
                result = min(result, max(currSum, restMaxSum))
            return result
        
        return backtrack(0, 0)