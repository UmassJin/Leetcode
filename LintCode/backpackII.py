'''
Given n items with size Ai and value Vi, and a backpack with size m. What's the maximum value can you put into the backpack?

Have you met this question in a real interview? Yes
Example
Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 9.

Note
You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.

Challenge
O(n x m) memory is acceptable, can you do it in O(m) memory?
'''

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        if m == 0 or not A or not V: return 0
        n = len(A)
        dp = [[0 for i in xrange(m+1)] for j in xrange(n+1)]
        
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                if j >= A[i-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]] + V[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
            
        return dp[n][m]
        

# Solution 2: use only one array, here we need to iterate from end to the beginning 
# otherwise the value will be modified 

    def backPackII(self, m, A, V):
        if m == 0 or not A or not V: return 0
        n = len(A)
        dp = [0 for i in xrange(m+1)]

        for i in xrange(1, n+1):
            for j in xrange(m, 0, -1):
                if j >= A[i-1]:
                    dp[j] = max(dp[j], dp[j-A[i-1]] + V[i-1])
        return dp[m]
