Write a function to find the longest common prefix string amongst an array of strings.

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ''
        length = len(strs)
        
        compare = strs[0]
        for i in xrange(len(compare)):
            for char in strs[1:]:
                if len(char) == i or char[i]!=compare[i]:
                    return compare[:i]
        return compare
        
    def longestCommonPrefix_1(self, strs):
        result = ''
        if len(strs) == 0 or len(strs[0]) == 0:
            return result
        
        if len(strs) == 1:
            return strs[0]
        flag = False
        
        for i in xrange(len(strs[0])):
            for j in xrange(1, len(strs)):
                if (i < len(strs[j]) and strs[j][i] == strs[0][i]):
                        flag = True
                else:
                    flag = False
                    break
            if flag:    
                result += strs[0][i]
            else:
                break
        
        return result        
