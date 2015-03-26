Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        bracket_dict = {'(':')',
                        '[':']',
                        '{':'}',
                       }
        for bracket in s:
            if bracket in bracket_dict.keys():
                stack.append(bracket)
            elif not stack or bracket != bracket_dict[stack.pop()]:
                    return False
        return len(stack) == 0
        

    def isValid_1(self, s):
        if len(s) == 1:
            return False
        if len(s) == 0:
            return True
        
        stack = []
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                 if i == ')' and stack and stack.pop() == '(':
                      continue 
                 elif i == ']' and stack and stack.pop() == '[':
                     continue 
                 elif  i == '}' and stack and stack.pop() == '{':
                     continue 
                 else:
                     return False 
                     
        if stack != []:
            return False 
        return True                  
