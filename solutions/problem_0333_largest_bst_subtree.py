"""
LeetCode Problem 333: Largest BST Subtree
Solution by Eric Li
"""

from typing import Optional
from utils.tree_utils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def isValidBST(root):
            isValid = True
            
            if root is None:
                return (isValid, 0, None, None)
            
            lTreeValid, lTreeSize, lMinVal, lMaxVal = isValidBST(root.left)
            rTreeValid, rTreeSize, rMinVal, rMaxVal = isValidBST(root.right)

            if not lTreeValid or (lTreeSize > 0 and root.val <= lMaxVal):
                isValid = False
            
            if not rTreeValid or (rTreeSize > 0 and root.val >= rMinVal):
                isValid = False
            
            if not isValid:
                return (isValid, max(lTreeSize, rTreeSize), None, None)
            
            return (
                isValid, 
                1 + lTreeSize + rTreeSize, 
                lMinVal if lMinVal is not None else root.val, 
                rMaxVal if rMaxVal is not None else root.val)

        return isValidBST(root)[1]