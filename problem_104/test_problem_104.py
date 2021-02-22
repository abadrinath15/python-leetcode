import sys

sys.path.append("/Users/aditya/Documents/Python/Leetcode")

from problem_104 import Solution
from helpers.binary_tree import TreeNode, _list_to_tree
import pytest


class TestCase:
    def test_1(self, my_sln):
        tree = _list_to_tree([])
        assert my_sln.maxDepth(tree) == 0

    def test_2(self, my_sln):
        tree = _list_to_tree([0])
        assert my_sln.maxDepth(tree) == 1

    def test_3(self, my_sln):
        tree = _list_to_tree([3, 9, 20, None, None, 15, 7])
        assert my_sln.maxDepth(tree) == 3

    def test_4(self, my_sln):
        tree = _list_to_tree([1, None, 2])
        assert my_sln.maxDepth(tree) == 2


@pytest.fixture
def my_sln():
    return Solution()
