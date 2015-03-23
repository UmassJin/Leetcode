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
