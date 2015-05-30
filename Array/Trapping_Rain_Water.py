Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.
For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Method 1
# 基本思路就是维护一个长度为n的数组，进行两次扫描，一次从左往右，一次从右往左。第一次扫描的时候维护对于每一个bar左边最大的高度是多少，
# 存入数组对应元素中，第二次扫描的时候维护右边最大的高度，并且比较将左边和右边小的最大高度（我们成为瓶颈）存入数组对应元素中。
# 这样两遍扫描之后就可以得到每一个bar能承受的最大水量，从而累加得出结果。这个方法只需要两次扫描，所以时间复杂度是O(2*n)=O(n)。
# 空间上需要一个长度为n的数组，复杂度是O(n)。

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

# Method 2: 
# 另一种方法，相对不是那么好理解，但是只需要一次扫描就能完成。基本思路是这样的，用两个指针从两端往中间扫，
# 在当前窗口下，如果哪一侧的高度是小的，那么从这里开始继续扫，如果比它还小的，肯定装水的瓶颈就是它了，
# 可以把装水量加入结果，如果遇到比它大的，立即停止，重新判断左右窗口的大小情况，重复上面的步骤。
# 这里能作为停下来判断的窗口，说明肯定比前面的大了，所以目前肯定装不了水（不然前面会直接扫过去）。
# 这样当左右窗口相遇时，就可以结束了，因为每个元素的装水量都已经记录过了。

def trapRainWater(self, heights):
        if not heights: return 0
        
        left = 0; right = len(heights) - 1
        minv = 0
        result = 0 
        
        while left < right:
            minv = min(heights[left], heights[right])
            if minv == heights[left]:
                left += 1
                while left < right and heights[left] < minv:
                    result += minv - heights[left]
                    left += 1
            if minv == heights[right]:
                right -= 1
                while right > left and heights[right] < minv:
                    result += minv - heights[right]
                    right -= 1
        
        return result 
