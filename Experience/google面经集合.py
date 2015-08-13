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
# http://cs.stackexchange.com/questions/11265/find-non-overlapping-scheduled-jobs-with-maximum-cost
'''    

def non_overlapping(array):
    if not array:
        return None
    result = []
    n = len(array)
    array = sorted(array, key = lambda x: x[1])
    print "array: ", array
    dp = [ 0 for _ in xrange(n+1)]
    for i in xrange(1, n+1):
        cur = array[i-1]
        index = find_interval(array, cur[0], 0, n-1)
        dp[i] = max( dp[index+1]+cur[2], dp[i-1]) 
        print "dp: ", dp
    return dp[n]

def find_interval(array, target, start, end):
    if start > end:
        return end # Note: here we return end, not start not None 
    while start <= end:
        mid = (start + end)/2
        if array[mid][1] == target:
            return mid
        elif array[mid][1] > target:
            return find_interval(array, target, start, mid-1)
        elif array[mid][1] < target:
            return find_interval(array, target, mid+1, end)
        
test = [[3,8,3], [2,3,2],[1,5,2], [2,9,3], [8,13,2]]
print non_overlapping(test)

    
    
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
        tmp = (self._pointer+1)%2
        if self.its[tmp].has_next():
            self._pointer = tmp 	
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

some questions need to clear:
1) how about the word length less than 2 ?
2) we only consider the first letter and last letter ?
3) is there any limitation of the word length ?
brute force思路是: check each abbr of each word in dictionary, optimization is
use the trie to optimize the dictionary 

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

首先，这种游戏属于“无偏博弈”(impartial game)，意思是：“棋盘”上的棋子，即"+"号，双方都可以公平地使用；而且胜利的最终判定方法对二者来说是一样的。而象棋就不是无偏博弈，因为双方各有不同的棋子和胜利条件。其次这种游戏的终结条件是“正常终结条件”的，即最后无法move的那个人输。与之相对的还有一种叫做“misere终结条件”，即无法move的人赢。

以下将要谈到的所有定理和推理过程，都是仅适用于“无偏博弈”和“正常终结条件”的情况。

------------------------------

因为我们只能把连着的两个+号变为-号，所以对我们来说，“棋盘”状态可以由一组“连续的+的个数来表示”，比如“+++----+-++----++++”可以表示为(3, 1, 2, 4)。 因为其中那个单独的+号对结果没有影响，而且3和2出现的顺序也无关紧要，所以我们扔掉“1”，然后将这个序列排序，即得较简的表达方式：(2,3,4)。

所以，这个游戏其实就是从某个初始状态开始，不断进入下一个状态，直至无法改变状态为止。如果以每一个可能的状态做为一个节点，那么整个游戏中能出现的所有状态和这些状态直接的转移方式共同构成了一个有向无环图。之所以无环，是因为我们没法将-号变回+号，所以我们永远不可能回到之前的状态。

比如，从状态(2, 3, 4)开始，我们能进入的可能状态是
(2-2, 3, 4) => (3,4)
(2, 3-1, 4) => (2,4)
(2, 3, 4-2) => (2,2,3)
(2, 3, 2, 2) => (2,2,2,3)

由于游戏结束时序列中必然没有连续的两个+号，所以按照我们的简化记法，此时的状态为().

接下来是两个重要概念，第一是Sprague-Grundy（SG）函数g(x)，其中x是“游戏图”中的一个节点（状态），如果我们用{y1, y2, ..., yn}表示x的所有子节点（即下一步状态）。那么SG函数的定义是：

g(x) = FirstMissingNumber(g(y1), g(y2), ... g(y3))

这是个递归定义的函数。如果x没有子节点，那么定义g(x) = 0；如果x有n个子节点，比如有3个子节点，g值分别为{0,1,3}，那么g(x)的值是这个列表中第一个没有出现的>=0的值，此时g(x) = 2。

为什么需要引入这样一个函数？此处给出一个定理，各位暂时承认他即可：


本帖最后由 stellari 于 2015-7-13 13:09 编辑


原题：


给定一个仅由+和-组成的字符串，如“++++-----+++++-----++-+”，两名玩家轮流地将“相邻的两个++flip为--”，直至轮到一方时，如果他不能继续flip，则这名玩家输。问对于给定的字符串，如何判断（在双方都使用最优策略的情况下）先手玩家是否一定能赢？


此题的面经请点这里。


------------------------------

[转发]
这种解法需要了解博弈论的知识，一般面试应该是不做要求的。只是放在这里供大家参考：

首先，这种游戏属于“无偏博弈”(impartial game)，意思是：“棋盘”上的棋子，即"+"号，双方都可以公平地使用；而且胜利的最终判定方法对二者来说是一样的。而象棋就不是无偏博弈，因为双方各有不同的棋子和胜利条件。其次这种游戏的终结条件是“正常终结条件”的，即最后无法move的那个人输。与之相对的还有一种叫做“misere终结条件”，即无法move的人赢。

以下将要谈到的所有定理和推理过程，都是仅适用于“无偏博弈”和“正常终结条件”的情况。

------------------------------

因为我们只能把连着的两个+号变为-号，所以对我们来说，“棋盘”状态可以由一组“连续的+的个数来表示”，比如“+++----+-++----++++”可以表示为(3, 1, 2, 4)。 因为其中那个单独的+号对结果没有影响，而且3和2出现的顺序也无关紧要，所以我们扔掉“1”，然后将这个序列排序，即得较简的表达方式：(2,3,4)。

所以，这个游戏其实就是从某个初始状态开始，不断进入下一个状态，直至无法改变状态为止。如果以每一个可能的状态做为一个节点，那么整个游戏中能出现的所有状态和这些状态直接的转移方式共同构成了一个有向无环图。之所以无环，是因为我们没法将-号变回+号，所以我们永远不可能回到之前的状态。

比如，从状态(2, 3, 4)开始，我们能进入的可能状态是
(2-2, 3, 4) => (3,4)
(2, 3-1, 4) => (2,4)
(2, 3, 4-2) => (2,2,3)
(2, 3, 2, 2) => (2,2,2,3)

由于游戏结束时序列中必然没有连续的两个+号，所以按照我们的简化记法，此时的状态为().

接下来是两个重要概念，第一是Sprague-Grundy（SG）函数g(x)，其中x是“游戏图”中的一个节点（状态），如果我们用{y1, y2, ..., yn}表示x的所有子节点（即下一步状态）。那么SG函数的定义是：

g(x) = FirstMissingNumber(g(y1), g(y2), ... g(y3))

这是个递归定义的函数。如果x没有子节点，那么定义g(x) = 0；如果x有n个子节点，比如有3个子节点，g值分别为{0,1,3}，那么g(x)的值是这个列表中第一个没有出现的>=0的值，此时g(x) = 2。

为什么需要引入这样一个函数？此处给出一个定理，各位暂时承认他即可：

------------

定理1：如果一个节点x的g(x)=0，那么x状态一定是“先手必输”的状态；否则一定是“先手必赢”。

------------

因此，我们如果能递归算出g(字符串初始状态)的值，那么我们就可以立即判断输赢。


但是，递归计算这个式子会比较繁琐。因为，一个连续序列经常会被分割成两个不连续的序列，这样递归计算的复杂度会比较高。所以我们引入第二个定理，即著名的Sprague-Grundy定理：

------------

定理2：如果一个游戏G由许多相同规则的子游戏G1,G2,..., Gk组成，那么对于游戏G的一个状态x = {x1,x2,...,xn}，SG函数g(x) = g(x1) ^ g(x2) ^ ... ^ g(xn)。其中^表示“异或”。

------------

在我们这个游戏里，多个不相邻的+++子序列，就可以看做多个子游戏。所以，我们就可以用DP来代替递归了，比如当前状态为(10)，它的后继状态可能是(8), (7), (2,6), (3,5), (4,4)。这里，我们就没有必要再次递归去算(2,6), (3,5)和(4,4)，因为根据SG定理, g((2,6)) = g(2) ^ g(6), g((3,5)) = g(3) ^ g(5) ....一般地，对于各种可能状态，我们有如下的计算公式：

g(0) = 0;        // 一个+都没有，先手必输
g(1) = 0;        // 只有一个+，先手必输
g(2) = FirstMissingNumber(g(0)) = 1     // 两个+，先手必赢
g(3) = FirstMissingNumber(g(1))        = 1            // 先手必赢
g(4) = FMN(g(2), g(1) XOR g(1)) = 2    // 两种情况：A 1111->0011 OR 1100，也就是状态2，B 1111-> 1001  
...
g(9) = FMN(g(0)^g(7), g(1)^g(6), g(2)^g(5), g(3)^(4)).
...
g(x) = FMN(g(0)^g(x-2), g(1)^g(x-3), g(2)^g(x-4), ... g(x/2)^g(x/2)).

因为计算每一个g(x)都要进行x/2次异或，且FirstMissingNumber也是一个O(x)的操作，所以计算g(1)~g(x)共需要O(x^2)时间。在长为N的“棋盘”上，最大的连续+串的长也为N，所以最差时间复杂度是O(N^2)。需要额外空间保存[0, 1,2,3,4,5...N]状态下的g值，因此空间复杂度是O(N)。

另外，如果最初的状态不是一个连续的+号序列，而是几个不连续的+号序列，比如x = (2,3,8)。 那么我们只要分别算x1 = (2), x2 = (3), x3 = (8)三种情况的g值，然后三者取异或即可，对时间空间复杂度没有影响。

-----------------------------------

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
 84. There are a set of dictionary words and a set of license plate numbers. Write a code/algorithm to find the shortest 
 dictionary word which contains all the characters in the license plate, irrespective of the order of characters. 
 Ex: RC101 is the license plate number. The shortest word that can be found in the dictionary is CAR which has 
 characters 'R' and 'C' in the license plate. 
 
 思路: 一个brute force的想法是，把每个word排序，然后去掉数字，然后把每个字典里面的字母排序，然后依次比较word在不在每个字典里，
 找出最短的字典里的单词
 
 
 
給一個車牌號碼(美國的)，以及一個dictionary，請找出dictionary裡含有所有該車牌號碼裡的所有英文字母(case insensitive)的最短字串
ex:. 鐗涗汉浜戦泦,涓€浜╀笁鍒嗗湴
車牌 RO 1287 ["rolling", "real", "WhaT", "rOad"] => "rOad"
follow up:-google 1point3acres
(1) 如果dictionary裡有上百萬個字，該如何加速
(2) 如果dictionary有上百萬個字，然後給你上千個車牌號碼，要你回傳相對應的最短字串，該如何optimize?. 
 
 利用trie，将dictionary里面每个单词放入trie里的时候，排序，查找的时候，如果trie_node[char] < string[char], 查找
 '''
 
 '''
 85. similar question about Trie:
 # http://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver#746345
 '''

