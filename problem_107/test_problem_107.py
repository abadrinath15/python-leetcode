import sys
import pytest

sys.path.append("/Users/aditya/Documents/Python/Leetcode")
from helpers.binary_tree import TreeNode, _list_to_tree
from problem_107 import Solution


class TestCase:
    def test_1(self, get_sln):
        my_tree = _list_to_tree([3, 9, 20, None, None, 15, 7])
        assert get_sln.levelOrderBottom(my_tree) == [[15, 7], [9, 20], [3]]


@pytest.fixture
def get_sln() -> Solution:
    return Solution()
