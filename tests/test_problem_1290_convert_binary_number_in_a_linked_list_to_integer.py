import pytest
from solutions.problem_1290_convert_binary_number_in_a_linked_list_to_integer import Solution
from utils.linked_list_utils import build_singly_linked_list

@pytest.mark.parametrize("head, expected",[
    ([1,0,1], 5),
    ([0], 0)
])
def test_convert_binary_number_in_a_linked_list_to_integer(head, expected):
    result = Solution().getDecimalValue(build_singly_linked_list(head))
    assert result == expected