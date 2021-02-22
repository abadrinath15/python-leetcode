import sys
from typing import List

sys.path.append("/Users/aditya/Documents/Python/Leetcode")
from helpers.binary_tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            head = None
        else:
            mid_ind = len(nums) // 2
            head = TreeNode(nums[mid_ind])

            def _dc_build_tree(parent: TreeNode, nums_sub: List[int]) -> None:
                if len(nums_sub) >= 1:
                    mid_ind = len(nums_sub) // 2
                    new_parent = TreeNode(val=nums_sub[mid_ind])
                    if new_parent.val == parent.val and parent.left is None:
                        parent.left = new_parent
                    elif new_parent.val == parent.val and parent.right is None:
                        parent.right = new_parent
                    elif new_parent.val >= parent.val:
                        parent.right = new_parent
                    else:
                        parent.left = new_parent
                    _dc_build_tree(new_parent, nums_sub[:mid_ind])
                    _dc_build_tree(new_parent, nums_sub[mid_ind + 1 :])

            _dc_build_tree(head, nums[:mid_ind])
            _dc_build_tree(head, nums[mid_ind + 1 :])

        return head

    def sortedArrayToBST2(self, nums: List[int]) -> TreeNode:
        if not nums:
            head = None
        else:
            mid_ind = len(nums) // 2
            head = TreeNode(nums[mid_ind])
            head.left = self.sortedArrayToBST2(nums[:mid_ind])
            head.left = self.sortedArrayToBST2(nums[mid_ind + 1 :])

        return head
