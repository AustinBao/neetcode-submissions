class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        currLowest = prices[0]
        for price in prices:
            if price < currLowest:
                currLowest = price
            profit = max(profit, price - currLowest)
        return profit