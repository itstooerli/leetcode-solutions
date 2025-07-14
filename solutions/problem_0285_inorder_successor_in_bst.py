"""
LeetCode Problem 285: Inorder Successor in BST
Solution by Eric Li
"""
from typing import Optional
from utils.tree_utils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        '''
        The answer should either be one of
         1. an ancestor of the node
         2. the smallest value in the right subtree
        '''

        def findSuccessor(root, val, minSuccessor):
            if not root:
                return minSuccessor
            
            if root.val > val:
                if not minSuccessor or root.val < minSuccessor.val:
                    minSuccessor = root
                minSuccessor = findSuccessor(root.left, val, minSuccessor)
            else:
                minSuccessor = findSuccessor(root.right, val, minSuccessor)
            return minSuccessor

        minSuccessor = findSuccessor(root, p.val, None)
        return minSuccessor
