from __future__ import annotations
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

    def __eq__(self, o: Optional[TreeNode]) -> bool:
        try:
            node_q = [(self.left, o.left), (self.right, o.right)]
            while node_q:
                this_node, other_node = node_q.pop()
                if (
                    (this_node.val != other_node.val)
                    or ((this_node.left is None) ^ (other_node.left is None))
                    or ((this_node.right is None) ^ (other_node.right is None))
                ):
                    print(
                        f"Error; left = {this_node.val if this_node else None}, right = {other_node.val  if other_node else None}"
                    )
                    return False
                if this_node.left and other_node.left:
                    node_q.append((this_node.left, other_node.left))
                if this_node.right and other_node.right:
                    node_q.append((this_node.right, other_node.right))

            return True

        except AttributeError:
            return False

    def __repr__(self) -> str:
        return str(bt_breadth_visit(self))


def _list_to_tree(input_list: List[Optional[int]]) -> Optional[TreeNode]:
    if input_list:
        head = TreeNode(val=input_list.pop(0))
        node_queue = [head]
        for node in node_queue:
            try:
                left = input_list.pop(0)
                if left:
                    node.left = TreeNode(val=left)
                    node_queue.append(node.left)
                right = input_list.pop(0)
                if right:
                    node.right = TreeNode(val=right)
                    node_queue.append(node.right)
            except IndexError:
                return head
    else:
        return None


def bt_breadth_visit(head: TreeNode) -> List[List[TreeNode]]:
    tree_list = []
    if head:
        node_q = deque()
        node_q.append((head, 0))
        while node_q:
            node, depth = node_q.popleft()
            if node:
                append_val = node.val
                node_q.append((node.left, depth + 1))
                node_q.append((node.right, depth + 1))
            else:
                append_val = None

            if depth == len(tree_list):
                tree_list.append([append_val])
            else:
                tree_list[depth].append(append_val)

    return tree_list
