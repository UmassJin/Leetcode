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


class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """
    def fourSum(self ,numbers, target):
        if not numbers or len(numbers) < 4: return []
        n = len(numbers)
        numbers.sort()
        result = set()
        
        for i in xrange(n-3):
            if i == 0 or numbers[i] > numbers[i-1]:
                for j in xrange(i+1, n-2):
                    if j == i+1 or numbers[j] > numbers[j-1]:
                        left = j + 1; right = n-1
                        while left < right:
                            tmp = numbers[i] + numbers[j] + numbers[left] + numbers[right]
                            if tmp == target:
                                result.add((numbers[i], numbers[j], numbers[left], numbers[right]))
                                while left < right:
                                    left += 1
                                    if numbers[left] > numbers[left-1]:
                                        break
                                while left < right:
                                    right -=1
                                    if numbers[right] < numbers[right+1]:
                                        break
                                
                            elif tmp < target:
                                 while left < right:
                                    left += 1
                                    if numbers[left] > numbers[left-1]:
                                        break
                            elif tmp > target:
                                  while left < right:
                                    right -=1
                                    if numbers[right] < numbers[right+1]:
                                        break
                                
         
        return [list(i) for i in result]                       
