import pytest
import sys

sys.path.append("/Users/aditya/Documents/Python/Leetcode")
from helpers.binary_tree import TreeNode, _list_to_tree
from problem_108 import Solution


class TestCase:
    def test_1(self, my_sln):
        test = []
        assert my_sln.sortedArrayToBST(test) == None

    def test_2(self, my_sln):
        ans = _list_to_tree([2, 1, 3])
        test_input = [1, 2, 3]
        assert my_sln.sortedArrayToBST(test_input) == ans

    def test_3(self, my_sln):
        test_input = [1, 1, 1]
        ans = _list_to_tree([1, 1, 1])
        assert my_sln.sortedArrayToBST(test_input) == ans

    def test_4(self, my_sln):
        test_input = [1, 2, 2, 2, 3]
        print(ans := _list_to_tree([2, 2, 3, 1, None, 2, None]))
        print(my_res := my_sln.sortedArrayToBST(test_input))
        assert my_res == ans

    def test_5(self, my_sln):
        test_input = [1, 2, 2, 3, 4, 5, 6]
        print(my_res := my_sln.sortedArrayToBST(test_input))
        assert False

    def test_6(self, my_sln):
        test_input = [1, 2, 2, 4, 5, 6]
        print(my_res := my_sln.sortedArrayToBST(test_input))
        assert False

    def test_7(self, my_sln):
        test_input = [1, 2, 2, 3, 5, 6]
        print(my_res := my_sln.sortedArrayToBST(test_input))
        assert False


@pytest.fixture
def my_sln():
    return Solution()
