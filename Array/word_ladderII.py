Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        '''
        @trace_map: used to record each word and it's previous word, for example: 
        {cog:[log,dog], log:[lot], dog:[dot], dot:[hot], lot:[hot], hot:[hit]}
        @pre_set: used to record previous level words, need to removed in the dic before go to next level
        @cur_set: used to record current level words
        '''
        trace_map = {word:[] for word in dict}
        chars = string.ascii_lowercase
        pre_set = set([start])
        word_len = len(start)
        find = False
        result = []
        
        while pre_set and not find:
            cur_set = set([])
            for word in pre_set:
                dict.remove(word)
            for word in pre_set:
                if word == end:
                    find = True
                for i in xrange(word_len):
                    for char in chars:
                        if char != word[i]:
                            newword = word[:i] + char + word[i+1:]
                            if newword in dict:
                                trace_map[newword].append(word)
                                cur_set.add(newword)
            pre_set = cur_set
            
        if find:
            self.build_path(trace_map, end, [], result)
        return result 
        
    def build_path(self, trace_map, word, sublist, result):
        if len(trace_map[word]) == 0:
            sublist.insert(0,word)
            result.append(sublist)
        for ele in trace_map[word]:
            self.build_path(trace_map, ele, [word]+sublist, result)
        

# Reference:
# http://www.cnblogs.com/zuoyuan/p/3697045.html
# http://yucoding.blogspot.com/2014/01/leetcode-question-word-ladder-ii.html
