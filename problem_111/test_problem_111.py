import pytest
import sys

from problem_111 import Solution

sys.path.append("/Users/aditya/Documents/Python/Leetcode")
from helpers.binary_tree import TreeNode, _list_to_tree


class TestCase:
    def test_1(self, get_sln):
        input_list = []
        assert get_sln.minDepth(_list_to_tree(input_list)) == 0

    def test_2(self, get_sln):
        input_list = [2]
        assert get_sln.minDepth(_list_to_tree(input_list)) == 1

    def test_3(self, get_sln):
        input_list = [3, 9, 20, None, None, 15, 7]
        assert get_sln.minDepth(_list_to_tree(input_list)) == 2

    def test_4(self, get_sln):
        input_list = [2, None, 3, None, 4, None, 5, None, 6]
        assert get_sln.minDepth(_list_to_tree(input_list)) == 5


@pytest.fixture
def get_sln():
    return Solution()
