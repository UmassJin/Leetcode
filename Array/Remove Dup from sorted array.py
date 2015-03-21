I) 
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
Analysis: use two pointer 

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        if length == 0: return 0
        if length == 1: return 1
        
        slow = 0
        for fast in xrange(length):
            if A[slow]==A[fast]:
                continue
            else:
                slow += 1
                A[slow]=A[fast]
        return slow+1
        
II)
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?
For example,
Given sorted array A = [1,1,1,2,2,3],
Your function should return length = 5, and A is now [1,1,2,2,3].
