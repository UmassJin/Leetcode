Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

# Analysis: maintain a row length of Integer array H recorded its height of '1's, 
# and scan and update row by row to find out the largest rectangle of each row.

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        row = len(matrix)
        cal = len(matrix[0]) + 1
        result = 0
        height = [0 for _ in xrange(cal)]
        
        for i in xrange(row):
            stack = []
            for j in xrange(cal):
                if j < cal - 1:
                    if matrix[i][j] == "1":  # Note: here we should determine whether matrix[i][j]=='1' or not
                        height[j] += 1
                    else:
                        height[j] = 0
                
                while stack and height[stack[-1]] >= height[j]:  # 注意这里要用while ！！！否则只计算了一次的面积
                    h_index = stack.pop()
                    ht = height[h_index]
                    if stack:
                        width = j - stack[-1] - 1
                    else:
                        width = j
                    result = max(result, ht*width)
                stack.append(j)  
        return result 
                

'''
Note1 : need to use "while" not "if"
Input:
["01101","11010","01110","11110","11111","00000"]
Output:
5
Expected:
9
'''
