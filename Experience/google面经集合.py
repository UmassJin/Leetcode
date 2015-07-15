'''
http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=135449&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26sortid%3D311

1. 两个链表 求最大的公共后缀
'''

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_max_postfix(head1, head2):
    if not head1 or not head2: return None
    head1 = reverse_linkedlist(head1)
    head2 = reverse_linkedlist(head2)
    dummy = ListNode(0)
    result = dummy

    while head1 and head2:
        if head1.value == head2.value:
            tmp = head1.next  # Note bug here, we need to save the tmp, otherwise, head1.next will become None ! 
            result.next = head1
            result = result.next
            result.next = None 
            
            head1 = tmp
            head2 = head2.next
        else:
            break
    
    return dummy.next
    
def reverse_linkedlist(head1):
    pre = None
    cur = head1
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur 
        cur = next
    return pre

def print_list(head):
    while head:
        print "head.val: ", head.value
        head = head.next 


'''
2. permutations of a list without adjacent equal elements
'''

import collections
import heapq

def permutation_number(s):
    counts = collections.Counter(s)
    heap = [(-count, key) for key, count in counts.items()]
    heapq.heapify(heap)
    output = []
    last = None
    while heap:
        minuscount1, key1 = heapq.heappop(heap)
        if key1 != last or not heap:
            last = key1
            minuscount1 += 1
        else:
            minuscount2, key2 = heapq.heappop(heap)
            last = key2
            minuscount2 += 1
            if minuscount2 != 0:
                heapq.heappush(heap, (minuscount2, key2))
        output.append(last)
        if minuscount1 != 0:
            heapq.heappush(heap, (minuscount1, key1))
    return ''.join(output)

test1 = 'aaabbbccc'
test2 = 'aaaaaaaabbbddd'
print permutation_number(test1)
print permutation_number(test2)


# Best Reference: http://stackoverflow.com/questions/25285792/generate-all-permutations-of-a-list-without-adjacent-equal-elements

'''
3. find h index element in the array, at least n elements in the arrary larger than n, but here is no n+1 elements larger than n+1
'''
def find_h_index(arr):
    n = len(arr) - 1
    start = 0; end = n
    distance = 0
    while start <= end:
        if end % 2 == 0:
            mid = (start + end) / 2
        else:
            mid = (start + end) / 2 + 1
        
        if arr[mid] >= (n - mid):
            distance = n - mid
            end = mid - 1
        
        elif arr[mid] < (n - mid):
            start = mid + 1
            
    return distance

test1 = [0,3,4,7,8,9,10]
test2 = [0,3,4,7,8,9]
test3 = [1]

print find_h_index(test1)
print find_h_index(test2)
print find_h_index(test3)

'''
具体思路如下，其实就是binary search。 首先根据start和end得出mid，看A[mid]值是否大于数组长度减去mid
(假设A.length-mid = distance），如果是那么distance有可能成为h index. 因为数组有序，如果distance小于A[mid]，
那么有distance个元素的值大于distance。 此时如果A[mid]值小于distance，那么继续向高位找，start=mid+1。
如果A[mid]值大于distance，那么继续向低位找end=mid-1。如果低位找到更大的distance，那么返回低位的，
如果低位没找到更大的，就返回现在的distance。
'''




'''
4. 给一个数，要求把这个数分解成一些平方数的和，并且要求使用最短的平方数list 如 13 = 9 + 4 而不是 13 = 4+4+4+1
'''
def min_square(n):
    dp = [0 for i in xrange(n + 1)]
    dp[0] = 0; dp[1] = 1
    
    for i in xrange(2, n+1):
        res = 1<<31 - 1
        for j in xrange(1, i):
            if j * j  > i:
                break
            else:
                res = min(res, dp[i - j*j] + 1)
        dp[i] = res
        print "dp[%d]: %d" %(i, dp[i])
    return dp[n]

n = 12
print min_square(n)


'''
第二问本质上是个DP题。思路如下，要求和为n的最小平方数序列，先求出和为1到n-1的最小平方数序列。然后从1到n的平方根之间寻找和为（n-i*i）的数的最短平方序列。1<i<sqrt(n)
例如求和为12的最短的平方 序列 
f（12） = 3*3 + f（3） f（3） = 1 + 1 + 1  i = 3 结果为 12 = 9 + 1 + 1 + 1
f（12）=  2*2+ f( 8 )   f( 8 ) = 4 + 4   i = 2 结果为 12 = 4 + 4 + 4
f（12） = 1*1 + f（11） f（11）= 9+1+1 结果为 12 = 9 + 1 + 1 + 1
最后正确结果为 12 = 4 + 4 + 4
'''

# http://www.mitbbs.com/article_t/JobHunting/32966491.html
'''
5. 一种encoding只有1 byte encode或者两byte encode两种形式，如果说第一byte的第一
个bit是0，那么这个bit开始的这个byte encode一个字符；如果第一个byte的第一位是
1，那么他一定是两个byte encode一个字符，并且他的第二个byte的首bit可以是1或者
0. 题目要求，给你一串encode，请问最后一个字符是一个byte encode的还是两个byte
encode的。不允许顺序parse bit串。
'''


// 末字节high bit为1，是非法单字节编码，所以必然是双字节编码
if (lastByte & 0x80 != 0) return DoubleByteEncoding;

// 末第二字节high bit为0，不带末字节混，所以末字节肯定是单字节编码
if (last2ndByte & 0x80 == 0) return SingleByteEncoding;

// 末字节high bit为0，末二字节high bit为1的情况，不能确定，需要检查末第三
if (last3rdByte & 0x80 == 0)
    return DoubleByteEncoding; // 末第3个高位0，不带末第2混，所以倒数2和1是
双字节码

if (last4thByte & 0x80 == 0) //末4不带末3混，末3和末2组成双字节，最末一个单了
    return SingleByteEncoding;
    
到此为止，不用再继续推理了，可以总结规律了：

if (n == 1) return 1;

// 末高位1，必然是双字节编码
if (bytes[n-1] & 0x80 != 0) return 2;
// 末高位0，需要倒着扫描
else {
    for (int i = n - 2; i --; i >= 0) {
      // 看到0，就可以确定答案了，因为0必然是一个编码序列的结尾，后面是11...
110
      // n - 1 - i是这个11...110的串的长度，如果是奇数，那么末字节单溜
      if (bytes[i] & 0x80 == 0)
         return 2 - (n - 1 - i) % 2;
      // 到了第1个字节，并且高位是1，那么11...110串的长度是n - i，包括当前字节
      if (i == 0)
         return 2 - (n - i) % 2;

      // else, 当前是字节高位是1，继续倒扫，直到看到0，或者扫描完
    }
}

'''
6. 题目： Given a rectangular grid of colored pixels and a particular 
pixel in the grid, find the perimeter of the same-colored blob containing that pixel.
补充一下，因为是求包含所给像素的图形的周长，所以就是DFS到每个相同颜色的邻接像素，然后检查这个像素周围四个像素的颜色，
如果颜色不同或者越界了，周长+1，否则就继续DFS到那个像素。最后得到周长

说是像素其实就是一个一个边长为1的正方形小格子，每个格子有一个颜色，所以就是从给定格子出发做DFS，直到抵达一个在边缘的格子
（也就是说这个格子周围四个方向有一个方向颜色不同或者越界），有几个边满足条件就加几
'''

def find_pixel(grid, pixel):
        if not grid or not grid[0]: return 0
        perimeter = [0]

        for i in xrange(len(grid)):
                for j in xrange(len(grid[0])):
                        if grid[i][j] == pixel:
                            find_pixel_helper(grid, pixel, i, j, perimeter) 
        return perimeter[0]

def find_pixel_helper(grid, pixel, x, y, perimeter):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != pixel:
                perimeter[0] += 1
                if x >= 0 and x < len(grid) and y>= 0 and y < len(grid[0]) and grid[x][y] == 'D':
                    perimeter[0] -= 1
                return
        grid[x] = grid[x][:y] + 'D' + grid[x][y+1:]  
        
        find_pixel_helper(grid, pixel, x+1, y, perimeter)
        find_pixel_helper(grid, pixel, x-1, y, perimeter)
        find_pixel_helper(grid, pixel, x, y+1, perimeter)
        find_pixel_helper(grid, pixel, x, y-1, perimeter)

grid = ['01100','00011','00011','01110','00000']
#grid = ['01100','00011']
print find_pixel(grid, '1')

'''
7. Median in stream data
'''

