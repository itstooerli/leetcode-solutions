"""
LeetCode Problem 383: Ransom Note
Solution by Eric Li
"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCounter = Counter(magazine)
        noteCounter = Counter(ransomNote)
        for key in noteCounter:
            if key not in magCounter:
                return False
            elif noteCounter[key] > magCounter[key]:
                return False
        return True