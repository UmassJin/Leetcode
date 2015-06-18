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
            
'''
[转]
1. 我们对cnt1,cnt2减数时，相当于丢弃了3个数字（当前数字，n1, n2）。也就是说，每一次丢弃数字，我们是丢弃3个不同的数字。
而Majority number超过了1/3所以它最后一定会留下来。
设定总数为N, majority number次数为m。丢弃的次数是x。则majority 被扔的次数是x
而m > N/3, N - 3x > 0. 
3m > N,  N > 3x 所以 3m > 3x, m > x 也就是说 m一定没有被扔完
最坏的情况，Majority number每次都被扔掉了，但它一定会在n1,n2中。
2. 为什么最后要再检查2个数字呢？因为数字的编排可以让majority 数被过度消耗，使其计数反而小于n2，或者等于n2.前面举的例子即是。
另一个例子：
1 1 1 1 2 3 2 3 4 4 4 这个 1就会被消耗过多，最后余下的反而比4少。
'''