* [Median in Stream Data](https://github.com/UmassJin/Leetcode/blob/master/Experience/Median_in_stream_data.py)



'''
CTCI: from random5 to get random7
'''

import random

def rand5():
    return random.randint(0,4)

def rand7():
    num = 5 * rand5() + rand5()
    print num
    if num < 21:
        return num % 7

print rand7()


'''
8. Google Interview
from random2 to get random6
'''

# 思路:这道题的核心是保证产生random的概率一样，比如random7，则每个数字0到6产生的概率都为1/7,
# 对于random5来说，我们通过5*random5 + random5产生数字 0到24，然后取最小的3*7=21，所以取20
# 再mod7, 这里我们可以将random2先产生random4，然后通过random4产生

import random

def rand2():
    return random.randint(0,1)

def rand6():
    rand4 = 2*rand2() + rand2() 
    num = 4 * rand4 + rand4 # 0 to 9
    if num < 12:
        return num % 6

print rand6()

'''
9. 让你设计个matrix class，提供两个方法：update(x, y) & query(x1, y1, x2, y2)，update方法是update matrix上一个cell的值，
query方法是查询matrix上用(x1, y1)和(x2, y2)确定的矩形内所有值的总和。
有三种scenario，
第一种是update方法调用的次数远大于query方法的调用次数，
第二种是query方法的调用次数远大于update方法的调用次数，
第三种是两种方法调用次数一样多。
'''
'''
分析：
第一种情况，因为update次数多，那就不用对matrix做任何预处理，这样update是O(1)，query是O(N^2)。
第二种情况，因为query次数多，那就预处理一下matrix，新建一个辅助二维数组dp,使得dp[y][x]等于以(0,0)和(x,y)
两点确定的矩阵内的值的总和。这样update是O(N^2), query是O(1)
第三种情况，我们可以改变辅助二维数组dp的构成，使得dp[y][x]等于(0,y)到(x,y)的所有值的和，这样update是O(N)，query也是O(N)

这里可以考虑用segment tree(http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)
'''

'''
10. 题目是给一个string,一个set of string, 问string里面是否包含一个substring，使得这个substring的任意一个prefix + suffix能
组合成set里面的任意一个string，能就返回true，否则返回false
是这样，我少说了个条件，输入除了一个string和一个set of string,还有个整形变量len表示set里面每个string的长度（
也就是说set里的string长度都是一样的）。比如input string is "whoisyourdaddy", input set 包含两个 string "whu" and "ddy"，
那么function应该返回true，因为给的input string里面的substring "whoisyou" 的 prefix "wh" 和 suffix "u" 组成了 "whu"，
而另一个substring "daddy" or "ddy" 的 prefix "d" 和 suffix "dy" 组成了 "ddy"，因此这个例子里set里面所有的string都可以在
input string里面找到一个substring的一个prefix+suffix组合构成。
'''


'''
11. 给一个List，里面存着一些一个双向链表上的结点，这个List里面所有在双向链表上邻接的结点组成一个strong component，
求List里strong component的个数

给你个双向链表 1 <-> 2 <-> 4 <-> 7 <-> 9 <-> 11
给你个List里面有1,2,7,9,11, 那么 1,2组成一个strong component，7,9,11组成一个strong component。
解法就是建个HashSet然后把List里面的结点全丢进去，遍历一遍double linked List，遇到一个在HashSet里面的结点就从这个结点开始把所有
能到的在List里面的邻接结点从HashSet里面删掉，count++。换言之就是简易版的图遍历。
'''
class DoubleList_Node:
    def __init__(self, val = 0, pre = None, inext = None):
        self.val = val
        self.pre = pre
        self.next = inext

class Solution:
    def find_strong_comp(self, nodelist):
        if not nodelist: return []
        idict = { node.val: node for node in nodelist}
        count = 0

        for node in nodelist:
            if idict and (node.val in idict):
                tmp_pre = node.pre
                tmp_next = node.next
                while tmp_pre and (tmp_pre.val in idict):
                    del idict[tmp_pre.val]
                    tmp_pre = tmp_pre.pre
                while tmp_next and (tmp_next.val in idict):
                    del idict[tmp_next.val]
                    tmp_next = tmp_next.next
                del idict[node.val]
                count += 1
            elif not idict:
                break
        return count 
    
'''
test:
node1 = DoubleList_Node(2)
node2 = DoubleList_Node(3)
node3 = DoubleList_Node(5)
node4 = DoubleList_Node(7)
node5 = DoubleList_Node(9)
node6 = DoubleList_Node(8)
node7 = DoubleList_Node(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node2.pre = node1
node3.pre = node2
node4.pre = node3
node5.pre = node4
node6.pre = node5
node7.pre = node6

l = [node2, node1, node5, node4, node6, node7]
test = Solution()
print test.find_strong_comp(l)
'''


'''
12.
实现linux的diff命令，我就好好的问清楚了她期望的输入和输出，然后用java开始写，期间写遍历文件系统的function的时候一时半会想不起来java里相关的API了，
就跟妹子问咋办，妹子说不要求非要死记硬背API，你自己想想有什么API比较make sense的在白板上注明一下就行了，我正好这段时间上班就是写python干类似的事，
就一股脑把python的相关API在白板上注明出来，然后接着写代码。。写完后又大概跟妹子提了提如果给的路径下如果有symbolic link该怎么处理，妹子表示很满意。。
follow-up是怎么判断两个文件内容是否相同，文件太大怎么优化。.

第三题主要思路就是遍历两个输入路径，把路径树中的所有叶子结点找到（包括file和empty folder），把对应的相对路径拿出来放进对应的两个set里，
然后就是同时遍历两个set，找第一个set里没有的而第二个set里有的（+），以及第一个set里有的而第二个set里没有的（-），遇到相对路径相同的file
就转化为绝对路径读file content用md5算下hash value，比较看看内容是否一致。
'''


'''
13. 设计一个SparseVector class，包含set(long idx, int val), get(long idx), dotProduct(SparseVector otherVec)三个方法
'''


'''
14. 有一排数量无限的object，每个object有两个状态，可以用true和false来表示，object的状态是可切换的，初始情况下所有object的状态都是false。
让你设计一个class，实现两个方法：isToggled(long idx), toggle(long start, long end)。这题没记错的话之前面经里也出现过。我最后给出的方法是
维护一个list of intervals, 每次执行toggle时都要新加入一个新interval，然后把这个新interval merge进已有的interval list里面，这个解法的问题
在于实现起来非常复杂，因为做merge操作时你需要反转所有和新interval重叠的interval的状态，最后才把新interval里不重叠的部分加进list里面。最后
代码也没写完，但是写到中间我突然想起来之前看到一个面经里的比较类似的题，可以只记录每个object的toggle操作的次数，最后根据操作次数的奇偶来
判断object的状态，如此一来就不需要实际记录状态，只需要维护一个balanced interval tree，每次toggle就把新interval加进tree里，执行isToggled(long idx)时
计算所有包含给定idx的interval的数量就能决定对应的object的状态了。跟面试官提了提这个做法，面试官表示这就是他的解法，但是他觉得我给的解法也不错，
查询的复杂度要比他的方法低，就是难实现

不，面试官就是期待我提出这样的解法，他也说了如果写对应的代码的话不需要实现balanced interval tree，假设有这么个现成的数据结构给你用就行了。
因为interval tree不难写，但是balanced的就没那么好写了。。

https://github.com/UmassJin/Leetcode/blob/master/Algorithm/Segment_Tree.md

'''

'''
15. 设计一个random queue，支持push，pop，要求pop是random的
follow-up，每次push的时候会有相应的权重，要求pop按照权重random，换句话说，push 1,2,3，相应的权重1,2,3。那第一次pop需要保证1被pop的概率是1/6，
以此类推。有一个类似b+ tree的结构能解决follow-up。
'''

'''
16. 第二轮，偏向c++功底跟concurrency。实现memcopy，还有就是实现一个银行的类里面的几个算法，都很简单，但是对多线程调用的加锁需要有了解。
最后又问了一个实现每次调用，运行5秒，期间不停循环自增的简单算法，follow-up是如何应对系统管理员尴尬地恰巧在这段时间内改了系统时间。
'''


# http://www.1point3acres.com/bbs/thread-137081-1-1.html
'''
17. 
UTF8 validation
http://codereview.stackexchange.com/questions/59428/validating-utf-8-byte-array

0xxxxxxx  single byte
10xxxxxx  continous byte
110xxxxx  2 bytes sequence
1110xxxx  3 bytes sequence
11110xxx  4 bytes sequence
111110xx  5 bytes sequence
1111110x  6 bytes sequence
11111110  7 bytes sequence
11111111  8 bytes sequence
Valid    0xxxxxxx
Valid    110xxxxx 10xxxxxx
Valid    1110xxxx 10xxxxxx 10xxxxxx. 
Valid    0xxxxxxx 110xxxxx 10xxxxxx 0xxxxxxx
invalid  10xxxxxx
invalid  110xxxxx 0xxxxxxx 10xxxxxx
invalid  110xxxxx
'''

def validUTF8(data):
    if not data: return False
    
    size = 0
    for c in data:
        if size == 0 and c >> 7 == 0b0:
            continue
        elif size == 0:
            if c >> 5 == 0b110: size = 1
            elif c >> 4 == 0b1110: size = 2
            elif c >> 3 == 0b11110: size = 3
            elif c >> 2 == 0b111110: size = 4
            elif c >> 1 == 0b1111110: size = 5
            else:
                return False
        else:
            if (c >> 6) != 0b10:
                return False
            size -= 1
    return size == 0

data1 = [0b00000000] # T
data2 = [0b11011111,0b10000000] # T
data3 = [0b11011111,0b10000000,0b11000000] # F
data4 = [0b11011111,0b00000000, 0b10111111] # F
data5 = [0b00000000, 0b00011111, 0b11110111, 0b10111111,0b10111111] #F
data6 = [0b00000000, 0b00011111, 0b11110111, 0b10111111,0b10111111, 0b10000000] #T
print validUTF8(data1)
print validUTF8(data2)
print validUTF8(data3)
print validUTF8(data4)
print validUTF8(data5)
print validUTF8(data6)

# wiki: https://en.wikipedia.org/wiki/UTF-8#Description
# Reference: http://codereview.stackexchange.com/questions/59428/validating-utf-8-byte-array
# http://www.fgdsb.com/2015/01/10/valid-utf8/


'''
18.
Symetric rotation number boolean checkNum(String num)
ex: 16891 旋轉 180 以後還是 180 確認這個數有沒有符合這個規則
Follow Up: List<String> genNum(int len)

產生所有這個長度以下的所有組合
ex: len=3, {0,1,8,00,11,88,69,96,000,010,080,101,111,181,808,818,888,609,619,689,906,916,986}
'''

def rotation_number(number):
    if not number: return False
    idict = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
    n = len(number)
    left = 0; right = n - 1

    while left <= right:
        if number[left] not in idict or \
                number[right] not in idict:
                    return False
        if idict[number[left]] != number[right]:
            return False
        left += 1
        right -= 1
    return True


number1 = '8'
number2 = '7'
number3 = '609'
number4 = '321'
number5 = '916'
print rotation_number(number1)
print rotation_number(number2)
print rotation_number(number3)
print rotation_number(number4)
print rotation_number(number5)

'''
19. Followup question

思路：
奇数: 0, 1, 8
偶数：00, 11, 88, 69, 96
奇数：000, 010, 080, 101, 111, 181, 808, 818, 888, 609, 619, 689.....
偶数：0000, 0110, 0880, 0690, 0960, 1001, 1111, 1881, 1691, 1961, 8008, 8118, 8888, ......

奇数可以通过偶数加0, 1, 8 得到
偶数则可以通过加上00, 11, 88, 69, 96得到
'''
def find_rotate_number(n):
    if n < 1: return []
    res = []; pre = ['']
    list1 = ["0", "1", "8"]
    idict = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
    i = 1
    while i < n + 1:
        cur = []
        if i % 2 == 1:
            if pre == ['']:
                cur = list1
            else:
                for num in pre:
                    for digit in list1:
                        index = len(num)/2
                        newnum = num[:index] + digit + num[index:]
                        cur.append(newnum)
        elif i % 2 == 0:
            for num in pre:
                for digit in idict:
                    newnum = digit + num + idict[digit]
                    cur.append(newnum)
            pre = cur
        res.extend(cur)
        i += 1
    return res

print find_rotate_number(4)



'''
20. The pattern could be across the given set of strings.
只要他給的 pattern 在連續的 strings 可以組合起來成為 pattern string, return true-google 1point3acres

ex:
pattern: "horse"
strings: ["ah", "or", "settle"]

boolean contains(String pattern, Iterable<String> strs)
pattern: "abc"
strs : "ab", "cd"  -> true
strs : "aa", "bcd" -> true
strs : "ab", "ac"  -> false
'''


'''
21. Leetcode: count islands
-google 1point3acres
後面的 follow up 都是討論而已, 沒寫 code
Follow up: 如果是大地圖怎麼處理, 要你切 map, 考慮每個 submap 之間的關係. 
Follow up2: 平行化處理, 這個條件, 可能會讓你前面所想方法要重新思考

這時剩下15分鐘, 他就說再來個 follow up 好了 = =, 跟大圖無關, 一樣是 count island, 假設已經做了第一次的處理
Follow up3: 如果他現在要新增島到地圖上, 請回傳最新的 count
ex: int add(int x, int y), the function should return the new count

Follow up3.1 這個 function 能不能做到比 O(N*N) 還要好? (N為 map 邊長)

最後結束的時候, 他有跟我說解法, 就是當初在 count islands 的時候把每個 island 都建成一顆 tree
所以再判斷新加上去的 island 周圍的時候, 只要判斷周圍的 island 是不是有 common ancestor O(lgN)
如果是分開的兩個島, 現在被新的島串起來了的話, 就將兩顆 tree 接起來就好

思路[转发]：
本帖最后由 stellari 于 2015-6-29 20:44 编辑


今天在Lintcode上刷到Number of Islands II这道题，发现恰好和前两天面经版的一个Youtube面试出现的题的follow up是相同的。在网上简单搜了一下并没有看到关于这道题的详细解法，所以自己写了一个，分享给大家。

原题是这样的：

----------------------
Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.

Example 

Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].

return [1,1,2,2].

Note 

0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent
复制代码

大意就是在一个由grid组成的海洋上，每次将一个方格从海洋改变成陆地。在每次完成这个操作后，都要得到此时的岛屿数目。
--------------------

这实际上就是要动态维护一个图的Connected Component。这是并查集(Union-find set)的典型应用。所谓并查集，就是满足下列特征的数据结构：

1. 能表示一组不相交的集合，比如{{1, 2, 3}, {4, 5}, {6}, {7}}；
2. 最少支持以下三个操作:
    make-set(v): 加入一个新的集合，其中只有一个元素v。
    find(v): 给定元素v，查询v在哪一个集合当中。
    union(v1, v2): 给定元素v1和v2，将它们所在的集合合并为一个。

并查集通常用树形结构来表示。每一个集合是一棵多叉树，所以一组不相交集合构成了一个“forest”。比如{{1, 2, 3}, {4, 5}, {6}, {7}}这组不相交集合，可以用四棵树来表示:
   
   1           4       6         7
  / \         / 
  2   3      5
复制代码
其中每棵树的root可以是这个集合中的任意元素（一般是第一个加入该集合的元素）。其他元素都是root的子node，或子node的子node……等等。

我们可以用root来代表集合本身。这样，当给定树中的任何一个节点，我们就希望能够快速地找到这个节点所在的集合，也就是树的root。所以，每个节点必须储存它的parent节点。但是反过来，我们不需要在已知root的情况下，查找树中的一个节点，所以并不需要储存child节点。也就是说，并查集树和普通的树恰好相反。

这样的话，find函数就很容易写了
find(v)
  while (v is not root) 
        v = v->parent
  return v
复制代码
至于union函数，我们可以先找到两个节点所在的树的root，然后把较浅的树插入到较深的树中去。这样做的原因是希望得到的树能尽量平衡。为此，我们在每个节点中保存“以这个节点为root的树的深度”。如果树中只有root一个元素时，深度为0。

综合上述讨论，并查集树节点定义如下：
struct DJSetNode{
  int rank;
  DJSetNode* parent;
  DJSetNode(int r, DJSetNode* parent): 
        rank(r), parent(p) 
  {}
};
复制代码
这里的rank就是深度。之所以不叫“depth”，是因为以后我们可以对上述的并查集实现做进一步优化，称为Path Compression（本文不作讨论）。在作完这步优化以后，这个rank就和深度不对应了。

union函数可以实现如下：
union(v1, v2)
  root1 = find(v1)
  root2 = find(v2)
  if (root1 is root2) 
    return root1
  if (root1 has lower rank) 
    root2.parent = root1
    return root1
  else if (root2 has lower rank)
    root1.parent = root2
    return root2
  else // root1 and root2 have same depth
    root2.parent = root1
    root1.rank ++
    return root1
复制代码
----------------

在本题当中，我们可以将创建一个M x N的数组SEAMAP，类型为DJSetNode*。每次将一个坐标点(i, j)位置设为陆地时，我们做3件事：

1. 创建一个新的DJSetNode对象N
2. 将N作为一棵孤立的树插入到forest当中
3. 让SEAMAP[i, j]指向N

然后，我们查询SEAMAP[i, j]的四个邻位置。如果其中某些位置的值不为NULL，那么说明这里已经存在有岛屿，那么我们将N与那些位置所在的集合合并即可。对于四个邻位置，我们最多只要进行四次union操作即可。合并完成之后，forest中剩余的孤立树的个数即为孤立岛屿的个数。

由于并查集树都是平衡树，所以find和union都有O(logn)复杂度（其中n为岛屿位置的个数）。也就是说每添加一块岛屿，都仅需要O(logn)时间。

------------------
代码如下:
struct DJSetNode {
    int label;  // 保留字。本程序中并未用到。
    int rank;   // 在本程序中就是树的深度。
    DJSetNode* parent;
    DJSetNode(int lb, int r, DJSetNode* p): label(lb), rank(r), parent(p) {}
};
class Solution {
    unordered_set<DJSetNode*> forest;   // 包含当前所有树的根
    
    // MAKESET: 产生一个仅含一个元素的set，并将其作为一棵树加入forest
    DJSetNode* makeSet() {
        DJSetNode* cur = new DJSetNode(0, 0, nullptr);    
        forest.insert(cur);
        return cur;
    }

    // FIND: 给定任意一个元素，找到这个元素所在树的root
    DJSetNode* find(DJSetNode* n) {
        if (n == nullptr) return nullptr;
        while (n->parent) {
            n = n->parent;
        }
        return n;
    }

    // MERGE: 给定两个元素，合并这两个元素所在的树，并返回合并后树的root
    DJSetNode* merge(DJSetNode* n1, DJSetNode* n2) {
        DJSetNode* r1 = find(n1);   // 分别找到两元素所在的树的root
        DJSetNode* r2 = find(n2);
        if (r1 == r2) {             // 如果本来就在同一树，则不做任何事
            return r1;
        }

        if (r1->rank > r2->rank) {  // 如果树1的“深度”大于树2，
            r2->parent = r1;        // 则以树1为基础合并
            forest.erase(r2);       // 然后从forest中除去树2
            return r1;              // 这是为了保证合并后树的深度尽可能小
        }
        else if (r1->rank < r2->rank) { // 反之则以树2为基础合并，
            r1->parent = r2;
            forest.erase(r1);
            return r2;
        }
        else {                      // 若深度相同，则任选一树为基础合并
            r2->parent = r1;        // 此处选为树1
            forest.erase(r2);
            r1->rank++;             // 合并以后，树1的深度增加了1
            return r1;
        }
    }

    int add(const Point& p) {
        vector<DJSetNode*> nbs;     
        // 查看当前位置的四个邻点，如果为island，则将其加入队列
        if (p.x > 0 && seaMap[p.y][p.x-1]) nbs.push_back(seaMap[p.y][p.x-1]);
        if (p.y > 0 && seaMap[p.y-1][p.x]) nbs.push_back(seaMap[p.y-1][p.x]);
        if (p.x < NC-1 && seaMap[p.y][p.x+1]) nbs.push_back(seaMap[p.y][p.x+1]);
        if (p.y < NR-1 && seaMap[p.y+1][p.x]) nbs.push_back(seaMap[p.y+1][p.x]);

        DJSetNode* cur = makeSet(); // 先把当前加入的点看做一个新的孤立岛屿。
        seaMap[p.y][p.x] = cur;     // 

        for (int i = 0; i < nbs.size();++i) {
            cur = merge(cur, nbs[i]);   // 将这个岛屿分别与周围的邻岛合并
        }
        return forest.size();       // 此时forest中的tree数就是孤立岛屿的数目
    }
public:
    vector<vector<DJSetNode*> > seaMap;
    int NR, NC;
    vector<int> numIslands2(int n, int m, vector<Point>& operators) {
        seaMap = vector<vector<DJSetNode*> >(m, vector<DJSetNode*>(n, nullptr));
        NR = m, NC = n;

        vector<int> res;
        // 
        for (int i = 0; i < operators.size(); ++i) {
            int a = add(operators[i]);
            res.push_back(a);
        }
        return res;
    }
};
复制代码
------------------------------



# http://www.1point3acres.com/bbs/thread-137081-1-1.html
# http://www.1point3acres.com/bbs/thread-137243-1-1.html
'''


'''
# http://www.1point3acres.com/bbs/thread-120307-1-1.html
22. 
感觉稀里糊涂的，问了一个现在工作的问题，就接着问了一个coding的题目：
实现一个Map，带有getRandomValue的方法，要求所有put，get，remove，getRandomValue都必须是O(1)

在其中一个关键细节上卡了将近20分钟，中间面试官各种提示都没点醒问我，最后25分钟左右搞定，
但是好像和面试官的思路还是不一样。面试官没有再问其他问题，不知道是不是因为我太慢了。
# http://www.careercup.com/question?id=11353907
'''

class GetRandom:
    def __init__(self):
        self.idict = {}
        self.array = []

    def insert(number):
        if number not in self.idict:
            self.array.append(number)
            index = self.array.index(number)
            self.idict[number] = index

    def remove(number):
        if number in self.idict:
            index = self.idict[number]
            if index != len(self.array)-1:
                self.array[len(self.array)-1], self.array[index] = \
                        self.array[index], self.array[len(self.array)-1]
                idict[self.array[index]] = index
                del self.array[len(self.array)-1]
            del self.idict[number]
            
    def getRandom():
        randomnumber = random.randint(0, len(self.array)-1)
        return self.idict[randomnumber]
        
# Some question:
# 1) How could we handle duplicate number ?
# 2) How could we ensure the insert sequence of the element ?
# Discussion: http://www.careercup.com/question?id=11353907

'''
23. surpass count
Inversion Count for an array indicates – how far (or close) the array is from being sorted. 
If array is already sorted then inversion count is 0. 
If array is sorted in reverse order that inversion count is the maximum. 
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
# http://www.geeksforgeeks.org/counting-inversions/
'''

'''
similar: Maximal Surpasser Count Problem
输入一个数组，返回数组元素的surpasser个数的最大值。
数组元素a[i] 的surpasser是指元素a[j], j > i， a[j] > a[i]。
比如[10, 3, 7, 1, 23, 14, 6, 9] 这个数组中10的surpasser是23,14，个数是2。
而3的surpasser是7,23,14,6,9，个数为5，并且是最多的一个。所以返回5。
# http://www.fgdsb.com/2015/01/11/maximal-surpasser-count/

'''

def merge_sort(array):
    if not array: return None
    n = len(array)
    result = [0 for _ in xrange(n)]
    return rec_mergesort(array, result, 0, n-1)

def rec_mergesort(array, result, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) / 2
        inv_count = rec_mergesort(array, result, left, mid)
        inv_count += rec_mergesort(array, result, mid+1, right)
        inv_count += merge(array, result, left, mid+1, right)
    return inv_count

def merge(array, result, left, mid, right):
    i = left; j = mid 
    k = left
    inv_count = 0
    
    while (i < mid) and (j <= right):
        if array[i] <= array[j]:
            result[k] = array[i]
            i += 1
        else:
            result[k] = array[j]
            j += 1
            inv_count += mid - i
        k += 1
        
    while i < mid:
        result[k] = array[i]
        k += 1
        i += 1
    
    while j <= right:
        result[k] = array[j]
        k += 1
        j += 1
    
    k = left
    while k <= right:
        array[k] = result[k]
        k += 1
    return inv_count 

array = [1,20,6,4,5]  # output: 5
array = [2,4,1,3,5]   # output: 3
print merge_sort(array)


'''
# http://www.1point3acres.com/bbs/thread-121729-1-1.html
24. 第二轮，面的人是华裔小哥，人很喜感也挺nice，也是一上来做题。题目是给你一个positive的值K，然后按照fraction的值的小到大输出所有n/d, 
其中1<=d<=k, 0<=n<=d，还有一个要求输出的fraction不能有duplicate，比如1/2和2/4是duplicate，这种情况只要输出1/2。我用了一个hashtable来
处理duplicate的情况, fraction的实际小数的值对应其输出string，比如0.5对应1/2，因为输出要按从小到大顺序，所以还用了个arraylist存实际小
数的值，最后对这个List排了下序，然后结合hashtable和list输出最后结果。然后问时间复杂度，follow up，如果规定只想要输出某个数值区间的
fraction怎么办，数学的一些东西，算下值范围就好了，还问了这种情况的复杂度。
'''



'''
25. Google 电面
比较BST和hash table的优缺点
'''
# https://github.com/UmassJin/Leetcode/blob/master/Algorithm/HashTable_Implement.md


'''
26. detect cycle in a given tree, valid Tree.
Union-Find Algorithm: 详见21题
''' 
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
                self.rank[x] += 1

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


'''
27. give a float array and the weight for each array element write a function to generate each element probablistically based on the weight, 
这道题followup略难，根据weigt优化算法没答出来，最后问了面试小哥，要用Heap，想想也make sense，开始自己想到用heap但是小哥一直提示把我给带跑了。

类似的题目:
设计一个random queue，支持push，pop，要求pop是random的
follow-up，每次push的时候会有相应的权重，要求pop按照权重random，换句话说，push 1,2,3，相应的权重1,2,3。那第一次pop需要保证1被pop的概率是1/6，以此类推。
有一个类似b+ tree的结构能解决follow-up。

事实证明这道题很tricky，直接上vector，每次先跟最后swap再pop_back()就好了。。。
'''

'''
28. 一道面经题2D sparse matrix, how to get the number of 1's in constant time given two coordinate
'''


'''
29. 设计合并若干个字符串到一个字符串的encoding算法与对应的decoding算法
'''
def encode_strings(str_list):
    if not str_list: return ""
    result = ""

    for s in str_list:
        n = len(s)
        result += str(n) + '#' + s
    return result

def decode_strings(string):
    if not string: return ""
    result = []
    while len(string) > 0:
        index = string.index('#')
        length = int(string[index-1]) 
        substr = string[index+1: index+length+1]
        result.append(substr)
        string = string[index+length+1:]
        print "string: ", string
    return result

test = ['hello','world','how','are','you']
result =  encode_strings(test)
print result
print decode_strings(result)


'''
31.给int n，求n所有factors，然后问问算法的running time
# http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
'''

def find_factor(x):
    result = set()
    i = 1
    while i * i <= x:
        if x % i == 0:
            result.add(i)
            result.add(x//i)
        i += 1
    return result
    
print find_factor(4)
print find_factor(8)
print find_factor(18)

[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python find_factor.py
set([1, 2, 4])
set([8, 1, 2, 4])
set([1, 2, 3, 6, 9, 18])


'''
follow up
32. 接下来就是第一题的follow up，给distinct primes list，回传所有由这些primes组成的数字。再follow up，那给的primes有重复呢？
原本题是n=20，回传{1, 2, 4, 5, 10, 20}；后面两道题是给你{2, 5}，回传{1, 2, 5, 10}，或是primes有重复，例如给你{2, 2, 5}，
回传{1, 2, 4, 5, 10, 20}
# 原题链接: http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=134582&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
# Analysis: http://www.fgdsb.com/2015/01/17/factors-of-product-of-distinct-primes/
'''
# None-duplicate input 
def all_factors(primes):
    result = []
    dfs(result, primes, 0, 1)
    print result

def dfs(result, primes, i, cur):
    if i == len(primes):
        result.append(cur)
        return
    dfs(result, primes, i+1, cur)
    dfs(result, primes, i+1, cur*primes[i])
     
     
test = [2,3,7]
all_factors(test)

test1 = [2,3,5]
all_factors(test1)

# Duplicate input

# 通过一个pre来记录之前的数字primes，比如对于input[2,2,5]来说
# 1 --- 1 (not use primes[0])
#   ---- 1*2 (use primes[0])   
# 1*2 --- 1*2 (not use primes[1])
#     ---- 1*2*2 (use primes[1])


'''
follow up: 
33. Efficient program to print all prime factors of a given number
http://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
'''

def find_prime_factor(x):
    result = set()
    while x % 2 == 0:
        result.add(2)
        x = x / 2
    i = 3
    while i * i <= x:
        while x % i == 0:
            result.add(i)
            x = x / i
        i += 2
        
    if x > 2:
        result.add(x)
    return result


print "prime factor:"
print find_prime_factor(8)
print find_prime_factor(9)
print find_prime_factor(11)
print find_prime_factor(121)
print find_prime_factor(315)


'''
34. 两个input，第一个是一个机器的total_mem，第二个是一堆job，每个job包含starting_time，duration，mem_needed，mem_needed就是说这个工作需要这么多的memeory。
要求是输出bool，表示是否在任意时间内，所有重叠工作的memory总和都不能超过total_mem。也就是测试这个机器的total_mem够不够大。
# 原题：http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=116931&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
'''
首先其实这个内存使用变化是离散的，就是说类似一个直方图，而不是抛物线。
一个job变成两个事件点
Event{
    bool is_in;
    int time;
    int mem_used;
}

比如job 从 0开始 10结束，用了200mem
Event{true,0,200}, Event{false,10,200}.
按照time排序，time相同，is_in = false的优先。

然后你扫过去， is_in=true的你就加mem,is_in=false的你就-mem.每个事件点，你会加或减一次，每加或减一次后，就check是不是超过总的。
你要保证end的先减。否则你会误以为交界点超载

'''
Similar problem in G4G
http://www.geeksforgeeks.org/weighted-job-scheduling/
35. Weighted Job Scheduling 
Given N jobs where every job is represented by following three elements of it.
1) Start Time
2) Finish Time.
3) Profit or Value Associated.
Find the maximum profit subset of jobs such that no two jobs in the subset overlap
注意，这里是不允许有overlap 的
'''

# 思路：
DP + binary search 
http://www.fgdsb.com/2015/01/03/non-overlapping-jobs/
1. first, sort each job based on the finish time
2. maintain the dp[i], which means the max profit for the jobs till arr[i] (arr[i] included)
3. initialization: dp[0] = arr[0].profit
4. state: 
    for i in xrange(1, n):
        # calculate include this job, the max value
        include_profit = arr[i].profit
        l = latestNonConflict_job(arr, i)  # find the latest non-conflit previous job, if not, return -1
        if l != -1: 
            include_profit += table[l]
        # calculate exclude this job, and find the max value 
        table[i] = max(include_profit, table[i-1])
    return table[n-1]
    

    
    
'''
36. input: 一个文件，包含了很多单词，可以全部装入内存一个target number
output： 一个单词的最小set，这些单词的出现的频率的总和大于等于t
比如，文件中 A 500次，B 300, C 200, D100, t = 1000.  结果为 A，B, C. 
实际上就是求频率最高的一些单词，这个单词的总频率大于target。 我用了selection algorithm去解决的这个问题
# http://www.1point3acres.com/bbs/thread-131722-2-1.html
'''
# Use quick select (O(n))
# https://github.com/UmassJin/Leetcode/blob/master/Algorithm/Quick_Select.md


'''
37. 题目就是设计一个RMQ(http://en.wikipedia.org/wiki/Range_minimum_query) (我也是后来才知道这是RMQ的)
'''
# https://github.com/UmassJin/Leetcode/blob/master/Algorithm/Segment_Tree.md

'''
38. 找出一个树是另一个树的子树
# http://www.geeksforgeeks.org/check-if-a-binary-tree-is-subtree-of-another-binary-tree/
# http://www.geeksforgeeks.org/check-binary-tree-subtree-another-binary-tree-set-2/
'''
# O(n) algorithm

# method 1
def check_subtree(tree1, tree2):
    if not tree1: return False
    if not tree2: return True

    if identical_tree(tree1, tree2):
        return True

    return identical_tree(tree1.left, tree2) or \
            identical_tree(tree1.right, tree2)

def identical_tree(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False

    return tree1.val == tree2.val and \
            identical_tree(tree1.left, tree2) and \
            identical_tree(tree1.right, tree2)
    
# method 2    
# Use the inorder and preorder/postorder equal to determine 
def preorder(root):
    result = []
    queue = [root]
    while queue:
        node = queue.pop()
        result.append(node.val)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    result.append('#')
    return result
    
def inorder(root):
    result = []
    queue = []
    node = root
    while True:
        while node:
            queue.append(node)
            node = node.left
        if not queue:
            break
        node = queue.pop()
        result.append(node.val)
        node = node.right  
    result.append('#')  # Check the special case 
    return result

def check_subtree(tree1, tree2):
    pre_array1 = preorder(tree1)
    pre_array2 = preorder(tree2)

    in_array1 = inorder(tree1)
    in_array2 = inorder(tree2)

    return check_strstr(pre_array1, pre_array2) and \
            check_strstr(in_array1, in_array2)

# here use KMP algorithm to check the strstr

# we need to add '#' at the end of the preorder and inorder result 
# for the following special case 
'''
        Tree1
          x 
        /    \
      a       b
     /        
    c         


        Tree2
          x 
        /    \
      a       b
     /         \
    c            d
'''

'''
39. Write a function to get a positive integer n as input and return 0 or 1. The probability of returning 1 should be 1/(2^n)
G家的题。因为是1/2^n，那么执行最多n次rand() % 2即可。连续n次随机到0的概率就是1/(2^n)，中途只要随机到1就立即返回0即可。
# http://www.fgdsb.com/tags/Random/
'''
import random
def random01(n):
    for i in xrange(n):
        if random.randrange(2) == 1:
            return 0
    return 1

print random01(2)

'''
40.给一个Quack的类，里面有三个方法：
pop(): 随机从头或者尾扔出一个元素；
peek(): 随机看头或者尾的一个元素，peek()之后pop()的话一定会pop()出peek()的那个元素；
push(): 向尾部插入一个元素

问题是：给一个排序好的Quack,怎么把里面的元素原封不动的放到一个Array里面。
Follow up：如果quack里面有重复的元素，怎么处理。


对于不重复元素的情况，用queue存小的数，stack存大的数，先pop()一个数，再peek一下，比较这两个数，如果pop的大，
就代表肯定是quack的尾巴，反之肯定是头，然后插入queue或者stack就行了。这里假设quack有empty方法。
'''

from collections import deque

def recover_quack(quack):
    queue = deque()
    stack = []
    result = []

    while not quack.empty():
        number1 = quack.pop()
        if quack.empty():
            queue.append(number1)
            break

        number2 = quack.peek()
        if number1 > number2:
            stack.append(number1)
        else:
            queue.append(number1)

    while queue:
        result.append(queue.popleft())

    while stack:
        result.append(stack.pop())

    return result
    
'''
41. Random Node in A Binary Tree
Random return one node in the binary tree
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self):
        self.root = TreeNode(0)
        
    def choose_random(self):
        result = [None]
        self.choose_random_helper(self.root, 1, result)
        print "result: ", result
        return result[0].value

    def choose_random_helper(self, node, idx, result):
        if not node: return 
        print "idx: ", idx 
        if random.randrange(idx) == 0:
            result[0] = node
        
        self.choose_random_helper(node.left, idx+1, result)
        self.choose_random_helper(node.right, idx+1, result)
        
        
tree = Tree()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
tree.root.left = node1
tree.root.right = node2
tree.root.left.left = node3
tree.root.left.right = node4
print "tree: ", tree.root.left.left.value
print tree.choose_random()

'''
42. Implement rand10() with rand7()
'''
import random

def random7():
    return random.randrange(7)

def random10():
    tmp = 7 * random7() + random7()
    if tmp <= 40:
        print tmp % 10
    

'''
43 Minimum Sum of Manhattan Distance
已知平面(m*n)上有k个点，找到其中某个点P，使得P到其余所有点的Manhattan距离之和最短并求出这个最短距离。
# http://www.jiuzhang.com/problem/30/
O(klogk), k is the number of points in matrix, the time complexity of sort

follow up question:
如果要求这个点与所给的k个点不重合，该怎么办？

进阶：通过初阶的算法得到一个最优位置，如果这个位置与k个点重合，则从这个位置开始进行搜索，
将这个点周围的点和对应的距离放入到一个堆里，每次从堆中取出最小距离的点，然后将这个点周围的点放入堆中，
直到取出的点不与所给k个点重合。时间复杂度klogk，因为最多从堆中取出k+1个点即可找到一个不与所给k个点重合的点。堆每次操作为logk。

本题的最优算法较难想到。所以如果公司要求不高，答出O(nm)的方法即可。O(nm)的方法是因为假设我们知道在(x,y)这个位置的距离和为S，
那么当(x,y)移动到(x+1,y)和(x,y+1)的时候，我们可以在O(1)的时间更新S。方法是预处理每一行上方/下方有多少个k个点中的点，
每一列左侧/右侧有多少个k个点中的点。上面的解答基于nm>>klogk，如果k比较大，则还是O(nm)的方法更好。答题时需要答出对于给定参数
不同情况下采用不用算法这一点。
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def min_distance(pts):
    pts = sorted(pts, key = lambda x: x[0])
    x_sum = mht_sum(pts, True)
    
    pts = sorted(pts, key = lambda x: x[1])
    y_sum = mht_sum(pts, False)

    result = -1 << 31
    for i in xrange(len(pts)):
        result = min(result, x_sum[(pts[i].x, pts[i].y)] + y_sum[(pts[i].x, pts[i].y)])
    return result

def mht_sum(pts, get_x):
    n = len(pts)
    left = [0 for _ in xrange(n)]
    right = [0 for _ in xrange(n)]
    
    isum = 0
    for i in xrange(n):
        left[i] = isum
        isum += pts[i].x if get_x else pts[i].y
        
    isum = 0
    for i in xrange(n-1, -1, -1):
        right[i] = isum
        isum += pts[i].x if get_x else pts[i].y
        
    # calculate xi isum
    # (xi - x(i-1)) + (xi - x(i-2)) + ... + (x(i+1)-xi) + x(i+2)-xi..
    # i * xi - left[i] + right[i] - (n-1-i) * xi
    result = {}
    for i in xrange(n):
        p = pts[i].x if get_x else pts[i].y
        result[(pts[i].x, pts[i].y)] = p * i - left[i] + right[i] - (n-1-i) * p
    return result

'''
44. wiggle sort
对数组排序，使得 a1 <= a2 >= a3 <= a4 >=...
'''
# https://github.com/UmassJin/Leetcode/blob/master/Experience/wiggle_sort.py


'''
45. Intersection of Two Quadtrees
'''


'''
46. Peek Iterator 
写一个PeekIterator，包装一个普通的Iterator，要实现peek()方法，
返回当前iterator指向的元素，但是不能移动它。除此之外也要实现has_next()和next()方法。
# http://stackoverflow.com/questions/2425270/how-to-look-ahead-one-element-in-a-python-generator
# http://anandology.com/python-practice-book/iterators.html
# https://docs.python.org/3/tutorial/classes.html#iterators
'''

class generator:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def next(self):
        if self.has_next():
            i = self.i
            self.i += 1
            return i
        else:
            print "there is NO next value."
            return None
            #raise StopIteration()

    def has_next(self):
        if self.i >= self.n:
            return False
        else:
            return True

class PeekIterator:
    def __init__(self, generator):
        self.peek = []
        self.generator = generator

    def __iter__(self):
        return self

    def get_peek(self):  # Previous there is the error here since peek() function is duplicate with self.peek
        if self.peek == []:
            if self.has_next():
                cur = self.generator.next()
                self.peek.append(cur)
                print "cur: ", cur
                return cur
        else:
            return self.peek[-1]

    def has_next(self):
        if not self.generator.has_next() and not self.peek:
            return False
        else:
            return True

    def get_next(self):
        if not self.peek:
            if self.has_next():
                return self.generator.next()
        else:
            ret = self.peek[-1]
            self.peek.pop()
            return ret

gen = generator(5)
test = PeekIterator(gen)
print test.has_next()
print test.get_next()
print test.get_next()
print "peek: ", test.get_peek()
print test.get_next()

# Output: 
[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python iterater.py 
True
0
1
peek:  2
2


'''
47.写一个变形的iterator，给定两个iterator，让两个iterator进行交互输出。
例子：
A: 1234
B: abcd
则输出为：1a2b3c4d，如果一个读完了那就读没读完那个直到两个都读完为止。
G家电面题，又是iterator系列。很简单，但是尽量写的容易扩展一些，因为interviewer很可能会让你扩展到k个iterator的情况。
# http://www.fgdsb.com/2015/01/30/zigzag-iterator/
'''

import random

class generator:
    def __init__(self, n):
        self.n = n
        self.i = random.randrange(n)
        self.start = self.i
        print "self.start: ", self.start

    def __iter__(self):
        return self

    def next(self):
        if self.has_next():
            i = self.i 
            self.i += 1
            return i 
        else:
            print "there is NO next value."
            return None
            #raise StopIteration()
    
    def has_next(self):
        if self.i >= self.start + self.n:
            return False
        else:
            return True 

class ZigzagIterator:
    def __init__(self, g1, g2):
        self.its = [g1, g2]
        self._pointer = 0 if g1.has_next() else 1

    def get_next(self):
        ret = self.its[self._pointer].next()
        pre = self._pointer
        if self.its[self._pointer].has_next() and self._pointer == pre:
            self._pointer = (self._pointer + 1)%2
        return ret     

    def has_next(self):
        return self.its[self._pointer].has_next()


# test
t1 = generator(5)
t2 = generator(5)
test = ZigzagIterator(t1, t2)
print test.get_next()
print test.get_next()
print test.get_next()
print test.get_next()
print test.get_next()
print test.get_next()
print test.get_next()
print test.get_next()
print test.get_next()
print test.get_next()
print test.has_next()

# output
[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python iterater.py
self.start:  3
self.start:  3
3
3
4
4
5
5
6
6
7
there is NO next value.
None
False


'''
48. We have a schedular. Timer is available to the schedular. The clients of this schedular want to call this schedular with 2 parameters, 
1) time interval in ms 2) callback function. The schedular will invoke specified callback function after specified time intevals. 
Design data structure and implement it. 

这个函数的功能是用一个绝对时间点注册一个callback function。这个时间点你可以认为就是time(NULL)的返回值。当时间到时，系统会自动调用这个callback。
如果这个absolute_time是现在或者已经过去，那么立即调用它。但是系统同时只能注册一个callback，如果你调用这个函数多次，只有最后一次的才有效。

Analysis:

G家电面题，题目的思路是按照时间点的顺序来维护一个数据结构。每次调用一个回调时，将自动注册下一个。
比如现在有3个callback，按时间排序如下：
func1 -> func2 -> func3
首先注册func1，时间到时，系统调用func1。然后同时注册func2，以此类推。
那么只需要把传进来的callback做一次封装即可，当调用完毕后，我们需要做一个额外操作，也就是注册下一个callback。
因为要按照时间有序排列，我们需要一个map，以时间点为key。
'''

class CallBack:
    def __init__(self):
        self.record = {}
        self.current_timer = (1 << 31)-1

    def wrapper(self):
        self.record[self.current_timer]()
        del self.record[self.current_timer]

        if self.record:
            self.current_timer = self.record.keys()[0]
            register_system_timer_callback(self.current_timer, wrapper)

    def register_system_timer_callback(self, relative_time, callback):
        if relative_time == 0:
            callback()
            return
        cur_time = time.time()
        record[cur_time + relative_time] = callback
        if (cur_time + relative_time < self.current_timer):
            self.current_timer = cur_time + relative_time
            register_system_timer_callback(self.current_timer, wrapper)

'''
49. given a full binary tree, please write a function to encode the shape of the tree. Using the result that you get from part I to reconstruct the tree. 
You should use as little space as you can to reconstrcut it.
Generall Tree serialization 
https://github.com/UmassJin/Leetcode/blob/master/LintCode/Binary%20Tree%20Serialization.py
http://www.1point3acres.com/bbs/thread-131485-1-1.html
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.index = 0

    def serization(self, root):
        if not root: return None
        ret = 0
        queue = [root]
        while queue:
            node = queue.pop()
            ret <<= 1
            if node.left and node.right:
                ret |= 1
                queue.append(node.left)
                queue.append(node.right)
        return ret

    def deserization(self, array):
        if not array: return None
        bit_array = []

        while array:
            digit = array & 1
            bit_array.insert(0,digit)
            array >>= 1
        root = TreeNode(0)
        queue = [root]
        for bit in bit_array:
            if bit == 1:
                node = queue.pop(0)
                node.left = TreeNode(0)
                node.right = TreeNode(0)
                queue.append(node.left)
                queue.append(node.right)
            elif bit == 0:
                queue.pop()
        return root
~                    

'''
50. 要求实现对于一个window_size， 不停插入值，返回当前的平均数，
如果输入没有达到window_size则输出所有数的平均值，达到后踢掉最早的输入输出最新的平均值。
例子：
For Window size: 2
MovingAverage m(2)
m.get_next(1) -> 1
m.get_next(2) -> 1.5
m.get_next(3) -> 2.5
m.get_next(4) -> 3.5
'''

class MovingAverage:
    def __init__(self, n):
        self.num = []
        self.size = n
        self.sum = 0

    def get_next(self, number):
        self.num.append(number)
        self.sum += number
        while len(self.num) > self.size:
            tmp = self.num.pop(0)
            self.sum -= tmp
        average = (1.0*self.sum)/len(self.num)
        return average

test = MovingAverage(3)
test.get_next(1)
test.get_next(2)
test.get_next(3)
test.get_next(4)
test.get_next(5)
test.get_next(6)


'''
51. Product of word length which words that share no letters(all lower case)
E.g {feed , see, stuck }: max product: 5x4=20
Complexity?
Follow up:
optimal way to exit earlier in loop.
网上的一个思路
# http://www.quora.com/Given-a-dictionary-of-words-how-can-we-efficiently-find-a-pair-words-s-t-they-dont-have-characters-in-common-and-sum-of-their-length-is-maximum
'''
'''
自己的思路：
1. go through each word in the input list, then create the dictionary for each word like: O(n * m), m is len of word
'f': [0, ]
'e': [0, 1]
'd': [0]
's': [1, 2]
...

2. then for go through each word again, for the each word, find the union of each character, first one 
is [0, 1], time complexity O(m * n), then find maxlen of the rest of word, check the product of this word
and max length of word, update the result.
'''

'''
52. RLE run-length compression
Encode: helll=> he3l,   decode
Requirements:1. Decode(encode(s))==s; 2. Shortest length
Follow up: unit test: test requirement 1&2

思路：check the amount of each character and then add the amount before character
'''


'''
53. Word abbreviation,
e.g. Between=>b5n,  friend=>f4d
Follow-up: implement
Bool checkduplicate(string [] dict, string word)
E.g. {feed }, feed => false;  {door }, deer =>true;  {dare}, deer => false
如果dict里有word 和input word的abbreviation 一样，则return true

和phone interview有点像
'''

'''
54.Poland operation list convert to tree
E.g. {push 4, push 5, add, push 9, mul, sqrt} => tree: {sqrt,  {mul,{9, add(4,5)}}}
'''
import operator

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.operation = None
        self.left = None
        self.right = None
        
class polish_to_tree:
    def __init__(self):
        self.operation = {
                '+': lambda y, x: x + y,
                '-': lambda y, x: x - y,
                '*': lambda y, x: x * y,
                '/': lambda y, x: int(operator.truediv(x, y))
                }

    def build_tree(self, tokens):
        if not tokens: return 0
        stack = []
        for char in tokens:
            if char.isdigit():
                newnode = TreeNode(int(char))
                stack.append((int(char), newnode))
            elif char[0] == '-' and char[1:].isdigit():
                newnode = TreeNode(-int(char[1:]))
                stack.append((-int(char[1:]), newnode))
            elif char in self.operation:
                y, nodey = stack.pop()
                x, nodex = stack.pop()
                value = self.operation[char](y, x)
                newnode = TreeNode(int(value))
                newnode.operation = char
                newnode.left = nodey
                newnode.right = nodex
                stack.append((value, newnode))
        print stack[-1][0]
        return stack[-1][1].value
    
array = ["4", "13", "5", "/", "+"]
test = polish_to_tree()
print test.build_tree(array)



'''
55. 给定一个数字数组 ,其中每个元素是从末端数小于原数组中该元素的个数。求原数组。
原数组中元素是一个[1,n]的随机排列。

For example:
Count array: [3, 0, 1, 0]
Original array: [4, 1, 3, 2]

Can you give an O(nlogn) solution?
original question: http://www.mitbbs.com/article_t/JobHunting/32856675.html

分析：
Count array 就是一个rank
表示当前数字在还存在的[1..n]中的第几个

count array 
i  C[3,0,1,0]   N[1,2,3,4] 
0 C[0] = 3     N中第3个,N[3] = 4,在N里面删除4, N=[1,2,3]
1 C[1] = 0     N中第0个,N[0] = 1,在N里面删除1, N=[2,3]
2 C[2] = 1     N中第1个,N[1] = 3,在N里面删除3, N=[2]
3 C[3] = 0     N中第0个,N[0] = 2

所以答案是4 1 3 2

# 思路
1. 先简历一个segmenttree, 从[0, n-1]，每个叶子节点标记为1，
其他节点的值为这个节点下面有多少个为1的叶子节点。

2. find_kth function, which find tree 中 the kth 小的数字
看左子树有多少个为1的节点，如果大于等于k，那么就在左子树找。如果不到k，那么
就在右子树找k-左子树为1的叶子节点个数。
当你找到相应的叶子节点，那么他表示的区间[l,r](l == r)，l或者r就是我们要找的
[1..n]里面的第k个数

3. delete that node, then find next one 
'''
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = 0
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, irange):
        self.root = self.build_tree(0, irange-1)

    def build_tree(self, left, right):
        if left > right: return None
        newnode = Node(left, right)
        if left == right:
            newnode.count = 1
            return newnode

        mid = (left + right) / 2
        newnode.left = self.build_tree(left, mid)
        newnode.right = self.build_tree(mid+1, right)
        newnode.count = newnode.left.count + newnode.right.count
        return newnode

    def get_kth(self, k):
        cur = self.root
        while cur:
            if cur.start == cur.end:
                return cur.start
            left_cover = 0
            if cur.left:
                left_cover = cur.left.count
            if k <= left_cover:
                cur = cur.left
            else:
                k -= left_cover
                cur = cur.right
        return -1

    def remove_leaf(self, val):
        self.remove_helper(self.root, val)

    def remove_helper(self, cur, val):
        if not cur: return
        cur.count -= 1
        if cur.left and cur.left.start == val and cur.left.end == val:
            cur.left = None

        if cur.right and cur.right.start == val and cur.right.end == val:
            cur.right = None
        mid = (cur.start + cur.end)/2
        if val <= mid:
            self.remove_helper(cur.left, val)
        else:
            self.remove_helper(cur.right, val)

if __name__ == "__main__":
    array = [3, 0, 1, 0]
    test = SegmentTree(4)
    result = []
    for i in array:
        print "i: ", i
        kth = test.get_kth(i)
        print "kth: ", kth
        result.append(kth + 1)
        test.remove_leaf(kth)
    print result



'''
56. You are given two array, first array contain integer which represent heights of persons and second array contain how many 
persons in front of him are standing who are greater than him in term of height and forming a queue. Ex 
A: 3 2 1 
B: 0 1 1 
It means in front of person of height 3 there is no person standing, person of height 2 there is one person in front of him 
who has greater height then he, similar to person of height 1. Your task to arrange them 
Ouput should be. 
3 1 2 
Here - 3 is at front, 1 has 3 in front ,2 has 1 and 3 in front.
# 原题: http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=114856&extra=page%3D3%26filter%3Dsortid%26sortid%3D311%26searchoption%255B3046%255D%255Bvalue%255D%3D1%26searchoption%255B3046%255D%255Btype%255D%3Dradio&page=1
# 讨论：http://www.careercup.com/question?id=24532662
'''

'''
# 解法1, time complexity O(n^2)
假设队伍高度是：
数组A: 2 3 1 5 4

那么对应的在A之前比他高的人数是：
数组B: 0 0 2 0 1

那么首先把高度排序：
数组C: 5 4 3 2 1

然后对数组B从后往前扫
B[4] = 1, 说明 A[4] = C[1] = 4，同时从数组C删除4，此时数组C为：5 3 2 1. 
接下来：
B[3] = 0, 说明A[3] = C[0] = 5，同时从数组C删除元素5. C: 3,2, 1
...
Finally, we could get the result [2,3,1,5,4]

这个算法有个问题是，input should be 
height: [5, 4, 3, 2, 1]
taller: [0, 1, 0, 0, 2]
so we do not get the input as [0 0 2 0 1], which can not use this algorithm

# 解法2, check the discussion in the career cup:
Input: 
height:	6	5	4	3	2	1 
values:	0	0	0	2	2	4 

a) Each node when it enters has its "value" (Number of people greater in height) as its initial value. I am calling it the "current node" (till it reaches its final position).
b) A "current node" goes "left" to the existing node, when its value is <= the existing node's value. At that time it increments the existing node's value by 1.
When the "current node" goes "right", no change to any values.

Repeat for all nodes. Nodes to be pushed in decreasing order of height. Finally do in-order traversal.
The changes from the previous solution are no "right" rule & no +1 for the current node.

With this, the following will be the iterations...
a) 6 = 0
b) 5 = 0, 6 = 1
c) 4 = 0, 5 = 1, 6 = 2.
d) 4 = 0, 5 = 1, 3 = 2, 6 = 3.
e) 4 = 0, 5 = 1, 2 = 2, 3 = 3, 6 = 4.
f) 4 = 0, 5 = 1, 2 = 2, 3 = 3, 1 = 4, 6 = 5.

