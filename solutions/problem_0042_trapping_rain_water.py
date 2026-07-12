"""
LeetCode Problem 42: Trapping Rain Water
Solution by Eric Li
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        currentIdx = 0
        stack = []
        while currentIdx < len(height):
            while stack and height[stack[-1]] < height[currentIdx]:
                unfilledAirspaceIdx = stack.pop()
                if not stack:
                    break
                prevWallIdx = stack[-1]
                fillHeight = min(height[prevWallIdx], height[currentIdx]) - height[unfilledAirspaceIdx]
                fillDistance = currentIdx - prevWallIdx - 1
                fillAmount = fillHeight * fillDistance
                result += fillAmount
            stack.append(currentIdx)
            currentIdx += 1
        return result