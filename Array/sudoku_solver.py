'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        def check_valid(i, j):
            tmp = board[i][j]; board[i][j] = 'J'
            for row in xrange(9):
                if board[row][j] == tmp: return False
            for cal in xrange(9):
                if board[i][cal] == tmp: return False
            for p in xrange(3):
                for q in xrange(3):
                    if board[(i/3)*3+p][(j/3)*3+q] == tmp: # Note here!
                        return False
            board[i][j] = tmp
            return True 
        
        def sudoku(board):    
            for i in xrange(9):
                for j in xrange(9):
                    if board[i][j] == '.':
                        for k in xrange(1,10):
                            board[i][j] = str(k)
                            if check_valid(i,j) and sudoku(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True # Here we should return True after we checked all element 
                    
        sudoku(board)
        
# here we can not check the board[row][j] == board[i][j] directly 
# since for example input ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."], we set the board[0][0] as 1, then we pass i = 0 and j = 0 to the check function, we go through each cal which 
# row is 0, when check board[0][0], it always equal to the board[0][0], which is the issue 
