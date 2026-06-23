import pytest
from solutions.problem_0134_gas_station import Solution


@pytest.mark.parametrize("gas, cost, expected", [
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    ([2, 3, 4], [3, 4, 3], -1),
    ([5], [4], 0),
    ([5,1,2,3,4], [4,4,1,5,1], 4),
])
def test_canCompleteCircuit(gas, cost, expected):
    result = Solution().canCompleteCircuit(gas, cost)
    assert result == expected
