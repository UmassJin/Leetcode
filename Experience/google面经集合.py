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
Follow up: 如果是大地圖怎麼處理, 要你切 map, 考慮每個 submap 之間的關係. visit 1point3acres.com for more.
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
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
# http://www.geeksforgeeks.org/counting-inversions/
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

4. tic-tac-toe，给定场景是人机大战，人永远先开始下。要求把所有的棋盘布局组合都输出（人机各走一步算一个新的棋盘布局）。本轮有shadow。

5. 保龄球计分，给一组分数，输出实际每轮投完后的累计得分。

偏向c++功底跟concurrency。实现memcopy，还有就是实现一个银行的类里面的几个算法，都很简单，但是对多线程调用的加锁需要有了解。最后又问了一个实现每次调用，运行5秒，期间不停循环自增的简单算法，
follow-up是如何应对系统管理员尴尬地恰巧在这段时间内改了系统时间

'''
