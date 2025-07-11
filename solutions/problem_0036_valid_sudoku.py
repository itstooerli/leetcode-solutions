"""
LeetCode Problem 36: Valid Sudoku
Solution by Eric Li
"""

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)
        
        # z = 0 : [0,0], [0,2], [2,2], [2,0]
        # z = 1 : [0,3], [0,5], [2,5], [2,3]
        # z = 2 : [0,6], [0,8], [2,8], [2,6]
        # z = 3 : [3,0], [3,2], [5,2], [5,0]
        
        for x in range(9):
            for y in range(9):
                z = (x // 3) * 3 + y // 3
                val = board[x][y]
                
                if val == ".":
                    continue
                elif val in rows[x] or val in cols[y] or val in boxs[z]:
                    return False
                
                rows[x].add(val)
                cols[y].add(val)
                boxs[z].add(val)
        
        return True