from problem_88 import Solution
import pytest


class TestClass:
    def test_one(self, my_solution: Solution):
        nums_1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums_2 = [2, 5, 6]
        n = 3
        my_solution.merge(nums_1, m, nums_2, n)
        assert nums_1 == [1, 2, 2, 3, 5, 6]

    def test_two(self, my_solution):
        nums_1 = [1]
        m = 1
        nums_2 = []
        n = 0
        my_solution.merge(nums_1, m, nums_2, n)
        assert nums_1 == [1]

    def test_3(self, my_solution):
        nums_1 = [0]
        m = 0
        nums_2 = [1]
        n = 1
        my_solution.merge(nums_1, m, nums_2, n)
        assert nums_1 == [1]


@pytest.fixture
def my_solution():
    return Solution()
