class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = prices[0]
        profit = 0

        for price in prices[1:]:
            if bought > price:
                bought = price

            profit = max(profit,price - bought)

        return profit
