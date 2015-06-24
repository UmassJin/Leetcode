Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        if not nums: return 1
        n = len(nums)
        for i in xrange(n):
            while nums[i] != i + 1:
                if (nums[i] <= 0) or (nums[i] > n) or (nums[nums[i]-1] == nums[i]):break
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                # Note: the following assignment is wrong !!
                # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                 
        for i in xrange(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

# There are some cases need to consider:
# The negative number and the duplicate number 
# Some corner case: [1,1], [1], [2], [2,2]
# Note: multiple assignment, 从左边往右边复值，如果是nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]， 
# 则nums[nums[i]-1]先赋值给nums[i]--> nums[i]是nums[2-1]=nums[1]=1，则nums[i]＝1， 再计算
# Nums[i] 给nums[nums[i]-1]，这个时候，nums[i]为之前的值2，但是nums[nums[i]-1]=nums[1-1]=nums[0] ===> 2
# 所以nums[0] = 2不变！！！！
# 参考函数
#a, b = 1, 2
#while b < 10:
#    print "b: ", b
#    a, b = a + b, a
#    print "after a: %d b: %d" %(a,b)
#    a = a + 1
#    print "after2 a: %d b: %d" %(a,b)
'''
b:  2
after a: 3, b: 1
after2 a: 4, b: 1
b:  1
after a: 5, b: 4
after2 a: 6, b: 4
b:  4
after a: 10, b: 6
after2 a: 11, b: 6
b:  6
after a: 17, b: 11
after2 a: 18, b: 11
'''