'''


'''
57. Given an array of ages (integers) sorted lowest to highest, output the number of occurrences for each age.
For instance:
[8,8,8,9,9,11,15,16,16,16]
should output something like:
8: 3 
9: 2 
11: 1 
15: 1 
16: 3
Problem: # http://www.fgdsb.com/2015/01/03/count-numbers/
Analysis: # https://books.google.com/books?id=iBNKMspIlqEC&pg=PA66#v=onepage&q&f=false
思想是divide and conquer, first seperate the 32 bit into 16 blocks, and each block has 2 bits
then check the 1s in each block, if 2 1s, output is 10, if only has 1 1s, output is 01,
then move to the 4 bits in one block
'''
def count_one_array(x):
    x = ((x & 0b1010101010101010) >> 1) + (x & 0b0101010101010101)
    x = ((x & 0b1100110011001100) >> 2) + (x & 0b0011001100110011)
    x = ((x & 0b1111000011110000) >> 4) + (x & 0b0000111100001111)
    x = ((x & 0b1111111100000000) >> 8) + (x & 0b0000000011111111)
    return x

def count_one_array(x):
    x = ((x & 0xAAAAAAAA) >> 1) + (x & 0x55555555)
    x = ((x & 0xCCCCCCCC) >> 2) + (x & 0x33333333)
    x = ((x & 0xF0F0F0F0) >> 4) + (x & 0x0F0F0F0F)
    x = ((x & 0xFFFF0000) >> 8) + (x & 0x0000FFFF)
    return x


'''
58.设计一个电话本系统，实现三个功能：查找号码 boolean isTaken()，添加号码 void takeNumber()，
返回一个不在电话本里的没人用的号码 number giveMeANumber()。我一开始说用HashMap，这样前两个函数的复杂度都是O(1)，
第三个是O(n)。面试官说能不能优化第三个函数，我说用BST，每个节点多存一个value记录这个节点下还有几个available的号码，
giveMeANumber()的实现只要沿着value>0的node往下找就行了。这样三个函数的复杂度都是O(lgn).
这里已经给出所有电话号码的范围是 10位数字 
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=137822&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26sortid%3D311


