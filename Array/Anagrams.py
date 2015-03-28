Given an array of strings, return all groups of strings that are anagrams.
Note: All inputs will be in lower-case.

Reference: http://blog.csdn.net/linhuanmars/article/details/21664747
# Notes: anagrams definition: two strings, which have the same character, maybe different order 
# 1) Save the SORTED string as the key in the dictionary 
# 2) Save each string as the value (put into a list), then push them into the list 

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        result = []
        dict = {}
        
        for member in strs:
            newword = ''.join(sorted(member))
            if newword not in dict:
                dict[newword] = [member]
            else:
                dict[newword] += [member]
        
        for key in dict:
            if len(dict[key]) >= 2:
                result.extend(dict[key])
        
        return result 
