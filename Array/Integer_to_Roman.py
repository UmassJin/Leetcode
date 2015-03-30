Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @return a string
    def intToRoman_1(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        list = ''
        
        for i in range(0, len(values)):
            while num >= values[i]:  # Note: here we should use while not "if"
                num -= values[i]
                list += numerals[i]
            if num ==0:
                break
                
        return list  
        
    def intToRoman(self, num):
        digits = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD' ),
                  (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                  (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]      
        result = ''
        for digit in digits:
            while num >= digit[0]:  # Note: here we should use while not "if"
                result += digit[1]
                num -= digit[0]
            if num == 0: break
        return result 
        
