Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        start = 0; end = len(A)-1
        if len(A) == 0: return None
        
        while start< len(A) and end >= 0 and start <= end:
            mid = (start+end)/2
            if A[mid] == target: return mid
            elif A[mid] > target: 
                    end = mid -1
            elif A[mid] < target:
                    start = mid + 1
        return start

# Note: the while loop condition !
# Last the return value is start !
