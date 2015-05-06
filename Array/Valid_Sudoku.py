'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku_1(self, board):
        def check_available(i, j):
            tmp = board[i][j]; board[i][j] = 'J'
            for row in xrange(9):
                if board[row][j] == tmp:
                    return False
            
            for cal in xrange(9):
                if board[i][cal] == tmp:
                    return False
            
            for p in xrange(3):
                for q in xrange(3):
                    if board[(i/3)*3+p][(j/3)*3+q] == tmp:
                        return False
            
            board[i][j] = tmp
            return True 
            
        def sudo_helper(board):
            for i in xrange(9):
                for j in xrange(9):
                    if board[i][j] != '.':
                        if not check_available(i, j):
                            return False 
            return True
        
        return sudo_helper(board)
        
        

