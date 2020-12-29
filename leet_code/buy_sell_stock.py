"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""

class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        minprice = prices[0]
        maxprofit = 0
        for price in prices[1:]:
            if price - minprice > maxprofit:
                maxprofit = price - minprice
            minprice = price if price < minprice else minprice
        return maxprofit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))