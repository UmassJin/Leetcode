Given an expression string array, return the Reverse Polish notation of this expression. (remove the parentheses)

Have you met this question in a real interview? Yes
Example
For the expression [3 - 4 + 5] (which denote by ["3", "-", "4", "+", "5"]), 
return [3 4 - 5 +] (which denote by ["3", "4", "-", "5", "+"])


class Solution:
    # @param expression: A string list
    # @return: The Reverse Polish notation of this expression
    def convertToRPN(self, expression):
        if not expression: return None
        stack = []
        result = []
        
        for char in expression:
            if char.isdigit():
                result.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.precedence(stack[-1]) >= self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)
                
        while stack:
            result.append(stack.pop())
        return result 
    
    def precedence(self, char):
        if char in ('(',')'):
            return 0
        elif char in ('+','-'):
            return 1
        elif char in ('*', '/'):
            return 2


# Reference: http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
# Analysis:
# Create an empty stack called opstack for keeping operators. Create an empty list for output.
# Convert the input infix string to a list by using the string method split.
# Scan the token list from left to right.
# If the token is an operand, append it to the end of the output list.
# If the token is a left parenthesis, push it on the opstack.
# If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.
# If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence 
# and append them to the output list.
# When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.



# Polish Notation:
# -56 ==> 5-6 
# Reverse Polish Notation:
# 34+ ==? 3 + 4 
# 注意operator左边和右边的区别
