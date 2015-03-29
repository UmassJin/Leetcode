The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1: return s
        result = ['' for i in xrange(nRows)]
        index = -1; step = 1
        ret = ''
        
        for char in s:
            index = index + step 
            if index == nRows:
                index -= 2; step = -1
            elif index == -1:
                index = 1; step = 1
            result[index] += char 
        
        for i in xrange(len(result)):
            ret = ret+result[i]
        return ret
