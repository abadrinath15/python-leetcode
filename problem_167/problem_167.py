from typing import List, Tuple
from bisect import bisect_left


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return _shortening_list(numbers, target)


def _shorten_nums(
    numbers: List[int],
    target: int,
    adj: int = 0,
) -> Tuple[List[int], int]:
    if len(numbers) == 2:
        return numbers, adj
    mid = len(numbers) // 2
    if numbers[mid] + numbers[-1] < target:
        return _shorten_nums(numbers[mid + 1 :], target, adj + mid + 1)
    elif numbers[0] + numbers[mid] > target:
        return _shorten_nums(numbers[:mid], target, adj)
    else:
        return numbers, adj


def _shortening_list(numbers: List[int], target: int) -> List[int]:
    def _shorten_nums(
        numbers: List[int],
        target: int,
        adj: int = 0,
    ) -> Tuple[List[int], int]:
        if len(numbers) == 2:
            return numbers, adj
        mid = len(numbers) // 2
        if numbers[mid] + numbers[-1] < target:
            return _shorten_nums(numbers[mid + 1 :], target, adj + mid + 1)
        elif numbers[0] + numbers[mid] > target:
            return _shorten_nums(numbers[:mid], target, adj)
        else:
            return numbers, adj

    def _index_of(a, x) -> int:
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        return -1

    shortened_nums, adj = _shorten_nums(numbers, target)
    if len(shortened_nums) == 2:
        return [1 + adj, 2 + adj]
    l_index, r_index = 0, len(shortened_nums) - 1
    while l_index < r_index:
        if numbers[l_index] + numbers[r_index] == target:
            return [l_index + adj + 1, r_index + adj + 1]
        elif numbers[l_index] + numbers[r_index] > target:
            r_index -= 1
        else:
            l_index -= 1
