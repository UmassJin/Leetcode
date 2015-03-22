Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
For example,
Given board =
[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

# Analysis: Backtracking 

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def dfs(x, y, word):
            if len(word) == 0: return True
            
            if x < len(board)-1 and board[x+1][y] == word[0]:
                temp = board[x][y]
                board[x][y] = '#'
                if (dfs(x+1, y, word[1:])):
                    return True
                board[x][y]= temp    
                
            if x > 0 and board[x-1][y] == word[0]:
                temp = board[x][y]
                board[x][y] = '#'
                if (dfs(x-1, y, word[1:])):
                    return True
                board[x][y]= temp 
            
            if y < len(board[0])-1 and board[x][y+1] == word[0]:
                temp = board[x][y]
                board[x][y] = '#'
                if (dfs(x, y+1, word[1:])):
                    return True
                board[x][y]= temp 
            
            if y > 0 and board[x][y-1] == word[0]:
                temp = board[x][y]
                board[x][y] = '#'
                if (dfs(x, y-1, word[1:])):
                    return True
                board[x][y]= temp 
                
            return False    
        
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:
                    if (dfs(i, j, word[1:])):
                        return True
        return False    
    
    # Method 2 
    def exist(self, board, word):
        visited = {}
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board,word,i,j,visited,0):
                    return True
        return False
    
    def dfs(self,board, word, x, y, visited, pos):
        if pos == len(word):
            return True
        
        if x<0 or x == len(board) or y<0 or y == len(board[0]) \
           or visited.get((x,y)) or board[x][y]!= word[pos]:
            return False
        
        visited[(x,y)] = True
        result = self.dfs(board,word,x+1,y,visited,pos+1) or \
                 self.dfs(board,word,x-1,y,visited,pos+1) or \
                 self.dfs(board,word,x,y+1,visited,pos+1) or \
                 self.dfs(board,word,x,y-1,visited,pos+1)
        visited[(x,y)] = False

        return result 
        
