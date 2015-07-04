Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

#Reference:
#https://leetcode.com/discuss/9476/solution-does-not-need-table-palindrome-right-uses-only-space
#http://yucoding.blogspot.com/2013/08/leetcode-question-133-palindrome.html
#http://chaoren.is-programmer.com/posts/43805

class Solution:
    # @param s, a string
    # @return an integer
    # status: dp[i] how many palindrome in the string s[i:] with min cut, so the min cut is dp[i]-1
    # initialize: dp = [len(s),len(s)-1,...0] --> totaly len(s)+1
    # function: p[i][j] means s[i:j] (include i and j) whether is palindrome or not 
    #           dp[i] = min(dp[j+1]+1, dp[i]), 
    #           since s[i:j] is palindrome, so dp[i] = dp[j+1] + 1, # of palindrome in s[j+1:] add 1
    # result: dp[0]-1
    
    
    def minCut(self, s):
        if not s: return 0
        n = len(s)
        dp = [ n-i for i in xrange(n+1)]  # Note: here we need to assign the range(len(s))+1
        ispal = [[False for i in xrange(n)] for j in xrange(n)]
        
        for i in xrange(n-1, -1, -1):
            for j in xrange(i, n):
                if s[i] == s[j] and ((j-i<2) or ispal[i+1][j-1]):
                    ispal[i][j] = True
                    dp[i] = min(dp[j+1] + 1, dp[i])  # Note: here is dp[j+1]
        return dp[0] - 1

    # Method 2 
    def minCut(self,s):
        length = len(s)
        isPal = [[False for i in xrange(len(s))] for j in xrange(len(s))]
        dp = [ i + 1 for i in xrange(length)]
        for j in xrange(length):
            for i in reversed(xrange(j+1)):
                if s[i] == s[j] and (j-i<2 or isPal[i+1][j-1]):
                    isPal[i][j] = True
                    dp[j] = min(dp[j], dp[i - 1] + 1) if i > 0 else min(dp[j], 1) # i == 0
        return dp[length - 1] - 1
