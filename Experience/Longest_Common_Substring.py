"""
1. Subset(second le)
2. LCS
Given two strings 'X' and 'Y', find the length of the longest common substring.
For example, if the given strings are "GeeksforGeeks" and "GeeksQuiz",
the output should be 5 as longest common substring is "Geeks"
[Solution](http://www.geeksforgeeks.org/longest-common-substring/)
DP is O(n^2)
[Naive](http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/) way would be O(n * m^2), similar to KMP way
Which is for each word, we start search
str1 == substring of str2
Substring of str2 O(m^2)
search str1 O(n)
So O(n * m^2)
1. dp[i][j] is LCS of first i-1 chars in a ends with char i-1 and first j-1 chars in b ends with char j-1
2. init dp[i][j] = 0
3. dp[i][j] = dp[i-1][j-1] + 1 # if a[i] == b[j]
              0                # if a[i] != b[j]
4. max(dp[0...M][0...N])
"""
