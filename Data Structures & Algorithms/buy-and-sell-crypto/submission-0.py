class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 #buy
        r = 0 #sell
        maxprofit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxprofit = max(profit, maxprofit)
            else:
                l = r #if l is > r then we directly jump to r since r is at better price to buy
            r += 1 #we always do r += 1, even at l,r = 0 we have to increment to check if l < r
        return maxprofit
        
            
                
