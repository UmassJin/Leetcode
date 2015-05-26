'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        if not s: return 0
        result = 0
        for char in s:
            result *= 26
            result += ord(char)-64
        return result 

# 注意get nunber of the 'A' using ord(char)-64
