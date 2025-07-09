"""
LeetCode Problem 1751: Maximum Number of Events That Can Be Attended II
Solution by Eric Li
"""

from typing import List
from sortedcontainers import SortedList

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        '''
        Classic dynamic programming problem because the best option at day 0 is the event 
        with the highest value from the remaining events at the end of that event 0
        '''
        # Sort by start time but we will loop backwards
        sortedEvents = sorted(events, key = lambda x : (x[0], x[1], x[2]))
        
        # dpArray structure = [k events used before this day][sortedEventIndex]
        dpArr = [[0 for _ in range(len(events))] for _ in range(k)]

        # The max of any day is the max of going to an event starting today + the next available event
        # -OR- not going to the end today + the max of tomorrow
        # max(dpArr[k][x]) = max(dpArr[k + 1][x_end + 1], dpArr[k][x + 1])
        
        for kUsed in range(k-1, -1, -1):
            slByStartDays = SortedList() # Implements binary search
            for eventIdx in range(len(sortedEvents)-1, -1, -1):
                declineVal = dpArr[kUsed][eventIdx + 1] if eventIdx + 1 < len(sortedEvents) else 0
                
                startDay, endDay, currVal = sortedEvents[eventIdx]

                futureVal = 0
                slIdx = slByStartDays.bisect_right((endDay, 0, eventIdx))
                if slIdx < len(slByStartDays):
                    _, _, nextEventIdx = slByStartDays[slIdx]
                    futureVal = dpArr[kUsed + 1][-nextEventIdx] if kUsed + 1 < k else 0
                acceptVal = currVal + futureVal

                dpArr[kUsed][eventIdx] = max(acceptVal, declineVal)
                slByStartDays.add((startDay, -dpArr[kUsed][eventIdx], -eventIdx))
        print(sortedEvents)
        print(dpArr)
        # Best result will be the value of dpArr[0][0]
        return dpArr[0][0]