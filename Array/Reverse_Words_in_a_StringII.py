Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array

class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords_1(self, s):
        # Not sure the issue here 
        # start = -1

        # for i in xrange(len(s)):
        #     if s[i] == ' ':
        #         s[start+1:i] = s[start+1:i][::-1]
        #         start = i
        # s = s[::-1]

    def reverseWords(self, s):
        index = [i for i, x in enumerate(s) if x == ' ']
        for x, y in zip([-1] + index + [-1], index + [len(s)] * 2):
            s[x+1:y] = s[x+1:y][::-1]
            
# Note: 
# 1) enumerate usage
# 2) zip usage 
# 3) reverse the whole string and then reverse each word 
