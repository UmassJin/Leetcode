#Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
#Return the sum of the three integers. You may assume that each input would have exactly one solution.

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        res = num[0]+num[1]+num[2]
        if res == target: return res
        
        for i in xrange(len(num)):
            j = i+1
            k = len(num)-1
            
            while j < k:
                tmp = num[i]+num[j]+num[k]
                if tmp == target:
                    return tmp 
                
                tmpres = abs(target-tmp)
                if tmpres < abs(target-res):
                    res = tmp
                
                if tmp > target:
                    while j < k:
                        k -= 1
                        if num[k] != num[k+1]: break
                if tmp < target:
                    while j < k:
                        j += 1
                        if num[j] != num[j-1]: break
        return res
