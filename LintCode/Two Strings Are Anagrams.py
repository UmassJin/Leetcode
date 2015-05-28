'''
Easy Two Strings Are Anagrams

31% Accepted
Write a method anagram(s,t) to decide if two strings are anagrams or not.

Have you met this question in a real interview? Yes
Example
Given s="abcd", t="dcab", return true.

Challenge
O(n) time, O(1) extra space
'''

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        m = len(s); n = len(t)
        if m != n: return False
        
        m1 = ''.join(sorted(s))
        n1 = ''.join(sorted(t))
        
        return m1 == n1
