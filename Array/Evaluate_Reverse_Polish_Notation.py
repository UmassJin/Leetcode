Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
'''
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def __init__(self):
        self.operation = {
            '+': lambda y, x: x + y,  # Here, we could use Lambda ! 
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(operator.truediv(x, y))
            }
    
    def evalRPN(self, tokens):
        if not tokens: return 0
        stack = []
        
        for char in tokens:
            if char.isdigit():
                stack.append(int(char))
            elif char[0] == '-' and char[1:].isdigit():  # note here need to consider the negative number 
                stack.append(-int(char[1:]))
            elif char in self.operation:
                stack.append(self.operation[char](stack.pop(), stack.pop()))
        
        return stack[0]
        
        
# Original Solution
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        length = len(tokens)
        
        for i in xrange(length):
            if tokens[i] != '*' and tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '/':
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                
                if tokens[i] == '*':
                    stack.append(a*b)
                elif tokens[i] == '-':
                    stack.append(b-a)
                elif tokens[i] == '+':
                    stack.append(a+b)
                elif tokens[i] == '/':
                    if a*b < 0:
                        stack.append(-((-b)/a))
                    else: 
                        stack.append(b/a)
        
        result = stack.pop()
        return result 

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        if not tokens: return 0
        stack = []
        
        for char in tokens:
            
            if char == '+' or char == '-' or char == '*' or char == '/':
                digit2 = stack.pop()
                digit1 = stack.pop()
                if char == '+':
                    res = digit1 + digit2
                    stack.append(res)
                elif char == '-':
                    res = digit1 - digit2
                    stack.append(res)
                elif char == '*':
                    res = digit1 * digit2
                    stack.append(res)
                elif char == '/':
                    res = abs(digit1)/abs(digit2)
                    if digit1* digit2 < 0:
                        res = -res
                    stack.append(res)
                    
            elif char.isdigit():
                stack.append(int(char))
                
            elif char[0] == '-' and char[1:].isdigit():
                stack.append(int(char))
            else:
                return 0
        return stack[0]
