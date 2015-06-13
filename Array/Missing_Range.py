'''
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} lower
    # @param {integer} upper
    # @return {string[]}
    def findMissingRanges(self, nums, lower, upper):
        nums.append(upper+1)
        nums.insert(0,lower-1)
        length = len(nums)
        result = []
        for i in xrange(1, length):
            if nums[i] - nums[i-1] > 1:
                self.make_result(result, nums[i-1]+1, nums[i]-1)  
        
        return result 
    
    def make_result(self, result, start, end):
        if start == end:
            result.append(str(start))
        else:
            string = str(start) + "->" + str(end)
            result.append(string)
            
