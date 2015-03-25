Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.

class Solution:
    # @param A, a list of integers
    # @return a boolean
    
    # Note:
    # 1. dp[i] means whether we can jump to i
    # 2. dp[0] = True
    # 3. dp[i] = True if from i-1 ... 0 if we can jump to i
    # 4. dp[N-1]
    # TLE, this is the O(n^2) solution
    def canJump_1(self, A):
        result = [False for x in range(len(A))]
        for i in range(len(A)-1):
            number = A[i]
            for j in range(i,len(A)):    
                if number >= 0:
                    result[j] = True
                    number -= 1
        return result[len(A)-1]
    
    # Note: the step mean for the previous step,
    # What's the max step, and compre with the
    # recent one 
    def canJump_2(self, A):
        step = A[0]
        for i in range(1, len(A)):
            if step > 0:
                step -= 1
                step = max(step, A[i])
            else:
                return False
        return True   

    # Note:
    # 1. dp[i] means at i, we can jump to where
    # 2. dp[0] = A[0]
    # 3. dp[i] = max(A[i-1]-1, dp[i-1]-1), if dp[i] < 0: then return False
    # return True if we can finish the loop
    def canJump_3(self, A):
        dp = [0 for i in len(A)]
        dp[0] = A[0]
        for i in range(1,len(A)):
            dp[i] = max(dp[i-1]-1, A[i-1]-1)
            if dp[i] < 0:
                return False
        return True 
        
        # Constant DP
    def canJump_4(self, A):
        pre_max = A[0]
        for i in range(1, len(A)):
            max_jump = max(pre_max-1, A[i-1]-1)
            if max_jump < 0:            # Note this is < 0 but not <= 0
                return False
            pre_max = max_jump
        return True
