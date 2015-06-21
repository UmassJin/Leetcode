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
find h index element in the array, at least n elements in the arrary larger than n, but here is no n+1 elements larger than n+1
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
给一个数，要求把这个数分解成一些平方数的和，并且要求使用最短的平方数list 如 13 = 9 + 4 而不是 13 = 4+4+4+1
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
