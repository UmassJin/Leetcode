Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
For example,
Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    # Brute Force Solution 
    def spiralOrder(self, matrix):
      result = []
    
      while matrix:
        for element in matrix[0]:
            result.append(element)
        del matrix[0]
        
        if matrix:
            i = 0
            j = 0
            while i < len(matrix):
                n = len(matrix[j])
                result.append(matrix[i][n-1])
                del matrix[i][n-1]
                if len(matrix[i])==0:
                    del matrix[i]
                    i -= 1
                    j -= 1
                i += 1
                j += 1
        
        if matrix: 
            m = len(matrix)
            for i in range(len(matrix[m-1])-1,-1,-1):
                result.append(matrix[m-1][i])
                del matrix[m-1][i]
                if len(matrix[m-1])==0:
                    del matrix[m-1]
        
        if matrix:
            for i in range(len(matrix)-1,-1,-1):
                result.append(matrix[i][0])
                del matrix[i][0]
                if len(matrix[i])==0:
                    del matrix[i]
            
      return result       
    
    # Method 2
    def spiralOrder(self, matrix):
        result = []
        
        while matrix:
            result += matrix.pop(0)
            
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
                    
            if matrix:
                result += matrix.pop()[::-1]
            
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result            
