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

# DP solution
# https://leetcode.com/discuss/26399/python-dp-solution


# https://leetcode.com/discuss/26399/python-dp-solution
public boolean isMatch(String s, String p) {
    int count = 0;
    for (char c : p.toCharArray()) {
        if (c == '*')
            count++;
    }
    if (p.length() - count > s.length())
        return false;
    boolean[][] dp = new boolean[p.length() + 1][s.length() + 1];
    dp[0][0] = true;
    for (int j = 1; j <= p.length(); j++) {
        char pattern = p.charAt(j - 1);
        dp[j][0] = dp[j - 1][0] && pattern == '*';
        for (int i = 1; i <= s.length(); i++) {
            char letter = s.charAt(i - 1);
            if (pattern != '*') {
                dp[j][i] = dp[j - 1][i - 1] && (pattern == '?' || pattern == letter);
            } else
                dp[j][i] = dp[j][i - 1] || dp[j - 1][i];
        }
    }
    return dp[p.length()][s.length()];
    
class Solution:
# @return a boolean
def isMatch(self, s, p):
    length = len(s)
    if len(p) - p.count('*') > length:
        return False
    dp = [True] + [False]*length
    for i in p:
        if i != '*':
            for n in reversed(range(length)):
                dp[n+1] = dp[n] and (i == s[n] or i == '?')
        else:
            for n in range(1, length+1):
                dp[n] = dp[n-1] or dp[n]
        dp[0] = dp[0] and i == '*'
    return dp[-1]
