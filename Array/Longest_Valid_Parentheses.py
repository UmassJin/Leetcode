Given a string containing just the characters '(' and ')', find the length of the 
longest valid (well-formed) parentheses substring.
For "(()", the longest valid parentheses substring is "()", which has length = 2.
Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# Note: 
# 1. Use the stack to save the '('
# 2. Need to maintain the variable 'last', in case if there is a lot of ')'without '('
# 3. O(n) time, O(n) space 

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if len(s) < 2: return 0
        stack = []
        last = -1
        maxvalue = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if stack == []:
                    last = i
                else:
                    stack.pop()
                    if stack == []:
                        maxvalue = max(maxvalue, i-last)
                    else:
                        maxvalue = max(maxvalue, i-stack[len(stack)-1])
        return maxvalue 

    # O(n) time, O(n) space
    # Note: Here we iteration the string for two times
    # so when the first iteration ends (left to right), we have 2 scenarios: 
    # 1, all left brackets are closed (every left bracket matches a right bracket) 
    # 2, some left brackets are open (couldn't find enough right brackets to finish them). 
    # In the first case, things are perfect, we just return the max value. In the second case, 
    # we start the second iteration from right to left. This time, we try to find left brackets to 
    # match right brackets. Remember, the condition to start the second iteration is that we are having 
    # more left brackets than right brackets. Therefore, we know each right bracket will guarantee to 
    # find a left bracket to form a pair.
    
    def longestValidParentheses(self, s):
        maxvalue = 0; depth = 0; start = -1
        for i, char in enumerate(s):
            if char == '(': depth += 1
            else:
                depth -= 1
                if depth < 0:
                    start = i
                    depth = 0
                elif depth == 0:
                    maxvalue = max(maxvalue, i - start)
        
        depth = 0
        start = len(s)
        for i in xrange(len(s)-1,-1,-1):
            if s[i] == ')': depth += 1
            else:
                depth -= 1
                if depth < 0:
                    start = i
                    depth = 0
                elif depth == 0:
                    maxvalue = max(maxvalue, start - i)
        
        return maxvalue 
