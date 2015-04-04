'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
'''

class Solution:
    # @return an integer
    # Recursion (172ms)
    def numTrees_1(self, n):
        if n <= 1: return 1
        result = 0
        for i in xrange(1,n+1):
            result += self.numTrees(i-1)*self.numTrees(n-i)
        return result 
    
    # DP (46ms)    
    def numTrees(self, n):
        result = [0 for i in xrange(n+1)]
        result[0] = 1; result[1] = 1
        
        for i in xrange(2, n+1):
            for j in xrange(1, n+1):
                result[i] += result[j-1]*result[i-j]
        return result[n]

# status: result[i]: the number of unique BST for a sequence of length i.
# initialize: result[0]= 1; result[1] = 1, only one combination to construct a BST out of a sequence 
# function: 
result[n] = F(1,n) + F[2,n] +...F[n,n] 
F[i, n]: the number of unique BST, where the number i is the root of BST, and the sequence ranges from 1 to n.
F[i, n] = result[i-1] * result[n-i]  1<= i <= n
result[n] = result[0]*result[n-1] + result[1]*result[n-2]+..+result[n-1]*result[0]
# result: result[n]

# Reference: https://leetcode.com/discuss/24282/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i
