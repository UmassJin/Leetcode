'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
'''

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords_1(self, s):
        return ' '.join(s.split()[::-1])
    
    def reverseWords(self, s):
        result = ''
        word = ''
        for char in s:
            if char !=' ':
                word += char
            elif len(word) > 0:
                if result == '':
                    result = word + result
                else:
                    result = word + ' '+ result
                word = '' # Note: word need to clean to '' here
                
        if len(word) > 0:  # We need the other check here for the scenario "a" ---> 'a'
            if result != '':
                result = ' ' + result 
            result = word + result  
        return result 
