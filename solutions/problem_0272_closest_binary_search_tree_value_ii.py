"""
LeetCode Problem 272: Closest Binary Search Tree Value II
Solution by Eric Li
"""

from typing import List, Optional
from utils.tree_utils import TreeNode
import heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        '''
        Perform in-order traversal to get the sorted order and add to heap to track absolute
        value relative to target. Later, pop k values from the heap for the output.
        Could be optimized to stop searching/traversal when absolute value goes beyond bound
        of k most closest absolute values by using property of binary search tree. That is,
        all to the right will be continuously greater, and all to the left will be lesser.
        '''
        
        # In order traversal and add to heap by absolute difference to target
        sortedValues = []
        visited = set()
        stack = [root]
        while stack:
            currNode = stack.pop()
            currVal = currNode.val
            if currVal in visited:
                heapq.heappush(sortedValues, (abs(target - currVal), currVal))
            else:
                if currNode.right:
                    stack.append(currNode.right)
                
                stack.append(currNode)
                visited.add(currNode.val)
                
                if currNode.left:
                    stack.append(currNode.left)
        
        # Pop k values from heap
        output = []
        while k > 0:
            output.append(heapq.heappop(sortedValues)[1])
            k -= 1

        return output