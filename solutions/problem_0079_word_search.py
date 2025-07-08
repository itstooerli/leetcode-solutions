"""
LeetCode Problem 79: Word Search
Solution by Eric Li
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(visited=set(), wordIdx=0, row=0, col=0):
            if (row, col) in visited:
                return False
            
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            
            if board[row][col] == word[wordIdx]:
                if wordIdx == len(word) - 1:
                    return True
                
                visited.add((row, col))
                
                if backtrack(visited, wordIdx + 1, row + 1, col):
                    return True
                
                if backtrack(visited, wordIdx + 1, row - 1, col):
                    return True
                
                if backtrack(visited, wordIdx + 1, row, col + 1):
                    return True
                
                if backtrack(visited, wordIdx + 1, row, col - 1):
                    return True
                
                visited.remove((row, col))
            
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(set(), 0, i, j):
                    return True
        
        return False