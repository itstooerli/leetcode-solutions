"""
LeetCode Problem 3136: Valid Word
Solution by Eric Li
"""

class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set(['a','e','i','o','u'])
        digits = set(['0','1','2','3','4','5','6','7','8','9'])

        if len(word) < 3:
            return False
        
        hasVowel = False
        hasConsonant = False
        for char in word:
            if char.lower() in vowels:
                hasVowel = True
            elif char.isalpha():
                hasConsonant = True
            elif char in digits:
                pass
            else:
                return False
        
        return hasVowel and hasConsonant