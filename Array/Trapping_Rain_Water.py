Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.
For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        left_max = 0
        left_maxlist = [ 0 for i in xrange(len(A))]
        for i in xrange(len(A)):
            if A[i] > left_max: left_max = A[i]
            left_maxlist[i] = left_max
            
        right_max = 0
        result = 0
        for i in reversed(xrange(len(A))):
            if A[i] > right_max:
                right_max = A[i]
            result += min(left_maxlist[i], right_max) - A[i]    
            
        return result  
# Idea: go through the array from left to the right, find the maximum left value
# And then go through the array from the right to the left, find the maximum right value
# for the each value A[i], the max value could contain should be min(left_max, right_max) - A[i]
