'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        sign = [1, 1]
        total = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += sign.pop() * int(s[start:i])
                continue   # 注意这里要加continue!
            if s[i] in '+-(':
                sign.append(sign[-1] * (1,-1)[s[i] == '-'])
            elif s[i] == ')':
                sign.pop()
            i += 1
        return total 


# Reference: https://leetcode.com/discuss/39532/easy-18-lines-c-16-lines-python
