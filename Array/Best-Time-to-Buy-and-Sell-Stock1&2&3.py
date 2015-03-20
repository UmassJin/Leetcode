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
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple 
transactions at the same time (ie, you must sell the stock before you buy again).

The optimization solution is add ALL the profits if Prices[i]>Prices[i-1]
73ms
class Solution:
    # @param prices, a list of integer
    # @return an integer
    # 73ms
    def maxProfit(self, prices):
        length = len(prices)
        if length < 2: return 0
        profit = 0
        for i in xrange(len(prices)-1,0,-1):
            if (prices[i]>prices[i-1]):
                profit += (prices[i]-prices[i-1]) 
        return profit 
