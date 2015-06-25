'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

For example,
Given height = [2,1,5,6,2,3],
return 10.
'''

#思路分析:
#[G4G Set 2 O(n)](http://www.geeksforgeeks.org/largest-rectangle-under-histogram/)
#[G4G Set 1 O(nlogn)](http://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/)

'''
For every bar ‘x’, we calculate the area with ‘x’ as the smallest bar in the rectangle. If we calculate such area for every bar ‘x’ and find the maximum of all areas, 
our task is done. How to calculate area with ‘x’ as smallest bar? We need to know index of the first smaller (smaller than ‘x’) bar on left of ‘x’ and index of first 
smaller bar on right of ‘x’. Let us call these indexes as ‘left index’ and ‘right index’ respectively.
We traverse all bars from left to right, maintain a stack of bars. Every bar is pushed to stack once. A bar is popped from stack when a bar of smaller height is seen. 
When a bar is popped, we calculate the area with the popped bar as smallest bar. How do we get left and right indexes of the popped bar – the current index tells us the 
‘right index’ and index of previous item in stack is the ‘left index’.
'''

class Solution:
    # @param height, a list of integer
    # @return an integer

    def largestRectangleArea(self, height):
        height.append(0) # Corner case: [1]
        n = len(height)
        stack = []
        maxarea = 0
        i = 0
        while i < n: # 注意这里用while，不用for，否则会跳过一个
            if len(stack) == 0 or height[i] > height[stack[-1]]:  #注意这里不是比较height[i] > height[i-1]!
                stack.append(i)
                i += 1  
                # Note: we only need to i += 1 here! we do not need to add 1 in the else case 
                # since after we calculate the area, still need to push that value into stack!
            else:
                tmp_height = height[stack.pop()]
                if len(stack) == 0:
                    width = i # 注意这里 width = i 不是stack.pop()
                else:
                    width = i - stack[-1] -1 
                    # left_bound: stack[-1] + 1
                    # right_bound: i-1
                    # right_bound-left_bound+1: (i-1)-(stack[-1]+1) + 1 = i - stack[-1] -1
                tmparea = tmp_height * width
                maxarea = max(maxarea, tmparea)
        return maxarea 
