from typing import Optional, Tuple
import sys
sys.path.append("/Users/aditya/Documents/Python/Leetcode")

from helpers.binary_tree import TreeNode


def _balanced_helper(node: Optional[TreeNode]) -> Tuple[int, bool]:

    if node:
        left_depth, left_bool = _balanced_helper(node.left)
        right_depth, right_bool = _balanced_helper(node.right)
        if not (left_bool and right_bool):
            return -1, False
        if abs(left_depth - right_depth) > 1:
            return -1, False
        return max(left_depth, right_depth) + 1, True

    return 0, True


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root:
            return _balanced_helper(root)[1]
        else:
            return True
