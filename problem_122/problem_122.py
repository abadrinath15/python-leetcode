from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        buy_val = None
        for index, current_price in enumerate(prices):
            if buy_val is None or buy_val > current_price:
                buy_val = current_price
            else:
                if current_price > buy_val and (
                    index == len(prices) - 1 or prices[index + 1] < current_price
                ):
                    total_profit += current_price - buy_val
                    buy_val = None
        return total_profit
