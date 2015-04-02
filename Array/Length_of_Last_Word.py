Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord_1(self, s):
        return len(s.strip(' ').split(' ')[-1])
        
    def lengthOfLastWord(self,s):
        res = 0
        n = len(s)-1
        while n >= 0:
            if s[n] != ' ':
                res += 1
            elif res > 0:
                break
            n -= 1
        return res
