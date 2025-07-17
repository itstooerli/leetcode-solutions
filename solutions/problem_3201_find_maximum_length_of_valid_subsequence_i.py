"""
LeetCode Problem 3201: Find the Maximum Length of Valid Subsequence I
Solution by Eric Li
"""

from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        '''
        Take advantage of the fact that "valid" is based on a summation % 2, meaning that the result of the
        summation can only be 0 or 1. The summation is therefore dependent on whether it is even or odd. Then,
        we have the observation of the following summation types:
        1. odd + odd = even % 2 = 0
        2. even + even = even % 2 = 0
        3. even + odd = odd % 2 = 1
        4. odd + even = odd % 2 = 1 (these need to be distinct because the subsequence can vary based on this order)
        '''
        oddOddCount = 0
        evenEvenCount = 0
        evenOddCount = 0
        eoPrevValIsEven = False     # Whether the previous value in evenOdd was even, so next # is odd
        oddEvenCount = 0
        oePrevValIsEven = True      # Whether the previous value in oddEven was even, so next # is odd
        
        for val in nums:
            isEven = (val % 2) == 0

            if isEven:
                evenEvenCount += 1
                if not oePrevValIsEven:
                    oddEvenCount += 1
                    oePrevValIsEven = True
                if not eoPrevValIsEven:
                    evenOddCount += 1
                    eoPrevValIsEven = True
            else:
                oddOddCount += 1
                if oePrevValIsEven:
                    oddEvenCount += 1
                    oePrevValIsEven = False
                if eoPrevValIsEven:
                    evenOddCount += 1
                    eoPrevValIsEven = False

        return max(oddOddCount, evenEvenCount, evenOddCount, oddEvenCount)