import pytest
import sys
from problem_112 import Solution

sys.path.append("/Users/aditya/Documents/Python/Leetcode")
from helpers.binary_tree import TreeNode, _list_to_tree


class TestCase:
    def test_1(self, get_sln):
        input_list = []
        assert get_sln.hasPathSum(_list_to_tree(input_list), 1) == False

    def test_2(self, get_sln):
        input_list = [1, 2, 3]
        assert get_sln.hasPathSum(_list_to_tree(input_list), 5) == False

    def test_3(self, get_sln):
        input_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        assert get_sln.hasPathSum(_list_to_tree(input_list), 22) == True

    def test_4(self, get_sln):
        input_list = [1, 2]
        assert get_sln.hasPathSum(_list_to_tree(input_list), 0) == False


@pytest.fixture
def get_sln():
    return Solution()
