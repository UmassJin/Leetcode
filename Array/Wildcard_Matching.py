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
