### Union Find algorithm 
Reference: https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf

#### 1) Number of Islands follow up:
在一个由grid组成的海洋上，每次将一个方格从海洋改变成陆地。在每次完成这个操作后，都要得到此时的岛屿数目
这实际上就是要动态维护一个图的Connected Component
Reference: http://www.1point3acres.com/bbs/thread-137243-1-1.html

#### 2) Check the tree is Valid or not
Acturally check if there is cycle in the undirected graph 
Reference: http://www.geeksforgeeks.org/union-find/

```python
# Check Tree is Valid or not, check the Graph is cycle or not 
For each edge, make subsets using both the vertices of the edge. If both the vertices 
are in the same subset, a cycle is found.

class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.edge = [Edge() for _ in xrange(self.E)]

class Edge:
    def __init__(self):
        self.src = 0
        self.dest = 0

class UnionFind:
    def __init__(self):
        self.father = []
        self.rank = []

    def find(self, x):
        if self.father[x] == -1:
            return x
        return self.find(self.father[x])

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        if self.rank[x] < self.rank[y]:
            self.father[x] = y
        else:
            self.father[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1  # 注意在更新rank的时候，只有当两个rank相等的时候才需要加一，否则不变，如下图

    def validTree(self, graph):
        if not graph: return False
        self.father = [-1 for _ in xrange(graph.V)]
        self.rank = [0 for _ in xrange(graph.V)]

        for i in xrange(graph.E):
            x = self.find(graph.edge[i].src)
            y = self.find(graph.edge[i].dest)
            if x == y:
                print "this is cycle graph!"
                return True
            self.union(x, y)

```

![pic](https://cloud.githubusercontent.com/assets/9062406/8512632/58fbbdf6-2301-11e5-9e26-85efa559670c.png)



#### 3) Group Contacts
有这么一个class Contact，里面有一个string的name，和一个vector 装着email address，是这个Contact有的address，用一个list装着是因为一个人有可 能有多个email，现在给你vector，比如
{
    { "John", {"john@gmail.com"} },
    { "Mary", {"mary@gmail.com"} },
    { "John", {"john@yahoo.com"} },
    { "John", {"john@gmail.com", "john@yahoo.com", "john@hotmail.com"} },
    { "Bob",  {"bob@gmail.com"} }
}
现在我们知道如果email address相同的话，那么就说明是同一个人，现在要做的是根据这些email address，
把同一个contact给group起来

Reference: http://www.fgdsb.com/tags/Union-Find/
