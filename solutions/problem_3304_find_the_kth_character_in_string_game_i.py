"""
LeetCode Problem 3304: Find the K-th Character in a String Game I
Solution by Eric Li
"""

from math import floor, log2
class Solution:
    def kthCharacter(self, k: int) -> str:
        #if k == 1:
        #    return 'a'

        #return chr(ord(self.kthCharacter(k - 2**(floor(math.log2(k - 1))))) + 1)

        currK = k
        increment = 0
        while currK > 1:
            currK = currK - 2 ** (floor(log2(currK - 1)))
            increment += 1
        
        return chr(ord('a') + increment % 26)

        '''
        a 2^0 -->               [0]
        ab 2^1 -->              [0, 1]
        abbc 2^2 -->            [0, 1, 1, 2]
        abbcbccd 2^3 -->        [0, 1, 1, 2, 1, 2, 2, 3]
        abbcbccdbccdcdde 2^4    [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

        k
        1k  = 0
        2k  = 1 = 1k + 1
        3k  = 1 = 1k + 1
        4k  = 2 = 2k + 1 = 1k + 1 + 1
        5k  = 1 = 1k + 1 
        6k  = 2 = 2k + 1 = 1k + 1 + 1
        7k  = 2 = 3k + 1 = 1k + 1 + 1
        8k  = 3 = 4k + 1 = 1k + 1 + 1 + 1
        9k  = 1 = 1k + 1
        10k = 2 = 2k + 1
        11k = 2 = 3k + 1
        12k = 3 = 4k + 1
        13k = 2 = 5k + 1
        '''