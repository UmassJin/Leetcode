'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
'''

class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        result = []
        n, reminder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        result.append(sign+str(n)+'.')
        
        stack = []
        while reminder not in stack:
            stack.append(reminder)
            n, reminder = divmod(reminder*10, abs(denominator))
            result.append(str(n))
        
        index = stack.index(reminder)
        result.insert(1+index, '(')
        result.append(')')
        
        return ''.join(result).replace('(0)', '').rstrip('.')

# 思路: 
# first, consider the sign, and add it into the result 
# 注意在第一次求n 和 reminder的时候，必须要用abs(numerator), abs(denominator)，否则多加了一个sign
# 注意一些python的用法，divmod, stack.index('str'), insert, append, replace, rstrip, lstrip 
