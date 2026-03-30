class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        l, r = 0, 1 
        
        while l < r and r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r +=1
            else:
                diff = prices[r] - prices[l]
                maxProfit = max(diff, maxProfit)
                r+=1
        
        return maxProfit


        