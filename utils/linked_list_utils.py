from typing import Optional, List

class SinglyLinkedListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
def build_singly_linked_list(values: List[int]) -> Optional[SinglyLinkedListNode]:
    """Creates a linked list from a list of values. Returns the head."""
    if not values:
        return None

    dummy = SinglyLinkedListNode(0)
    current = dummy
    for val in values:
        current.next = SinglyLinkedListNode(val)
        current = current.next
    return dummy.next