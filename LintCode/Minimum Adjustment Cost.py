'''
Given an integer array, adjust each integers so that the difference of every adjacent integers are not greater than a given number target.

If the array before adjustment is A, the array after adjustment is B, you should minimize the sum of |A[i]-B[i]|

Have you met this question in a real interview? Yes
Example
Given [1,4,2,3] and target = 1, one of the solutions is [2,3,2,3], the adjustment cost is 2 and it's minimal.

Return 2.

Note
You can assume each number in the array is a positive integer and not greater than 100.
'''

class Solution:
    # @param A: An integer array.
    # @param target: An integer.
    def MinAdjustmentCost(self, A, target):
        if not A: return 0
        lena = len(A)
        dp = [[(1<<32)/2 for i in xrange(101)] for j in xrange(lena)]
        
        for i in xrange(lena):
            for j in xrange(1, 101):
                if i == 0:
                    dp[0][j] = abs(j - A[0])
                else:
                    for k in xrange(1, 101):
                        if abs(j-k) <= target:
                            dp[i][j] = min(dp[i][j], abs(j-A[i]) + dp[i-1][k])
        
        ret = dp[lena-1][0]
        for i in xrange(101):
            ret = min(ret, dp[lena-1][i])
        return ret

# 解题思路:
# 对于每一个 A[i], 我们从1到100一次遍历, 对于A[0]，直接将dp[0][j] = abs(A[0]-i)
# 对于 A[i], 将1到100一次遍历，计算出diff1 ＝ abs(j - A[i]) 1<=j<=100
# 然后为了保证A[i]-A[i-1] <= target, 所以diff1 加上 dp[i-1][k]  abs(k-j) <= target, 
# 实际上是计算 A[i]取j, A[i-1]取k时，min diff
# Status: dp[i][j]: 把index = i的值修改为j，所需要的最小花费
# Initialization: dp[0][j] = abs(A[0]-j) 1<= j <= 100
# Function: dp[i][j] = min(dp[i][j], abs(j-A[i]) + dp[i-1][k])
# Result: 遍历每一个dp[len(A)-1][j]取min

# Reference: http://www.cnblogs.com/yuzhangcmu/p/4153927.html
# https://github.com/algorhythms/LintCode/blob/master/Minimum%20Adjustment%20Cost.py
