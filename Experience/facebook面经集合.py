'''
1. There are a row of houses, each house can be painted with three colors red, blue and green. 
The cost of painting each house with a certain color is different. You have to paint all the houses 
such that no two adjacent houses have the same color. You have to paint the houses with minimum cost. 
How would you do it?

Note: Painting house-1 with red costs different from painting house-2 with red. The costs are different 
for each house and each color.

Reference: http://karmaandcoding.blogspot.com/2012/02/house-coloring-with-red-blue-and-green.html
'''

def sort_colors(matrix):
        if not matrix or not matrix[0]: return 0
        house_num = len(matrix)
        color_num = len(matrix[0])

        dp = [ [0 for i in xrange(color_num)] for j in xrange(house_num)]

        for i in xrange(house_num):
                for j in xrange(color_num):
                        if i == 0:
                                dp[0][j] = matrix[0][j]
                        else:
                                tmp = dp[i-1][:j] + dp[i-1][j+1:]
                                lastmin = min(tmp)
                                dp[i][j] = lastmin + matrix[i][j]
        return min(dp[house_num-1])

matrix = [[1, 2, 3], [6, 7, 5], [2, 6, 8]]
print sort_colors(matrix)


'''
2. Copy Random List, optimization use O(1)
'''


'''
3. large scale下怎么设计一个根据关键词查询status的service。我自然又是一顿瞎扯，神马invert index, consistent hashing, 想到什么扯什么。
然而这并没有什么卵用。。不论扯到什么大哥都要刨根问底，我到最后就完全招架不住了。。大哥的表情也就越来越蛋疼了。。这轮结束后我觉得基本
就没戏了，design面这么烂基本是硬伤，弥补不了了。
'''

'''
4
有这么一个class Contact，里面有一个string的name，和一个vector 装着email address，是这个Contact有的address，用一个list装着是因为一个人有可能有多个email，现在给你vector，比如
{
    { "Johhhn", {"john@gmail.com"} },
    { "Mary", {"mary@gmail.com"} },
    { "John", {"john@yahoo.com"} },
    { "John", {"john@gmail.com", "john@yahoo.com", "john@hotmail.com"} },
    { "Bob",  {"bob@gmail.com"} }
}

现在我们知道如果email address相同的话，那么就说明是同一个人，现在要做的是根据这些email address，
把同一个contact给group起来. 比如我们就可以知道#1，#3，#4是同一个人。注意不能根据名字来group，因为有可
能有相同名字的人，或者同一个人有可能有不同的名字来注册之类的。

* Reference: http://www.fgdsb.com/tags/Union-Find/
'''

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


