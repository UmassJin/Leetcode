'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        tokens = iter(re.findall('\d+|\S', s))
        total, sign = 0, 1
        
        for token in tokens:
            if token in "+-":
                total += sign * term
                sign = ' +'.find(token)
            elif token in "*/":
                n = int(next(tokens))
                term = term * n if token == "*" else term/n
            else:
                term = int(token)
        return total + sign * term
        
# Reference: https://leetcode.com/discuss/41632/easy-7-12-lines-three-solutions
