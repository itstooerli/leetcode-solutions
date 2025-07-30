import pytest
from solutions.problem_1233_remove_subfolders_from_the_filesystem import Solution

@pytest.mark.parametrize("folder, expected",[
    (["/a","/a/b","/c/d","/c/d/e","/c/f"], ["/a","/c/d","/c/f"]),
    (["/a","/a/b/c","/a/b/d"], ["/a"]),
    (["/a/b/c","/a/b/ca","/a/b/d"], ["/a/b/c","/a/b/ca","/a/b/d"]),
    (["/a","/a/b","/c/d","/c/d/e","/c/f","/a/z/y/x"], ["/a","/c/d","/c/f"]),
    (["/a/b/ca","/a/b/ca/ba","/a/b/d"], ["/a/b/ca","/a/b/d"])
])
def test_removeSubfolders(folder, expected):
    result = Solution().removeSubfolders(folder)
    assert sorted(result) == sorted(expected)