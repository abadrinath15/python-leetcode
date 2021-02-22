import pytest
from problem_122 import Solution


class TestCase:
    def test_1(self, get_sln):
        input_list = [7, 1, 5, 3, 6, 4]
        assert get_sln.maxProfit(input_list) == 7

    def test_2(self, get_sln):
        input_list = [1, 2, 3, 4, 5]
        assert get_sln.maxProfit(input_list) == 4

    def test_3(self, get_sln):
        input_list = [7, 6, 4, 3, 1]
        assert get_sln.maxProfit(input_list) == 0


@pytest.fixture
def get_sln():
    return Solution()
