import pytest
from problem_169 import Solution


class TestCase:
    def test_1(self, get_sln):
        input_list = [3, 2, 3]
        assert get_sln.majorityElement(input_list) == 3

    def test_2(self, get_sln):
        input_list = [2, 2, 1, 1, 1, 2, 2]
        assert get_sln.majorityElement(input_list) == 2

    def test_3(self, get_sln):
        input_list = [6, 5, 5]
        assert get_sln.majorityElement(input_list) == 5


@pytest.fixture
def get_sln() -> Solution:
    return Solution()