Analytis:
可以用tries做，每加上一个电话号码，查询一个电话号码，都是O(logn)或者电话号码的长度
在返回任意一个电话号码时候，直接看有没有出现trie里，并且返回


我是这样想的：在每个Trie节点中，记录“从当前节点开始可使用的号码个数”nAvail:
class TrieNode{
    int nAvail;
    int curDepth;
    TrieNode* next[10];
};

比如现在进行在搜索当中，我们已经决定了前5位号码是313-12（也就是当前所在的节点为“2”）。那么我顺次查看next[0]~next[9]。
如果这其中第next[ k ]为空，说明第6位号码只要是 k 的话，第7位以后是什么都没关系。那么我们新建一个next[ k ]节点。然后随机生成一个3位数(10-7=3)，插入到next[ k ]之后；

如果所有的next都不为空，那么我们可以从中那些nAvail不为0的next中随便选一个节点。然后进入这个节点并重复之前的步骤即可。

因为next的长度恒为10，所以在这个数组上进行的线性操作都可看做O(1)时间。因此搜索完L位号码的时间是O(L)

不过回头看看，这种方法可能不如BST。一是检查每位数字虽是常数时间，但是常系数可能会较大；二是上面的这种用数组的implementation不仅没有省内存，而且还费了不少内存，因为最后一层总共有10^10个节点，每个节点有10个next，这些全为空值的next占据了10^11量级的内存。

