Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

Better Solution:
https://leetcode.com/discuss/19973/8ms-c-solution-using-bfs-with-explanation

    # Note:
    # 1. dp[i][j] means whether s1[:i] and s2[:j] is interleave with s3[:i+j]
    # 2. dp[0...M][0...N] = False
    # 3. dp[i][j] = True   # if dp[i-1][j] == True and s1[i-1] == s3[i-1+j] or
    #                           dp[i][j-1] == True and s2[j-1] == s3[i+j-1]
    #             = False  # else
    # 4. dp[M][N]


class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        length1 = len(s1)
        length2 = len(s2)
        length3 = len(s3)
        if length1 + length2 != length3: return False
        
        dp = [[False for j in xrange(length2+1)]for i in xrange(length1+1)]

        for i in xrange(length1+1):
            for j in xrange(length2+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i>0 and dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
                elif j>0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[length1][length2]
