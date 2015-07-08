'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''

# https://leetcode.com/discuss/42348/3-6-easy-lines-c-java-python-ruby
def removeDuplicates(self, nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i
    
# https://leetcode.com/discuss/42340/python-lines-extra-variables-76ms-any-simpler-solution-else
def removeDuplicates(self, nums):
        if len(nums) < 3: 
            return len(nums)
        pos = 1
        for i in range(1, len(nums)-1):
            if nums[i-1] != nums[i+1]:
                nums[pos] = nums[i]
                pos += 1
        nums[pos] = nums[-1]
        return pos + 1    


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        n = len(nums)
        if n < 2: return n
        
        times = 1
        slow = 0
        for fast in xrange(1, n):
            if nums[fast] == nums[slow]:
                times += 1
                if times <= 2:
                    slow += 1
                    nums[slow] = nums[fast]   # test case [1,1,1,1,3,3] --> need to update slow !
            else:
                slow += 1
                nums[slow] = nums[fast]
                times = 1
        return slow + 1
        
