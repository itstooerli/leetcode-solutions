from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def trees_equal(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
    if not t1 and not t2:
        return True
    if t1 and t2 and t1.val == t2.val:
        return trees_equal(t1.left, t2.left) and trees_equal(t1.right, t2.right)
    return False

def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    
    # Search left subtree
    left = find_node(root.left, val)
    if left:
        return left

    # Search right subtree
    return find_node(root.right, val)