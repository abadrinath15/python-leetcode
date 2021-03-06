from collections import deque
import sys
from typing import Dict, Optional, List, Tuple, Set

sys.path.append(r"/Users/aditya/Documents/Python/Leetcode")
from helpers.linked_list import ListNode, list_to_linked_list


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_num = 0
        l2_num = 0
        exp = 0
        while l1 is not None and l2 is not None:
            l1_num += 10 ** exp * l1.val
            l2_num += 10 ** exp * l2.val
            l1 = l1.next
            l2 = l2.next
            exp += 1
        while l1 is not None:
            l1_num += 10 ** exp * l1.val
            l1 = l1.next
            exp += 1
        while l2 is not None:
            l2_num += 10 ** exp * l2.val
            l2 = l2.next
            exp += 1
        summed_val = str(l1_num + l2_num)
        head_r = ListNode(val=int(summed_val[-1]))
        head = head_r
        for num in reversed(summed_val[:-1]):
            temp = ListNode(int(num))
            head.next = temp
            head = head.next
        return head_r

    def longestPalindrome(self, s: str) -> str:
        # Go learn manacher's algo
        dp_grid = [[True for _ in range(len(s))]] + [
            [False for _ in range(len(s))] for _ in range(len(s) - 1)
        ]
        longest_length = 1
        longest_palin = s[0]
        for end_ind in range(2, len(s) + 1):
            for start_ind in range(0, len(s) - 1):
                sub_str = s[start_ind : start_ind + end_ind]
                if sub_str[0] == sub_str[-1]:
                    if end_ind == 2 or dp_grid[end_ind - 3][start_ind + 1]:
                        (dp_grid[end_ind - 1])[start_ind] = True
                        if len(sub_str) > longest_length:
                            longest_length = len(sub_str)
                            longest_palin = sub_str
        return longest_palin

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        guess = (len(height) - 1) * min(height[left], height[right])
        while left < right:
            if height[left] < height[right]:
                guess = max(height[left] * (right - left), guess)
                left += 1
            else:
                guess = max(height[right] * (right - left), guess)
                right -= 1
        return guess

    def intToRoman(self, num: int) -> str:
        char_list = []
        while num > 0:
            if num >= 1000:
                char_list.extend(["M" for _ in range(num // 1000)])
                num = num % 1000
            elif num >= 900:
                char_list.append("CM")
                num -= 900
            elif num >= 500:
                char_list.append("D")
                num -= 500
            elif num >= 400:
                char_list.append("CD")
                num -= 400
            elif num >= 100:
                char_list.extend(["C" for _ in range(num // 100)])
                num = num % 100
            elif num >= 90:
                char_list.append("XC")
                num -= 90
            elif num >= 50:
                char_list.append("L")
                num -= 50
            elif num >= 40:
                char_list.append("XL")
                num -= 40
            elif num >= 10:
                char_list.extend(["X" for _ in range(num // 10)])
                num = num % 10
            elif num >= 9:
                char_list.append("IX")
                num -= 9
            elif num >= 5:
                char_list.append("V")
                num -= 5
            elif num >= 4:
                char_list.append("IV")
                num -= 4
            else:
                char_list.extend(["I" for _ in range(num // 1)])
                break

        return "".join(char_list)

    def letterCombinations(self, digits: str) -> List[str]:
        import itertools

        if digits == "":
            return []

        telephone_map = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z"),
        }
        return [
            "".join(x)
            for x in itertools.product(*map(lambda x: telephone_map[x], digits))
        ]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations

        pos_set = set(pos := [x for x in nums if x > 0])
        neg_set = set(negs := [x for x in nums if x < 0])
        num_zeros = len([x for x in nums if x == 0])
        res = []
        seen = set()
        for curr_tup in permutations(pos, r=2):
            if (sorted_tup := tuple(sorted(curr_tup))) not in seen:
                if (curr_neg := -1 * sum(curr_tup)) in neg_set:
                    res.append([curr_tup[0], curr_tup[1], curr_neg])
                    seen.add(sorted_tup)
        for curr_tup in permutations(negs, r=2):
            if (sorted_tup := tuple(sorted(curr_tup))) not in seen:
                if (curr_pos := -1 * sum(curr_tup)) in pos_set:
                    res.append([curr_tup[0], curr_tup[1], curr_pos])
                    seen.add(sorted_tup)
        if num_zeros > 0:
            for po in pos:
                if (curr_neg := po * -1, po) not in seen:
                    if curr_neg in neg_set:
                        res.append([po, curr_neg, 0])
                        seen.add((curr_neg, po))

        if num_zeros > 2:
            res.append([0, 0, 0])
        return res

    def removeNthFromEnd(self, head: ListNode, n: int) -> Optional[ListNode]:
        from collections import deque

        head_r = head
        end_deque = deque(maxlen=n + 1)
        while head is not None:
            end_deque.append(head)
            head = head.next

        if n == len(end_deque):
            head_r = head_r.next
            return head_r
        prior = end_deque.popleft()
        try:
            remove = end_deque.popleft()
        except IndexError:
            return None
        try:
            next_node = end_deque.popleft()
        except IndexError:
            prior.next = None
            return head_r

        prior.next = next_node
        return head_r

    def generateParenthesis(self, n: int) -> List[str]:
        def _gen_par_helper(
            curr_str: str,
            open_parens: int,
            close_parens: int,
            res: List[str],
        ):
            if len(curr_str) == 2 * n:
                res.append(curr_str)
                return
            if open_parens < n:
                _gen_par_helper(curr_str + "(", open_parens + 1, close_parens, res)
            if close_parens < open_parens:
                _gen_par_helper(curr_str + ")", open_parens, close_parens + 1, res)
            return res

        return _gen_par_helper("", 0, 0, [])
