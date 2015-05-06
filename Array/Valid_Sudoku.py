'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''
class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        if not board: return 

        for i in xrange(9):
            row = []
            cal = []
            for j in xrange(9):
                if board[i][j] != '.' and board[i][j] not in row:
                    row.append(board[i][j])
                elif board[i][j] in row:
                    return False
                
                if board[j][i] != '.' and board[j][i] not in cal:  # Note: here is if not the elif !!!
                    cal.append(board[j][i])
                elif board[j][i] in cal:
                    return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                square = []
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] != '.' and board[i+x][j+y] not in square:
                            square.append(board[i+x][j+y])
                        elif board[i+x][j+y] in square:
                            return False
        return True 
        


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
        
        

