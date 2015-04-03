Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if len(A) == 0:
            return 0
            
        slow = -1
        for fast in xrange(len(A)):
            if A[fast] == elem:
                continue 
            else:
                slow += 1
                A[slow] = A[fast]
    
        return slow+1  
