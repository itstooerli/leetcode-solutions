"""
LeetCode Problem 3440. Reschedule Meetings for Maximum Free Time II
Solution by Eric Li
"""

from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        initialFreeTime = []
        for idx in range(len(startTime)):
            if idx == 0 and startTime[idx] > 0:
                initialFreeTime.append((startTime[idx], 0, startTime[idx]))
            
            freeStart = endTime[idx]
            if idx == len(startTime) - 1:
                freeEnd = eventTime
            else:
                freeEnd = startTime[idx + 1]
            
            freeTime = freeEnd - freeStart

            if freeTime > 0:
                initialFreeTime.append((freeTime, freeStart, freeEnd))

        initialFreeTime.sort(key = lambda x: (-x[0], x[1], x[2]))

        if len(initialFreeTime) == 0:
            return 0
        
        maxFreeTime = 0
        for idx in range(len(startTime)):
            meetingLength = endTime[idx] - startTime[idx]
            prevMeetingEnd = endTime[idx - 1] if idx > 0 else 0
            nextMeetingStart = startTime[idx + 1] if idx < len(startTime) - 1 else eventTime
            
            # Calculate sliding the meeting first
            maxFreeTime = max(maxFreeTime, nextMeetingStart - prevMeetingEnd - meetingLength)

            # Calculate moving to another free space
            for freeTimeIdx in range(len(initialFreeTime)):
                freeLength, freeStart, freeEnd = initialFreeTime[freeTimeIdx]

                # No more free time that fits meeting length
                if meetingLength > freeLength:
                    break
                
                # Already calculated sliding
                if freeStart == prevMeetingEnd or freeEnd == nextMeetingStart:
                    continue
                
                # Found valid rescheduling time
                maxFreeTime = max(maxFreeTime, nextMeetingStart - prevMeetingEnd)
                break

        return maxFreeTime