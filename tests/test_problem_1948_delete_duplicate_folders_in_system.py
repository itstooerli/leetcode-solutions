import pytest
from solutions.problem_1948_delete_duplicate_folders_in_system import Solution

@pytest.mark.parametrize("paths, expected",[
    ([["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]], [["d"],["d","a"]]),
    ([["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]], [["c"],["c","b"],["a"],["a","b"]]),
    ([["a","b"],["c","d"],["c"],["a"]], [["c"],["c","d"],["a"],["a","b"]]),
    ([["a"],["c"],["d"],["a","b"],["c","b"],["d","a"],["a","d"]], [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"],["a","d"]]),
    ([["b"],["f"],["f","r"],["f","r","g"],["f","r","g","c"],["f","r","g","c","r"],["f","o"],["f","o","x"],["f","o","x","t"],["f","o","x","d"],["f","o","l"],["l"],["l","q"],["c"],["h"],["h","t"],["h","o"],["h","o","d"],["h","o","t"]], [["b"],["f"],["l"],["c"],["h"],["f","r"],["f","o"],["l","q"],["h","t"],["f","r","g"],["f","o","l"],["f","r","g","c"],["f","r","g","c","r"]])
])
def test_delete_dpulicate_folders_in_system(paths, expected):
    result = Solution().deleteDuplicateFolder(paths)
    assert sorted(result) == sorted(expected)