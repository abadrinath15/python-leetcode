import pytest
from problem_121 import Solution


class TestCase:
    def test_1(self, get_sln):
        input_prices = [7, 1, 5, 3, 6, 4]
        assert get_sln.maxProfit(input_prices) == 5

    def test_2(self, get_sln):
        input_prices = [7, 6, 5, 4, 3, 2, 1]
        assert get_sln.maxProfit(input_prices) == 0


@pytest.fixture
def get_sln():
    return Solution()
