Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        list = []
        string = ''
        self.addParen(list, n, n, string)
        return list
    
    def addParen(self, list, leftrem, rightrem, string):
        if rightrem < 0:
            return
        if leftrem == 0 and rightrem == 0:
            list.append(string)
            
        if leftrem > 0:
            self.addParen(list, leftrem-1, rightrem, string + '(')
            
        if rightrem > leftrem:
            self.addParen(list, leftrem, rightrem-1, string + ')')
