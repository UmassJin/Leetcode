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


# Bad answer, AC but not consice ! 
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        
        left = 0; right = m-1; row = 0
        while left <= right:
            mid = (left+right)/2
            if target > matrix[mid][0]:
                if target <= matrix[mid][n-1]:
                    row = mid
                    break
                left = mid + 1
            elif target == matrix[mid][0]:
                return True
            else:
                right = mid -1 
        
        if left > right: return False
        left = 0; right = n-1
        while left <= right:
            mid = (left+right)/2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target == matrix[row][mid]:
                return True
            else:
                right = mid - 1
        return False 
