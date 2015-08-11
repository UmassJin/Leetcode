'''
1. Given a list of words, find whether a new word is anagram of word in list
2. Implement an LRU cache. 
3. Using Object Oriented Design principles, design a method to check if a Sudoku board is valid 
(skeleton code was provided which was initially passed in through a 2-d array).  
4. Lots of question related to hash table.  
5. Implement boggle 
6. Implement LRU cache with get and set operations in constant time O(1). 
7. 1. Segment Tree; 2. How to diagnose latency in data center;  
8. Print all permutations of 3 pair of parens. ()()(), (()()), (())(),,,. etc 
9. 电话combination那道，算法很熟悉了，dfs，不过好长时间没做，边think aloud 边码，还算顺利
让自己弄几个test case 跑跑，但没有一次bug free，忘了考虑0，1的case ＝＝还有关于unsigned int 的warning
接着聊了聊怎么 code review，加一些comments啊什么的

10. 面试四轮，第一轮是个韩裔小哥，两道题，happy number和anagram。
第二轮白人，换硬币那题。
第三轮ABI经理，问了一大顿behavioural question，最后剩10分钟问了八皇后。
第四轮白人，设计扫雷的游戏，实现其中点一个格子，返回结果（要么失败，要么一片没有雷的区域，list of JSON object)。
其中第二轮第四轮都是要求现场编译运行的。我用python所以相对比较轻松一点。

'''

