from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        else:
            res = [[1]]
        for row_ind in range(0, numRows - 1):
            prior_row = res[row_ind]
            current_row = (
                [1]
                + [
                    prior_row[col] + prior_row[col - 1]
                    for col in range(1, len(prior_row))
                ]
                + [1]
            )
            res.append(current_row)

        return res
