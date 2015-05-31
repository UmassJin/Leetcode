'''
Give you an integer matrix (with row size n, column size m)，find the longest increasing continuous subsequence in this matrix. (The definition of the longest increasing continuous subsequence here can start at any row or column and go up/down/right/left any direction).

Have you met this question in a real interview? Yes
Example
Given a matrix:

[
  [1 ,2 ,3 ,4 ,5],
  [16,17,24,23,6],
  [15,18,25,22,7],
  [14,19,20,21,8],
  [13,12,11,10,9]
]
return 25

'''

class Solution:
    # @param {int[][]} A an integer matrix
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequenceII(self, A):
        if not A or not A[0]: return 0
        
        m = len(A); n = len(A[0])
        result = 1
        dp = [[0 for i in xrange(n)] for j in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                result = max(result, self.dfs(A, i, j, dp, result))
        return result 
    
    def dfs(self, A, i, j, dp, result): 
        if dp[i][j] != 0: return dp[i][j]
        
        dx = [0,1,0,-1]
        dy = [-1,0,1,0]
        
        for k in xrange(4):
            x = i + dx[k]
            y = j + dy[k]
            if x >= 0 and x < len(A) and y >= 0  and y < len(A[0]) and A[x][y] > A[i][j]:
                dp[i][j] = max(dp[i][j], self.dfs(A, x, y, dp, result))
        
        dp[i][j] += 1
        return dp[i][j]
