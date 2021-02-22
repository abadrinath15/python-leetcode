import sys

sys.path.append("/Users/aditya/Documents/Python/Leetcode")

from helpers.binary_tree import TreeNode
from collections import deque


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        node_q = deque([(root, 1)])
        while node_q:
            curr_node, nodes_visited = node_q.popleft()
            if curr_node.left is None and curr_node.right is None:
                return nodes_visited
            if curr_node.left:
                node_q.append((curr_node.left, nodes_visited + 1))
            if curr_node.right:
                node_q.append((curr_node.right, nodes_visited + 1))
