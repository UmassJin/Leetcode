'''
Given an array of integers, find two non-overlapping subarrays which have the largest sum.

The number in each subarray should be contiguous.

Return the largest sum.

Have you met this question in a real interview? Yes
Example
For given [1, 3, -1, 2, -1, 2], the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2], they both have the largest sum 7.

Note
The subarray should contain at least one number

Challenge
Can you do it in time complexity O(n) ?
'''

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here    
        if not nums:
            return 
        n = len(nums)
        left_max = list(nums)
        right_max = list(nums)

        cur = nums[0]
        for i in xrange(1, n):
            cur = max(0, cur)
            cur += nums[i]
            left_max[i] = max(left_max[i-1], cur)
            
        cur = nums[n-1]
        for i in xrange(n-2, -1, -1):
            cur = max(cur, 0)
            cur += nums[i]
            right_max[i] = max(right_max[i+1], cur)
            
        result = -1 << 31  
        for i in xrange(n-1):
            result = max(result, left_max[i] + right_max[i+1])
        return result 
