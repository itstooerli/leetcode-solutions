"""
LeetCode Problem 290: Word Pattern
Solution by Eric Li
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        patTrack = {}
        wordTrack = {}
        for idx in range(len(pattern)):
            currPat = pattern[idx]
            currWord = words[idx]
            if currPat in patTrack:
                if patTrack[currPat] != currWord:
                    return False
            if currWord in wordTrack:
                if wordTrack[currWord] != currPat:
                    return False
            patTrack[currPat] = currWord
            wordTrack[currWord] = currPat
        return True