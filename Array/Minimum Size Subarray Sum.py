'''
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

'''

    def minSubArrayLen(self, s, nums):
        if not nums: return 0
        isum = 0; start = 0; minlen = len(nums)+1
        for i in xrange(len(nums)):
            isum += nums[i]
            while isum >= s:
                minlen = min(minlen, i-start+1)
                isum -= nums[start]  # 注意：这里先减去start的数字，start再+1
                start += 1
        if minlen == len(nums)+1:
            return 0
        return minlen
