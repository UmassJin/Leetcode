You are given a string, S, and a list of words, L, that are all of the same length. 
Find all starting indices of substring(s) in S that is a concatenation of each word in L 
exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        num_word = len(words)
        len_word = len(words[0])
        lengths = len(s)
        ret = []
        
        for i in xrange(lengths - len_word*num_word + 1):
            sublist =  [s[j: j+len_word] for j in xrange(i, i+len_word*num_word, len_word)]
            
            found = True
            for word in words:
                if word in sublist:
                    sublist.remove(word)
                else:
                    found = False
                    break
            if found:
                ret.append(i)
        return ret


class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        wordnum = len(L)
        wordlen = len(L[0])
        result = []
        dic_global = {}
        for i in L:
            if i not in dic_global:
                dic_global[i] = 1
            else:
                dic_global[i] += 1
        
        for i in xrange(len(S)-wordlen*wordnum+1):  # Note: here is "len(S)-wordlen*wordnum+1"
            j = 0
            dict = {}
            while j < wordnum:
                word = S[i+wordlen*j:i+wordlen*j+wordlen] 
                if word not in dic_global:
                    break
                if word not in dict:
                    dict[word] = 1
                else:
                    dict[word] += 1
                if dict[word] > dic_global[word]:
                    break
                j += 1
            
            if j == wordnum: result.append(i) # Note: here need to add "j == wordnum"
        return result 
