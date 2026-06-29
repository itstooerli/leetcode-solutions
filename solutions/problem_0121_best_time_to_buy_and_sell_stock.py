"""
LeetCode Problem 121: Best Time to Buy and Sell Stock
Solution by Eric Li
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Return the maximum profit obtainable from one transaction."""
        result = 0
        minPastPrice = float('inf')
        for val in prices:
            if val < minPastPrice:
                minPastPrice = val
            result = max(result, val - minPastPrice)
        return result