'''
86.Given a array of pairs where each pair contains the start and end time of a meeting (as in int),
Determine if a single person can attend all the meetings
For example:
Input array { pair(1,4), pair(4, 5), pair(3,4), pair(2,3) }
Output: false

Follow up:
determine the minimum number of meeting rooms needed to hold all the meetings.
Input array { pair(1, 4), pair(2,3), pair(3,4), pair(4,5) }
Output: 2
'''

class interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def meeting_room(meetings):
    if not meetings: return 0
    result = 0
    cur = 0
    times = []
    for meeting in meetings:
        times.append(meeting.start)
        times.append(-meeting.end)
    times = sorted(times, cmp = lambda x, y: cmp(abs(x), abs(y)))
    
    for t in times:
        if t >= 0:
            cur += 1
            result = max(cur, result)
        else:
            cur -= 1
    return result

a1 = interval(1,4)
a2 = interval(2,3)
a3 = interval(3,4)
a4 = interval(5,6)
meetings = [a1, a2, a3, a4]
print meeting_room(meetings)


'''
87.Maximum Sum Rectangle in Matrix Feb 16 2015
Given a 2D array, find the maximum sum subarray in it.

For example:
Given a matrix:
# http://www.geeksforgeeks.org/dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/
'''
def findmaxsum(matrix):
    if not matrix or not matrix[0]:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    result = 0
    for left in xrange(n):
        temp = [0 for i in xrange(m)]
        for right in xrange(left,n):
            for k in xrange(m):
                temp[k] += matrix[k][right]
            current = 0          
            tmp_sum = temp[0]
            for i in temp:
                current += i
                tmp_sum = max(current, result)
                current = max(0, current)
            result = max(result, tmp_sum)
    return result

m = [[1, 2, -1, -4, -20],[-8, -3, 4, 2, 1],[3, 8, 10, 1, 3], [-4, -1, 1, 7, -6]]
print findmaxsum(m)

'''
88. 输入是一个 N*N的矩阵，代表地势高度。如果下雨水流只能流去比他矮或者一样高的地势。
矩阵左边和上边是太平洋，右边和下边是大西洋。求出所有的能同时流到两个大洋的点。

For example:
Pacific: ~
Atlantic: *
~  ~   ~   ~   ~   ~  ~
~  1   2   2   3  (5) *
~  3   2   3  (4) (4) *
~  2   4  (5)  3   1  *
~ (6) (7)  1   4   5  *
~ (5)  1   1   2   4  *
*  *   *   *   *   *  *
括号里即为结果：
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
'''

def flow_water(matrix):
    if not matrix or not matrix[0]:
        return None
    n = len(matrix)
    result = []
    visited_pac = {}
    visited_alt = {}

    for i in xrange(n):
        visited_pac[(i,0)] = True
        search(visited_pac, matrix, i, 0)

    for i in xrange(n):
        visited_pac[(0,i)] = True
        search(visited_pac, matrix, 0, i)

    print "pac: ", visited_pac
    for i in xrange(n):
        visited_alt[(i,n-1)] = True
        search(visited_alt, matrix, i, n-1)

    for i in xrange(n):
        visited_alt[(n-1,i)] = True
        search(visited_alt, matrix, n-1, i)

    print "alt: ", visited_alt
    for key, value in visited_pac.items():
        if visited_alt.has_key(key):
            result.append(key)
    result.sort()
    return result        

def search(visited, matrix, x, y):
    n = len(matrix)
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    for d in dirs:
        new_x = x + d[0]
        new_y = y + d[1]
        if new_x >= n or new_x < 0  or new_y >= n or new_y < 0:
            continue
        if matrix[x][y] > matrix[new_x][new_y] or visited.has_key((new_x, new_y)):
            continue 
        visited[(new_x, new_y)] = True
        search(visited, matrix, new_x, new_y)

test = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print flow_water(test) 

'''
89. I was given this problem in an interview. How would you have answered?

Design a data structure that offers the following operations in O(1) time:

insert
remove
contains
get random element


Consider a data structure composed of a hashtable H and an array A. The hashtable keys are the elements in the data structure, and the values are their positions in the array.

insert(value): append the value to array and let i be it's index in A. Set H[value]=i.
remove(value): We are going to replace the cell that contains value in A with the last element in A. let d be the last element in the array A at index m. let i be H[value], the index in the array of the value to be removed. Set A[i]=d, H[d]=i, decrease the size of the array by one, and remove value from H.
contains(value): return H.contains(value)
getRandomElement(): let r=random(current size of A). return A[r].
since the array needs to auto-increase in size, it's going to be amortize O(1) to add an element, but I guess that's OK.
'''

def __init__(self):
    self.dict = {}
    self.array = []
    self.size = 0

def insert(self, number):
    array.append(number)
    self.dict[number] = self.size
    self.size += 1

def remove(self, number):
    if self.contains(number):
      index = array.index(number)
      if index != len(self.array) - 1:
          hash[array[-1]] = index
          array[index], array[-1] = array[-1], array[index]
      del array[-1]
      del hash[number]
      self.size -= 1
    else:
      return False

def contains(self, number):
    if number not in self.dict.keys():
      return False
    else:
      return True 

def get_random_ele(self, index):
    if index < len(self.array):
        return self.array[index]
    else:
        return False 

'''
四叉树压缩黑白图片，一个图片递归分成2x2四部分，如果一个区域颜色一样就设为叶子节点，算黑像素比例
follow up是给两个图片，把白色视为不透明，黑色视为透明，重叠在一起，返回一个图片，都用四叉树表示
这个递归不难，感觉做的不错，最后出了一个小bug，在他提示下改了

90.Given a quadtree structure:
struct QuadNode {
    QuadNode(int num_ones = 0) : ones(num_ones) {}
    int ones{ 0 };
    QuadNode* child[4]{ nullptr };
};
Please build a quadtree to represent a 0-1 matrix, assume the matrix is a square and the dimension is power of 2.
Given two such quadtrees with same depth, please write a function to calculate how many 1s are overlapped.
For example:
Matrix 0:
0 1
1 1
Matrix 1:
0 0
1 1
Your function should return 2.
'''
import collections

class QuadNode:
    def __init__(self, num=0):
        self.ones = num
        self.children = {}

class QuadTree:
    def __init__(self):
        self.root = QuadNode()

    def build_tree(self, matrix):
        if not matrix or not matrix[0]:
            return None
        n = len(matrix)
        self.root = self.build_helper(n, matrix, 0, 0)
        return self.root

    def build_helper(self, size, matrix, row, col):
        if size == 1:
            return QuadNode(matrix[row][col])

        node = QuadNode()
        size = size/2
        coord = [[row, col], [row+size, col], [row, col+size], [row+size, col+size]]
        for i in xrange(4):
            node.children[i] = self.build_helper(size, matrix, coord[i][0], coord[i][1])
            node.ones += node.children[i].ones
        return node


class Solution:
    def intersections(self, t1, t2):
        return self.intersections_helper(t1, t2, 0)

    def intersections_helper(self, t1, t2, sum):
        if not t1 or not t2 or not t1.ones or not t2.ones:
            return 0
        ret = sum
        if not t1.children or not t2.children:
            ret += (t1.ones & t2.ones)
        else:
            for i in xrange(4):
                ret += self.intersections_helper(t1.children[i], t2.children[i], sum)
        return ret

test1 = QuadTree()
test2 = QuadTree()
matrix1 = [[0,1],[1,1]]
matrix2 = [[0,1],[1,1]]
test1.build_tree(matrix1)
test2.build_tree(matrix2)
test = Solution()
print test.intersections(test1.root, test2.root)


'''
91.给你一组Treenode，他们每个有一个id，一个parentId，一个value，让你输出所有subtree的sum of value。
注意这个是没有children node的，只有parentId。
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=114594&extra=page%3D1%26filter%3Dsortid%26sortid%3D311&page=1
'''
class TreeNode(object):
    def __init__(self, id=0, parent=None, value=0):
        self.id = id
        self.parent = parent
        self.value = value
        self.level = 0
        self.sum = value
        
