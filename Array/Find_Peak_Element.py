'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.

'''

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        return self.peak_helper(nums, 0, len(nums)-1)
        
    def peak_helper(self, nums, start, end):
        if start == end:
            return start
        if end - start == 1:
            if nums[start] > nums[end]:
                return start
            else:
                return end
        
        mid = (start + end)/2
        
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid 
        
        if nums[mid] < nums[mid-1]:
            return self.peak_helper(nums, start, mid-1)
        
        if nums[mid] < nums[mid+1]:
            return self.peak_helper(nums, mid+1, end)
        
# test case: [2,1,2] 
# when we use the recursion, we need to compare the nums[mid] < nums[mid-1], not nums[mid] > nums[mid-1].
# otherwise the above case [2,1,2] will return None, actually, it could return index 0 or index 2. 
