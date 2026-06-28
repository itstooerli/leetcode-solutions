"""
LeetCode Problem 134: Gas Station
Solution by Eric Li
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Return starting station index to complete a circular tour, or -1 if impossible."""
        totalSurplus = 0
        runningGas = 0
        result = -1
        for idx, val in enumerate(gas):
            if result >= 0 and runningGas + val < cost[idx]:
                # if we had a starting position
                # and we determine we can't make it, we 
                # reset the starting position
                result = -1
                runningGas = 0
            
            if result == -1 and val >= cost[idx]:
                # if we haven't found a starting place yet
                # and we have enough gas to reach the next station
                # this is a possible starting position
                result = idx
            
            netGas = val - cost[idx]
            totalSurplus += netGas
            if result >= 0:
                runningGas += netGas

        if totalSurplus < 0:
            return -1
        return result
