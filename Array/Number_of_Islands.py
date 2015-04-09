'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''

class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        result = 0
        self.used = [[False for i in xrange(n)] for j in xrange(m)]
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1' and not self.used[i][j]:
                    result += 1
                    self.dfs(grid, i, j)
        
        return result 
        
    def dfs(self, grid, i, j):
        row = len(grid)
        cal = len(grid[0])
        self.used[i][j] = True  
        if i > 0 and grid[i-1][j] == '1' and not self.used[i-1][j]:
            self.dfs(grid, i-1, j)
        if i < row-1 and grid[i+1][j] == '1' and not self.used[i+1][j]:
            self.dfs(grid, i+1, j)
        if j > 0 and grid[i][j-1] == '1' and not self.used[i][j-1]:
            self.dfs(grid, i, j-1)
        if j < cal-1 and grid[i][j+1] == '1' and not self.used[i][j+1]:
            self.dfs(grid, i, j+1)
            
