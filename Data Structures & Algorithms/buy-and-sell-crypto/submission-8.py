class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <= 1:
            return 0

        buyIndex, sellIndex = 0, 1
        maxProfit = 0

        while sellIndex < len(prices):
            if prices[sellIndex] < prices[buyIndex]:
                buyIndex = sellIndex
                sellIndex = buyIndex + 1

            else:
                if maxProfit < prices[sellIndex] - prices[buyIndex]:
                    maxProfit = prices[sellIndex] - prices[buyIndex]
                sellIndex += 1

        return maxProfit
            