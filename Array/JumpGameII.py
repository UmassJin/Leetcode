Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

class Solution:
    # @param A, a list of integers
    # @return an integer
    # Reference: Analysis http://tech-wonderland.net/blog/leetcode-jump-game-ii.html
    # DP, TLE by OJ, O(N^2)
    # state: dp[i]denote the minimum number of jumps 
    # function: dp[i] = min(dp[i],dp[j]+1)
    # initialize: dp[0] = 0
    # answer: dp[len(A)-1]
    # assume the input array is [2,3,1,1,4], i=2，A[i]= 1,go through j=0,1, which less than 2,
    # if A[j]+j > i: which means from j could jump to i, dp[j]+1, also compare with dp[i]
    
    def jump_1(self, A):
        length = len(A)
        if length <= 1: return 0
        dp = [length for i in xrange(length)]
        dp[0] = 0
        for i in xrange(len(A)):
            for j in xrange(i):
                if A[j] + j >= i:   # Note: here should be >= 
                    dp[i] = min(dp[i],dp[j]+1)
        return dp[length-1]
        
    # Greedy:
    # still, keep the current maximum reach distance, and the number of steps to reach this current 
    # maximum distances, and keep another variable to record the next maximum reachable distance, 
    # which cost the current steps plus 1. The key idea behind is that, all the positions before the 
    # maximum reachable distance would be able to be reached! Then we linear scan the array to keep 
    # updating the current maximum and the next maximum as well as the number of steps. We can achieve 
    # the linear time algorithm.
    
    def jump(self, A):
        length = len(A)
        if length <= 1: return 0
        maxReachableDis = 0
        maxNextAval = 0
        minstep = 0
        
        for i in xrange(length):
            if i > maxReachableDis:
                if maxNextAval > maxReachableDis:
                    maxReachableDis = maxNextAval 
                    minstep += 1
            maxNextAval = max(maxNextAval, A[i]+i)
        return minstep 
