'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, nums):
        n = len(nums)
        if n < 2: return 0
        imin = min(nums); imax = max(nums)
        gap = 0
        
        bucket_size = (imax - imin - 1)/(n - 1) + 1
        #bucket_size = int(math.ceil((imax - imin)/(n-1))) # wrong! [3,6,9,1]
        bucket_arr = [[float('inf'), float('-inf')] for i in xrange(n)]
        
        for num in nums:
            index = (num - imin) /bucket_size
            bucket_arr[index][0], bucket_arr[index][1] = min(num, bucket_arr[index][0]), max(num, bucket_arr[index][1])
        
        pre_max = bucket_arr[0][1]
        for bucket in bucket_arr[1:]:
            if bucket[0] == float('inf'):
                continue
            gap = max(gap, bucket[0]-pre_max)
            pre_max = bucket[1]
        return gap
        
# test case: [1,1000000], 
# Reference: https://leetcode.com/discuss/18499/bucket-sort-java-solution-with-explanation-o-time-and-space
# 这道题目的思路是：对于给定的区间[imin, imax],the max gap between the numbers should not smaller than ceiling[(imax-imin)/(n-1)]
# for example: [1,2,3,4,5,6,7,8,9], 如果给定的个数为3，区间为1到9，最小的gap为4，任意取3个数，会发现最小gap肯定为4
# 我们取n个bucket，所以第kth bucket contains numbers in [min+(k-1)gap, min + k* gap]
# Basically we argue that the largest gap can not be smaller than (max-min)/(N-1), 
# so if we make the buckets smaller than this number, any gaps within the same bucket is not the amount we are looking for, 
# so we are safe to look only for the inter-bucket gaps.
