'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
'''

# Method 1: use the 2D array DP, the details showed in the following links 
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]: return 0
        m = len(matrix); n = len(matrix[0])
        dp = [[0  for i in xrange(n)] for j in xrange(m)]
        maxsize = 0
        
        for i in xrange(n):
            dp[0][i] = int(matrix[0][i]) - 0
            maxsize = max(maxsize, dp[0][i])
        
        for j in xrange(m):
            dp[j][0] = int(matrix[j][0]) - 0
            maxsize = max(maxsize, dp[j][0])
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxsize = max(dp[i][j], maxsize)
                else:
                    dp[i][j] = 0
        return maxsize * maxsize
    
# Best Solution: we only need one array           
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]: return 0
        m = len(matrix); n = len(matrix[0])
        maxsize = 0; last_lefttop = 0
        dp = [0 for _ in xrange(n+1)]
        
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if matrix[i-1][j-1] == '0':
                    dp[j] = 0
                else:
                    tmp = dp[j]
                    dp[j] = min(dp[j-1], dp[j], last_lefttop) + 1
                    maxsize = max(maxsize, dp[j])
                    last_lefttop = tmp
                
        return maxsize * maxsize          
            
# https://leetcode.com/discuss/38489/easy-solution-with-detailed-explanations-8ms-time-and-space            
