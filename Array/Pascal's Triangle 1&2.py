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


class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        pre = []
        for i in xrange(rowIndex + 1):  # Note: here is rowIndex + 1
            line = [1]*(i+1)
            if i > 1:
                for j in xrange(1, i):
                    line[j] = pre[j-1] + pre[j]
            pre = line[:]
        return pre
