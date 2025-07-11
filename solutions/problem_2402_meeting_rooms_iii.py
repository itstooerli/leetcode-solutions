"""
LeetCode Problem 2402: Meetings Rooms III
Solution by Eric Li
"""

from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort by start time
        meetings.sort()
    
        openRooms = [(x, 0) for x in range(n)]
        heapq.heapify(openRooms)
        activeMeetings = []
        meetingsPerRoom = [0 for _ in range(n)]
        for startTime, endTime in meetings:
            # Update open rooms based on new start time
            while len(activeMeetings) > 0 and activeMeetings[0][0] <= startTime:
                prevMeetingEnd, openRoomId = heapq.heappop(activeMeetings)
                heapq.heappush(openRooms, (openRoomId, prevMeetingEnd))
            
            if len(openRooms) > 0:
                # If open room, take the open room
                openRoomId, prevMeetingEnd = heapq.heappop(openRooms)
                heapq.heappush(activeMeetings, (max(startTime, prevMeetingEnd) + endTime - startTime, openRoomId))
            else:
                # If no room, need to time skip
                prevMeetingEnd, openRoomId = heapq.heappop(activeMeetings)
                heapq.heappush(openRooms, (openRoomId, prevMeetingEnd))

                # Make sure to pop all meetings that end at the same time
                while len(activeMeetings) > 0 and activeMeetings[0][0] <= prevMeetingEnd:
                    tempMeetingEnd, openRoomId = heapq.heappop(activeMeetings)
                    heapq.heappush(openRooms, (openRoomId, tempMeetingEnd))
                
                # Now take an open room
                openRoomId, prevMeetingEnd = heapq.heappop(openRooms)
                heapq.heappush(activeMeetings, (prevMeetingEnd + endTime - startTime, openRoomId))

            # Log the meeting
            meetingsPerRoom[openRoomId] += 1
        
        # Find the room with the most meetings, tie to the lowest index
        maxVal = -1
        maxIdx = -1
        for idx, val in enumerate(meetingsPerRoom):
            if val <= maxVal:
                continue
            maxVal = val
            maxIdx = idx
        return maxIdx