'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between 
nums[i] and nums[j] is at most t and the difference between i and j is at most k.
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k <= 0 or t < 0: return False  # 这里check k <= 0, t < 0: [0], 0, 0 return False 
        idict = collections.OrderedDict() # 用 ordered dict to track the order of the key 
        
        for num in nums:
            bucket = num if t == 0 else num // t
            
            for m in (idict.get(bucket-1), idict.get(bucket), idict.get(bucket+1)):
                if m != None and abs(num - m) <= t:  # here we could not use "if m ", since if m == 0: it will also return False!
                    return True 
                    
            if len(idict) == k: 
                idict.popitem(False)
            idict[bucket] = num
        
        return False 

# testcase: 
# Input:	[3,6,0,2], 2, 2
# Output:	false
# Expected:	true

# https://leetcode.com/discuss/38176/python-ordereddict
# https://leetcode.com/discuss/38206/ac-solution-in-java-using-o-n-bucket-with-explanation
