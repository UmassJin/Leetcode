'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        length = len(nums)
        if length < 2: return
        i = length -2
        while i > -1 and nums[i] >= nums[i+1]:  # 注意duplicate input [5,1,1]
            i -= 1
        if i == -1:
            nums.sort()
            return
        else:
            min_index = i + 1
            for k in xrange(i+1, length):
                if nums[k] > nums[i] and nums[k] <= nums[min_index]:
                    min_index = k
            
            nums[i], nums[min_index] = nums[min_index], nums[i]
            nums[i+1:] = sorted(nums[i+1:])
            # nums[i+1:].sort()  # 这里不能用这种形式，因为nums[i+1:]相当于一个copy，然后再sort()，实际上是对copy的sort
            # 所以这里应该用sorted()，然后复制给nums[i+1:]
            return
