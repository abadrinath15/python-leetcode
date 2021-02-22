import sys
from typing import Dict, Optional, Deque, List
import math


sys.path.append(r"/Users/aditya/Documents/Python/Leetcode/")
from helpers.linked_list import ListNode
from helpers.binary_tree import TreeNode, _list_to_tree


class Solution:
    def isHappy(self, n: int) -> bool:
        seen_nums = set()
        while n != 1 and n not in seen_nums:
            seen_nums.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1

    def removeElements(self, head: ListNode, val: int) -> Optional[ListNode]:
        return _removeElements_func(head, val)

    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        multiples_set = set(range(2, n, 2))
        for i in range(3, math.ceil(math.sqrt(n)), 2):
            if i not in multiples_set:
                multiples_set.update(range(2 * i, n, i))
        return max(0, n - len(multiples_set) - 1)

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for char_s, char_t in zip(s, t):
            if char_s in s_dict and s_dict[char_s] != char_t:
                return False
            else:
                s_dict[char_s] = char_t
            if char_t in t_dict and t_dict[char_t] != char_s:
                return False
            else:
                t_dict[char_t] = char_s
        return True

    def reverseList(self, head: ListNode) -> ListNode:
        return _reverseList_iter(head)

    def containsDuplicate(self, nums: List[int]) -> bool:
        dupes_set = set()
        for num in nums:
            if num in dupes_set:
                return True
            dupes_set.add(num)
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupes_dict: Dict[int, int] = {}
        for index, num in enumerate(nums):
            if num in dupes_dict:
                if index - dupes_dict[num] <= k:
                    return True
            dupes_dict[num] = index
        return False

    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges_list = []
        range_start = None
        range_end = None
        for num in nums:
            if range_start is None:
                range_start = num
            elif range_end is None:
                if num > range_start + 1:
                    ranges_list.append(f"{range_start}")
                    range_start = num
                else:
                    range_end = num
            elif num > range_end + 1:
                ranges_list.append(f"{range_start}->{range_end}")
                range_start, range_end = num, None
            else:
                range_end = num
        if range_start is not None:
            if range_end:
                ranges_list.append(f"{range_start}->{range_end}")
            else:
                ranges_list.append(f"{range_start}")

        return ranges_list

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        stack_seq = queue_seq = head.val
        counter = 0
        digit_move = 10
        while (head := head.next) is not None:
            queue_seq = 10 * queue_seq + head.val
            stack_seq += head.val * digit_move
            digit_move *= 10

        return queue_seq == stack_seq

    def moveZeros(self, nums: List[int]) -> None:
        zero_ind = None
        for ind, num in enumerate(nums):
            if num == 0:
                if zero_ind is None:
                    zero_ind = ind
            elif zero_ind is not None:
                nums[zero_ind] = num
                nums[ind] = 0
                while nums[zero_ind] != 0 and zero_ind < len(nums):
                    zero_ind += 1


def _removeElements_iter(head: ListNode, val: int) -> Optional[ListNode]:
    while head and head.val == val:
        head = head.next
    head_r = head
    while head and head.next:
        if head.next.val == val:
            head.next = head.next.next
        else:
            kead = head.next

    return head_r


from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.tail_q = self.q2
        self.body_q = self.q1

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.tail_q.append(x)
        if len(self.tail_q) > 1:
            self.body_q_tail = self.tail_q.popleft()
            self.body_q.append(self.body_q_tail)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        Best: O(1)
        Worst: O(N)
        """
        if self.tail_q:
            return self.tail_q.pop()
        if len(self.body_q) == 1:
            return self.body_q.popleft()
        while len(self.body_q) > 2:
            self.tail_q.append(self.body_q.popleft())
        new_tail_val = self.body_q.popleft()
        old_tail_val = self.body_q.popleft()
        self.body_q.append(new_tail_val)
        self.tail_q, self.body_q = self.body_q, self.tail_q
        return old_tail_val

    def top(self) -> int:
        """
        Get the top element.
        Best: O(1)
        Worst: O(N)
        """
        if self.tail_q:
            return self.tail_q[0]
        while len(self.body_q) > 1:
            self.tail_q.append(self.body_q.popleft())
        self.tail_q, self.body_q = self.body_q, self.tail_q
        return self.tail_q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        O(1)
        """
        return len(self.tail_q) + len(self.body_q) == 0


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

    def peek(self) -> int:
        """
        Get the front element.
        """

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """


from functools import reduce


def _removeElements_func(head: ListNode, val: int) -> Optional[ListNode]:
    def _drop_vals(
        curr_node: Optional[ListNode], next_node: Optional[ListNode]
    ) -> Optional[ListNode]:
        if next_node.val == val:
            curr_node.next = next_node.next if next_node.next else None
            return curr_node
        return next_node

    while head and head.val == val:
        head = head.next
    if head:
        reduce(_drop_vals, head)
    return head


from collections import deque


def _reverseList_iter(head: ListNode) -> Optional[ListNode]:
    if not head:
        return None
    ln_deque: Deque[ListNode] = deque()
    while head.next:
        ln_deque.append(head)
        head = head.next
    head_r = head
    while ln_deque:
        head.next = ln_deque.pop()
        head = head.next
    head.next = None
    return head_r
