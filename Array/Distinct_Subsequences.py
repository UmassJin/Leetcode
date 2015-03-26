Given a string S and a string T, count the number of distinct subsequences of T in S.
A subsequence of a string is a new string which is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
Here is an example:
S = "rabbbit", T = "rabbit"
Return 3.

Reference:
https://leetcode.com/discuss/19735/a-dp-solution-with-clarification-and-explanation
https://github.com/cyandterry/Python-Study/blob/master/Leetcode/Distinct_Subsequences.py
https://missaleetcodenotes.wordpress.com/2015/03/12/leetcode-distinct-subsequences/

Analysis:
S: lengths, j; T: lengtht, i 
status: dp[i][j] means the numbers of first i-1 chars in T is matched first j-1 chars in S 
initialize: dp[i][0] = 0; dp[0][j] = 1
function:     # dp[i][j] = dp[i][j-1] + dp[i-1][j-1] # if T[i-1] == S[j-1]
              #          = dp[i][j-1]                # if T[i-1] != S[j-1]

1) if S[j-1] != T[i-1], dp[i][j] = dp[i][j-1], which means must delete the (j-1)th 
chars in S, so the subsequence can equal to T, the result is the same with T[0...i-1] to S[0...j-2]
2) if S[j-1] == T[i-1], there are two options, if we use the char S[j-1] to match to T[i-1], then 
the number of distinct subsequence of T[0,...i-1] in S[0...j-1] is the same as the result for 
T[0...i-2] in S[0...j-2]. Or if we not use this match, which means delete the char in S, thus result
is the same as the result for T[0,...i-1] in S[0...j-2]

result: dp[lengtht][lengths]

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        lengths = len(S)
        lengtht = len(T)
        
        dp = [ [0 for j in xrange(lengths+1)] for i in xrange(lengtht+1)]
        
        for i in xrange(lengtht+1):
            for j in xrange(lengths+1):
                if i == 0:
                    dp[0][j] = 1
                elif j == 0:
                    dp[i][0] = 0
                elif S[j-1] == T[i-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[lengtht][lengths]
        
    # 大概意思就是， 因为算的是S的子串和T匹配的方法， 所以一旦S[:j-1]和T[:i]有x种匹配方法时
    # S[:j]必定也至少和T[:i]有x种匹配方法，但尤其当S[j-1]==T[i-1]的时候，需要再加上S[:j-1]和T[:i-1]的匹配方法数
    #     r a b b b i t
    #   1 1 1 1 1 1 1 1
    # r 0 1 1 1 1 1 1 1
    # a 0 0 1 1 1 1 1 1
    # b 0 0 0 1 2 3 3 3
    # b 0 0 0 0 1 3 3 3
    # i 0 0 0 0 0 0 3 3
    # t 0 0 0 0 0 0 0 3