另外就算是用BST存的话，每个节点处也需要储存号码（32位整数）+左右指针（假设各32位）= 12 byte。最后总共需要12 x 10^10 = 120G内存，很可能放不到一台机器里。如果再跟面试官扯扯这时候如何处理的话，说不定会有加分。

=============================

第三题我也被面过，用的是Trie w/ boolean array, 不用Hashmap是因为 map的initial size是256，对于这种只需要存0-9十个数的情况就很不划算了, 用trie只需要存每层0-9十个boolean,如果这个数已用就把 相应的index set一下.
补充内容 (2015-7-10 13:44):
用boolean array更省地方，因为boolean 只是一个bit，int 是8个
'''

'''
59. 给string a, string b,判断b里面是否存在子字符串是a的anagram。
最开始写了个isAna(string a, string b)的函数，判断两个字符串是不是anagram。然后在主函数里移动window，
调用isAna检查window里面的substring是不是anagram。然后问我有没有啥改进的，我想了半天觉得可以在isAna外面维持一个hashmap，
每次移动window的时候加一个新字符减一个最后的字符，然后和目标字符串比较，但是时间复杂度还是没变。。十分郁闷的问他怎么搞，
他说你这时间复杂度已经够低了。。改进的点是不要每次都在isAna里面建一个新的hashmap，并且不要每次pass一个substring给isAna，
pass一个start point什么的就行。。。
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=87561&extra=page%3D3%26filter%3Dsortid%26sortid%3D311%26searchoption%255B3046%255D%255Bvalue%255D%3D1%26searchoption%255B3046%255D%255Btype%255D%3Dradio&page=1
http://www.geeksforgeeks.org/anagram-substring-search-search-permutations/

