#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

#Note:
#Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
#The solution set must not contain duplicate triplets.
#198ms

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        result = []
        if len(num) == 0:
            return []
        if len(num) == 1 and num[0] != 0:
            return []
        
        for i in xrange(len(num)):
            j = i + 1
            k = len(num) - 1
            
            if i==0 or num[i] > num[i-1]:  # optimization 
              while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == 0:
                    if (numbers[i], numbers[j], numbers[k]) not in result:
                        result.append((numbers[i], numbers[j], numbers[k]))   # 注意duplicate result 
                    j = j + 1
                    k = k - 1
                    while (j<k and (num[j] == num[j-1])): j +=1 # add the check and reduce the running time 
                    while (j<k and (num[k] == num[k+1])): k -=1
                    
                elif sum < 0:
                    while j<k:
                        j = j +1
                        if num[j] > num[j-1]: break  # optimization 
                else:
                    while j<k:
                        k = k-1
                        if num[k] < num[k+1]: break
        
        return result   