class Solution:
    def __init__(self):
        self.maxlevel = 0

    def all_sum(self, nodes):
        if not nodes:
            return
        for node in nodes:
            self.cal_level(node)

        level = {}
        for node in nodes:
            level.setdefault(node.level, []).append(node)

        for i in xrange(self.maxlevel, -1, -1):
            for node in level[i]:
                node.parent.sum += node.value            

    def cal_level(self, node):
        ret = 0
        if node.level != 0 and node.parent:
            return node.level
        if not node.parent:
            node.level = 0
        else:
            ret = self.cal_level(node.parent) + 1
            node.level = ret
            self.maxlevel = max(self.maxlevel, ret)
        return ret 


'''
92. 给一个0/1数组R代表一条河，0代表水，1代表石头。起始位置R[0]等于1，
初速度为1. 每一步可以选择以当前速度移动，或者当前速度加1再移动。只能停留在石头上。问最少几步可以跳完整条河流。

给定数组为R=[1,1,1,0,1,1,0,0]，最少3步能过河：
第一步先提速到2，再跳到R[2]；
第二步先提速到3，再跳到R[5]；
第三步保持速度3，跳出数组范围，成功过河

Sample solution like the following, always check the same speed and the speed + 1 part
we could use the similar solution like jump game II

if array[i+pre_speed]:
	max_reachable = max(max_reachable, i + pre_speed)
if array[i+pre_speed]:
	max_reachable = max(max_reachable, i + pre_speed + 1)
'''

int min_river_jumps_dp(const vector<int>& river) {
    if (river.empty()) return 0;
    vector<vector<pair<size_t, int>>> vp(river.size());
    vp[0].emplace_back(1, 1);
   
    int ret = INT_MAX;
    for (auto i = 0; i < vp.size(); ++i) {
        if (!river[i]) continue;
       
        for (auto pr : vp[i]) {
            if (i + pr.first >= vp.size()) {
                ret = min(pr.second, ret);
            } else if (river[i + pr.first]) {
                vp[i + pr.first].emplace_back(pr.first, pr.second + 1);
            }
            if (i + pr.first + 1 >= vp.size()) {
                ret = min(pr.second, ret);
            } else if (river[i + pr.first + 1]) {
                vp[i + pr.first + 1].emplace_back(pr.first + 1, pr.second + 1);
            }
        }
    }
    return ret == INT_MAX ? -1 : ret;
}


'''
93. Merge Two BST
You are given two balanced binary search trees.
Write a function that merges the two given balanced BSTs into a balanced binary search tree.
Your merge function should take O(M+N) time and O(1) space.
G家onsite题，算是很多小问题的综合题。因为不允许用extra space，可以先把两个输入BST给转换成链表，
然后merge两个链表，再把merge完的链表重新转化成BST。

#  注意用in-order的顺序来将BST转换为single linked list
#  注意可以用recursion的方法merge two linked list

'''

'''
94. Smallest Range
You have k lists of sorted integers. Find the smallest range that includes at least one number from each of the k lists.

For example,
List 1: [4, 10, 15, 24, 26]
List 2: [0, 9, 12, 20]
List 3: [5, 18, 22, 30]

The smallest range here would be [20, 24] as it contains 24 from list 1, 20 from list 2, and 22 from list 3.
G家题，实际上就是k路归并的变种题。维护一个长度为n的min heap（n为数组个数），每次找一个最小的，同时保持记录一个最大的。
比如那个例子：
heap初始化为[0,4,5]，min = 0, max = 5，当前最小range为[0,5]。
pop掉最小的再push，[4,5,9]，min = 4, max = 9，当前最小range还是[0,5]。
继续，[5,9,10]，min = 5, max = 10，当前最小range还是[0,5]。
继续，[9,10,18]，min = 9, max = 18，当前最小range还是[0,5]。
继续，[10,12,18]，min = 10, max = 18，当前最小range还是[0,5]。
继续，[12,15,18]，min = 12, max = 18，当前最小range还是[0,5]。
继续，[15,18,20]，min = 15, max = 20，当前最小range还是[0,5]。
继续，[18,20,24]，min = 18, max = 24，当前最小range还是[0,5]。
继续，[20,22,24]，min = 20, max = 24，当前最小range变成[20,24]。
'''

'''
94.
二维矩阵里面有obstacle，已知有k个点，求房间中离这k个点距离之和最短的那个点。
对所有的K个点做一次BFS，记录下每个点的最短距离和，最后扫一遍找出最小值即可。复杂度是O(K*N^2)，感觉有更优的解。
'''

import collections
from collections import deque

class Node(object):
    def __init__(self):
        self.visited = False
        self.dis = 0

def find_min_sum(matrix):
    if not matrix or not matrix[0]:
        return None
    m = len(matrix); n = len(matrix[0])
    food_queue = deque([])
    node_matrix = [[Node() for i in xrange(n)] for j in xrange(m)]
    for i in xrange(m):
        for j in xrange(n):
            if matrix[i][j] == 'P':
                food_queue.append((i,j))
    for q in food_queue:
        # reset all the nodes as Non-visited
        for i in xrange(m):
            for j in xrange(n):
                node_matrix[i][j].visited = False 
        # two queue to check the nodes around food 
        dis_queue = deque([0])
        node_queue = deque([q])
        # BFS, check the around nodes 
        node_matrix[q[0]][q[1]].visited = True
        while node_queue:
            node = node_queue.popleft()
            dis = dis_queue.popleft()
            row = node[0]; cal = node[1]
            cord = [[0,1],[0,-1],[1,0],[-1,0]]
            for c in cord:
                newrow = row + c[0]
                newcal = cal + c[1]
                if newrow < 0 or newrow >= m or newcal < 0 or newcal >= n:
                    continue 
                if node_matrix[newrow][newcal].visited:
                    continue 
                if matrix[newrow][newcal] == '1':
                    continue 
                node_matrix[newrow][newcal].visited = True 
                node_matrix[newrow][newcal].dis += dis + 1
                node_queue.append((newrow, newcal))
                dis_queue.append(dis+1)
    result = (1 << 31) -1
    result1 = []
    for i in xrange(m):
        for j in xrange(n):
            if matrix[i][j] == '0':
                if node_matrix[i][j].dis < result:
                    result = node_matrix[i][j].dis
                    result1 = [i, j]
    print result
    print result1

matrix = [["0","0","1","0"],["1","P","0","0"],["0","0","P","0"],["0","0","0","P"]]
find_min_sum(matrix)
                    
'''
95.
Rolling Ball Game Jan 6 2015
一个球从起点开始沿着通道，看能不能滚到终点。不过有限制， 每次球一走到底要不到边界，要不到障碍物，中间不能停留。 
可以上下左右走，然后让写个function 给定起点， 终点，和图，判断是不是solvable.
For example (1代表有障碍, 0代表可以通过):
'''
import collections
from collections import deque

def bolling_game(matrix, start, end):
    if not matrix or not matrix[0]:
        return False
    m = len(matrix); n = len(matrix[0])
    visited = {}
    visited[start] = True
    queue = deque([start])
    while queue:
        node = queue.popleft()
        next_pos = get_next(matrix, node[0], node[1])
        for p in next_pos:
            if p in visited:
                continue
            if p[0] == end[0] and p[1] == end[1]:
                return True
            visited[p] = True
            queue.append(p)
    return False

def get_next(matrix, x, y):
    m = len(matrix); n = len(matrix[0])
    next_pos = []
    stop = False
    for i in xrange(x+1, m):
        if matrix[i][y] == '1':
            next_pos.append((i-1, y))
            stop = True
            break
    if not stop and x != m-1:
        next_pos.append((m-1,y))

    stop = False
    for i in xrange(x-1, -1, -1):
        if matrix[i][y] == '1':
            next_pos.append((i+1, y))
            stop = True
            break
    if not stop and x != 0:
        next_pos.append((0, y))

    stop = False
    for i in xrange(y+1, n):
        if matrix[x][i] == '1':
            next_pos.append((x, i-1))
            stop = True
            break
    if not stop and y != n-1:
        next_pos.append((x, n-1))

    stop = False
    for i in xrange(y-1, -1, -1):
        if matrix[x][i] == '1':
            next_pos.append((x, i+1))
            stop = True
            break
    if not stop and y != 0:
        next_pos.append((x, 0))

    print "next: ", next_pos
    return next_pos


matrix = [["0","0","0","1"],["1","0","0","1"],["1","0","0","0"]] # True
matrix1 = [["0","0","0","1"],["1","0","1","1"],["1","0","0","0"]] # False
print bolling_game(matrix, (0,0),(2,3))
print bolling_game(matrix1, (0,0),(2,3))
                                          

'''
96.
一个 n x n 矩阵，每个房间可能是封闭的房间，可能是警察，可能是开的房间，
封闭的房间不能过，返回一个n x n矩阵，每一个元素是最近的警察到这个房间的最短距离。
初始矩阵中-1代表封闭房间，INT_MAX代表普通房间，0代表有警察的房间。

常规思路是对每一个警察做一次BFS，复杂度为O(n^3)。可以一开始找出所有警察，然后一起push到BFS的queue里面，同时搜索。复杂度可降为O(n^2)。
本题出现的频率还是很高的，比如还有这样的描述形式：
给一个matrix里面有人，墙和空格，把空格里填上需要走到最近的人那里的步数。

注意这题目与94题，找出到k个点最小距离的区别，
对于94题来说，我们要找出每个点到k个点的距离，所以对于每个点in k，需要遍历所有的相邻点 O(k*N^2)，
但是对于这题来说，只要找出最近的警察的距离，所以我们可以用一个queue，先将所有警察的点放入，
搜索邻接的点，然后再依次搜索邻接的点，这里是保证到最近的警察的最小距离的O(N^2).

Similar question:
Given a heatmap which is a 3 dimension matirx and define a movement rule: a point on the heatmap can only go down hill. 
Ask: given some points on the heatmap, find out the higest point that can meet all the given points.
说白了就是给个矩阵，上面都有自己的value，然后movement规定了只能从大的value走到小的value，然后再给几个点，问可以到这些点的最高的点是哪一个。

1. 将每个给定的点的坐标放入一个deque里面，然后依次对每个点做BFS,
2. 对于每个给定的点周围的点，如果这个点value > 给定的点，那么将这个点的数字+1
3. 然后再走一遍整个matrix，找到数字等于k的点，并且找出matrix最大的值。

optimization: 
1. 可以每次扫描一个点之后，只针对范围内的点再次扫描？
2. 从给定的点的最大值开始扫描？
'''

