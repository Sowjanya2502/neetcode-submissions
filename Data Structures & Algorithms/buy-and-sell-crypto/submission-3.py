class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit =0
        for price in prices:
            if buy > price:
                buy = price
            profit = max(profit, abs(buy-price))
        return profit