# Better solution: http://www.geeksforgeeks.org/anagram-substring-search-search-permutations/

'''

import collections

def check_ana(a, b):
    if len(a) < len(b) or not a or not b: return False
    idict = collections.defaultdict(int)
    for char in b:
        idict[char] += 1
    m = len(a); n = len(b)
    for i in xrange(m-n+1):
        tmp = idict
        if isAna(a[i:i+n], tmp):
            return True
    return False

def isAna(a, tmp_idict):
    for char in a:
        tmp_idict[char] -= 1
        if tmp_idict[char] < 0:
            return False
    if sum(tmp_idict.values()) > 0:
        return False
    return True 

a = "helloworld"
b = "ollel"
print check_ana(a, b)


# General check if two string are anagram or not
import collections

def isAna(a, b):
    if len(a) != len(b):
        return False
    idict = collections.defaultdict(int)
    for char in a:
        idict[char] += 1

    for char in b:
        idict[char] -= 1
        if idict[char] < 0:
            return False
    if sum(idict.values()) > 0:
        return False
    return True

a = "hello"
b = "lloeh"
c = "helllo"
d = "heoool"

print isAna(a, b)
print isAna(a, c)
print isAna(a, d)



'''
60. 给一个整形数组，找离数组的平均值最近的数
写完后问如果该成一个可能随时加数进去的list，怎么找最近的数。分别说说怎么实现add(int)和findNearestAvg()。
我想了想说大概用list或者用tree维持一个sorted list然后再二分查找，但是感觉不能同时保证add和find都是logN的。。
然后他觉得是对的就下一题了。。
就是leetcode上面的maxPoint，但是返回的不是最多的穿过的点的数目，返回这条线
'''


'''
61. 有序数组中都是正数且为unique number，找出两个数A、B，so that A-B = 一个给定的数C。要求使用常数空间和O(N)时间。
# http://www.mitbbs.com/article_t/JobHunting/32861939.html
思路：use two pointers, p0 = 0 , p1 = 1
if A[p1] - A[p0] < target: p1 +=1
elif A[p1] - A[p0] > target: p0 += 1
else return (p0, p1)

if p1 == p2, p2 = p1 + 1
'''

'''
63. 给一个字典，一个字符串， 找出可以由这个字串合法转成的最长单词。 转换操作时删除一个或多个字符 

假设字典是 
Apple orange banana
输入 orange 返回 orange
输入 daxpple 返回 apple
'''



'''
64. similar question:
Given a dictionary of words and an initial character. find the longest possible word in the dictionary by 
successively adding a character to the word. At any given instance the word should be valid word in the dictionary.
ex : a -> at -> cat -> cart -> chart ....

# http://stackoverflow.com/questions/2534087/successive-adding-of-char-to-get-the-longest-word-in-the-dictionary
# http://stackoverflow.com/questions/17717223/find-the-longest-word-in-the-dictionary-such-that-it-can-be-built-from-successiv
'''
import string
import collections

def find_longest_word(beginchar, wordDict):
    if not beginchar or not wordDict:
        return 0
    chars = string.ascii_lowercase
    queue = collections.deque([beginchar])
    result = 0

    while queue:
        size = len(queue)
        for _ in xrange(size):
            word = queue.popleft()
            for i in xrange(len(word)+1):
                for char in chars:
                    newword = word[:i] + char + word[i:]
                    if newword in wordDict:        
                        queue.append(newword)
                        print "queue: ", queue
                        result = max(result, len(newword))
    print result                    
    

wordDict = ["hot","dot","dog","lot","log", "ta","tan", "tap","tape", "tang",
            "taped", "tamped", "strang","strange","stamped","ta","ca","cat"]

find_longest_word('a', wordDict)


'''
65. You are given a dictionary, in the form of a file that contains one word per line. E.g., 
abacus 
deltoid 
gaff 
giraffe 
microphone 
reef 
qar 
You are also given a collection of letters. E.g., {a, e, f, f, g, i, r, q}. 
The task is to find the longest word in the dictionary that can be spelled with the collection of 
letters. For example, the correct answer for the example values above is “giraffe”. (Note that 
“reef” is not a possible answer, because the set of letters contains only one “e”.)
# http://www.careercup.com/question?id=16148684
'''
import collections

def find_longest_word(letters, words):
    if not letters or not words:
        return None
    dict_letter = collections.Counter(letters)
    letter_len = len(dict_letter)
    result = 0

    for word in words:
        flag = True
        tmp = dict_letter.copy()
        if len(word) > letter_len:
            continue 
        for char in word:
            tmp[char] -= 1
            if tmp[char] < 0:
                flag = False
                break
        if flag:    
            result = max(result, len(word))
    return result

words = ["abacus", "deltoid", "gaff", "giraffe", "microphone", "reef", "qar"]
letters = ['a','e','f','f','g','i','r','q']
print find_longest_word(letters, words)
~                                       


'''
66. 一个logfile，有timestamp，userid，x，y。写个方法，找出任意两个userid，在一定的range里，timestamp最近的一对pair
'''



'''
67. 加了一个小问题，三角形三个顶点各有一只小虫，小虫只能沿着线走，但方向任选，问一段时间后，两只小虫碰一块儿的几率是多少
# http://www.programmerinterview.com/index.php/puzzles/3-ants-on-a-triangle-riddle/

