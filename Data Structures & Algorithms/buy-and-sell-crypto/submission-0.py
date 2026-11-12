class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        

        while r < len(prices):
            # if prices of left are smaller than right this loop goes on,
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            
            # otherwise left moves to right
            else:
                l = r
            # this keeps on incrementing the right pointer
            r += 1
        return maxProfit
        


        