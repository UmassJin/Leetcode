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

# Method 2 in the LintCode, note the optimization ! 
    def wordSegmentation(self, s, dict):
        if not s: return True
        n = len(s)
        dp = [False for i in xrange(n+1)]
        dp[0] = True
        
        count = [0 for i in xrange(26)]
        
        for word in dict:
            for char in word:
                count[ord(char)-ord('a')] += 1
        
        for char in s:
            if count[ord(char) - ord('a')] == 0:
                return False
        
        for i in xrange(1,n+1):
            for j in xrange(i-1,-1,-1): # Here we could iterate from the i-1 to 0
                if s[j:i] in dict and dp[j]:  
                    dp[i] = True
                    break
                    
        return dp[n]
