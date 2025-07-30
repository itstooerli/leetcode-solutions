import pytest
from solutions.problem_0272_closest_binary_search_tree_value_ii import Solution
from utils.tree_utils import build_tree_from_list, find_node

@pytest.mark.parametrize("root, target, k, expected",[
    ([4,2,5,1,3], 3.714286, 2, [4,3]),
    ([1], 0.000000, 1, [1]),
    ([4,2,5,1,3], 3.714286, 4, [4,3,5,2])
])
def test_closest_binary_search_tree_value_ii(root, target, k, expected):
    tree = build_tree_from_list(root)
    result = Solution().closestKValues(tree, target, k)
    assert sorted(result) == sorted(expected)