from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        freq_elem = nums[0]
        for num in nums:
            if counter == 0:
                freq_elem = num
                counter += 1
            elif num == freq_elem:
                counter += 1
            else:
                counter -= 1

        return freq_elem
