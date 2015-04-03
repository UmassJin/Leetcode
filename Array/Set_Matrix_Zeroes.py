My Submissions Question Solution 
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    
    # Solution 1
    def setZeroes_1(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        tmp_cal = []
        tmp_row = []
        mark = 0
        
        for row in range(m):
            for cal in range(n):
                if matrix[row][cal] == 0:
                    if cal in tmp_cal:
                        continue
                    for i in range(m):
                        if matrix[i][cal] != 0:
                            matrix[i][cal] = 0
                        else:
                            if i not in tmp_row:
                                tmp_row.append(i)
                    tmp_cal.append(cal)
            if row in tmp_row:
                for j in range(n):
                    matrix[row][j] = 0
                mark = 0
        
  # Solution 2               
    def setZeroes(self, matrix):
        col_0 = 1
        lengthr = len(matrix)
        lengthc = len(matrix[0])
        
        for row in xrange(lengthr):
            if matrix[row][0] == 0:
                col_0 = 0  # Since the matrix[0][0] is the same one, use col_0 to record column
            for cal in xrange(1, lengthc):
                if matrix[row][cal] == 0:
                    matrix[0][cal] = 0; matrix[row][0] = 0
        
        for row in xrange(lengthr-1,-1,-1):
            for cal in xrange(lengthc-1,0,-1):
                if matrix[0][cal] == 0 or matrix[row][0] == 0:
                    matrix[row][cal] = 0
                    
        if col_0 == 0:   # This is very important ! which handle the test case 
                for i in xrange(lengthr):
                       matrix[i][0]=0
    

# Use Test case test: [[1,1,1],[0,1,2]]

                
