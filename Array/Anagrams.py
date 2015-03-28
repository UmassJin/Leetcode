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
            newword = ''.join(sorted(member)) # Note: here we need to join the member into string 
            if newword not in dict:
                dict[newword] = [member]
            else:
                dict[newword] += [member]
        
        for key in dict:
            if len(dict[key]) >= 2:
                result.extend(dict[key])  # Note: Here not use the append, use extend 
        
        return result 

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        d = {}
        for s in strs:
            key = ''.join(sorted(s))
            d.setdefault(key,[]).append(s)
        ret = []
        for key in d:
            if len(d[key]) > 1:
                ret.extend(d[key])
        return ret
    # Note:
    # 1. Need to use extend here, return those len(d[key]) > 1
    # 2. Need to remember the definition of Anagrams

    Input:      ["tea","and","ate","eat","dan"]
    Output:     ["and","dan"]
    Expected:   ["and","dan","tea","ate","eat"]
