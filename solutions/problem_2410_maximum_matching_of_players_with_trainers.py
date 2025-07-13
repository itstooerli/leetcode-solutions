"""
LeetCode Problem 2410: Maximum Matching of Players with Trainers
Solution by Eric Li
"""

from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Seems like greedy should work here
        players.sort(key = lambda x: -x)
        trainers.sort(key = lambda x: -x)

        pIdx = 0
        tIdx = 0
        matchups = 0
        while pIdx < len(players) and tIdx < len(trainers):
            if players[pIdx] <= trainers[tIdx]:
                matchups += 1
                tIdx += 1
            pIdx += 1
        
        return matchups