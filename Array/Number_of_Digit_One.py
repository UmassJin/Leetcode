'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''
# https://leetcode.com/discuss/44281/4-lines-o-log-n-c-java-python
# CTCI, Hard 18.4

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        ones = 0; m = 1
        while m <= n:
            a = n/m; b = n%m
            ones += (a + 8)/10 * m + (a % 10 == 1) * (b + 1)
            m *= 10
        return ones    
    
    def countDigitOne_1(self, n):
        if n == 0: return 0
        s = str(n); count = 0
        for digit in xrange(len(s)):
            count += self.count_helper(n, digit)
        return count
        
    def count_helper(self, n, d):
        powerof10 = 10**d
        nextpowerof10 = powerof10 * 10
        right = n % powerof10
        
        rounddown = n - n % nextpowerof10
        roundup = rounddown + nextpowerof10 
        
        digit = (n/powerof10)%10
        
        if digit < 1:
            return rounddown / 10
        elif digit == 1:
            return rounddown / 10 + right + 1
        else:
            return roundup / 10
