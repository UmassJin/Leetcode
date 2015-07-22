### Union Find algorithm 
Reference: https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf

#### 1) Number of Islands follow up:
在一个由grid组成的海洋上，每次将一个方格从海洋改变成陆地。在每次完成这个操作后，都要得到此时的岛屿数目
这实际上就是要动态维护一个图的Connected Component
* Reference: http://www.1point3acres.com/bbs/thread-137243-1-1.html

#### 2) Check the tree is Valid or not
Acturally check if there is cycle in the directed graph and also need to check if there is more than one root ! 
并查集的理解思路相对简单一些，首先初始化一个长度为n的并查集，遍历所有edge，首先find这个edge的两个节点，如果已经有同一个祖先，则表明存在环，也就不可能是树。构建并查集之后，再扫一遍找出祖先的数量即可，超过一个就不是树。
* Reference: http://www.geeksforgeeks.org/union-find/

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
    
    def num_sets(self, n):
        count = 0
        for i in xrange(n):
            if self.father[i] == i:
                count +=1
        return count 

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
        
        # Important here ! Need to check if the V is more than 1 or not ! 
        return num_sets(graph.V) == 1

```

![pic](https://cloud.githubusercontent.com/assets/9062406/8512632/58fbbdf6-2301-11e5-9e26-85efa559670c.png)



#### 3) Group Contacts
有这么一个class Contact，里面有一个string的name，和一个vector 装着email address，是这个Contact有的address，用一个list装着是因为一个人有可能有多个email，现在给你vector，比如
```
{
    { "Johhhn", {"john@gmail.com"} },
    { "Mary", {"mary@gmail.com"} },
    { "John", {"john@yahoo.com"} },
    { "John", {"john@gmail.com", "john@yahoo.com", "john@hotmail.com"} },
    { "Bob",  {"bob@gmail.com"} }
}
```
现在我们知道如果email address相同的话，那么就说明是同一个人，现在要做的是根据这些email address，
把同一个contact给group起来. 比如我们就可以知道#1，#3，#4是同一个人。注意不能根据名字来group，因为有可
能有相同名字的人，或者同一个人有可能有不同的名字来注册之类的。

* Reference: http://www.fgdsb.com/tags/Union-Find/

```python
class Contact:
    def __init__(self, name, email):
        self.name = name
        self.emails = email # list of emails 

class UnionFind:
    def __init__(self, n):
        self.father = [i for i in xrange(n)]
        self.ranks = [0 for i in xrange(n)]

    def find(self, x):
        if self.father[x] == x:
            return x
        return find(self.father[x])

    def do_union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        if self.ranks[x] < self.ranks[y]:
            self.father[x] = y
        else:
            self.father[y] = x
            if self.ranks[x] == self.ranks[y]:
                self.ranks[x] += 1
                
class Solution:
    def group_contacts(self, contact):
        n = len(contact)
        uf = UnionFind(n)
        email_map = {}
        # first build the map like 
        # {"john@gmail.com":[0,3],
        #  "mary@gmail.com": [1],
        #  "john@yahoo.com": [2,3],
        #  "john@hotmail.com": [3],
        #  "bob@gmail.com": [4]}
        for i in xrange(n):
            for email in contact[i].emails:
                email_map.setdefault(email, []).append(i)
        
        # then for each list in each email, join them into one group
        # so father init: [0,1,2,3,4]
        # after [0,1,0,0,4]
        for p in email_map:
            for j in xrange(len(email_map[p])-1):
                uf.do_union(j, j+1)

        # Then group for each root, create a list
        # {0: [0,2,3],
        #  1, [1],
        #  4, [4]}
        group = {}
        for i in xrange(n):
            group.setdefault(uf.find(i),[]).append(i)

        result = []
        for p in group:
            rec = []
            for i in group[p]:
                rec.append(contact[i])
            result.append(rec)
        return result
```




