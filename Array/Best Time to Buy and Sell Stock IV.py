'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

'''

class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        if not prices: return 0
        length = len(prices)
        
        if k > len(prices)//2: 
            return sum((i-j) for i, j in zip(prices[1:], prices[:-1]) if i > j)
            
        dp = [[0 for j in xrange(length)] for i in xrange(k+1)]
        
        for i in xrange(1,k+1):
            tmpmax = -prices[0]
            for j in xrange(1, length):
                dp[i][j] =  max( dp[i][j-1], prices[j]+tmpmax)
                tmpmax = max(tmpmax, dp[i-1][j-1]-prices[j])
        return dp[k][length-1]

# status: dp[i][j] is the max profit for up to i transactions by time j (0<=i<=K, 0<=j<=T).
# Case 1: Because buy and sell prices may not be the same, when k>len/2, that means we can do as many transactions as we want. 
# So, in case k>len/2, this problem is same to Best Time to Buy and Sell Stock II.
# Case 2: Normal case
# t[i][j] = Math.max(t[i][j - 1], prices[j] + tmpMax) gives us the maximum price when we sell at this price; 
# tmpMax = Math.max(tmpMax, t[i - 1][j-1] - prices[j]) gives us the value when we buy at this price and leave 
# this value for prices[j+1].
# tmpMax means the maximum profit of just doing at most i-1 transactions, using at most first j-1 prices, 
# and buying the stock at price[j] - this is used for the next loop.



# Reference: https://leetcode.com/discuss/25603/a-concise-dp-solution-in-java
