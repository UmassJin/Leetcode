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

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array may contain duplicates.

My resolution :)

    def findMin(self, num):
        left, right = 0, len(num)-1
        minvalue = num[0]
        
        while left <= right:
            mid = (left+right)/2
            if num[mid] > num[left]:
                    minvalue = min(num[left],minvalue)
                    left = mid + 1
            elif num[mid] < num[left]: 
                    minvalue = min(num[mid], minvalue)
                    right = mid -1
            else:
                left +=1
            minvalue = min(minvalue, num[mid])  # Note: This is important !!! # need to check in every loop !
        return minvalue

# test case: [3,1]
# test case: [1,1,2,0,0,1]

Method 1
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        right = len(num) -1 
        left = 0
        result = num[0]
        
        while left < right-1:
            mid = (left+right)/2
            
            if num[left] < num[mid]:
                result = min(num[left], result)
                left = mid + 1
                
            elif num[mid] < num[left]:
                result = min(num[mid], result)
                right = mid - 1
            
            else:
                left += 1
        
        return min(result, num[left], num[right])     
    
    Method 2
    def findMin(self,num):
        L = 0; R = len(num)-1
        while L < R and num[L] >= num[R]:
            mid = (L+R)/2
            if num[L]< num[mid]:
                L = mid+1
            elif num[L]> num[mid]:
                R = mid
            else:
                L = L +1
        return num[L]   
