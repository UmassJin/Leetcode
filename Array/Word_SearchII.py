'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        #self.children = {}
        self.flag = False # use the flag to determine the word exist or not
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.flag = True
        
        # for char in word:
        #     if char not in node.children:
        #         newNode = TrieNode()
        #         node.children[char] = newNode
        #         node = newNode
        #     else:
        #         node = node.children[char]
        
        # node.value = word
    
    def startwith(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        def dfs(x, y, letter, node):
            if node.flag:
                result.append(letter)
                node.flag = False
                
            if (0 <= x < len(board)) and (0 <= y < len(board[0])):
                char = board[x][y]
                child = node.children.get(char)
                if child:
                    board[x][y] = None
                    dfs(x+1, y, letter+char, child) 
                    dfs(x-1, y, letter+char, child)  
                    dfs(x, y+1, letter+char, child)  
                    dfs(x, y-1, letter+char, child)
                    board[x][y] = char
        
        trie = Trie()
        result = []
        
        for word in words:
            trie.insert(word)
            
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                 if trie.startwith(board[i][j]):
                        dfs(i, j, '', trie.root)
        return result 
    

        
