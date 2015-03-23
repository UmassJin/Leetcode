Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Method 1
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 0:
            return None
        array = [0 for i in xrange(len(triangle))]
        array[0] = triangle[0][0]
        
        for line in xrange(1, len(triangle)):
            for element in range(len(triangle[line])-1, -1, -1):
                if element == len(triangle[line])-1:
                    array[element] = array[element-1] + triangle[line][element]
                elif element == 0:
                    array[element] = array[element] + triangle[line][element]
                else:
                    array[element] = min(array[element], array[element-1]) + triangle[line][element]
        return min(array)            
        
Method 2        
    def minimumTotal(self, triangle):
        length = len(triangle)
        minlist = triangle[length-1]
        
        for i in xrange(length-2,-1,-1):
            for j in xrange(len(triangle[i])):
                minlist[j] = triangle[i][j] + min(minlist[j],minlist[j+1])
        return minlist[0]
            
