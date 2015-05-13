'''
Given two words (beginWord and endWord), and a dictionary, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.


Given two words (beginWord and endWord), and a dictionary, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
'''

# Method 1: use two BFS ! 
import collections, string

class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        if not beginWord or not endWord or not wordDict:
            return 0
        queue1 = collections.deque([beginWord])
        queue2 = collections.deque([endWord])
        start_set = {beginWord}
        end_set = {endWord}
        chars = string.ascii_lowercase  # Here we could get 'abcdef....xyz'
        n = len(beginWord)
        length1, length2 = 1, 1
        
        while queue1 and queue2:
            len1, len2 = len(queue1), len(queue2)
            for _ in xrange(len1):
                word = queue1.popleft()
                for i in xrange(n):
                    for char in chars:
                        if char != word[i]:
                            newword = word[:i] + char + word[i+1:]
                            if newword in end_set:
                                return length1+length2
                            if (newword in wordDict) and (newword not in start_set):
                                start_set.add(newword)
                                queue1.append(newword)
            length1 += 1
            
            for _ in xrange(len2):
                word = queue2.popleft()
                for i in xrange(n):
                    for char in chars:
                        if char != word[i]:
                            newword = word[:i] + char + word[i+1:]
                            if newword in start_set:
                                return length1+length2
                            if (newword in wordDict) and (newword not in end_set):
                                end_set.add(newword)
                                queue2.append(newword)
            length2 += 1
        return 0
            

# Method 2: here we use BFS, need to remove each checked word in dic, otherwise there is the loop !
    def ladderLength_1(self, beginWord, endWord, wordDict):
        if not beginWord or not endWord or not wordDict:
            return 0
        queue = collections.deque([beginWord])
        chars = string.ascii_lowercase
        length = 1
        n = len(beginWord)
        
        while queue:
            size = len(queue)
            for _ in xrange(size):
                word = queue.popleft()
                if word == endWord:
                    return length 
                for i in xrange(n):
                    for char in chars:
                        if char != word[i]:
                            newword = word[:i] + char + word[i+1:]
                            if newword in wordDict:
                                queue.append(newword)
                                wordDict.remove(newword)  #注意，要把已经检查过的word去掉！
            length += 1
        return 0
