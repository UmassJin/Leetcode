```
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
```


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    # Recursion 
    def permute_1(self, nums):
        result = []
        if len(nums) == 1: return [nums]
        else:
            for i in xrange(len(nums)):
                for ele in self.permute(nums[:i] + nums[i+1:]):
                    result.append([nums[i]] + ele)
            return result 
            
    # Iteration         
    def permute(self, num):
            result = [[]]
            for i in num:
                permutations = []  # Note: here permutations need to clean
                if result == [[]]:
                    result = [[i]]
                else :
                    for j in result :
                        for k in range(len(j)+1) :  # Note: this for loop should be after temp = j[:]
                            temp = j[:]
                            temp.insert(k,i)
                            permutations.append(temp)
                    result = permutations[:]
            return result
