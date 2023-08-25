class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        init_price = prices[0]
        profit = 0
        for i in range(len(prices[:-1])):
            if prices[i] < init_price:
                init_price = prices[i]
            if prices[i+1] - init_price > profit:
                profit = prices[i+1] - init_price
        return profit

