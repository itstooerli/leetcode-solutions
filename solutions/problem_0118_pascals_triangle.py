"""
LeetCode Problem 79: Word Search
Solution by Eric Li
"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        Could build triangle manually, would be easier to read and more straightforward.
        Instead though, we'll attempt to build each row directly for more of a challenge, 
        This avoids reliance on the other rows in the hopes that this will be more performant.

        # Notice Pattern:
        # First the obvious is that each row starts and ends with a 1.
        # Second each row is mirrored so we only need to calculate half the row.
        # Third each row's subsequent values are the previous value multipled by a specific fraction,
        #   for example, for row 8, we start with 1, then multiply that value with 8/1 (8), then multiple
        #   that value by 7/2 (28), multiply that value by 6/3 (56), multiply that value by 5/4 (70).
        #   The numerator decreases from the row index, the denominator increases from 1 until we can't anymore.
        # (0) 1
        # (1) 1,1
        # (2) 1,2,1
        # (3) 1,3,3,1
        # (4) 1,4,6,4,1
        # (5) 1,5,10,10,5,1
        # (6) 1,6,15,20,15,6,1
        # (7) 1,7,21,35,35,21,7,1
        # (8) 1,8,28,56,70,56,28,1
        # (9) 1,9,36,84,126,84,36,9,1

        # 2- 1, 2/1
        # 3- 1, 3/1
        # 4- 1, 4/1, 3/2
        # 5- 1, 5/1, 4/2
        # 6- 1, 6/1, 5/2, 4/3
        # 7- 1, 7/1, 6/2, 5/3
        # 8- 1, 8/1, 7/2, 6/3, 5/4
        '''

        output = []
        for rowIdx in range(numRows):
            # Create Row
            row = [1 for _ in range(rowIdx+1)]
            # Ignore end values since we know they're 1
            startIdx = 1
            endIdx = rowIdx - 1
            # Initialize numerator and denominator
            numerator = rowIdx
            denominator = 1
            # Loop until we cross the middle values since it's mirrored
            while startIdx <= endIdx:
                # Calculate current value
                prevVal = row[startIdx - 1]
                currVal = prevVal * numerator // denominator
                # Set values
                row[startIdx] = currVal
                row[endIdx] = currVal
                #  Increment/decrement
                numerator -= 1
                denominator += 1
                startIdx += 1
                endIdx -= 1
            # Add row to output
            output.append(row)
        
        return output
