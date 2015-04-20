#Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
# Find all unique quadruplets in the array which gives the sum of target.
#Note:
#Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
#The solution set must not contain duplicate quadruplets.

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        numlength = len(num)
        result = set()
        if numlength < 4: return []
        num.sort()
        dict = {}
        
        for i in xrange(numlength-1):
            j = i+1
            while j < numlength:
                if num[i]+num[j] not in dict:
                    dict[num[i]+num[j]] = [(i,j)]
                else:dict[num[i]+num[j]].append((i,j))
                j += 1
            i+=1
        for p in xrange(numlength-2):
            for q in xrange(p+1,numlength):
                tmpsum = target-num[p]-num[q]
                if tmpsum in dict:
                    for queue in dict[tmpsum]:
                        if q < queue[0]: result.add((num[p],num[q],num[queue[0]],num[queue[1]]))
                        # Note: here we need to check the q < queue[0] !!! 
        
        return [list(i) for i in result]

#if q < queue[0]: result.add((num[p],num[q],num[queue[0]],num[queue[1]]))
# Corner case: we add q < queue[0] !!
#Input:	[2,1,0,-1], 2
#Output:	[[-1,2,0,1],[-1,2,-1,2],[-1,1,0,2],[0,2,-1,1],[-1,0,1,2],[0,1,0,1],[0,1,-1,2]]
#Expected:	[[-1,0,1,2]]
