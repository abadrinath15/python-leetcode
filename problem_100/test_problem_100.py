import pytest
from problem_100 import Solution, TreeNode
from typing import List, Optional


def _list_to_tree(input_list: List[Optional[int]]) -> Optional[TreeNode]:
    if input_list:
        head = TreeNode(val=input_list.pop(0))
        _build_tree_rec(input_list, head)
    else:
        head = None
    return head


def _build_tree_rec(input_list: List[Optional[int]], node: TreeNode) -> None:

    try:
        if node.val:
            node.left = TreeNode(val=input_list.pop(0))
            node.right = TreeNode(val=input_list.pop(0))
            _build_tree_rec(input_list, node.left)
            _build_tree_rec(input_list, node.right)
    except IndexError:
        return


class TestCase:
    def test_1(self, my_solution):
        p = _list_to_tree([])
        q = _list_to_tree([])
        assert my_solution.isSameTree(p, q) == True

    def test_2(self, my_solution):
        p = _list_to_tree([0])
        q = _list_to_tree([])
        assert my_solution.isSameTree(p, q) == False

    def test_3(self, my_solution):
        p = _list_to_tree([])
        q = _list_to_tree([0])
        assert my_solution.isSameTree(p, q) == False

    def test_4(self, my_solution):
        p = _list_to_tree([1, 2, 3])
        q = _list_to_tree([1, 2, 3])
        assert my_solution.isSameTree(p, q) == True

    def test_5(self, my_solution):
        p = _list_to_tree([1, None, 2])
        q = _list_to_tree([1, 2])
        assert my_solution.isSameTree(p, q) == False

    def test_7(self, my_solution):
        p = _list_to_tree([1, 2, 1])
        q = _list_to_tree([1, 1, 2])
        assert my_solution.isSameTree(p, q) == False


@pytest.fixture
def my_solution():
    return Solution()
