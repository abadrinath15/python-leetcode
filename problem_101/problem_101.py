from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetricR(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def _recurse_sym(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not (left or right):
                return True
            if left and right:
                if left.val != right.val:
                    return False
                else:
                    return _recurse_sym(left.left, right.right) and _recurse_sym(
                        left.right, right.left
                    )
            else:
                return False

        return _recurse_sym(root.left, root.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        node_q = [(root.left, root.right)]
        while node_q:
            left, right = node_q.pop()
            if (left is None) ^ (right is None):
                return False
            if left and right:
                if left.val != right.val:
                    return False
                else:
                    node_q += [(left.left, right.right), (left.right, right.left)]
        return True
