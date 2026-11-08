class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
            
        curMin = prices[0]
        curMaxProfit = 0

        for price in prices:
            curProfit = price - curMin
            
            if price < curMin:
                curMin = price
            elif curProfit > curMaxProfit:
                curMaxProfit = curProfit
        
        return curMaxProfit