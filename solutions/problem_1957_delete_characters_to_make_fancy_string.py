"""
LeetCode Problem 1957: Delete Characters to Make Fancy String
Solution by Eric Li
"""

class Solution:
    def makeFancyString(self, s: str) -> str:
        output = ""
        prevLetter = ""
        counter = 0

        for val in s:
            if val == prevLetter:
                counter += 1
            else:
                counter = 1
            
            if counter < 3:
                output += val
            
            prevLetter = val
        
        return output