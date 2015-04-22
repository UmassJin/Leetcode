You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        
        for i in xrange(n):
            for j in xrange(i+1, n):  #注意这里从i+1开始！！！
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    
        for i in xrange(n):
            matrix[i].reverse()
        
