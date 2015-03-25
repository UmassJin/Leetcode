Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].
Return true because "leetcode" can be segmented as "leet code".

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    # Note:
    # 1. dp[i] means from first i-1 chars can be break
    # 2. dp[0] = True
    # 3. dp[i] = for j in (i-1, ... 0) if dp[j] and s[j:i] in dict
    # 4. dp[N] !!! Very important here it's N not N-1
    def wordBreak(self, s, dict):
        length = len(s)
        dp = [False for i in xrange(length+1)]
        dp[0] = True
        
        for i in xrange(1,length+1):
            for j in xrange(i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
                    break
        return dp[length]
