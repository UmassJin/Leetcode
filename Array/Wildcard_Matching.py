Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false

# https://leetcode.com/discuss/30620/my-java-dp-solution

# Reference: http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html
# Notes:
# 1) Definiton of '?' and '*', '?' could match any single char, '*' match any sequqnce of chars 
# 2) Example isMatch("abebdcd","?b*cd") → True
#    a-->'?'; b-->b; '*'-->'ebd';'cd'-->'cd'
# 3) Example isMatch("abebdcbd","?b*cd") → False
#    a-->'?';b--:>b; 'ebd'-->'*';'c'-->'c';'b'-->'d' --> False
# 4) We need the variable 'ss', since for the example isMatch("hi","*?")
# 5) 'aacbb', '*b' --> True
#    'aacbcb', '*b'  --> True


class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        spointer = ppointer = ss = 0
        star = -1 
        len_s = len(s); len_p = len(p)
        while spointer < len_s:
            if ppointer < len_p and (s[spointer] == p[ppointer] or p[ppointer] == '?'):
                spointer += 1; ppointer += 1
            elif ppointer < len_p and p[ppointer] == '*':
                star = ppointer; ppointer += 1; ss = spointer
            elif star != -1:
                ppointer = star + 1; ss += 1; spointer = ss
            else:
                return False
        
        while ppointer < len_p and p[ppointer] == '*':
            ppointer += 1
        return ppointer == len_p   

# Reference: [Yu's Garden] http://www.cnblogs.com/yuzhangcmu/p/4116153.html
# [九章算法答案] http://www.jiuzhang.com/solutions/wildcard-matching/
# [Other good solution] http://blog.csdn.net/abcbc/article/details/8868711


# DP solution: 
# Status: dp[i][j]: the matching True/False for s[:i-1] and p[:j-1]
# Initialization:    dp[0][0] = True
#                    dp[0][j] = (p[j-1] == '*' and dp[0][j-1])
# Function: dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]     if p[j-1] != '?' and != '*'
#                      dp[i-1][j-1]                          if p[j-1] == '?'
#                      dp[i][j-1] || dp[i-1][j-1] || dp[i-2][j-1] || ... || dp[0][j-1] = dp[i][j-1] || dp[i-1][j] if p[j-1] == '*'
class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        lens = len(s)
        lenp = len(p)
        
        dp = [[False for i in xrange(lenp+1)] for j in xrange(lens+1)]
        dp[0][0] = True
        
        for i in xrange(1,lenp+1):
            dp[0][i] = (dp[0][i-1] and p[i-1] == '*')
        
        for i in xrange(1, lens+1):
            for j in xrange(1, lenp+1):
                if p[j-1] != '*' and p[j-1] != '?':
                    dp[i][j] = (dp[i-1][j-1] and (s[i-1] == p[j-1]))
                elif p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = (dp[i][j-1] or dp[i-1][j])
                    
        return dp[lens][lenp]
