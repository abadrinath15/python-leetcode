from helpers.binary_tree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        node_q = [(root, 1)]
        leaf_depths = [1]

        while node_q:
            node, depth = node_q.pop()
            if node.left:
                node_q.append((node.left, depth + 1))
            if node.right:
                node_q.append((node.right, depth + 1))
            if not (node.left or node.right):
                leaf_depths.append(depth)

        return max(leaf_depths)
