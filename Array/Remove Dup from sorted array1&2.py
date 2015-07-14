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
Analysis: Use a flag to indicate the count 

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) < 3: return
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        return self.removeDupk(A,2)
        
    def removeDupk(self,A, k): 
        length = len(A)
        if length <= k: return length
        
        slow = 0; count = 1
        for fast in xrange(1,length):
            if A[fast] == A[fast-1]:
                if count < k:
                    slow +=1
                    A[slow] = A[fast]
                    count += 1
            else:
                slow += 1
                A[slow] = A[fast]
                count = 1
        return slow+1
