from __future__ import annotations
from collections import deque
import itertools
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def __iter__(self):
        while self:
            yield self
            self = self.next

    def __eq__(self, o: ListNode) -> bool:
        for left, right in itertools.zip_longest(self, o):
            if not (left or right):
                return True
            try:
                if left.val != right.val:
                    return False
            except AttributeError:
                return False
        return True


def list_to_linked_list(input_list: List[int]) -> Optional[ListNode]:
    if not input_list:
        return None
    input_dq = deque(input_list)
    head = ListNode(input_dq.popleft())
    head_r = head
    for val in input_dq:
        head.next = ListNode(val)
        head = head.next
    return head_r
