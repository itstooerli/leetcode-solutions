"""
LeetCode Problem 3307: Find the K-th Character in a String Game II
Solution by Eric Li
"""

from typing import List
from math import floor, ceil, log2

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        if k == 1:
            return 'a'
        
        prevK = k - 2 ** (floor(log2(k - 1)))
        prevChar = self.kthCharacter(prevK, operations)
        opIdx = ceil(log2(k)) - 1
        if operations[opIdx] == 0:
            currChar = ord(prevChar)
        elif operations[opIdx] == 1:
            currChar = (((ord(prevChar) + 1) - ord('a')) % 26) + ord('a')

        return chr(currChar)
        '''
        See problem #3304 for original logic.
        Need to find the idx that this copy relies on and then perform the operation on it.
        - The previous k is subtracting the lower power of 2 from the current k.
        - The operations index is the power of 2 closest to k
        '''

        # [1,0,0] abababab
        # [0,1,0] aabbaabb
        # [0,0,1] aaaabbbb
        # [0,1,1] aabbbbcc
        # [1,1,0] abbcabbc
        # [1,1,1] abbcbccd
        # [1,0,1] ababbcbc

        # 1
        # 2 > 1
        # 3 > 1
        # 4 > 2 > 1
        # 5 > 1
        # 6 > 2 > 1
        # 7 > 3 > 1
        # 8 > 4 > 2 > 1