The only possibility that ants can not meet each other is 2, clockwise or anti-clockwise, but the totally 3 ants could choose
the ways are 2^3 = 8, so the possiblity that any two ants meet each other is (8-2)/8 = 0.75
'''

'''
68. 先上来问了下quicksort, 举一个worse case 时间复杂度的例子， 然后coding, 一个n的数组，没有重复， 0到n-1都在这个数组里面， 
只能读，不能写（swap除外），问怎么排序，我上来就说quicksort ：）然后问有没有再优化的，想了下给了个O（n)的，不到20行搞定

# quick sort: 
# https://github.com/UmassJin/Leetcode/blob/master/Algorithm/Different_Sort_Algorithms.md#quick-sort
# quick sort disadvantage: 
# http://www.geeksforgeeks.org/when-does-the-worst-case-of-quicksort-occur/
# O(n) sort algorithm: swap the element to the correct position in array 

The answer depends on strategy for choosing pivot. In early versions of Quick Sort where leftmost (or rightmost) element is 
chosen as pivot, the worst occurs in following cases.

1) Array is already sorted in same order.
2) Array is already sorted in reverse order.
3) All elements are same (special case of case 1 and 2)

Since these cases are very common use cases, the problem was easily solved by choosing either a random index for the pivot, 
choosing the middle index of the partition or (especially for longer partitions) choosing the median of the first, middle and 
last element of the partition for the pivot. With these modifications, the worst case of Quick sort has less chances to occur, 
but worst case can still occur if the input array is such that the maximum (or minimum) element is always chosen as pivot
'''


'''
69. Sort n numbers in range from 0 to n^2 – 1 in linear time
# http://www.geeksforgeeks.org/sort-n-numbers-range-0-n2-1-linear-time/
# Radix Sort: http://www.geeksforgeeks.org/radix-sort/

Sort a nearly sorted array:
http://www.geeksforgeeks.org/nearly-sorted-algorithm/
'''

'''
70. 问garbage collection和arc的区别，各自的优点和缺点，我运气好，以前学ios programming的时候专门看了的，然后他让我用doubly linked list给他展示，
随便画一画，然后问我arc有什么缺点（他是想问我memory cycle), 我但是没想到，就说我不太清楚，他说这个doubly linked list不会用cycle吗，
我说如果你用weakref就不会，顿时向我投来了肯定的目光。。。也许是我yy的
2 给以个二叉搜索树和一个iterator,先问你怎么存data才能让这个树可以接受重复元素，我说存一个object,里面是Key和计数器，他说好，
然后开始写代码，问题是怎么判断这个树和Iterator里面元素和计数都一样，我说用一个hashmap的counter,先去in order traverse这个数，存在map里，
然后再比较iterator，最后看看这个map 的counter是否为0或者为空，他说好，写吧，这题明显是想考bst 的 in order，然后用stack写了个iterative的traverse,
中间粗心犯了个小错误，stack里面Object存错了，被面试官指出然后改正，后面的很简单的code没让写，不过时间也不多了，他说你问我问题吧。

# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=118515&extra=page%3D3%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
'''

'''
71. Count frequencies of all elements in array in O(1) extra space and O(n) time
Given an unsorted array of n integers which can contain integers from 1 to n. Some elements can be repeated multiple times and 
some other elements can be absent from the array. Count frequency of all elements that are present and print the missing elements.
# http://www.geeksforgeeks.org/count-frequencies-elements-array-o1-extra-space-time/
'''
def count_frequency(array):
    if not array: return None
    n = len(array)
    i = 0

    while i < n:
        if array[i] < 0:
            i += 1
            continue
        index = array[i] - 1
        if array[index] > 0:
            array[i] = array[index]
            array[index] = -1
        else:
            array[index] -= 1
            array[i] = 0
            i += 1
    return array

test = [2,3,3,2,5]
test1 = [3,3,3,3,3]
print count_frequency(test)
print count_frequency(test1)


def count_frequency2(array):
    if not array: return None
    n = len(array)
    array = [array[i]-1 for i in xrange(n)]
    
    for i in xrange(n):
        array[array[i]%n] = array[array[i]%n] + n
        
    array = [array[i]/n for i in xrange(n)]
    return array

test = [2,3,3,2,5]
test1 = [3,3,3,3,3]
print count_frequency2(test)
print count_frequency2(test1)

Output:
[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python count_frequency.py 
[0, -2, -2, 0, -1]
[0, 0, -5, 0, 0]
[0, 2, 2, 0, 1]
[0, 0, 5, 0, 0]


'''
72. 进制转换， 十进制转换为any进制，会给一个base input
'''

'''
73. BST构建，插入，删除, return the next node;
'''

'''
74. 给一个array of 硬币，第i次翻面所有i的倍数的位置的硬币，（第0次，第1次全翻，第2次翻2, 4, 6, ...）输出最后结果。要求O(n logn)解法。
'''


'''
75. cypher graphics equivalent, 判断两个string是不是cypher graphics equivalent，并证明cypher graphics equivalent是否symmetric和transitive。
cypher graphics equivalent是指，比如说ABC和DEF就cypher graphics equivalent，因为A=>D, B=>E, D=>F。ABC和ADD就不是。

给一个disordered array，判断是否有两个数相等。
给一个disordered array和一个int dist，判断是否有两个数相等且距离小于dist。
给一个disordered array和一个int targe和一个int dist，判断是否有两个数a, b使 Math.abs(a-b) <= target。且a, b的index距离小于dist。

# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=124484&extra=page%3D2%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
'''


'''
76. input string：“+++--++-+”
游戏规则：每人每次可以 flip "++" to "--"（必须是相邻的）

第一问：generate all possible moves
第二问：determine if this player can will
Extra：这两个问题的implementation的Big-O. 1

下个人没法flip了这个人就赢；all possible moves for next flip
# http://www.1point3acres.com/bbs/thread-137953-1-1.html
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=137928&extra=page%3D1%26filter%3Dsortid%26sortid%3D311&page=2
# http://web.mit.edu/sp.268/www/nim.pdf
'''


'''
77. Three segments of lengths A, B, C form a triangle iff
A + B > C
B + C > A
A + C > B

e.g.
6, 4, 5 can form a triangle
10, 2, 7 can’t

Given a list of segments lengths algorithm should find at least one triplet of segments that form a triangle (if any).

Method should return an array of either:

3 elements: segments that form a triangle (i.e. satisfy the condition above)
empty array if there are no such segments
Follow up:
Could you return the number of all valid triangles? You can assume there’s no duplicates in the original array.

# http://www.geeksforgeeks.org/find-number-of-triangles-possible/
'''
def triangle(array):
    if not array or len(array) < 3: return 0
    count = 0
    n = len(array)
    for i in xrange(n-2):
        k = i + 2
        for j in xrange(i+1, n):
            while k < n and  array[i] + array[j] > array[k]:
                k += 1
            count += k - j - 1
    return count

arr = [10, 21, 22, 100, 101, 200, 300]
print triangle(arr)


'''
78.给定一个word list 和一个target word，要求输出在word list 里跟target word的edit distance 相差不大于k的所有words。

这是Airbnb的电面题。直接用edit distance挨个遍历一遍也能做，但是如果word list很大，那重复计算会非常多，这时候可以用trie来优化。
下面举个例，假设字典为["cs", "ct", "cby"]，target word为"cat"，k=1。
# 原题：http://www.mitbbs.com/article_t/JobHunting/32692817.html
# 解法：http://stevehanov.ca/blog/index.php?id=114
'''


'''
79.给一个dictionary, 一个string,找出dict 里能全部用string里的letter 表示的所有最长的词。
For example:
字典包含如下单词：
abcde, abc, abbbc, abbbccca, abbbcccabbcx
给string = "abc"，最长单词应为"abbbccca"

# http://www.mitbbs.com/article_t/JobHunting/32634303.html

80. Similar question:
You are given a string 's' and you are given a dictionary of english words. 
You goal is to write an algorithm that returns all words from the dictionary the can be formed by 
characters from that string 's'. 

Example: 
s = "ogeg" 
following words can be formed from 's': go egg ego . . . 
Further it is given that string 's' always consists of four lower case characters. 
Lets say that the dictionary is contained in a file and can be fitted in the memory. 
It is up to you which data structure you use to represent the dictionary. 
How would you design an efficient algorithm? Follow up: What if the dictionary file can not be fitted in the memory?
# http://www.careercup.com/question?id=6270813198090240
'''
import collections

class TrieNode:
    def __init__(self):
        self.value = None
        self.end = False
        self.children = collections.defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add_word(self, word):
        node = self.root
        word = word.strip()
        
        for char in word:
            node = node.children[char]
        node.end = True
        node.value = word
        
    def search_longest_str(self, idict, string):
        if not idict or not string:
            return None
        for word in idict:
            self.add_word(word)
        print "node: ", self.root.children
        result = [""]
        self.search(result, "", self.root, string)
        return result[0]

    def search(self, result, cur, node, string):
        if not node:
            return
        if node.end and len(cur) > len(result[0]):
            print "node.value: ", node.value
            result[0] = cur

        for child in node.children:
            if child in string:
                self.search(result, cur + child, node.children[child], string)
        
test = Trie()
idict = ["abcde ", " abc", " abbbc", "abbbccca", "abbbcccabbcx"]
string = "abc"


'''
82. Given a dictionary of words, and a set of characters, judge if all the characters 
can form the words from the dictionary, without any characters left. 
For example, given the dictionary {hello, world, is, my, first, program}, 
if the characters set is "iiifrssst", you should return 'true' because you can form {is, is, first} from the set; 
if the character set is "eiifrsst", you should return 'false' because you cannot use all the characters from the set. 

P.S. there may be tens of thousands of words in the dictionary, and the chars set length could be up to hundreds, 
so I really need some efficient algorithm.

