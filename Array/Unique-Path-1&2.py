Unique Path I
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach 
the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        result = [0 for i in xrange(n)]
        result[0] = 1
        
        for i in xrange(m):
            for j in xrange(1,n):
                result[j] += result[j-1]
        
        return result[n-1]

Unique Path II
Follow up for "Unique Paths":
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
Note: m and n will be at most 100.

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        result = [ 0 for i in xrange(len(obstacleGrid[0]))]
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        for i in xrange(len(obstacleGrid)):
            for j in xrange(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    result[j] = 0
                else:
                    if j > 0:
                        result[j] += result[j-1]
                    elif i == 0 and j == 0:
                        result[j] = 1
        
        return result[len(obstacleGrid[0])-1]            
