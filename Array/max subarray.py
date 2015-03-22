Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 0:
            return None
        if len(A) ==1:
            return A[0]

        psum = A[0]
        max_value = A[0]

        for i in range(1, len(A)):
            psum = psum + A[i]
            if A[i]> psum:
                psum = A[i]
            if A[i] > max_value:
                max_value = A[i]
            if psum > max_value:
                max_value = psum
            
        return max_value 
    
    def maxSubArray(self, A):
        current = 0
        result = A[0]
        for i in A:
            current += i
            result = max(current,result)
            current = max(0,current)
        return result

