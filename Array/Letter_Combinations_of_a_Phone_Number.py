Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

class Solution:
    # @return a list of strings, [s1, s2]
    dict = {'1':'',
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'}
            
    def letterCombinations(self, digits):
        if len(digits)==0: return []
        result = ['']  # Note: here we should use [''] not empty []
        for digit in digits:
            ret = []
            for comb in result:
                for char in Solution.dict[digit]:
                    ret.append(comb+char)
            result = ret
        return result 
            
    # Recursion 1
    def letterCombinations_1(self, digits):
        if len(digits)==0: return []
        result = []
        self.combination_rec(digits,0,result,'')
        return result 
    
    def combination_rec(self,digits,i,result,ret):
        if i == len(digits):
            result.append(ret)
            return 
        for char in Solution.dict[digits[i]]:
            self.combination_rec(digits,i+1,result,ret+char)
    
    # Recursion 2 
    def letterCombinations_2(self, digits):
        if digits == "":
            return [""]
        result = []
        result = self.get_result_2([], 0, digits)
        return result
    
    def get_result_2(self, result, i, digit):
        if i == len(digit): return result
        str1 = Solution.dict[digit[i]]
        result2 = []
        for char in str1:
            if result == []:
                result2.append(char)
            else:
                for m in xrange(len(result)):
                    temp = result[m]+char     
                    result2.append(temp)
        return self.get_result(result2, i+1, digit)            
        
