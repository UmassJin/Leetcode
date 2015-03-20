I)
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0; highest = 0
        length = len(prices)
        if length <= 1: return 0
        for i in xrange(length-1,-1,-1):
            highest = max(highest,prices[i])
            profit = max(profit, highest-prices[i])
        return profit 
        
        
II)
