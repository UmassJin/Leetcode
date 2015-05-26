'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        count = 0
        result = 0
        for num in nums:
            if count == 0:
                result = num
                count += 1
            elif result == num:
                count += 1
            else:
                count -= 1
        return result 
