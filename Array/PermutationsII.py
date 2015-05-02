```
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
```

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        result = []
        length = len(nums)
        prev = None
        nums.sort()
        if length == 1: return [nums]
        if length == 0: return []
        
        for i, num in enumerate(nums):
            if prev == num: continue
            else: prev = num
            for ele in self.permuteUnique(nums[:i]+nums[i+1:]):
                result.append([num] + ele)
        
        return result 
