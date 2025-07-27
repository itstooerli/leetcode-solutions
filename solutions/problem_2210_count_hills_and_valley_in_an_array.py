"""
LeetCode Problem 2210: Count Hills and Valleys in an Array
Solution by Eric Li
"""

from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        numHillOrValley = 0
        prevPtr = 0
        currPtr = 1
        
        while currPtr < len(nums) - 1:
            prevVal = nums[prevPtr]
            currVal = nums[currPtr]
            nextVal = nums[currPtr + 1]
            
            # If equal ground, move forward
            if currVal == nextVal:
                currPtr += 1
                continue
            
            # Check if hill or valley
            if currVal > prevVal and currVal > nextVal:
                numHillOrValley += 1
            elif currVal < prevVal and currVal < nextVal:
                numHillOrValley += 1
            prevPtr = currPtr
            currPtr += 1

        return numHillOrValley