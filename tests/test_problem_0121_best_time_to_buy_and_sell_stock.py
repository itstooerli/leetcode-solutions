import pytest
from solutions.problem_0121_best_time_to_buy_and_sell_stock import Solution


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2, 3, 4, 5], 4),
        ([2, 4, 1], 2),
    ],
)
def test_maxProfit(prices, expected):
    result = Solution().maxProfit(prices)
    assert result == expected
