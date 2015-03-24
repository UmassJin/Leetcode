Given a m x n grid filled with non-negative numbers, find a path from top left to bottom 
right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

# Note: here we use one dimensional array is enough 
# state: dp[i] 表示从起点走到第i列的最小和
# initialize: dp[0] = grid[0][0], then
              第0行，dp[j]=grid[i][j]+dp[j-1]
              第0列，dp[j]=grid[i][j]+dp[j]
# result: dp[n-1]

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [0 for i in xrange(n)]
        
        for i in xrange(m):
            for j in xrange(n):
                if i == 0:
                    if j == 0:
                        dp[j] = grid[i][j]
                    else:
                        dp[j] = grid[i][j] + dp[j-1]
                else:
                    if j == 0:
                        dp[j] += grid[i][j]
                    else:
                        dp[j] = min(grid[i][j] + dp[j-1], grid[i][j]+ dp[j])
        
        return dp[n-1]    
    
    # Use two division array 
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]
    
