'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''


class TrieNode:
    def __init__(self):
        self.value = None
        self.isend = False 
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        node = self.root
        word = word.strip()
        
        for char in word:
            if char not in node.children:
                child = TrieNode()
                node.children[char] = child
                node = child
            else:
                node = node.children[char]
        node.isend = True
        node.value = word

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        word = word.strip()
        return self.search_dfs(word, self.root)
        
    def search_dfs(self, word, node):
        for i, char in enumerate(word):
            if char != '.':
                if char not in node.children:
                    return False
                node = node.children[char]
            elif char == '.':
                for child in node.children:
                    if self.search_dfs(word[i+1:], node.children[child]):
                        return True
                return False
        return node.isend

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
