import sys

sys.path.append("/Users/aditya/Documents/Python/Leetcode")

from helpers.binary_tree import TreeNode


def _path_sum_helper(root: TreeNode, targetSum: int) -> bool:
    new_target = targetSum - root.val
    if not (root.left or root.right):
        return True if new_target == 0 else False
    if root.left and root.right:
        return _path_sum_helper(root.left, new_target) or _path_sum_helper(
            root.right, new_target
        )
    if root.left:
        return _path_sum_helper(root.left, new_target)
    if root.right:
        return _path_sum_helper(root.right, new_target)


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        return _path_sum_helper(root, targetSum)
