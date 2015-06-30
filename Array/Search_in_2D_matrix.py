```
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true
```
# Good answer !

    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        left = 0; right = m*n - 1
        
        while left <= right:
            mid = (left+right)>>1
            value = matrix[mid/n][mid%n]
            if value == target:
                return True
            elif value > target:
                right = mid -1 
            elif value < target:
                left = mid + 1
        
        return matrix[right/n][right%n] == target  # Use right, not left ! case: [[1]] 2
        
