Given two words word1 and word2, find the minimum number of steps 
required to convert word1 to word2. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:
a) Insert a character
b) Delete a character
c) Replace a character

class Solution:
    # @return an integer
    # Note:
    # State: dp[i][j] is Edit Distance of first i-1 chars in word1 with first j-1 chars in word2
    # Initialize: dp[0][j] = j, dp[i][0] = i
    # Function: dp[i][j] = dp[i-1][j-1]                                   # if word[i-1] == word[j-1]
    #             = min( dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1 # if word[i-1] != word[j-1]
    # Result: dp[M][N]
    def minDistance(self, word1, word2):
        length1 = len(word1)
        length2 = len(word2)
        
        dp = [ [0 for j in xrange(length2+1)] for i in xrange(length1+1)]
        
        for i in xrange(length1+1):
            for j in xrange(length2+1):
                if i == 0:
                    dp[0][j] = j
                elif j == 0:
                    dp[i][0] = i
                elif word1[i-1] == word2[j-1]: # 判断 i-1 和 j-1 !! 不是 i 和 j
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        return dp[length1][length2]
             
