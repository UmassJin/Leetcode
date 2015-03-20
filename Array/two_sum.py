Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

class Solution:
    # @return a tuple, (index1, index2)
    # 68ms
    def twoSum(self, num, target):
        tmpnum = num[:]
        tmpnum.sort()
        length = len(num)
        i = 0; j = length-1
        
        while i < j:
            tmpval = tmpnum[i]+tmpnum[j]
            if tmpval == target:
                res1 = num.index(tmpnum[i])
                num.reverse()
                res2 = len(num)-1-num.index(tmpnum[j])
                if res1<res2: return (res1+1,res2+1)
                else: return(res2+1,res1+1)
            if tmpval > target:
                    j -= 1
                  
            if tmpval < target:
                    i += 1
    
    # 79ms
    def twoSum(self, num, target):
        dic = {}
        for i in xrange(len(num)):
            if num[i] in dic:
                result1 = dic[num[i]] +1
                result2 = i +1
            else:
                dic[target-num[i]] = i
        
        return (result1,result2)
