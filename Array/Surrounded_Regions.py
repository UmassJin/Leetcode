'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

'''

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    
    def solve(self, board):
        if not board: return 
        queue = []
        
        m = len(board); n = len(board[0])
        
        for i in xrange(m):
                self.dfs(i, 0, board, queue)
                self.dfs(i, n-1, board, queue)
                
        for j in xrange(1, n-1):
                self.dfs(m-1, j, board, queue)
                self.dfs(0, j, board, queue)
    
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'J':
                    board[i][j] = 'O'
                    
    def dfs(self, x, y, board, queue):
        self.check(x, y, board, queue)
        while queue:
            i, j = queue.pop()
            self.check(i+1, j, board, queue)  # 注意这里不是用dfs,用check
            self.check(i-1, j, board, queue)
            self.check(i, j+1, board, queue)
            self.check(i, j-1, board, queue)

    def check(self, x, y, board, queue):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != 'O': return
        queue.append((x,y))
        board[x][y] = 'J'

# 解题思路:
# instead of go through every node in the board, we only need to go through the edge 
# of the board, if there is 'O' in the edge, then find all the adjecent 'O', make it
# as 'J', then go through the board again, if the 'O', will mark it as 'X', if 'J', 
# mark it as 'O'
