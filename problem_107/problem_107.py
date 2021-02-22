from collections import deque

from typing import List
import sys

sys.path.append("/Users/aditya/Documents/Python/Leetcode")
from helpers.binary_tree import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        node_q = deque([(root, 0)])
        res = []
        while node_q:
            node, depth = node_q.popleft()
            try:
                res[depth].append(node.val)
            except IndexError:
                res.append([node.val])
            if node.left:
                node_q.append((node.left, depth + 1))
            if node.right:
                node_q.append((node.right, depth + 1))

        return list(reversed(res))
