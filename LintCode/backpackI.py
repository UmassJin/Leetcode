'''
Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

Have you met this question in a real interview? Yes
Example
If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can select [2, 3, 5], so that the max size we can fill this backpack is 10. If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.

You function should return the max size we can fill in the given backpack.

Note
You can not divide any item into small pieces.

Challenge
O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.

'''

class Solution_MLE:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        if not A: return 0
        n = len(A)
        dp = [[0 for i in xrange(m+1)] for j in xrange(n+1)]
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                if j < A[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]] + A[i-1])
        return dp[n][m]


class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        if not A: return 0
        n = len(A)
        dp = [0 for i in xrange(m+1)]
        for i in xrange(1, n+1):
            for j in xrange(m, 0, -1):
                if j >= A[i-1]:
                    dp[j] = max(dp[j], dp[j-A[i-1]] + A[i-1])
        return dp[m]

# dp[i][j] means we put the first i items for backpack j   
# function: if j >= A[i-1], dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]] + A[i-1]), put the ith item or not 
# result: dp[n][m]
        
