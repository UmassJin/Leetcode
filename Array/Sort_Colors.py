Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if A == []: return 
        start = 0; i = 0; end = len(A)-1
        
        while i <= end:  # Note: here is i<= end
            if A[i] == 0:
                A[i], A[start] = A[start], A[i]
                i += 1
                start += 1
                
            elif A[i] == 2:
                A[i], A[end] = A[end], A[i]
                end -= 1
                
            else:
                i += 1
