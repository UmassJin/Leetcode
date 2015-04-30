```
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
```

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        result = []
        if n == 0: return result 
        checklist = [-1 for i in xrange(n)]
        self.queen_helper(result, n, [], checklist, 0)
        return result 
    
    def check_helper(self, checklist, depth, i):
        for k in xrange(depth):
            if (checklist[k] == i) or (abs(checklist[k]-i) == depth-k):
                    return False
        return True 
        
    def queen_helper(self, result, n, sublist, checklist, depth):
        if depth == n:
            result.append(sublist); return
        
        for i in xrange(n):
            if self.check_helper(checklist, depth, i):
                checklist[depth] = i
                s = '.'*n
                self.queen_helper(result, n, sublist + [s[:i]+'Q'+s[i+1:]], checklist, depth + 1)
                
    def solveNQueens_1(self, n):
        def check(depth, j):
            for i in xrange(depth):
                #if board[i] == j or abs(board[i]-j) == abs(depth-i):
                if board[i] == j:
                    return False
            return True        
            
        def dfs(depth, valuelist):
            if depth == n: result.append(valuelist); return
            for i in xrange(n):
                if check(depth, i):
                    board[depth] = i
                    s = '.' * n
                    dfs(depth+1, valuelist + [s[:i]+'Q'+s[i+1:]])
            
        board = [-1 for i in xrange(n)]
        result = []
        dfs(0,[])
        return result
