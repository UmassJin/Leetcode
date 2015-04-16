'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

For example,
Given height = [2,1,5,6,2,3],
return 10.
'''

#思路分析:
#[G4G Set 2 O(n)](http://www.geeksforgeeks.org/largest-rectangle-under-histogram/)
#[G4G Set 1 O(nlogn)](http://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/)


class Solution:
    # @param height, a list of integer
    # @return an integer

    def largestRectangleArea(self, height):
        height.append(0) # Corner case: [1]
        n = len(height)
        stack = []
        maxarea = 0
        i = 0
        while i < n:
            if len(stack) == 0 or height[i] > height[stack[-1]]:
                stack.append(i)
                i += 1  
                # Note: we only need to i += 1 here! we do not need to add 1 in the else case 
                # since after we calculate the area, still need to push that value into stack!
            else:
                tmp_height = height[stack.pop()]
                if len(stack) == 0:
                    width = i
                else:
                    width = i - stack[-1] -1 
                    # left_bound: stack[-1] + 1
                    # right_bound: i-1
                    # right_bound-left_bound+1: (i-1)-(stack[-1]+1) + 1 = i - stack[-1] -1
                tmparea = tmp_height * width
                maxarea = max(maxarea, tmparea)
        return maxarea 
