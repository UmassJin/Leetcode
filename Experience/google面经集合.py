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
8. 让你设计个matrix class，提供两个方法：update(x, y) & query(x1, y1, x2, y2)，update方法是update matrix上一个cell的值，
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
'''

'''
9. 题目是给一个string,一个set of string, 问string里面是否包含一个substring，使得这个substring的任意一个prefix + suffix能
组合成set里面的任意一个string，能就返回true，否则返回false
是这样，我少说了个条件，输入除了一个string和一个set of string,还有个整形变量len表示set里面每个string的长度（
也就是说set里的string长度都是一样的）。比如input string is "whoisyourdaddy", input set 包含两个 string "whu" and "ddy"，
那么function应该返回true，因为给的input string里面的substring "whoisyou" 的 prefix "wh" 和 suffix "u" 组成了 "whu"，
而另一个substring "daddy" or "ddy" 的 prefix "d" 和 suffix "dy" 组成了 "ddy"，因此这个例子里set里面所有的string都可以在
input string里面找到一个substring的一个prefix+suffix组合构成。
'''


'''
10. 给一个List，里面存着一些一个双向链表上的结点，这个List里面所有在双向链表上邻接的结点组成一个strong component，
求List里strong component的个数

给你个双向链表 1 <-> 2 <-> 4 <-> 7 <-> 9 <-> 11
给你个List里面有1,2,7,9,11, 那么 1,2组成一个strong component，7,9,11组成一个strong component。
解法就是建个HashSet然后把List里面的结点全丢进去，遍历一遍double linked List，遇到一个在HashSet里面的结点就从这个结点开始把所有
能到的在List里面的邻接结点从HashSet里面删掉，count++。换言之就是简易版的图遍历。
'''


'''
11.
实现linux的diff命令，我就好好的问清楚了她期望的输入和输出，然后用java开始写，期间写遍历文件系统的function的时候一时半会想不起来java里相关的API了，
就跟妹子问咋办，妹子说不要求非要死记硬背API，你自己想想有什么API比较make sense的在白板上注明一下就行了，我正好这段时间上班就是写python干类似的事，
就一股脑把python的相关API在白板上注明出来，然后接着写代码。。写完后又大概跟妹子提了提如果给的路径下如果有symbolic link该怎么处理，妹子表示很满意。。
follow-up是怎么判断两个文件内容是否相同，文件太大怎么优化。.

第三题主要思路就是遍历两个输入路径，把路径树中的所有叶子结点找到（包括file和empty folder），把对应的相对路径拿出来放进对应的两个set里，
然后就是同时遍历两个set，找第一个set里没有的而第二个set里有的（+），以及第一个set里有的而第二个set里没有的（-），遇到相对路径相同的file
就转化为绝对路径读file content用md5算下hash value，比较看看内容是否一致。
'''

# CTCI
'''
from random5 to get random7
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
Google Interview
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

