# nCr = n! / (r! *(n-r)!)
# nC(r+1) = n! / (r+1)! *(n-r-1)!) = n! * / ((r! * (r+1)) * ((n - r)! / (n-r))
# = n! / (r! * (n-r)!) * (n-r) / (r+1) = nCr * (n-r) / (r+1)
from typing import List


import itertools


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 2
        return list(
            itertools.accumulate(
                range(1, rowIndex), lambda x, y: x * (rowIndex - y) // (y - 1)
            )
        )
