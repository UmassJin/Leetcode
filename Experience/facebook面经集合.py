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

'''
5. 给你一个array，返回array里面最大数字的index，
但是必须是最大数字里面随机的一个index。比如[2,1,2,1,5,4,5,5]必须返回[4,6,7]中的随机的一个数字，要求O(1)space.

# Reservoir Sampling https://github.com/UmassJin/Leetcode/blob/master/Algorithm/Reservoir_Sampling_Google.md
# http://www.fgdsb.com/2015/01/15/random-maximum/
'''

import random

def random_max(array):
    if not array: return None
    n = len(array)
    imax = -1 << 31
    result = 0

    for i in xrange(len(array)):
        if array[i] > imax:
            imax = array[i]
            count = 1
            result = array[i]
        elif array[i] == imax:
            count += 1
            print "count: ", count
            if random.randrange(count) == 0:
                print "count: ", count
                print "i: ", i
                result = array[i]
    return result           

test = [2,1,2,1,5,4,5,5]
print random_max(test)


'''
输出count最多的连续的字符。
For example:
"this is a sentence" => [t, h, i, s, i, s, a, s, e, n, t, e, n, c, e]
"thiis iss a senntencee" => [i, s, n, e]
"thiisss iss a senntttenceee" => [s, t, e]
"thiisss iss a sennnntttenceee" => [n]

'''
def contiguous_letter(s):
    if not s: return 0
    l = 0; maxlen = 0
    n = len(s)
    result = []
    while l < n:
        while l < n and s[l] == ' ':
            l += 1
        c = l + 1
        while c < n and s[c] == s[l]:
            c += 1
        if maxlen == c - l:
            result.append(s[l])
        elif maxlen < c - l:
            result = [s[l]]
            maxlen = c - l
        l = c
    return result

test1 = "thiisss iss a senntttenceee"
test2 = "this is a sentence"
print contiguous_letter(test1)
print contiguous_letter(test2)


'''
# http://www.mitbbs.com/article_t/JobHunting/33003737.html
一个月以前面的了，没什么营养，还是发给大家看看吧, 希望对大家有帮助，已经跪了。

电面： 中国大叔面的，大叔很nice，遇到我写有bug的时候都会着急的提醒我，题也很
简单。

1： 给n个点找出离远点最近的k个， k<<n。
2: 给三个 api isSmall()  isMid() isBig() 给一个array 排序，只要不被迷惑， 知
道其实是lc 上 sort color的变种就很简单了。

On Site：

1： 聊自己的research，白人manager，说自己以前是faculty，人非常nice。气场也比
较合， 我讲完之后还说把email给我，说我面试后有问题可以问他，然后问了个 two 
sum。

2：亚洲小哥，也很nice，第一道题是 Lc 上的String Multiplication。 然后出了一
个打印 tree路径的题，后来问我做过没有，只能说做过类似的，后来换了一道 的 
decode way 变形，要把所有的可能的组合都打印出来，写了一个recursion。

中午和内推我的本版汤唯姐姐吃饭，在此谢谢汤唯姐姐，大牛非常nice，大家内推可以
去找他。吃饭的时候还说，上午过了最难的两轮，下午都是国人面试官，应该简单点。

3：国人面试官，貌似气场不太合，我写code的时候尽量解释，可能人家
觉得我也做不出来，无聊的看了很久手机。出了这个题
http://www.mitbbs.com/article_t/JobHunting/32906379.html

class IntFileIterator {
  boolean hasNext();
  int next();
}

class{
  public boolean isDistanceZeroOrOne(IntFileIterator a, IntFileIterator b)；

}
// return if the distance between a and b is at most 1.. 
// Distance: minimum number of modifications to make a=b
// Modification:
//   1. change an int in a
//   2. insert an int to a
//   3. remove an int from a

都怪自己事先没把本版的题都做一遍，然后就跪在这道题上了，巧的是貌似帖子的一个
妹子也是这个国人同学面的，大家记得一定把这道题做一下。

4. 国人面试官面出的 design：Shorten Url。面试官人非常nice，可是自己答的一般
，在此谢谢他。
'''
