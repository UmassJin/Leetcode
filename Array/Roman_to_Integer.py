Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @return an integer
    def romanToInt(self, s):
        numerals = { "M": 1000, 
                     "D": 500, 
                     "C": 100, 
                     "L": 50, 
                     "X": 10, 
                     "V": 5, 
                     "I": 1 }
        result = 0
        pre = s[0]
        for char in s:
            if numerals[char] <= numerals[pre]:
                result += numerals[char]
            else:
                result += numerals[char] - 2*numerals[pre]
            pre = char
        return result 
