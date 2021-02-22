from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_val = 0
        for price in reversed(prices):
            if price > max_val:
                max_val = price
            elif (curr_profit := max_val - price) > max_profit:
                max_profit = curr_profit
        return max_profit
