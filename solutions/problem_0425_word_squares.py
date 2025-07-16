"""
LeetCode Problem 425: Word Squares
Solution by Eric Li
"""

from typing import List
from collections import defaultdict

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # Compile prefixes
        dictionary = defaultdict(set)
        for word in words:
            for charIdx in range(1, len(word)):
                dictionary[word[:charIdx]].add(word)
        
        squareLen = len(words[0])
        squares = []
        currSequence = []
        candidateWords = words.copy()
        while candidateWords:
            currWord = candidateWords.pop()
            
            # Check for separator that indicates earlier in square sequence
            if currWord == "":
                currSequence.pop()
                continue

            # Add to current square and check if complete
            currSequence.append(currWord)
            if len(currSequence) == squareLen:
                squares.append(currSequence.copy())
                currSequence.pop()
                continue

            # Check for next candidate word in square
            header = ""
            squareIdx = len(currSequence)
            for word in currSequence:
                header += word[squareIdx]
            
            if header in dictionary and len(dictionary[header]) > 0:
                candidateWords.append("")
                candidateWords += dictionary[header]
            else:
                currSequence.pop()
                continue
        
        return squares