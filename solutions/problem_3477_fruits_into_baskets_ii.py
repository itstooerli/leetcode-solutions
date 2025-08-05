"""
LeetCode Problem 3477: Fruits into Baskets II
Solution by Eric Li
"""

from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        '''
        Basic implementation of checking for unfilled baskets. Could be optimized to either
        remove filled baskets or better track nearest open basket.
        '''
        unplaced_fruits = 0
        filled_baskets = set()
        for fruit in fruits:
            found_basket = False
            for basket_idx in range(len(baskets)):
                if basket_idx in filled_baskets or fruit > baskets[basket_idx]:
                    continue
                baskets[basket_idx] -= fruit
                found_basket = True
                filled_baskets.add(basket_idx)
                break
            if not found_basket:
                unplaced_fruits += 1
        return unplaced_fruits