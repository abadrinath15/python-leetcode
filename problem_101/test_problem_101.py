import sys

sys.path.append("/Users/aditya/Documents/Python/Leetcode")
import os

from problem_101 import Solution
from helpers.binary_tree import TreeNode, _list_to_tree

test = TreeNode()

import pytest


class TestCase:
    def test_1(self, get_sln):
        my_tree = _list_to_tree([1, 2, 2, 3, 4, 4, 3])
        assert get_sln.isSymmetric(my_tree) == True

    def test_2(self, get_sln):
        my_tree = _list_to_tree([1, 2, 2, None, 3, None, 3])
        assert get_sln.isSymmetric(my_tree) == False

    def test_3(self, get_sln):
        my_tree = _list_to_tree([1, 2, 2, 2, None, 2])
        assert get_sln.isSymmetric(my_tree) == False

    def test_4(self, get_sln):
        my_tree = _list_to_tree([])
        assert get_sln.isSymmetric(my_tree) == True

    def test_5(self, get_sln):
        my_tree = _list_to_tree([1, 2, 2, None, 3, 3])
        assert get_sln.isSymmetric(my_tree) == True

    def test_6(self, get_sln):
        my_tree = _list_to_tree([5, 4, 1, None, 1, None, 4, 2, None, 2, None])
        assert get_sln.isSymmetric(my_tree) == False

    def test_7(self, get_sln):
        my_tree = _list_to_tree([2, 3, 3, 4, 5, 5, 4, None, None, 8, 9, 9, 8])
        assert get_sln.isSymmetric(my_tree) == True

    def test_8(self, get_sln):
        my_tree = _list_to_tree([3, 4, 4, 5, None, None, 5, 6, None, None, 6])
        assert get_sln.isSymmetric(my_tree) == True


@pytest.fixture
def get_sln():
    return Solution()