'''
97.3. given a probability = [.5 .1 .2 .2], label = [A B C D], write a data structure that generates the label based on the prob. 
我说先找cumulative probability［.5, .6, .8 1]， 然后弄个0～1之间的random数字比较过去找它的位置就好。
他就说有没有更快的方法。 其实他想叫我用binary search，但是我一直以为是不是有什么O（1）的解法，浪费了一些时间后才发现原来
他想要binary search， 最后弄出来了。
'''

'''
98.second is given a dict of words [aba, cbc], find the letter to letter probability. b->a 50%, b->c 50%. 这个做的还可以，有一个小bug

第4题是sorted。 letter of probability的题目是这样， 做一个27x27的matrix， 26 个代表字母，最后一个代表开始或者结束，
然后你每个字母走过去找它出现的次数，最后除一下row sum求概率就好。比如 [aba, acb]，a之后出现b的机率是50%， 出现c的几率是50%。 
b之后出现a的机率是50%，b最为结尾的几率是50%。 a作为开头的机率是2/3， a最为结尾的机率是1/3。

补充内容 (2015-7-18 05:50):
说错了， a－b的机率是1/3， a－c的机率是1/3， a－end的机率是1/3.

就是你要建一个表， 然后可以随时查一个字母后出现另外一个字母的机率。 比如a之后接b的机率是什么，c之后接k的机率是什么。
这些机率要从字典里算出来。
'''

'''
99.hamming distance between a and b, a, b < 2^64. 这题很快就做了出来。就是把a^b>>i &1  64 次。 然后他就说要想办法speed up，
说给我64G的ram。我想了很久最后说可以搞个2^8的字典，然后把a^b分8段比就好。 他就说为什么用8， 然后就问我2^8的字典要用多少空间. 
我没记空间大小的那些知识，所以不会做...几经提示后结论是可以用2^32的字典要4G空间，这样比两次就好。他最后又问说如果你用这个方法，
但是ram只有2g，那会发生什么情况。 我就说那会有error吧。他就说什么error。我说不出来。
他就说“you clearly have never used win 95 swap space”. 然后差不多就结束了。

就是建个字典比如 1010－》2， 1111-》4，1011-》3 这样的， 每个数字对应它的hammingdistance。 当你要查1001 0010这样的数字，
你只要把头尾两段分别查一下加起来就好。这样只要2个operation。
'''

'''
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=129346&extra=page%3D3%26filter%3Dsortid%26sortid%3D311%26searchoption%255B3046%255D%255Bvalue%255D%3D1%26searchoption%255B3046%255D%255Btype%255D%3Dradio&page=1
100.
第二轮来了个老硬，问了两个题，第一题先上来热身一下，问有好多个口袋，里面放了不同数量的硬币，并且口袋被从1到N标记了。两个人问游戏，
每次可以从口袋里拿出和标记数一样多的硬币，知道有一方不能再拿硬币为止，然后那个人就输了。问给定这样的口袋，谁会赢。
我一开始以为是之前地里有人遇到过的++--的string的那个题，但是听老硬说是个热身题，应该不会太难，再仔细一想，发现只要看一共可以做多少起拿硬币的动作，
如果是奇数次就是先手赢，偶数次就是后手赢。我说了想法，老硬哈哈一笑说，简单吧，我们就不写code了，现在正式上题。然后第二道来了，
也是我整个面试做的最不好的一道题。 

第二题还是有很多口袋，里面好多硬币，然后可以对第i个和第i+1个做combine，combine的cost是第i个和第i+1个口袋里硬币数的sum，问怎么样做combine可以都到
最少的cost。我一上来觉得这道应该用DP做，但是和老硬讨论了20分钟也没有什么好的方法，老硬似乎也不太满意，然后我就开始威逼利诱套hint，老硬说要把大case分成小case，
我一下反应过来是要brute force做recursion，然后5分钟秒掉code，不过最后还是让老硬抓出一个小bug。诶，估计要挂就是挂在了这一轮。
# http://blog.csdn.net/acdreamers/article/details/18039073
# http://www.cnblogs.com/titicia/p/4344765.html

'''


def stone_merge(stones):
    if not stones: return 0
    n = len(stones)
    dp = [[(1<<31)-1 for i in xrange(n)] for j in xrange(n)]
    isum = [0 for i in xrange(n)]
    isum[0] = stones[0]
    for i in xrange(1, n):
        isum[i] = isum[i-1] + stones[i]

    for step in xrange(n):
        i = 0; j = step
        while j < n:
            if step == 0:
                dp[i][j] = 0
            elif step == 1:
                dp[i][j] = stones[i] + stones[j]
            elif step > 1:
                tmp = isum[j] - (isum[i-1] if i > 0 else 0)
                for k in xrange(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + tmp)
            i += 1
            j += 1
            
    for i in xrange(n):
        print "dp: ", dp[i]
    return dp[0][n-1]

test1 = [13, 7, 8]
test = [7,13,7,8,16]
print stone_merge(test)

'''
similar question:
Least cost to cut a batten
The cost of cutting each segment is the cost of the segment length, an array is storing each end point,
For example:
[0, 3, 7, 8, 11, 12], the batten length is 12, there are 4 cuting point


int getMinCost(int a[], int n){
    if (NULL == a || n <= 1)
        return -1;
    int rec[100][100] = {0};
    for (int i = 2; i < n; i++){
        for (int j = 0; j < n-i; j++){
            int nMin = INT_MAX;
            for (int k = 1; k < i; k++)
                nMin=min(nMin,rec[j][j+k]+rec[j+k][j+i]+a[j+i]-a[j]);
            rec[j][j+i] = nMin;
        }
    }
   
    return rec[0][n-1];
}
'''

'''
101.
1.烙印，在面试前碰到了，刚刚好都等着，问我 你是哪个xxx么？ 我就是今天要面你的。。 当时我就心里想完了。。但是题目挺简单。
给一个infinite array 只有0 - 9 设计一个
def getprobability(n):得到某个数出现的概率。

我用的reservoie sampling 做的，然后我补充如果直接hashing 会overflow. 然后考虑到一multi thread情况，需要写两个函数，一个专门产生 sampling list
一个专门计算概率。 这里要有做个checker看看产生的list是不是有效，也就是 0-9数的概率和要为1
follow up:
现在你得到概率，你怎么按照概率产生刚刚的数。 
两个方法，第一个直接用刚刚的array random index取数，但是问题是如果是multithread 调用这样做有问题。 第二个方法：定时产生所有数的accumulate probablilty 根据这个probabolity array generate number即可。
答完烙印还挺满意，拍了照片。。
'''


'''
102. 
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=115853&extra=page%3D5%26filter%3Dsortid%26sortid%3D311%26searchoption%255B3046%255D%255Bvalue%255D%3D1%26searchoption%255B3046%255D%255Btype%255D%3Dradio&page=1
说是一次party完以后，有的人负责酒水费用有的人负责汽油费用有的人负责。。这样形成一个有向图的结构，A欠B多少钱，B欠C多少钱，C可能欠A、B分别多少钱，
问怎么reduce/combine到最后形成一些pairs，比如A欠B 20，C欠A20，reduce到最后只需要C给B20块就行。这个pairs表达的transactions做到最小。
这题想了半天跟他说dfs、然后一边走一边修改edge最后还是没给出一个具体的答案。看来本人脑子太笨。。。无法符合Google Coder的要求啊

第一轮第二题那个pair感觉应该是求二分图的最大权匹配。先把每个点拆成两个点，比如一个A只有出度，一个A'只有入度。然后在这个二分图里面求其最大权匹配。
网上搜这个：二分匹配总结（匈牙利算法+最大权+最小权）

Minimum vertex cover:
Formally, a vertex-cover of an undirected graph G=(V, E) is a subset V′ of V such that if edge (u, v) is an edge of G, 
then u is in V′, or v is in V′, or both. The set V′ is said to "cover" the edges of G. 
The following figure shows examples of vertex covers in two graphs (and the set V' is marked with red).
A minimum vertex cover is a vertex cover of smallest possible size.
途中每条边都有一个顶点在minimum vertex set 中
最小覆盖： 最小覆盖要求用最少的点（Ｘ集合或Ｙ集合的都行）让每条边都至少和其中一个点关联。

Maximal matching:
Given a graph G = (V,E), a matching M in G is a set of pairwise non-adjacent edges; that is, no two edges share a common vertex.
In other words, a matching M of a graph G is maximal if every edge in G has a non-empty intersection with at least one edge in M.
图中的每一条边，都有一个顶点和M中的定点相交
# http://dingdongsheng.cool.blog.163.com/blog/static/1186187552009431405995/
# https://en.wikipedia.org/wiki/Bipartite_graph

'''

'''
103.
web server使用多线程处理用户请求还是多进程处理，进程间怎么通信，线程和进程区别什么，什么是死锁，如何防止死锁，什么是virtual memory，
什么是page fault等等。然后写Pascal Triangle，写完他让我reduce空间复杂度到O(1)，
'''


