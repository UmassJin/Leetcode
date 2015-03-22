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

Maximum Product Array 
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

class Solution:
    # @param A, a list of integers
    # @return an integer
    #Analysis: save the min value and the max value at the same time
Method 1:
    def maxProduct(self, A):
        mintmp = maxtmp = result = A[0]
        for i in xrange(1,len(A)):
            tmplist = [mintmp*A[i], maxtmp*A[i], A[i]]
            mintmp, maxtmp = min(tmplist), max(tmplist)
            result = max(maxtmp,result)
        return result
        

Method 2:
Fist we assume there is no zero in the A[]. The answer must be 
A[0] A[1] .... A[i] OR A[j] *A[j+1] A[n - 1]. (Try to prove yourself)
Then when we have zero in the A[] (assum A[k] == 0). We could see 
A[0],A[1]...A[k - 1 ] As An Array and A[k + 1] A[k + 2]...A[n-1] is another.
    def maxProduct(self, A):
        front = 1; end = 1; result = -99999
        for i in xrange(len(A)):
            front *= A[i]
            end *= A[len(A)-1-i]
            result = max(result,front,end)
            if front == 0: front = 1
            if end == 0: end = 1
        return result
