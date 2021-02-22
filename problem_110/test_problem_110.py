import pytest
import sys
from typing import List

sys.path.append("/Users/aditya/Documents/Python/Leetcode")
from helpers.binary_tree import _list_to_tree
from problem_110 import Solution


class TestCase:
    def test_1(self, get_sln) -> None:
        input_list = []
        assert get_sln.isBalanced(input_list) == True

    def test_2(self, get_sln) -> None:
        input_list = [2, 1, 3]
        assert get_sln.isBalanced(_list_to_tree(input_list)) == True

    def test_3(self, get_sln) -> None:
        input_list = [1, 1, None]
        assert get_sln.isBalanced(_list_to_tree(input_list)) == True

    def test_5(self, get_sln) -> None:
        input_list = [3, 9, 20, None, None, 15, 7]
        assert get_sln.isBalanced(_list_to_tree(input_list)) == True

    def test_4(self, get_sln) -> None:
        input_list = [1, 2, 2, 3, 3, None, None, 4, 4]
        assert get_sln.isBalanced(_list_to_tree(input_list)) == False


@pytest.fixture
def get_sln():
    return Solution()
