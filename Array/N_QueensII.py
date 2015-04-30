Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        if n == 0: return 0
        self.result = 0   # Here we should use the global variable, otherwise the result will not change
        checklist = [-1 for i in xrange(n)]
        self.queen_helper(n, 0, checklist)
        return self.result 
        
    def check_helper(self, depth, i, checklist):
            for k in xrange(depth):
                if checklist[k] == i or abs(checklist[k] - i) == abs(depth-k):
                    return False
            return True
            
    def queen_helper(self, n, depth, checklist):
        if depth == n: 
            self.result += 1; return
        for i in xrange(n):
            if self.check_helper(depth, i, checklist):
                checklist[depth] = i
                self.queen_helper(n, depth+1, checklist)
        
