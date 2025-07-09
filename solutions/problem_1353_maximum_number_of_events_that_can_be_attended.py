"""
LeetCode Problem 1353: Maximum Number of Events That Can Be Attended
Solution by Eric Li
"""

from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Maximize events by sorting by start time with end time as tiebreaker
        eventsByStart = sorted(events, key = lambda x : (x[0], x[1]))
        maxDay = max(event[1] for event in events)

        pq = []
        ans = 0
        eventIdx = 0

        for day in range(1, maxDay + 1):
            # If the start day is before today, add to list of possible events by end day
            while eventIdx < len(eventsByStart) and eventsByStart[eventIdx][0] <= day:
                heapq.heappush(pq, eventsByStart[eventIdx][1])
                eventIdx += 1
            
            # If the end day is before today, then we can't go, so ignore
            while pq and pq[0] < day:
                heapq.heappop(pq)
            
            # Otherwise, pull the earliest day and attend it
            if pq:
                heapq.heappop(pq)
                ans += 1
        
        return ans