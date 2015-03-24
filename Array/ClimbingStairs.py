You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n<= 1: return n
        result = [0 for j in xrange(n+1)]
        result[0]=0;result[1]=1;result[2]=2
        for i in xrange(3,n+1):
            result[i] = result[i-1] + result[i-2]
        return result[n]
        
    # Note:
    # 1. dp[i] means from 0 to i-1 stair, how many ways to go
    # 2. dp[0] = 1, dp[1] = 2
    # 3. dp[i] = d[i-1] + dp[i-2]
    # 4. dp[N-1]
    def climbStairs(self, n):
        if n <= 1: return n
        dp = [0 for i in xrange(n)]
        dp[0] = 1; dp[1] = 2
        for i in xrange(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
        
    def climbStairs(self, n):
        if n <= 2: return n
        fn1 = 1; fn2 = 2
        fn = 0
        for i in xrange(3,n+1):
            fn = fn1 + fn2
            fn1 = fn2
            fn2 = fn 
        return fn
