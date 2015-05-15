'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n == 0: return 0
        if n == 1: return 1 
        
        slow = 0
        for fast in xrange(n):
            if A[slow] == A[fast]:
                continue
            else:
                slow += 1
                A[slow] = A[fast]
        return slow + 1
