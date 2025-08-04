"""
LeetCode Problem 904: Fruit Into Baskets
Solution by Eric Li
"""

from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        Purely based on "once you reach a tree with a fruit that cannot fit in your baskets, you must stop"
        this is very likely to be a good sliding window problem. Add fruits until you cannot and then remove
        fruits to open a up a basket.
        '''        
        basket1_id = -1
        basket2_id = -1
        basket1_count = 0
        basket2_count = 0
        leftPtr = 0
        rightPtr = 0
        maxFruit = 0

        while rightPtr < len(fruits):
            currFruit_id = fruits[rightPtr]
            
            # If fruit is already in a basket, add to it.
            if currFruit_id == basket1_id:
                basket1_count += 1
            elif currFruit_id == basket2_id:
                basket2_count += 1
            else:
                # Otherwise, remove fruits until a basket opens up
                while basket1_count > 0 and basket2_count > 0:
                    oldFruit_id = fruits[leftPtr]
                    if oldFruit_id == basket1_id:
                        basket1_count -= 1
                    elif oldFruit_id == basket2_id:
                        basket2_count -= 1
                    leftPtr += 1
                
                # Add to newly open basket
                if basket1_count == 0:
                    basket1_id = currFruit_id
                    basket1_count += 1
                else:
                    basket2_id = currFruit_id
                    basket2_count += 1
            maxFruit = max(maxFruit, basket1_count + basket2_count)
            rightPtr += 1
            
        return maxFruit