Write a function to find the longest common prefix string amongst an array of strings.

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ''
        length = len(strs)
        
        compare = strs[0]
        for i in xrange(len(compare)):  #注意这里是 strs[0]的长度
            for char in strs[1:]:
                if len(char) == i or char[i]!=compare[i]:
                    return compare[:i]
        return compare

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        #if len(strs) == 1: return strs[0]
        str_size = len(strs[0])
        result = ''
        
        for j in xrange(str_size):
            for s in strs[1:]:
                if len(s) <= j or s[j] != strs[0][j]:
                    return result
            result += strs[0][j]  # after checking all the substring in the list, then add the result 
        return result 

# test case: ['a','b'] => ''
# test case: [''] => ''
# test case: ['a','aa'] => 'a'
# test case: ['aa', 'a'] => 'a'

