import pytest
from solutions.problem_0285_inorder_successor_in_bst import Solution
from utils.tree_utils import build_tree_from_list, find_node

@pytest.mark.parametrize("root, p, expected",[
    ([2,1,3], 1, 2),
    ([5,3,6,2,4,None,None,1], 6, None),
    ([5,3,6,1,4,None,None,None,2], 4, 5),
    ([6,2,8,0,4,7,9,None,None,3,5], 3, 4)
])
def test_largest_bst_subtree(root, p, expected):
    tree = build_tree_from_list(root)
    result = Solution().inorderSuccessor(tree, find_node(tree, p))
    assert result == find_node(tree, expected)