import pytest
from solutions.problem_0333_largest_bst_subtree import Solution
from utils.tree_utils import build_tree_from_list

@pytest.mark.parametrize("root, expected",[
    ([10,5,15,1,8,None,7], 3),
    ([4,2,7,2,3,5,None,2,None,None,None,None,None,1], 2),
    ([3,2,4,None,None,1], 2)
])
def test_largest_bst_subtree(root, expected):
    result = Solution().largestBSTSubtree(build_tree_from_list(root))
    assert result == expected