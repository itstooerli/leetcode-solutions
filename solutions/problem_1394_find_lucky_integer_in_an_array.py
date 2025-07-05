"""
LeetCode Problem 1394: Find Lucky Integer in an Array
Solution by Eric Li
"""

from typing import List
from collections import defaultdict

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Count the frequency (could use Counter())
        dataDict = defaultdict(int)
        for val in arr:
            dataDict[val] += 1
        
        # Check the frequency for luck integers
        ans = -1
        for key in dataDict:
            if key == dataDict[key]:
                ans = max(ans, dataDict[key])
        
        return ans
        
        '''
        It's probably easiest to sort, but counting once and then checking again is O(n).
        '''