class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 :
            return 0
        buyDayIndex = 0
        buyPrice = prices[0]

        sellDayIndex = 0
        sellPrice = prices[0]
        
        maxProfit = 0

        for i in range(len(prices)):
            if (buyPrice > prices[i]):
                buyPrice = prices[i]
                buyDayIndex = i

            if (prices[i] > buyPrice and prices[i] - buyPrice > maxProfit):
                maxProfit =  prices[i] - buyPrice
                sellPrice = prices[i]
                
        return maxProfit