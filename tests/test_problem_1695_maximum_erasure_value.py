import pytest
from solutions.problem_1695_maximum_erasure_value import Solution

@pytest.mark.parametrize("nums, expected",[
    ([4,2,4,5,6], 17),
    ([5,2,1,2,5,2,1,2,5], 8)
])
def test_maximum_erasure_value(nums, expected):
    result = Solution().maximumUniqueSubarray(nums)
    assert result == expected