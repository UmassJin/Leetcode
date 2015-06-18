'''
Given an array of integers and a number k, the majority number is the number that occurs more than 1/k of the size of the array.

Find it.

Have you met this question in a real interview? Yes
Example
Given [3,1,2,3,2,3,3,4,4,4] and k=3, return 3.

Note
There is only one majority number in the array.
'''

class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        if not nums or len(nums) < k: return None
        idict = {}
        total = 0
        i = 0
        
        while i < len(nums) and total < k-1:
            if nums[i] not in idict:
                idict[nums[i]] = 1
                total += 1
            else:
                idict[nums[i]] += 1
            i += 1
        
        while i < len(nums):
            if nums[i] in idict:
                idict[nums[i]] += 1
            else:
                if 0 in idict.values():
                    for k, v in idict.items():
                        if v == 0:
                            del idict[k]
                            break
                    idict[nums[i]] = 1
                else:
                    for item in idict:
                        idict[item] -= 1
            i += 1
        
        new_idict = {}
        maxnum = 0; maxcount = 0
        for num in nums:
            if num in idict.keys():
                new_idict[num] = new_idict.get(num, 0) + 1
                if new_idict[num] > maxcount:
                    maxcount = new_idict[num]
                    maxnum = num
                    
        return maxnum
            