class Solution:
    # @return a list of strings, [s1, s2]
    dict = {'0':'',
            '1':'',
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'}
            
    # Iteration 
    def letterCombinations(self, digits):
        if not digits: return []
        result = ['']  # Note: here we should use [''] not empty []
        for digit in digits:
            ret = []
            for comb in result:
                for char in Solution.dict[digit]:
                    ret.append(comb+char)
            if ret:     # Note: add ret here, we need to consider the case "12" 
                result = ret
        return result 
            

    # Recursion
    def letterCombinations(self, digits):
            if not digits: return []
            result = []
            length = len(digits)
            self.letter_com_helper(digits, result, '', length)
            return result 
            
    def letter_com_helper(self, digits, result, substr,length):
        if len(substr) == length:
            result.append(substr); return 
        
        for i, digit in enumerate(digits):
            if digit == "1" or digit == '0':  # take care the special '1' and '0' case 
                length -= 1
            for char in Solution.dict[digit]:
                self.letter_com_helper(digits[i+1:], result, substr + char,length)
            
    # test case:
    # Input: "22"
    # Output: ["aa","ab","ac","ba","bb","bc","ca","cb","cc","a","b","c"]
    # Expected: ["aa","ab","ac","ba","bb","bc","ca","cb","cc"]

'''
10. subsetsI and subsetsII
11. search in rotated array
12. sprial matrix

13. 
Word Ladder II
以前只写过找所有path然后在dfs出最短path的解，烙印不让用，问有没有更好的方法
。。。我建了个Graph，用BFS+mp搜，磕磕碰碰写了个大概。。。

14. 
给一个tuple list, 按weight random select. 比如给 [(“hello”, 2.34), (“world”, 4.68)…] world出现的概率是hello的两倍
第二题, reverse string的变种。 只reverse word不reverse punctuation。比如 “this,,,is.a word” -> “word,,,a.is this”


'''


'''
1，background
2，project
3，coding problem
给一个String array，找出每个元素的Anagram，按照相同的anagram分为一组，最后输出每一组元素。
我用了HashMap<String, ArrayList<String>>来做的，在计算key的时候，需要按字母顺序sort String作为key，
于是follow up就是怎么不用sort，于是我就说可以把每一个string统计一下a,b,c。。。的频率，然后输出一个pattern a1b3c4。
把这个pattern作为map的key。

4，问当你用browser打开www.uber.com的时候，发生了生么。我就用http请求，到dns，到server，再返回，浏览器render之类的讲了一下
'''

----------------------------------------------

'''
System Design:

1. 第三轮：一个漂亮国人妹纸加一个白男。 systemdeisgn，给两个题目，让我选一个，一个是designnetflix另一个是design uber, 
我就直接选 了designuber。我跟面thumbtack一样先用了最经典 的3tier 架构大法，然后一点一点改进。
system design问的很细，问mobile app怎么跟backend通信，问通信是哪些protocal， 传输的信息是什么，
哪里加cache，distributed db怎么弄之类。基本我答的还算顺利。感觉面试官挺满意这轮的。

2.  设计excel， 先实现基本功能再优化（比如存图片怎么弄）

3. 先是问了project，涉及很具体的算法和dataset处理之类；问了hadoop；
然后就是用coderpad考了一题OOD
Represent a deck of playing cards in an object-oriented design. 
(1) Write a function to output the deck. (2) Write a fn to shuffle the deck.

4. 
design一个uber eat。说是system design结果我感觉更像product design

5. 
之前也看了好多uber的面经， 本以为会考算法 leetcode， 结果却考了一个ood的题目

直接上原题
Develop an API Rate-limit Throttling Client
要求写一个api， 请求第三方api， 如果一秒内的请求太多， 自己的api就直接忽略掉。
面试小哥给了个框架
import time
import datetime

class GoogleMapsClient(object):
“””3rd party maps client; we CANT EDIT THIS.”””

def __init__(self):
self.requests_made = 0


 
def make_request(self):
self.requests_made += 1
now = datetime.datetime.now().time()
return “%d – %s – San Francisco” % (self.requests_made, now)

刚开始对python time的单位不熟悉，有个bug。后来改了
class MyRequest(object):

def __init__(self):
self.client = GoogleMapsClient()
self.time = time.time()
self.request_times = 0

def make_request(self):

if (time.time()-self.time)>1:
self.time = time.time()
self.request_times = 0
else:
self.request_times += 1
if self.request_times>=10:
time.sleep(1)
return self.client.make_request()


 
Follow up 是如何让myclient 继续接受request。 可能我也没听明白题意， 小哥直接说time.sleep(1).

面试题目就这一个， 开始还有介绍自己和简历。求水果啊。。


6. 电面是一个美国小哥，开始聊了聊简历之后给了一道系统设计题，设计一个Service可以输入用户location查询附近的
公交站台和所有即将到这些站台的公交车。我随便和他扯了一些系统设计的还有优化算法之类的东西，后来让我写一个
控制访问API频率（Ratelimit）的function， 用了一个Queue写完就结束了。

7. 让我设计一个 Netflix， follow up 很多 比如如何限制同一个用户多处登录不能同时看一个资源，
如何实现根据用户的网速调整清晰度，怎么热门推荐等等。

8. 第二个人 ： 进来直接不闲聊直接让我打开自己电脑开始写一些代码，设计一个 Excel ， 
每个cell里面是一个String。 一开始想当然说可以直接用二维矩阵存，后来改成list of lists， 
最后改成了HashMap。后续还有evaluate一个string相关的问题（给了黑盒evaluate函数，
对每个cell实现evaluate和支持修改）。

9. 第三个人 ： 纯聊简历，干聊project，面试官没有准备一道题，到最后我就已经是在找话说了。


'''

-----------------------------------------

'''
culture fit:
她让我说了下我现在的proj，具体问了proj怎么设计的，为什么，有哪些可以值得改进的。然后问些behavior，
比如你之前 有没有projfail过，为什么之类的。最后问了我whyuber, where’s ur passion之类的。
'''

'''
change the people's traditional life style, 
safety is the most important problem
add the mini meter to know how long to the desitination
how to ensure there is no overcharged 
language issue 
add/set the time for pick up 

uber rush
uber essentials
uber eats
'''



# given a list of filenames, each file has been sorted
# merge into a big file

from random import randint
import heapq

class MyFile(object):
    def __init__(self, n):
        self.lines = []
        self.i = 0
        self.length = 3
        r = 0
        for i in xrange(n):
            pass
            # r = randint(r, r + 100)
            # self.lines.append(str(r))
        self.lines.append('abc' + str(randint(1,200)))
        self.lines.append('efg' + str(randint(1,200)))
        self.lines.append('xyz' + str(randint(1,200)))
        
        # sort by alphabetical order
        # compare 1st letter
        # if 1st letter is same,compare 2nd, etc.
        # content of file:
        # acd
        # abc
        # xyz
        # xyy
        # sorted:
        # abc
        # acd
        # xyy,
        # xyz
        # sorted(str, cmp = lambda x: )
    
    def nextline(self):
        if self.i < self.length:
            self.i += 1
            return self.lines[self.i - 1]
        else:
            return None

def merge_karray(files):
    '''
    @ input files list: [file1, file2, file3...]
    @ output:
    '''
    if not files:
        return None
    heap = []
    result = []
    k = len(files)
    for i in xrange(k):
        ele = files[i].nextline()
        if ele:
            heap.append((MyLine(ele), i))
    heapq.heapify(heap)
    #print "heap: ", heap
    
    while heap:
        element = heapq.heappop(heap)
        value, file_index = element[0], element[1]
        result.append(value.string)
        new_value = files[file_index].nextline()
        if new_value:
            heapq.heappush(heap, (MyLine(new_value), file_index))
    return result 


#  "abc", "abcd"
class MyLine(object):
    def __init__(self, string):
        self.string = string
        
    def __cmp__(self, other):
        for i in xrange(min(len(self.string), len(other.string))):
            if self.string[i] > other.string[i]:
                return 1
            elif self.string[i] < other.string[i]:
                return -1
            else:
                continue
        if len(self.string) > len(other.string):
            return 1
        elif len(self.string) < len(other.string):
            return -1
        else:
            return 0
        # comapre between 2 strings
        
        
            
if __name__ == '__main__':
    f1 = MyFile(10)
    f2 = MyFile(20)
    f3 = MyFile(15)
    k = 10
    files = []
    for i in xrange(k):
        files.append(MyFile(3))
    str1 = "abcd"
    str2 = "abcf"
    # test = MyLine(str1)
    # __cmp__
    #print MyLine("abcz") < MyLine("abcd")
    
    # files
#     for f in files:
#         print '-'*20
#         l = f.nextline()
#         while l:
#             print l
#             l = f.nextline()
    print merge_karray(files)



'''
onsite:
1. given the intervals, find the largest interval and the maximum overlap interval 
2. culture fit
3. system design, design the msgs, what's app, wechat
4. living code
   give the file, which has
   > input:
   column1, column2
   "a",b
   "a,b","c/"f"
   > output:
   [{
   "column1":"a",
   "column2": "b"
   },
   { 
   "column1": "a,b",
   "column2": "c"f"
   }]
   
5. culture fit, and simple coding 
'''
