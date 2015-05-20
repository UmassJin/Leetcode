##[Trie](http://blog.csdn.net/v_july_v/article/details/6897097)

### 第一部分 介绍
#### 3个基本性质
1. 根节点不包含字符，除根节点外每一个节点都只包含一个字符。
2. 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串。
3. 每个节点的所有子节点包含的字符都不相同。

#### 实例分析
Trie树是简单但实用的数据结构，通常用于实现字典查询。我们做即时响应用户输入的AJAX搜索框时，就是Trie开始。
本质上，Trie是一颗存储多个字符串的树。相邻节点间的边代表一个字符，这样树的每条分支代表一则子串，
而树的叶节点则代表完整的字符串。和普通树不同的地方是，相同的字符串前缀共享同一条分支。
下面，再举一个例子。给出一组单词，inn, int, at, age, adv, ant, 我们可以得到下面的Trie：

![pic](http://hi.csdn.net/attachment/201110/22/0_13192967247f7E.gif)

* 每条边对应一个字母。
* 每个节点对应一项前缀。叶节点对应最长前缀，即单词本身。
* 单词inn与单词int有共同的前缀“in”, 因此他们共享左边的一条分支，root->i->in。同理，ate, age, adv, 和ant共享前缀"a"，所以他们共享从根节点到节点"a"的边。

#### [比较Trie and Hashtable](http://en.wikipedia.org/wiki/Trie)
##### As discussed below, a trie has a number of advantages over binary search trees.[4] A trie can also be used to replace a hash table, over which it has the following advantages:
* Looking up data in a trie is faster in the worst case, O(m) time (where m is the length of a search string), compared to an imperfect hash table. An imperfect hash table can have key collisions. A key collision is the hash function mapping of different keys to the same position in a hash table. The worst-case lookup speed in an imperfect hash table is O(N) time, but far more typically is O(1), with O(m) time spent evaluating the hash.
* There are no collisions of different keys in a trie.
* Buckets in a trie, which are analogous to hash table buckets that store key collisions, are necessary only if a single key is associated with more than one value.
* There is no need to provide a hash function or to change hash functions as more keys are added to a trie.
* A trie can provide an alphabetical ordering of the entries by key.

#####Tries do have some drawbacks as well:
* Tries can be slower in some cases than hash tables for looking up data, especially if the data is directly accessed on a hard disk drive or some other secondary storage device where the random-access time is high compared to main memory.[5]
* Some keys, such as floating point numbers, can lead to long chains and prefixes that are not particularly meaningful. Nevertheless a bitwise trie can handle standard IEEE single and double format floating point numbers.
* Some tries can require more space than a hash table, as memory may be allocated for each character in the search string, rather than a single chunk of memory for the whole entry, as in most hash tables.


#### 代码实现
* 对于Trie而言，每个节点记录下一个字母的数值，一直到根节点，只有到达根节点时，再update value的值。

```python

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.value = None
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        word = word.strip()
        
        for char in word:
            if char not in node.children:
                child = TrieNode()
                node.children[char] = child
                node = child 
            else:
                node = node.children[char]
        node.value = word

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        if node.value == word:
            return True
        else:
            return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
```

#### Time complexity 
* Create Trie: O(n*len) (n is number of total wors, len is the length of word)
* Insert: O(m) (m is the length of insert word)
* Search: O(m) (m is the length of search word)

### 第二部分 [Suffix Tree](http://blog.csdn.net/v_july_v/article/details/6897097)
* [G4G: Suffix Tree Introduction](http://www.geeksforgeeks.org/pattern-searching-set-8-suffix-tree-introduction/)
* A Suffix Tree for a given text is a compressed trie for all suffixes of the given text


