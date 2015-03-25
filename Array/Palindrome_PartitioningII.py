Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

Reference:
https://leetcode.com/discuss/9476/solution-does-not-need-table-palindrome-right-uses-only-space
http://yucoding.blogspot.com/2013/08/leetcode-question-133-palindrome.html

class Solution:
    # @param s, a string
    # @return an integer
    # status: dp[i] how many palindrome in the string s[i:] with min cut, so the min cut is dp[i]-1
    # initialize: dp = [len(s),len(s)-1,...0] --> totaly len(s)+1
    # function: p[i][j] means s[i:j] (include i and j) whether is palindrome or not 
    #           dp[i] = min(dp[j+1]+1, dp[i])
    # result: dp[0]-1
    
    def minCut(self, s):
        p = [[False for i in xrange(len(s))] for j in xrange(len(s))]
        dp = [ 0 for i in (range(len(s)+1))]  # Note: here we need to assign the range(len(s))+!
        for i in range(len(s)+1):
            dp[i] = len(s)-i
        
        for i in range(len(s)-1,-1,-1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i<2 or p[i+1][j-1]):
                    p[i][j] = True
                    dp[i] = min(dp[j+1] + 1, dp[i])  # Note: here is dp[j+1]
        return dp[0]-1            
            
