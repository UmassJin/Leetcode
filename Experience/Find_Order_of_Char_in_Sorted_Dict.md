#### [Given a sorted dictionary of an alien language, find order of characters](http://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/)

* Check the Algorithm/ part for the [Topology Sort](https://github.com/UmassJin/Leetcode/blob/master/Algorithm/Topology_Sort.md)

```python
class Node:
    def __init__(self):
        self.visited = "White"
        self.adjacent = []
        
def printOrder(words, alpha):
    graph = {}
    for char in alpha:
        graph[char] = Node()    
        # {'a': Node(visited, []),'b': Node(visited, []) }
    
    for i in xrange(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        for j in xrange(min(len(word1),len(word2))):
            if word1[j] != word2[j]:
                graph[word1[j]].adjacent.append(word2[j])
                break # Very important!! We only compare the fist Non-equal char
    
    print topologicalSort(graph)
    
def topologicalSort(graph):
    queue = []
    for node in graph:
        if graph[node].visited == "White":
            topologicalUtil(graph, node, queue)
    return queue

def topologicalUtil(graph, node, queue):
    if graph[node].visited == "Gray":
        print "This is the cycle graph!"
    if graph[node].visited == "White":
        graph[node].visited = "Gray"
        for adja in graph[node].adjacent:
            topologicalUtil(graph, adja, queue)
        graph[node].visited = "Black"
        queue.insert(0,node)
    
printOrder(['baa','abcd','abca','cab','cad'],'abcd')
printOrder(['caa','aaa','aab'],'abc')

>>> output: 
[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python new_sort_dic.py
['b', 'd', 'a', 'c']
['c', 'a', 'b']

```
