"""
LeetCode Problem 1290: Convert Binary Number in a Linked List to Integer
Solution by Eric Li
"""

from typing import Optional
from utils.linked_list_utils import SinglyLinkedListNode as ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        output = 0
        currNode = head
        while currNode:
            output *= 2
            output += currNode.val
            currNode = currNode.next
        return output