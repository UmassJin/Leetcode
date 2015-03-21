Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
You may assume no duplicate exists in the array.

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        length = len(num)  
        if length == 0: return None
        
        left = 0; right = length -1
        minvalue = num[0]
        while left <= right:
            mid = (left+right)/2
            if num[mid] < num[right]:
                right = mid-1
            else:
                left = mid+1
            minvalue = min(minvalue,num[mid])
        return minvalue
