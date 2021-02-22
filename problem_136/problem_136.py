from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_numbers = {}
        for num in nums:
            if num in seen_numbers:
                seen_numbers[num] += 1
            else:
                seen_numbers[num] = 1

        for key, value in seen_numbers.items():
            if value == 1:
                return key