'''
104.
问了一个二叉树的问题，找出二叉树中所有的重复子树
'''

'''
105.  
How many balanced binary tree there are with n leaf nodes? Prove and write codes.
http://ideone.com/PRusHP
'''


'''
106.
第一题, 找出一个二叉树的最深节点。
这个题目实际是送分给我的。结果我太紧张，用递归函数完成算法，但是把返回最深节点程序写成了返回最深深度。后来考官提醒我不对，
我方寸有点乱，推翻全部递归算法，重新用DFS写了一个非递归算法。结果虽然正确，但是过于复杂。后来想了想，
其实这个问题稍微修改一下原有递归算法就好了。面试官是个老白，人还算NICE。
'''
max_height = 0
result_node = tree_node(0)
def find_deepest_node(root):
    if not root:
        return None
    global max_height
    global result_node
    find_deepest_helper(root, 0)
    return result_node.val
    
def find_deepest_helper(root, height):
    global max_height
    global result_node
    if not root:
        return
    if not root.left and not root.right:
        if max_height < height:
            print "height: ", height
            max_height = height
            result_node = root 
    
    find_deepest_helper(root.left, height+1)
    find_deepest_helper(root.right, height+1)

max_height_left = 0
left_node = tree_node(0)
def find_deepest_left_node(root):
    if not root:
        return None
    global max_height_left
    global left_node   
    find_deepest_left_helper(root, 0, False)
    return left_node.val
    
def find_deepest_left_helper(root, height, isleft):
    global max_height_left
    global left_node
    if not root:
        return
    if not root.left and not root.right and isleft:
        if max_height_left < height:
            print "height: ", height
            max_height_left = height
            left_node = root

    find_deepest_left_helper(root.left, height+1, True)
    find_deepest_left_helper(root.right, height+1, False)

'''
107.
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=111785&extra=page%3D5%26filter%3Dsortid%26sortid%3D311%26searchoption%255B3046%255D%255Bvalue%255D%3D1%26searchoption%255B3046%255D%255Btype%255D%3Dradio&page=1
1. We can write a 3 level for loop body directly as follows:
    for (int i  = 0;  i < 56; ++i){
                do_something(i);
                for(int j = 0; j < 151; ++j){
                        do_something(j);
                        for(int k = 0; k < 151; ++k){
                                do_something(k);. 
                        }
                }
    }
   
However, when the levels are very deep (such as 50 levels), we cannot manually write the for loop body directly just like above codes. 
Given an array arr, where arr[i] represents the loop count at level i, write an iterative algorithm to implement the multi-level loop.

其实一开始我是用递归来解的，写完代码后面试官问递归有什么问题。问题就是递归是利用了线程的栈，
由于栈一般只有几百K，所以当层数很大时栈空间不够用。于是就自己在堆上创建空间来模仿栈 (其实就是层数大小的int数组)，
栈的每一层(数组的每个元素)记录该层已经做到第几步了。面试官对这个解法很满意，于是编程并写测试用例验证。

void multiLevelOperation(int *levelCountArr, int n) {
    if(n == 0) return;
    int *levelStack = new int[n + 1];
    int curSP = 0;
    levelStack[0] = 0;
    while(curSP >= 0) {
        if(curSP == n || levelStack[curSP] == levelCountArr[curSP]) {
            --curSP;
            if(curSP >= 0) ++levelStack[curSP];
        }
        else {        
            do_operation(levelStack[curSP]);
            levelStack[++curSP] = 0;
        }
    }
    delete [] levelStack;
}


# http://ideone.com/JAAQ4Y


'''

'''
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=106578
107. tic－tac－toe： 给一个board，以current state判断是o 赢， x 赢， 
还是没人赢。follow up每次只能取一行的信息，每次只能存储O（2N＋K）的数据
'''

'''
108. 给一个list和k（number）。找一个区域k，使得这个区域里k的最大值和最小值的差值最大，返回这个值。用heap或priority queue做dp。
'''

'''
109. tourament question:  input is players like（A,B,C,D）, print total rounds[[(A, B), (C, D)], [(A, C), (B, D)], [(A, D), (B, C)]]
'''

'''
110.
# http://www.mitbbs.com/article_t/JobHunting/32582249.html
第二轮是给一个int N，让输出所有的长度为N的valid string的个数，valid string的
定义是由A,B,C三种字母组成，并且在这个string中任意连续的三个字母不能包括A,B,C
三个字母，比如BACCA就不是valid string，因为前三个字母B,A,C包含了这三个字母。
我用了一个三维的DP做，但是边界条件没有写好
# similar question: https://github.com/UmassJin/Leetcode/blob/master/Experience/Fence_Painter.py
'''
def valid_string(n):
    dp_same = 3
    dp_dif = 0
    
    for i in xrange(n-1):
        dp_same, dp_dif = dp_same+dp_dif, dp_same*2 + dp_dif
    return dp_same + dp_dif


'''
111.
多叉树，每个节点是一个整数，求书中最长递增路径比如5,6,7,8,9
'''

'''
112.
第二题是个矩阵，每个节点是一个计算机，计算机之间传一个文件的cost是节点值x路径长度，选择所有计算机为接收端，求所有文件传输的cost
快速写了个暴力方法
尝试动态规划无果
后来想到可以cache所有行列的cost和，正这一边反着一遍，然后状态转移就是O(1)了，但是没时间写了，在他提议下写了一个一维特殊情况的代码，中间有个加号还忘了写，算是sloppy coding吧
希望大牛们指点一下这个题
'''

'''
http://www.1point3acres.com/bbs/thread-133413-1-1.html
113.
一堆密码箱，每个密码都是四位0-9之间，算一个暴力破解序列，包含所有可能的四位序列，让这个序列尽量短
给了一个贪心算法，代码写的比较长，而且没bug free.
'''

'''
114.
最后一轮，求sum(n^i) 就是1+n+n2+n3+...+n^N， 快速写了一个O(N)之后让我优化，
其实这个二分O(lgN)很容易想的，但是当时用了很长时间表现不太好。
'''

'''
115.
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. 
Determine the maximum value obtainable by cutting up the rod and selling the pieces. 
For example, if length of the rod is 8 and the values of different pieces are given as following, 
then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)

Example:
Pricing list: {1, 5, 8, 9, 10, 17, 17, 20}
Result = 22 (cut into two pieces of length 2 and 6)
'''

def rod_cut(price):
    '''
    args; return; raise
    '''
    if not price: return 0
    n = len(price)
    dp = [0 for _ in xrange(n+1)]
    for i in xrange(1, n+1):
        dp[i] = price[i-1]
        for j in xrange(1, i):
            dp[i] = max(dp[i], price[j-1] + dp[i-j])
    return dp[n]

price = [1, 5, 8, 9, 10, 17, 17, 20]
print rod_cut(price)


'''
116.
Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that 
maximizes product of lengths of all parts. You must make at least one cut. Assume that the length 
of rope is more than 2 meters.
Examples:
Input: 2, return 1 because 1x1 = 1
Input: 5, return 6 because 2x3 = 6
'''
def cut_rope(length):
    dp = [0 for i in xrange(length + 1)]
    for i in xrange(2, length+1):
        for j in xrange(1, i):
            dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
    return dp[n]
    
'''
这题还有一个O(n)的解法。当n>4的时候，
每次cut实际上都是按照每隔3来一次。比如n=5的时候，解就是3x2，n=7的时候，解就是3x4，n=10的时候，解就是3x3x4。
int cut_rope(int n) {
    if (n == 2 || n == 3) return n - 1;
   
    int ret = 1;
    while (n > 4) {
        n -= 3;
        ret *= 3;
    }
    return n * ret;
}
'''
    
'''
117.
Given an integer array, adjust each integers so that the difference of every adjcent integers are not greater 
than a given number target.
If the array before adjustment is A, the array after adjustment is B, you should minimize the sum of |A[i]-B[i]|
Note:
You can assume each number in the array is a positive integer and not greater than 100
Example:
Given [1,4,2,3] and target=1, one of the solutions is [2,3,2,3], the adjustment cost is 2 and it’s minimal. Return 2.

# https://github.com/UmassJin/Leetcode/blob/master/LintCode/Minimum%20Adjustment%20Cost.py
'''
    
'''
118.
Given an array of integers. Find two disjoint contiguous subarrays such that the absolute difference 
between the sum of two subarray is maximum.
Note: The subarrays should not overlap.

For example:
Array: { 2, -1, -2, 1, -4, 2, 8 }
Result subarrays: {-1, -2, 1, -4 }, { 2, 8 }
Maximum difference = 16
'''
 
def max_diff_two_subarr(array):
    """
    @ args:
    @ return:
    @ raise error:
    """
    if not array:
        return None
    n = len(array)
    left_max = list(array)
    left_min = list(array)
    right_max = list(array)
    right_min = list(array)
    sum_min = array[0]; sum_max = array[0]

    for i in xrange(1, n):
        if sum_min > 0: sum_min = 0
        if sum_max < 0: sum_max = 0
        sum_min += array[i]
        sum_max += array[i]

        left_min[i] = min(left_min[i-1], sum_min)
        left_max[i] = max(left_max[i-1], sum_max)

    sum_min = array[n-1]; sum_max = array[n-1]
    for i in xrange(n-2, -1, -1):
        if sum_min > 0: sum_min = 0
        if sum_max < 0: sum_max = 0
        sum_min += array[i]
        sum_max += array[i]
        
        right_min[i] = min(right_min[i+1], sum_min)
        right_max[i] = max(right_max[i+1], sum_max)
    print "left_max: ", left_max
    print "left_mix: ", left_min
    print "right_max: ", right_max
    print "right_min: ", right_min

    result = -1 << 31 
    for i in xrange(n-1):
        result = max((right_max[i+1] - left_min[i]), result)
    for i in xrange(1, n):
        result = max((left_max[i-1] - right_min[i]), result)
    print result
    
