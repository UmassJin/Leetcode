Given an expression string array, return the Polish notation of this expression. (remove the parentheses)

Have you met this question in a real interview? Yes
Example
For the expression [(5 − 6) * 7] (which represented by ["(", "5", "−", "6", ")", "*", "7"]), 
the corresponding polish notation is [* - 5 6 7] (which the return value should be ["*", "−", "5", "6", "7"]).

Clarification
Definition of Polish Notation:

http://en.wikipedia.org/wiki/Polish_notation
http://baike.baidu.com/view/7857952.htm


class Solution:
    # @param expression: A string list
    # @return: The Polish notation of this expression
    def convertToPN(self, expression):
        if not expression: return None
        stack = []
        result = []
        
        for char in reversed(expression):  ＃从input string从后往前扫描
            if char.isdigit():
                result.append(char)
            elif char == ')':
                stack.append(char)
            elif char == '(':
                while stack and stack[-1] != ')':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.precedence(stack[-1]) > self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)
        
        while stack:
            result.append(stack.pop())   # 注意要把剩余的符号append到result上去
            
        result.reverse() # 注意，这里需要用reverse
        
        return result 
    
    def precedence(self, char):
        if char in ('(', ')'):
            return 0
        elif char in ('+', '-'):
            return 1
        elif char in ('*', '/'):
            return 2
