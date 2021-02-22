import sys

sys.path.append(r"/Users/aditya/Documents/Python/Leetcode/")
from helpers.linked_list import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not (headA and headB):
            return None
        a_len, b_len = 0, 0
        a, b = headA, headB
        while a:
            a_len += 1
            a = a.next
        while b:
            b_len += 1
            b = b.next

        for _ in range(0, max(b_len - a_len, 0)):
            headB = headB.next

        for _ in range(0, max(a_len - b_len, 0)):
            headA = headA.next

        while headA and headB:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None