test = [2, -1, -2, 1, -4, 2, 8]
print max_diff_two_subarr(test)

[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python max_diff_subarr.py
left_max:  [2, 2, 2, 2, 2, 2, 10]
left_mix:  [2, -1, -3, -3, -6, -6, -6]
right_max:  [10, 10, 10, 10, 10, 10, 8]
right_min:  [-6, -6, -5, -4, -4, 2, 8]
16
None


'''
119.
Given a directed graph, check whether the graph contains a cycle or not. Your function should 
return true if the given graph contains at least one cycle, else return false. 
For example, the following graph contains three cycles 0->2->0, 0->1->2->0 and 3->3, 
so your function must return true.

有向图中存在环当且仅当这个图中有back edge。Back edge指的是一条从一个节点到自身或者到他的祖先的edge。
下图中有三条back edge（用x表示）。
然后用DFS做就好了。用一个vector或者set来保存当前DFS过程中经过的节点，如果已经经过，则有cycle。
注意每个顶点都要判断一次。
时间复杂度：
如果做一个full DFS, 时间复杂度是O(V^2 + VE)，但是这里我们在碰到之前已经访问过的节点就返回了，
所以每个节点只被访问一次，所以最终时间复杂度是O(V + E)。

'''
class Graph:
    def __init__(self, v, edge):
        self.V = v
        self.E = edge

def dfs(node, visited, backtrack):
    if not visited[node]: 
        visited[node] = True
        backtrack[node] = True
        for neighbor in node.neighbors:
            if not visited[neighbor] and dfs(neighbor, visited, backtrack):
                return True
            elif backtrack[neighbor]:
                return True
    backtrack[node] = False
    return False     

def detect_cycle_graph(graph):
    if not graph: return None
    visited = [False for i in xrange(graph.V)]
    backtrack = [False for i in xrange(graph.V)]
    
    for node in graph.V:  # Note, here we need to check each node 
        if dfs(node, visited, backtrack):
            return True
    return False
    

'''
120. Strongly Connected Graph 
# https://github.com/UmassJin/Leetcode/blob/master/Algorithm/Strongly_Connect_Graph.py
'''

'''
121. Maximum length of the loop 
Given an array
Indexes 0 1 2 3 4
Values 3 2 1 4 0
Values are the next index of the jump 0 -> 3 -> 4 -> 0... 1 -> 2 -> 1...
Write a function to detect if there are loops. If yes, get the max length of the loop possible, otherwise just return zero.
'''
def max_length_loop(array):
    def dfs(index, len):
        if visited[index]:
            result[0] = max(result[0], len-length[index])
            return 
        visited[index] = True
        length[index] = len
        dfs(array[index], len + 1)

    if not array:
        return 0
    n = len(array)
    visited = [False for _ in xrange(n)]
    length = [0 for _ in xrange(n)]
    result = [0]
    for i in xrange(n): # check each index in the array 
        dfs(i, 0)
    return result[0] 


test = [1,2,3,4,0]
print max_length_loop(test)


'''
122.
一个数组 A: 1 3 0 2 4 7
input: dest-node: A0
output: all the source nodes: (A1, A3, A4)

数组中每个元素表示他能走的步数，既能向左走 又能向右走，能到A[0]的点有A[1]和A[4]，A[1]可以走3步到A[4] A[4]能走4步道A[0]。
'''


import collections

def find_all_source(array, dest):
    if not array:
        return None
    graph = {}
    visited = {}
    result = []
    n = len(array)
    for i in xrange(len(array)):
        if array[i] == 0:
            continue
        if array[i] + i < n and array[i] + i >= 0:
            graph.setdefault((array[i]+i),[]).append(i)
        if i - array[i] < n and i - array[i] >= 0:
            graph.setdefault((i - array[i]),[]).append(i)
    
    visited[dest] = True
    queue = collections.deque([dest])
    while queue:
        node = queue.popleft()
        if node in graph:
            for src in graph[node]:
                if src not in visited:
                    result.append(src)
                    queue.append(src)
                    visited[src] = True
    return result 

test = [1,3,0,2,4,7]
print find_all_source(test, 0)


'''
122.
Count Numbers Jan 3 2015
Given an array of ages (integers) sorted lowest to highest, output the number of occurrences for each age.
For instance:
[8,8,8,9,9,11,15,16,16,16]
should output something like:

'''
def count_number(array):
    if not array:
        return None
    count = 0; step = 1; number = array[0]
    index = 0
    result = []
    n = len(array)
    while index < n:
        count += step
        step *= 2
        if index + step >= n or array[index+step] != number:
            step = 1
            if index + step < n and array[index+step] != number:
                result.append((number, count))
                count = 0
                number = array[index+step]
        index += step
    result.append((number, count))
    return result 

test1 = [8,8,8,9,9,11,15,16,16,16]
test2 = [1,2,3,4,5]
print count_number(test1)
print count_number(test2)


'''
123.
Interleave two linked-list
for example
Given
1->2->3->4
5->6
return 1->5->2->6->3->4
'''

ListNode * interleave(ListNode *p, ListNode *q) {
    if(!p && !q) return nullptr;
    if(!p) return q;
    if(!q) return p;
    q->next = interleave(p->next,q->next);
    p->next = q;
    return p;
}


'''
124.
第二轮是个阿三，感觉很吊的样子，一副大爷样地坐在那里，让我很不爽。他就问了很
简单的一道题，然后就是不停地问我如何改进。
2. Given a list of words, find two strings S & T such that:
    a. S & T have no common character
    b. S.length() * T.length() is maximized
Follow up: how to optimize and speed up your algorithm
'''


'''
125. given the level of the tree, find how many full trees are there. 
'''
def full_tree(level):
    '''
    @args: level is input level of the tree
    @output: how many full binary tree for this level
    @let's say need to calculate level 4's full tree
    @maintain the left tree as i-1, then right tree may have sum(dp[i-k] (2<=k<=i-1))
    @maintain the right tree as i-1, left is also sum(dp[i-k] (2<=k<=i-1))
    @and then add dp[i-1]*dp[i-1]
    '''
    if level == 0:
        return 0
    dp = [0 for _ in xrange(level+1)]
    dp[1] = 1; dp[2] = 1
    for i in xrange(3, level+1):
        tmp = 1
        for k in xrange(2, i):
            tmp = tmp * dp[i-k]
        dp[i] = dp[i-1] * (2 * tmp + dp[i-1])
        #dp[i] = dp[i-1] * tmp * 2 + dp[i-1] * dp[i-1]
    return dp[level]


print full_tree(3)
print full_tree(4)
print full_tree(5)


'''
126.
Given a BST and a number x, find two nodes in the BST whose sum is equal to x.
You can’t use extra memory like converting BST into one array and then solve this like 2sum.
# http://codercareer.blogspot.com/2013/03/no-46-nodes-with-sum-in-binary-search.html
'''


'''
127.Snake and Ladder Problem
# http://www.geeksforgeeks.org/snake-ladder-problem-2/
'''

'''
128. Given a snake and ladder board, find the minimum number of dice throws required to reach the 
destination or last cell from source or 1st cell. Basically, the player has total control over 
outcome of dice throw and wants to find out minimum number of throws required to reach last cell.
If the player reaches a cell which is base of a ladder, the player has to climb up that ladder 
and if reaches a cell is mouth of the snake, has to go down to the tail of snake without a dice throw.
# http://www.fgdsb.com/categories/Not-in-LeetCode/page/9/
# http://www.geeksforgeeks.org/snake-ladder-problem-2/
'''

import collections
from collections import deque

def snake_ladder(move, n):
    '''
    @ move: move[-1] means this is regular cell, move[i] != -1 
      means there is ladder or snake in this cell
    @ n: means the total number of the board 
    '''
    queue = [(0,0)]
    visited = {0:True}
    
    while queue:
        node = queue.popleft()
        index = node[0]
        cur_dis = node[1]
        
        while (move[index] != -1):
            index = move[index]
        for i in xrange(index+1, index+7):
            if i in visited:
                continue
            if i == n -1:
                return cur_dis + 1
            
            visited[i] = True      
            queue.append((i, cur_dis+1))
    return -1


'''
129.
define a tree, how to check whether a n-ary tree is unival tree (the value in each node is same). 
How to get how many unival tree in a n-ary tree  
'''

'''
130
'''
import random

def weighted_choice(seq):
    if not seq:
        return None
    total_value = sum(v for _, v in seq)
    random_value = random.randint(0, total_value-1)
    print "random_value: ", random_value
    pre = 0
    partial_sum = 0
    for value, i in seq:
        partial_sum += i
        if pre <= random_value < partial_sum:
            print ""
            return value
        pre = partial_sum
    return None


seq = [("a",3),("b",5),("c",8)]
print weighted_choice(seq)


'''
131.
http://www.mitbbs.com/article_t1/JobHunting/33021975_0_1.html
1.leetcode上原题  number of islands
2.follow up：count rank 2 islands, where a rank 2 island is an island inside
a lake located on a continent. A continent is a piece of land located in 
the ocean; the ocean is any body of water that touches the edges of the map.

Example:
000000000
000001100
001111100
011000100
001010100
001000100
001111100
000000000
上面这个例子里应该返回1.

3.If the input 2d array is too large to fit in memory, how to handle?

我从第二个follow up开始就回答的磕磕绊绊，最后也没写code，一直在跟面试官讨论
。后来思路终于讨论出来了，但第二个follow up面试官提示说water的那个dfs和第一
问里的dfs有什么不同，后来明白他想说water的dfs要考虑对角线情况。第三个follow 
up更是不知道怎么回答，瞎扯了一通。

请教各位大侠们，第三问该怎么考虑？
'''


'''
132. 给一个binary tree 打印所有的path~~然后问了时间空间复杂度~~就用一般递归做的
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=139354&extra=page%3D1%26filter%3Dsortid%26sortid%3D311&page=1
'''
 # 42. print out the path from root to the leaf in the binary tree
 
def print_path(root):
    if not root:
        return
    result = []
    print_path_helper(root, result, [])
    return result

def print_path_helper(node, result, subpath):
    if not node:
        return
    if not node.left and not node.right:
        result.append(subpath[:]+[node.value])  # Note: here we should use the subpath[:], not the subpath directly 
    else:
        print_path_helper(node.left, result, subpath+[node.value])
        print_path_helper(node.right, result, subpath+[node.value])

# time complexity: O(nlogn)
# space complexity: O(n)

>>> list1 = [1,2,3]
>>> result = []
>>> result.append(list1)
>>> result
[[1, 2, 3]]
>>> id(result[0])
4565113024
>>> id(list1)
4565113024
>>> list1.append(5)
>>> result
[[1, 2, 3, 5]]


'''
133.
2. good number问题。 一个数如果能用（至少两组）两个立方数相加得到那么就是good number。print小于等于n的所有good number。
   分析时间复杂度。
   我先把小于n的所有立方数存起来。然后就变成了2 sum问题了。。。
   
第二题答的是O(n^(4/3))，外层大循环是O(n)，里层的存的立方数是O(n^(1/3))，两个相乘。阿三考官嘟囔了半天我也没太听明白他到底什么意思= =
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=139354&extra=page%3D1%26filter%3Dsortid%26sortid%3D311&page=1
'''
import collections

def happy_number(n):
    if n == 0: return 0
    seq = []
    result = []
    for i in xrange(1, n+1):
        tmp = i * i * i
        if tmp > n:
            break
        seq.append(tmp)
    print "seq: ", seq 
    table = collections.defaultdict(int)
    for i in xrange(len(seq)):
        for j in xrange(i+1, len(seq)):
            table[seq[i]+seq[j]] += 1   
            if table[seq[i]+seq[j]] > 1:
                result.append(seq[i] + seq[j])
    print result
    
happy_number(500)

'''
134.Implement a function to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
'''
def compress_string(string):
    if not string: return None
    count = 1; i = 1
    cur = string[0]
    result = []
    while i <= len(string):
        if i < len(string) and string[i] == cur:
            count +=1
        else:
            result.append(cur+str(count))
            if i < len(string):
                cur = string[i]
            count = 1
        i += 1
    return ''.join(result)

print compress_string("aabccccaaadddddd")


'''
135. compress string 
For example, the string aabcccccaaa would become a*2b*1c*5a*3. the original string may still have 
number and *
'''

def compress_string(string):
    if not string: return None
    count = 1; i = 1
    cur = string[0]
    result = []
    while i < len(string):
        if cur.isdigit():
            result.append("#"+cur)
            cur = string[i]
            i += 1
        elif cur == "*":
            result.append("#"+cur)
            cur = string[i]
            i += 1
        else:
            while i < len(string) and string[i] == cur:
                count +=1
                i += 1
            result.append(cur+"*"+str(count))
            if i < len(string):
                cur = string[i]
            count = 1 
            i += 1
    return ''.join(result)

print compress_string("aa2*5bccc")
print compress_string("aa2*5bcccc3*aaadddddd")


'''
136. 
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=134847&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
Q)  Write a program to count the total number of pages reachable from a website.
For example, given "nytimes.com", count the number of pages reachable from there.
You can assume you are given a function to fetch the page and extract the inner links, e.g.:
List<String> fetchPageAndExtractUrls(String url);
'''
def fetch_pages(url):
    visited = {}
    total_url = [0]
    fetch_helper(url, total_url, visited)
    return total_url[0]

def fetch_helper(url, total_url, visited):
    children = fetchPageAndExtractUrls(url)
    if not children:
        return
    for child in children:
        if child not in visited:
            visited[child] = True
            total_url[0] += 1
            fetch_helper(child, total_url, visited)
            

'''
137.
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=134847&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
Q) Given a tiny computer with a 1 MHz CPU and 1 KiB of RAM memory;
no input;
only output is an LED light that says “I am done”.
(1 MHz == 1 million instructions per second)
I load an arbitrary unknown program onto this computer.. 
How long do we have to wait in wall-clock time before we can prove the program has an infinite loop?
'''
因为数据和程序都在内存中，所以，如果在某这两个时间点，内存中的内容处于完全相同的状态，
那么从这两个时间点之后的所有状态也一定会完全相同（除非这是台量子计算机）。
那么，如果一个程序在开始执行之后，内存先后出现两个完全相同的状态的话，那么这个程序一定是死循环。. 

1kilobyte = 2^13 bit, 所以该计算机内存可能存在的不同状态是2^14种。
因为每次instruction都一定会改变内存的状态（因为但凡有一次不改变，那就已经死循环了），
所以这个计算机最大能执行的不相同操作是2^14次（因为如果程序在2^14次操作中还没能停机，
那第2^14+1次操作一定和之前的2^14次操作中的某一个相同）。
又因为运行速度是1秒10^6 = 2^20次操作，因此在2^(-6) = 0.016秒内，就能够进行2^14次操作。
也就是说，如果0.016秒内还没能停下的程序，就永远不会停下了。


'''
138. 
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=138912&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
第二题，一道Math题。就是求float number 的squre root: public float sqrt(float f, int p)， 
precision是表示小数点后位数（2就要两位一致）。我就先找到result两边的integer标为l , r。 
然后就一阵二分法。问题是， 判断precision和大于一小于一时出错了。然后一阵改。。。。。
表示很无奈。这种math， corner cases特别多的没准备好。说好的array， string，说好的tree，说好的recursive呢，都没有。。.

判断数据是否符合精确度，就用两个数都乘以10^p，再取整比较是否相等。比如p=2， f=0.64, curRes = 0.639就不行因为
都乘以100以后取整是64， 和63不相等。 如果curRes = 0.645就没问题。

至于curRes，我就先二分法取到整数范围，比如8开平方根在（2,3）范围，再再（2,3)范围内二分，判断精确度。要注意的是，
（2,3）大于1和（0,1）小于一两种范围二分的时候方向不同。大于一越平方越大，小于一越平方越小

精确度要求是小数点平方根res的平方和要求根的数f，小数点之后p位要保持一致。所以比如p=2，如果res^2和f分别是1.50和1.501是可以的，
如果是1.499和1.50就不行了。然而这两个却都符合相差绝对值小于0.01
'''

def sqrt_float(num, p):
    '''
    @num: float number
    @p: precision after dot 
    '''
    if num <=0: return 0
    l = 0; r = num
    if num < 1: r = 1

    while l <= r:
        mid = (l + r) / 2.0
        print "l: %f, r: %f, mid: %f" %(l, r, mid)
        if mid * mid > num:
            r = mid 
        elif mid * mid < num:
            l = mid
        if judge_precision(num, mid*mid, p): 
            return mid 
    return None    
    
def judge_precision(num, res, p):
    if int(num*(10**p)) == int(res*(10**p)):
        print "res: ", int(res*(10**p))
        return True
    return False
        
print sqrt_float(1.6, 2)

[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python sqrt_float.py 
l: 0.000000, r: 1.600000, mid: 0.800000
l: 0.800000, r: 1.600000, mid: 1.200000
l: 1.200000, r: 1.600000, mid: 1.400000
l: 1.200000, r: 1.400000, mid: 1.300000
l: 1.200000, r: 1.300000, mid: 1.250000
l: 1.250000, r: 1.300000, mid: 1.275000
l: 1.250000, r: 1.275000, mid: 1.262500
l: 1.262500, r: 1.275000, mid: 1.268750
res:  160
1.26875


print sqrt_float(0.556, 2)

[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python sqrt_float.py 
l: 0.000000, r: 1.000000, mid: 0.500000
l: 0.500000, r: 1.000000, mid: 0.750000
l: 0.500000, r: 0.750000, mid: 0.625000
l: 0.625000, r: 0.750000, mid: 0.687500
l: 0.687500, r: 0.750000, mid: 0.718750
l: 0.718750, r: 0.750000, mid: 0.734375
l: 0.734375, r: 0.750000, mid: 0.742188
res:  55
0.7421875

'''
139.
Given an array of N=10^6 int32 and an int32 X, compute the exact number of triples (a, b, c) 
of distinct elements of the array so that a + b + c <= X
其实就是和3Sum差不多，不过写完被他问了可能的overflow问题，然后立马改了下就结束了

假设X很大，比如是2^31，而数组中的数字是1,2,3...10^6，那么数组中的每一个triplet都满足条件，
最后数出来的个数会是C(3, 10^6) ~= 2^58。这在C++中就必须上long long了。但是如果数组再稍微大一点，
比如到10^7的话，long long就可能hold不住了；所谓的overflow应该就是指这个。所以这个限制非常关键，
如果是面试官一开始主动提出来这个限制的话，我觉得算是比较良心的。

当然，三个int32的和会超过int32这也是一个重要的overflow的点。多谢指出。这两个overflow的点都可以通过使用long long进行规避
'''

'''
140
Binary Tree Maximum Path Sum
Can not have the near node in the final path 
'''
def maxpathsum_bt(root):
    if not root:
        return None
    result = [-1<<32]
    maxpath(root, result)
    return result[0]

def maxpath(node, result):
    '''
    return (include node, exclude node)
    '''
    if not node: return (0,0)
    l = maxpath(node.left, result)
    r = maxpath(node.right, result)
    
    isum = max(0, l[1]) + max(0, r[1]) + node.value
    result[0] = max(result[0], isum)
    include = node.value + max(0, l[1],r[1])

    isum = 0
    isum1 = max(0, l[0], l[1]) 
    isum2 = max(0, r[0], r[1])
    isum = isum1 + isum2
    result[0] = max(result[0], isum)
    exclude = max(isum1, isum2)

    return (include, exclude)
    
    


========================================================================================

'''
Design 
'''

This is just a plug, from me, for you to know about processes, threads and concurrency issues. 
A lot of interviewers ask about that stuff, and it's pretty fundamental, so you should know it. 
Know about locks and mutexes and semaphores and monitors and how they work. Know about deadlock 
and livelock and how to avoid them. Know what resources a processes needs, and a thread needs, 
and how context switching works, and how it's initiated by the operating system and underlying 
hardware. Know a little about scheduling. The world is rapidly moving towards multi-core, and 
you'll be a dinosaur in a real hurry if you don't understand the fundamentals of "modern" 
(which is to say, "kinda broken") concurrency constructs.

The best, most practical book I've ever personally read on the subject is Doug Lea's Concurrent 
Programming in Java. It got me the most bang per page. There are obviously lots of other books 
on concurrency. I'd avoid the academic ones and focus on the practical stuff, since it's most 
likely to get asked in interviews.


swap space 

 交换空间和虚拟内存的区别在于使用的系统不一样,产生的技术手段不一样,以下是详解,希望对你有所帮助! 
交换空间: 
Linux 中的交换空间（Swap space）在物理内存（RAM）被充满时被使用。如果系统需要更多的内存资源，而物理内存已经充满，
内存中不活跃的页就会被移到交换空间去。虽然交换空 间可以为带有少量内存的机器提供帮助，但是这种方法不应该被当做是对内存的取代。
交换空间位于硬盘驱动器上，它比进入物理内存要慢。 
交换空间可以是一个专用的交换分区（推荐的方法），交换文件，或两者的组合。 
交换空间的总大小应该相当于你的计算机内存的两倍和 32 MB这两个值中较大的一个，但是它不能超过 2048 MB（2 GB）。 
虚拟内存: 
虚拟内存是文件数据交叉链接的活动文件。是WINDOWS目录下的一个"WIN386.SWP"文件，这个文件会不断地扩大和自动缩小。 
就速度方面而言,CPU的L1和L2缓存速度最快，内存次之，硬盘再次之。但是虚拟内存使用的是硬盘的空间，为什么我们要使用速度最慢的硬盘来做 
为虚拟内存呢？因为电脑中所有运行的程序都需要经过内存来执行，如果执行的程序很大或很多，就会导致我们只有可怜的256M/512M内存消耗殆尽。
而硬 盘空间动辄几十G上百G，为了解决这个问题，Windows中运用了虚拟内存技术，即拿出一部分硬盘空间来充当内存使用。 


1 billion files  each file 4k you have more id than files, which means files are dupliacte.
your computer has 4k memory 1TB disk.
design a method to remove duplicate files and store those files
given id track the file from your disk...

做法是  hashing files to disk and store the id. but hashing always has collusion, which means you need to  have another map<id, location>
写完简单的想法大哥拍了照片。。。然后follow up了一下我加了几个case 大哥又拍了照片。。。因为都是psudo code.... 我只用python....可是这题明显没法用。。. 
讲起来很复杂，后来才知道是google big table 但是是在准备材料system design的倒数第二条。。。.


# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=106364&extra=page%3D2%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3089%5D%5Bvalue%5D%5B3%5D%3D3%26searchoption%5B3089%5D%5Btype%5D%3Dcheckbox%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
有N个node,每个都不停的向外发送timestamps,具体发送哪些timestamp是每个node决定的,从其他node来说是随机的.现在要收集这些node发送的所有timestamp.
如果某个timestamp被发现从超过99%的node上发送出来,记录下来.需要怎么做?这些timestamp很多,是不能完全放进去内存里面的.如果node非常多,怎么scale?
我给的方案是用HashMap<Timestamp, count>,分布存到多台机器上面。阿三表示数据很多，每台机器的内存都存不下，让我优化。我的进一步方案是再设定一个时限T，
过期的数据可以丢掉。阿三要求进一步优化。我的再进一步方案是对于这个时限T再分割成n个小格。这个n需要通过实验根据具体实际情况来确定。
如果在T／n时间里面，某些Timestamp的count小于某个设定值，比如0.01N，认为这个timestamp被收集到0.99N的可能性已经趋近于0，可以忽略了，
从HashMap里面删除。最后阿三还是表示不满意，不能完全理解我的方案



面试官看上去有点百度的张曈气质，一上来就气势汹汹的问了个google的cas，一个分块存储的文件系统，给你一个read block的接口和write block的接口，
要求把一个文件存储到这个系统上，设计一个读一个文件，和一个写一个文件的类，并实现。。。。写完就没时间了，还出了个bug。。。。。。。
面试官感觉很不满意


#http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=116504&extra=page%3D5%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
第三题，设计一个 KEY-VALUE机制，必须在O(1)做下列操作: 插入，删除，get(),random_get（）,可以使用hashmap.
这个题目非常tricky. 貌似可以直接使用一个HASHMAP就能完成，但是实际上random_get必须把每个K-V对与一个0到N的整数关联，这个如果直接
把MAP放到一个LIST里面去，算法效率就变成了O(N). 我最终使用了两个HASHMAP来实现这个功能，一个HASH表记录0-N的整数下标与KEY的关系，
另外一个HASH表记录K-V，还有这个下标。这个算法其实在删除时也有问题，因为删除后会有下标GAP.我实际上是使用了一个机制，让删除操作，. 1point3acres.com/bbs
每次只删除HASH表最后那个K-V值（之前让最后值与删除值换个位置）。面试官是个亚裔小年轻，非常NICE.


# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=129355&extra=page%3D3%26filter%3Dsortid%26sortid%3D311%26searchoption%255B3046%255D%255Bvalue%255D%3D1%26searchoption%255B3046%255D%255Btype%255D%3Dradio&page=1
'''
你好，那我就讲一下music list那道题吧：
你有一个music的播放列表，里面的歌曲unique，但是播放列表的长度未知。
这个音乐播放器APP有两个模式：random模式和shuffle模式。
random模式就是每次随机播放列表里的一首歌；
shuffle模式就是shuffle列表里的歌，然后顺序播放，放完以后重新shuffle，再顺序播放；
现在给你一个播放历史记录，要求你写一个函数来判断用户使用的是random模式，还是shuffle模式。
'''


'''
# http://www.1point3acres.com/bbs/thread-135955-1-1.html
3. design: distributed game ,   付费转账 如何 减少 transcation fee 
4. group Card  ,  follow up: 如何定义接口 让客户可以自己定义 hashfunction. 
'''

'''
1. 系统设计：给一个url和一个给定的api可以返回所有从这个url可以直接链接到的url。要求统计所有能访问到url数。
结果先让我coding，我以为搞错了，后来coding完了，followup就是怎么解决scalable的问题，给定的那个API有什么问题
以及怎么改进（最后引申到设计web crawler），怎么解决url无效等等问题。


2. 第一题local minimum，第二题在数组中检查x距离内是否有重复。

3. 1000个文件每个有1TB的大小，服务器每台100GB内存，1TB硬盘。文件基本上一次写入就不会变化了，读的次数比较多。问怎么设计这样的系统。followup怎么解决fault tolerance，再增加1000个这样文件，怎么办，等等。
* if reads are more frequency than write, we should keep Availability (low latency) than Consistency, since write may be very 
small, we could use the cache to save the logs. 
* Total amount of file is 10^3 * 10^12 = 10^15; 100GB = 100 * 10^9 = 10^11B main memory, 10^13B Disk, use the latest Recent Cache.
* If there are many servers, could use the Quorums to ensure the consistency, choose W=N and R=1 to ensure the quick read.

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

1.2 system design：一种新型的storage，怎么样用来scan engineer的hard disk来做备份
4. system design：logging query － 有好几个小问，例如，如何得到过去一个月浏览某主页的次数，来自某个国家的浏览数，等等

5. design: chromecast, how to know which app can be supported? There is a 
cloud that can give the information to the chrome cast, appID, deviceID, 
cache design. 

3. design: distributed game ,   付费转账 如何 减少 transcation fee 
4. group Card  ,  follow up: 如何定义接口 让客户可以自己定义 hashfunction. 


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

Such abbreviations are not always unique -- for example, “a11y” could stand for “accessibility”, “automatically”, etc. 
Given a list of words, determine if the abbreviation of the word is unique. 


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


'''
onsite:
1. find the shortest distance for each unlocked cell in matrix (警察那题)
2. find whether three points in the same line, if in the same line, the rate is 1.0, otherwise is 0
3. game, matrix, each matrix is dead or alive, if x < 2, died, if x > 3 died, if x = 3, alive, others maintain the same 
4. two rows array, find the minimum obstacle need to move if we want to move from the top left to right down 
   do the in-order for the two trees, use the minimum space, less than O(n), maybe O(logn)
'''
