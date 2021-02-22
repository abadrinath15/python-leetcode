from problem_167 import Solution
import pytest


class TestCase:
    def test_1(self, get_sln):
        input_list = [5, 25, 75]
        input_target = 100
        assert get_sln.twoSum(input_list, input_target) == [2, 3]

    def test_2(self, get_sln):
        input_list = [2, 7, 11, 15]
        input_target = 9
        assert get_sln.twoSum(input_list, input_target) == [1, 2]

    def test_3(self, get_sln):
        input_list = [2, 3, 4]
        input_target = 6
        assert get_sln.twoSum(input_list, input_target) == [1, 3]

    def test_4(self, get_sln):
        input_list = [1, 3, 4, 4]
        input_target = 8
        assert get_sln.twoSum(input_list, input_target) == [3, 4]


@pytest.fixture
def get_sln() -> Solution:
    return Solution()
