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
'''

'''
先是问了project，涉及很具体的算法和dataset处理之类；问了hadoop；
然后就是用coderpad考了一题OOD
Represent a deck of playing cards in an object-oriented design. 
(1) Write a function to output the deck. (2) Write a fn to shuffle the deck.
'''


'''
电话combination那道，算法很熟悉了，dfs，不过好长时间没做，边think aloud 边码，还算顺利
让自己弄几个test case 跑跑，但没有一次bug free，忘了考虑0，1的case ＝＝还有关于unsigned int 的warning
接着聊了聊怎么 code review，加一些comments啊什么的
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
subsetsI and subsetsII
search in rotated array
sprial matrix

2 Word Ladder II
以前只写过找所有path然后在dfs出最短path的解，烙印不让用，问有没有更好的方法
。。。我建了个Graph，用BFS+mp搜，磕磕碰碰写了个大概。。。
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
