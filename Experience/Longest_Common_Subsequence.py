"""
Need to distinguish from Longest Common Substring
Examples:
LCS for input Sequences "ABCDGH" and "AEDFHR" is "ADH" of length 3.
LCS for input Sequences "AGGTAB" and "GXTXAYB" is "GTAB" of length 4.
[Solution](http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/)
DP way is O(m*n)
Normal way O(m^2 *n)
1. dp[i][j] is LCS for first i chars of a and first j chars of b
2. dp[i][j] = 0
3. dp[i][j] = dp[i-1][j-1] + 1             # if a[i] == b[j]
            = max(dp[i-1][j], dp[i][j-1])  # if a[i] != b[j]
4. dp[M][N]
Keep reading for [print LCS](http://www.geeksforgeeks.org/printing-longest-common-subsequence/)
"""
def Longest_Common_Subsequence(a,b):
    lengtha = len(a)
    lengthb = len(b)

    dp = [ [0 for j in xrange(lengthb+1)] for i in xrange(lengtha+1)]

    for i in xrange(1,lengtha+1):
        for j in xrange(1, lengthb+1):
            if a[i-1] != b[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = dp[i-1][j-1] + 1

    return dp[lengtha][lengthb]

print Longest_Common_Subsequence('ABCDGH', 'AEDFHR')
print Longest_Common_Subsequence('AGGTAB', 'GXTXAYB')
print Longest_Common_Subsequence('B', 'B')
print '-'*10

def LCS_recur(a,b):
    if not a or not b: return 0
    if a[-1] == b[-1]:
        return 1 + LCS_recur(a[:-1],b[:-1])
    else:
        return max(LCS_recur(a[:-1], b), LCS_recur(a, b[:-1]))

print LCS_recur('ABCDGH', 'AEDFHR')
print LCS_recur('AGGTAB', 'GXTXAYB')
print LCS_recur('B', 'B')
print '-'*10
    
print "Print the Longest Common Subsequence"
def LCS(a,b):
    lengtha = len(a)
    lengthb = len(b) 
    
    dp = [ [0 for j in xrange(lengthb+1)] for i in xrange(lengtha+1)]

    for i in xrange(1,lengtha+1):
        for j in xrange(1, lengthb+1):
            if a[i-1] != b[j-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:
                 dp[i][j] = dp[i-1][j-1] + 1

    result = []
    while i >0 and j>0:
        if a[i-1] == b[j-1]:
            result.insert(0,a[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(result)

print LCS('ABCDGH', 'AEDFHR')
print LCS('AGGTAB', 'GXTXAYB')

