'''
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob_helper(self, nums, start, end):
        pre = 0; cur = 0
        for i in xrange(start, end):
            tmp = pre
            pre = cur
            cur = max(tmp+nums[i], pre)
        return max(pre, cur)
        
    def rob(self, nums):
        n = len(nums)
        if n == 0 : return 0
        if n == 1 : return nums[0]
        return max(self.rob_helper(nums, 0, n-1), self.rob_helper(nums, 1, n))


# test case: [1] or [0]
# test case: [2,1,1,2]

# Reference: https://leetcode.com/discuss/36544/simple-ac-solution-in-java-in-o-n-with-explanation
