Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        tmp_start = -1
        tmp_end = -1
        left = 0
        right = len(A)-1

        while left <= right:
            mid = (left + right)/2
            if A[mid] == target:
                #if start == -1 or mid < start:
                #    start = mid
                #elif end == -1 or mid > end:
                #    end = mid 
                tmp_start = mid
                while tmp_start-1 >= 0 and A[tmp_start-1] == target:
                    tmp_start -= 1
                tmp_end = mid
                while tmp_end+1 <= len(A)-1 and A[tmp_end +1] == target:
                    tmp_end += 1
                return [tmp_start, tmp_end]    
                
            elif A[mid] < target:
                left = mid +1
            elif A[mid] > target:
                right = mid -1
        
        return [tmp_start, tmp_end]        
        
               
                
