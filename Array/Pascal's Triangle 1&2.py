I)
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

class Solution:
    # @return a list of lists of integers
    # Method 1 
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1],[1,1]]
        if numRows == 2:
            return result
        for i in xrange(2,numRows):
            pre_list = result[i-1]
            current_list = [1]
            for j in xrange(1, i):
                current_list.append(pre_list[j-1] + pre_list[j])
                if j == i-1:
                    current_list.append(1)
                    break
            result.append(current_list)
        return result     
 
     # Method 2 
     def generate(self, numRows):
         result = []
         for i in xrange(numRows):
             result.append([1]*(i+1))
             if i > 1:
                 for j in xrange(1,i):
                    result[i][j] = result[i-1][j-1]+result[i-1][j]
         return result 
         
II)
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].
Note:
Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        result = []
        for i in xrange(rowIndex+1):
            result.append([1]*(i+1))
            if i > 1:
                for j in xrange(1,i):
                    result[i][j] = result[i-1][j] + result[i-1][j-1]
        return result[rowIndex]