some questions ask:
1) If the input word could be used multiple times ?
2) Just find one of the answer is fine and return True or False, do not need the shortst one ?
'''

import collections

class TrieNode:
    def __init__(self):
        self.value = None
        self.end = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        word = word.strip()
        word = ''.join(sorted(word))

        for char in word:
            node = node.children[char]
        node.end = True
        node.value = word

    def search(self, word, idict):
        wdict = collections.Counter(word)
        result = []
        for word in idict:
            self.add_word(word)
        self.search_helper(wdict, result, "", self.root)
        if len(result) > 0:
            print "True"
        else:
            print "False"
        return result


    def search_helper(self, wdict, result, cur, node):
        if sum(wdict.values()) == 0:
            if node.end:
                result.append(cur)
            return

        if node.end:
            temp = wdict.copy()
            self.search_helper(temp, result, cur, self.root)

        for child in node.children:
            if child in wdict and wdict[child]-1 >= 0:
                wdict[child] -= 1
                self.search_helper(wdict, result, cur + child, node.children[child])
                wdict[child] += 1

def main():
    test = Trie()
    idict = ['abc', 'abde', 'cfg', 'cde','hello']
    word = "abccde"
    print test.search(word, idict)

if __name__ == "__main__":
    main()


'''
83. 给一个dictionary, 再给一个set of coding string （g5, goo3, goog2, go2le………). 
return all string from dictionary that can be matched with the coding string. 要求尽量减少dictionary look up 次数
# http://www.fgdsb.com/tags/Trie/
'''


'''
 84. There are a set of dictionary words and a set of license   plate numbers. Write a code/algorithm to find the shortest 
 dictionary word which contains all the characters in the license plate, irrespective of the order of characters. 
 Ex: RC101 is the license plate number. The shortest word that can be found in the dictionary is CAR which has 
 characters 'R' and 'C' in the license plate. 
 
 思路: 一个brute force的想法是，把每个word排序，然后去掉数字，然后把每个字典里面的字母排序，然后依次比较word在不在每个字典里，
 找出最短的字典里的单词
 
 利用trie，将dictionary里面每个单词放入trie里的时候，排序，查找的时候，如果trie_node[char] < string[char], 查找
 '''
 
 '''
 85. similar question about Trie:
 # http://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver#746345
 '''


========================================================================================

'''
Design 
'''

'''
你好，那我就讲一下music list那道题吧：
你有一个music的播放列表，里面的歌曲unique，但是播放列表的长度未知。
这个音乐播放器APP有两个模式：random模式和shuffle模式。
random模式就是每次随机播放列表里的一首歌；
shuffle模式就是shuffle列表里的歌，然后顺序播放，放完以后重新shuffle，再顺序播放；
现在给你一个播放历史记录，要求你写一个函数来判断用户使用的是random模式，还是shuffle模式。
'''

'''
1. 系统设计：给一个url和一个给定的api可以返回所有从这个url可以直接链接到的url。要求统计所有能访问到url数。
结果先让我coding，我以为搞错了，后来coding完了，followup就是怎么解决scalable的问题，给定的那个API有什么问题
以及怎么改进（最后引申到设计web crawler），怎么解决url无效等等问题。
'''
'''
2. 第一题local minimum，第二题在数组中检查x距离内是否有重复。

3. 1000个文件每个有1TB的大小，服务器每台100GB内存，1TB硬盘。文件基本上一次写入就不会变化了，读的次数比较多。问怎么设计这样的系统。followup怎么解决fault tolerance，再增加1000个这样文件，怎么办，等等。


偏向c++功底跟concurrency。实现memcopy，还有就是实现一个银行的类里面的几个算法，都很简单，但是对多线程调用的加锁需要有了解。最后又问了一个实现每次调用，运行5秒，期间不停循环自增的简单算法，
follow-up是如何应对系统管理员尴尬地恰巧在这段时间内改了系统时间

6. Design Question: Get program running on data centers, try catch and scalability , cache followups

7. 第五题是design题。问我设计程序给一个program name, 得到它在哪些data center上运行

我设计了 .
List<String> getProgramOnDataCenter(String ProgramName)
boolean isOnDataCenter(String ProgramName, String DCName)

然后就是一些exception handle，server上如何处理dragger，如何设计cache

8. 然后是一个design题，design一个cache，然后需要设计哪些操作，需要考虑哪些参数，用什么hardware储存。。

10. 设计售票系统， 要求
1. 每次返回5张可选最多
2. 保证不会给两个不同user返回同一个可选座位
3. 用户2分钟之内，没有购买，重新开始

11. system design，什么一堆page判断duplicate，如何断定一个page比另外一个page更trustful

12. 设计题，问用什么数组实现搜索推荐，先讨论了几种方案，最后说用trie

13. 德州扑克
 we have n cards, four suites (H, C, D, S). 1<=value<=13， we have the following hands type:
 Straight flush      Four of a kind      Full house  Flush Straight Three of a kind Two pair One pair
 Questions: given n cards, and find out the best hands type we could have, n is not 52. and the output does 
 not have to be five. 如果你找到three of a kind，但是没有找到比它更大的了，那这三张就是Output3. 

14. 选址建房子。图论的题，意思是给一个matrix，上面有一堆商店，每个商店有建房子需要的材料，要求找到建房子最佳的地址，
使到每家商店的距离之和最短，matrix里面还包含不能走的格子。要求先设计类后给算法

15. 假设Google有一个内部系统，可以接受来自员工的各种订单，例如定个鲜花，定个蛋糕之类的。内部系统会连到一个外部系统，
这个外部系统会处理这些订单，发给相应的vendor去接单。
问，这两个系统有哪些问题需要考虑。

16. 一辆车有Year, Make, Model。假设一个Dealer有很多很多车，如何才能得到每一种unique car有多少辆。unique car的意思是说，
Year, Make, Model这三个特征，只要有一个和其他车不同，就是unique car。

17. 假设用一个N叉树存一个员工管理系统，从上到下按照级别一级一级递减，最顶端是CEO，往下是各个级别的经理，再是普通员工，
所以每一个节点都是一个员工。现在给出任意一个节点，要得到从这一点开始往上的职位层级，问要怎么做，不用写代码，说一说就行

二面是一个哥们问如何对一个用户进行好友推荐，这个推荐的人应该和用户有最多的共同好友。是图问题。

三面是写一个meeting schedule, 求最少的房间。

题目一：社交网络中，如何实现好友推荐。抽象成图，然后找出共同好友最多的那个人。

题目二：生产者消费者问题。
题目三：假设google在火星上弄了个data center， 如何无人值守给他升级内核。如何判断机器挂掉了，挂掉了怎么办。

＃ http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=94183&extra=page%3D6%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
＃ http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=107236&extra=page%3D6%26filter%3Dsortid%26sortid%3D311%26searchoption%255B3046%255D%255Bvalue%255D%3D1%26searchoption%255B3046%255D%255Btype%255D%3Dradio&page=1

18. Design a google calendar 
# http://martinfowler.com/apsupp/recurring.pdf
# http://stackoverflow.com/questions/85699/whats-the-best-way-to-model-recurring-events-in-a-calendar-application

'''



'''
System Design 分类
'''
=========================================
'''
游戏类

1. 设计贪吃蛇， 怎么定义蛇， 怎么移动， 怎么吃， 怎么判断时候活着， 怎么定义游戏版
# https://github.com/UmassJin/Leetcode/blob/master/Design/OS_concepts/Game/snake.md
# http://www.hawstein.com/posts/snake-ai.html
# https://github.com/Hawstein/snake-ai/blob/master/snake.py

# 我们可以通过一个二位数组来定义board, 一位数组定义snake
# Initialization: snake_size = 1; snake_head = snake_array[0];
# Move: up, down, left, right, avoid the snake itself, check the board size, recorde each step since snake need to move
# empty the tail block in snake
# Eat: the simplest method for "eat" is use the BFS to find the shortest path to the food, but this may lead to the no path
# then we need to use the "Wander" function, after discuss the simple verion, we could use the "virtual snake" to test the 
# safe path, if the path is "safe", which means whether snake has the path to follow it's tail, here we could use the tail as 
# the fake "food" and then find whether there is path, then for each move, we use the BFS and check the safety, if there is no
# path between head and food and head and tail, choose the random one, 

1. 目标是食物时，走最短路径
2. 目标是蛇尾时，走最长路径
一般而言， 我们会让蛇每次都走最短路径。这是针对蛇去吃食物的时候， 可是蛇在追自己的尾巴的时候就不能这么考虑了。
我们希望的是蛇头在追蛇尾的过程中， 尽可能地慢。这样蛇头和蛇尾间才能腾出更多的空间，空间多才有得发展。


2. tic-tac-toe，给定场景是人机大战，人永远先开始下。要求把所有的棋盘布局组合都输出（人机各走一步算一个新的棋盘布局）。
# Minmax wiki: https://en.wikipedia.org/wiki/Minimax
# Minmax tic-tac-toe: http://neverstopbuilding.com/minimax
# 中文版: http://univasity.iteye.com/blog/1170226

Pseudocode:
==========
function minimax(node, depth, maximizingPlayer)
    if depth = 0 or node is a terminal node
        return the heuristic value of node
    if maximizingPlayer
        bestValue := -∞
        for each child of node
            val := minimax(child, depth - 1, FALSE)
            bestValue := max(bestValue, val)
        return bestValue
    else
        bestValue := +∞
        for each child of node
            val := minimax(child, depth - 1, TRUE)
            bestValue := min(bestValue, val)
        return bestValue

(* Initial call for maximizing player *)
minimax(origin, depth, TRUE)


def minimax(game, depth):
    if game.over:
	return score(game) 
    depth += 1
    scores = []
    moves = []
     
    # Populate the scores array, recursing as needed
    game.get_available_moves.each do |move|
        possible_game = game.get_new_state(move)
        scores.push minimax(possible_game, depth)
        moves.push move
    end

    # Do the min or the max calculation
    if game.active_turn == @player
        # This is the max calculation
        max_score_index = scores.each_with_index.max[1]
        @choice = moves[max_score_index]
        return scores[max_score_index]
    else
        # This is the min calculation
        min_score_index = scores.each_with_index.min[1]
        @choice = moves[min_score_index]
        return scores[min_score_index]
    end
end

# max-min pruning 
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

这一优化被称为alpha-beat剪枝，算法描述如下：
   1. 有两个值被传递到每个树的节点：
            值alpha，记录着找到的最好的“大值”（MAX value）；
            值beta，记录着找到的最好的“小值”（MIN value）。
   2. 在MAX层时，在对每个子路径进行估值前，用前一路径的返回值与beta值作比较。如果该值大于beta值，那么跳过对当前节点的搜索；
   3. 在MIN层时，在对每个子路径进行估值前，用前一路径的返回值与alpha值作比较。如果该值小于alpha值，那么跳过对当前节点的搜索。


01 function alphabeta(node, depth, α, β, maximizingPlayer)
02      if depth = 0 or node is a terminal node
03          return the heuristic value of node
04      if maximizingPlayer
05          v := -∞
06          for each child of node
07              v := max(v, alphabeta(child, depth - 1, α, β, FALSE))
08              α := max(α, v)
09              if β ≤ α
10                  break (* β cut-off *)
11          return v
12      else
13          v := ∞
14          for each child of node
15              v := min(v, alphabeta(child, depth - 1, α, β, TRUE))
16              β := min(β, v)
17              if β ≤ α
18                  break (* α cut-off *)
19          return v

3. 保龄球计分，给一组分数，输出实际每轮投完后的累计得分。


4. 设计扫雷游戏
# http://code.tutsplus.com/tutorials/build-a-minesweeper-game-within-200-lines-of-code--active-8578

'''






'''
Google Phone interview 
'''
Please use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.

Write a function that accepts an array of numbers as input, and returns the largest product (multiplication)  of any two numbers in that array

Input: [0, 3, 5, 7]
Output: 35

def maxProduct(nums):
	if not nums or len(nums) < 2: return 0
	minval = nums[0]
	maxval = nums[0]
	result = nums[0]	

	for i in xrange(1, len(nums)):
result = max(minval * nums[i], maxval* nums[i], result)
		maxval = max(maxval, nums[i])
		minval = min(minval, nums[i])
	return result 

def maxProduct(nums):
	if not nums or len(nums) < 2: return 0
	result = nums[0]
	maxval = nums[0]
	
	for i in xrange(len(nums)):
		if nums[i] == 0:
			result = max(result, 0)
			continue
		else:
			for j in xrange(i+1, len(nums)):
				tmp = nums[i] * nums[j]
				result = max(tmp, result)
	return result 



test case:
[0] ⇒ 0
[1] ⇒ 0
[0, 1] ⇒ 0
[-1, -6, 3] => 6
[0, 3, 5, 7]


 "internationalization" -> "i18n"
 "localization" -> "l10n"

Such abbreviations are not always unique -- for example, “a11y” could stand for “accessibility”, “automatically”, etc. Given a list of words, determine if the abbreviation of the word is unique. 


 "internationalization" -> "i18n"
 "localization" -> "l10n"
accessibility -> “a11y”

True

 "internationalization" -> "i18n"
 "localization" -> "l10n"
accessibility -> “a11y”
automatically -> a11y
‘ab’ -> ‘a0b’
False


def abbreviation_unique(array):
	if not array or len(array) < 2: return True
	n = len(array)
	check = {}
	for i in xrange(n):
		strlen = len(array[i])
		abbre = array[i][0] + str(strlen-2) + array[i][strlen-1]
 		if abbre in check:
			return False
		else:
			check[abbre] = 1
	return True 

n string in the input array
time complexity: O(n)
space complexity: O(n)

