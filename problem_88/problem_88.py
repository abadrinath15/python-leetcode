from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        m -= 1
        n -= 1
        for full_ind in reversed(range(len(nums1))):
            if n < 0:
                break
            if m < 0:
                nums1[: (full_ind + 1)] = nums2[: (n + 1)]
                break
            if nums1[m] < nums2[n]:
                nums1[full_ind] = nums2[n]
                n -= 1
            else:
                nums1[full_ind] = nums1[m]
                m -= 1
