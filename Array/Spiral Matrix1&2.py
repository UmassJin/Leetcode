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


Spiral Matrix II
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
For example,
Given n = 3,
You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
Method 1 
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        result = []
        loop = 1
        value = 1

        if n == 0:
            return []
        if n == 1:
            return [[1]]

        for i in range(n):
            result.append([])

        for i in range(n):
            result[0].append(value)
            value += 1

        step = 0
        while loop <= n:
            row = step+1

            while row <= n-(step+1):
                result[row].insert(step,value)
                value += 1
                row += 1
            row = n-step-1

            tmp = step
            for i in range(n-loop):
                result[row].insert(tmp,value)
                value += 1

            loop += 1
            row = row-1

            while row >= step+1:
                result[row].insert(step,value)
                value +=1
                row -= 1
            row += 1
            for i in range(n-loop):
                result[row].insert(i+step+1, value)
                value+= 1
            loop += 1
            step += 1
        return result

Method 2 
    def generateMatrix(self, n):
        result = [[0 for j in xrange(n)] for i in xrange(n)]
        i = 0; k = 1
        while k <= n*n:
            j = i
            while j < n-i:
                result[i][j]=k
                j+= 1; k+=1
                
            j = i +1
            while j < n-i:
                result[j][n-i-1]=k
                j+=1; k+=1
                
            j = n-i-2
            while j > i:
                result[n-i-1][j] = k
                j-=1; k+= 1
                
            j = n-i-1
            while j >i:
                result[j][i] = k
                j-=1; k+=1
            i += 1
        return result 
