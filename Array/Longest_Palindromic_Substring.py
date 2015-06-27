Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

# Solution 1. DP solution (TLE)
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        N = len(s)
        dp = [ [ False for j in range(N)] for i in range(N) ]
        for i in range(N):
            dp[i][i] = True

        for i in range(N-1):
            dp[i][i+1] = s[i] == s[i+1]

        length = 2
        max_length = 1

        while length < N:
            start = 0
            while start + length < N:
                if dp[start+1][start+length-1] and s[start] == s[start+length]:
                    dp[start][start+length] = True
                    max_length = max(max_length, length+1)
                start += 1
            length += 1
        return max_length

    # Notice
    # 1. dp[i][j] means if s[i:j] is a palindrome
    # 2. dp[i][i] = True
    #    dp[i][i+1] = True if s[i] == s[i+1]
    # 3. dp[start][start+length] = True if s[start] == s[star+length] and dp[start+1][start+length-1]
    # 4. Update length
    # This dp way is O(n^2) will get TLE
    
# Solution 2, Good!!
# Explaination: https://leetcode.com/discuss/21332/python-o-n-2-method-with-some-optimization-88ms

    def longestPalindrome(self, s):
        if len(s)==0:
            return 0
        maxLen=1
        start=0
        for i in xrange(len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1 # 注意这个start的更新，必须在maxlen前面！
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen] 

# https://leetcode.com/discuss/32204/simple-c-solution-8ms-13-lines
