Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        lengthp = len(p)
        lengths = len(s)
        dp = [[ False for i in xrange(lengthp+1)] for j in xrange(lengths+1)]     
        dp[0][0] = True
        
        for i in xrange(lengths+1):
            for j in xrange(1, lengthp+1):
                if p[j-1] != '.' and p[j-1] != '*':
                    if i > 0:
                        dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
                
                elif p[j-1] == '.':
                    if i > 0:
                        dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i][j-2]
                    if i > 0:
                        dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
        return dp[lengths][lengthp]

'''    
* state: ```dp[i][j]``` 表示```s[0:i-1]```是否能和 ```p[0:j-1]```匹配
* initialize:  ``` dp[0][0] = True ```
* function: 
dp[i][j] =  dp[i-1][j-1] and s[i-1][j-1]  if p[j-1] != '.' and p[j-1] != '*'
            dp[i-1][j-1]                  if p[j-1] == '.'
            dp[i][j-1]  or dp[i][j-2]     if p[j-1] == '*' 匹配0个或者1个元素 
            匹配0个元素，即消去p[j-2]，此时p[0: j-1] = p[0: j-3]
            匹配1个元素，此时p[0: j-1] = p[0: j-2]
            dp[i-1][j] and (s[i-1] = p [j-2] or p[j-2] == '.')
* answer: ```dp[M][N]```
* Reference: [Leetcode artical](http://articles.leetcode.com/2011/09/regular-expression-matching.html)
*            [Good Analysis] (http://bangbingsyb.blogspot.com/2014/11/leetcode-regular-expression-matching.html)
             [Recursion Answer](http://blog.csdn.net/fightforyourdream/article/details/17717873)
             [Yu's Garden](http://www.cnblogs.com/yuzhangcmu/p/4105529.html)

'''
