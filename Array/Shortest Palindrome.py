'''
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases. Thanks to @Freezen for additional test cases.
'''

class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        if not s: return s
        new_s = s + '#' + s[::-1]
        n = len(new_s)
        arr = [0 for i in xrange(n)]
        
        for i in xrange(1, n):
            index = arr[i-1]
            while index > 0 and new_s[index] != new_s[i]:
                index = arr[index-1]
            arr[i] = index + (1 if new_s[index] == new_s[i] else 0)
        
        return s[arr[n-1]:][::-1] + s 
