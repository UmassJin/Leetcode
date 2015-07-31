####Good Reference
*[Heapify in Python](http://interactivepython.org/runestone/static/pythonds/Trees/heap.html)

*[Heap Sort](http://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/Sorting/heapSort.htm)

#### Attribute
* In our heap implementation we keep the tree balanced by creating a complete binary tree. A complete binary tree is a tree in which each level has all of its nodes. The exception to this is the bottom level of the tree, which we fill in from left to right.

##### [Find the kth maximum number in unsorted array](http://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/)

```python

def minChild(heaplist, i, length):
    if i * 2 + 1 > length:
        return i * 2
    else:
        if heaplist[i*2] > heaplist[i*2 + 1]:
            return i*2 + 1
        else:
            return i*2

def heapify(heaplist, i, length):
    while (i*2) < length:
        minc = minChild(heaplist, i, length)
        if heaplist[i] > heaplist[minc]:
            heaplist[i], heaplist[minc] = heaplist[minc], heaplist[i]
        i = minc # important!    

def build_heap(alist,k):  
    length = k
    i = length // 2
    alist.insert(0,0) # Add 0, so the count is based on 1 other than 0 !!!
    heaplist = alist # Can not use heaplist = alist[:] !! this is the copy !!
    while i > 0:
        heapify(heaplist, i, length)
        print "i: ", i
        i -= 1

def heap_find_kth_num(num,k):
    build_heap(num,k)
    num.pop(0)  # Need to pop the 0 !!!
    print "num: ", num
    for p in xrange(k, len(num)):
        if num[p] > num[0]:
            print "num[p]:  ", num[p]
            num[p], num[0] = num[0], num[p]
            build_heap(num, k)
            num.pop(0)
    print "num: ", num
    return num[0]        
        
    
array = [15,8,4,7,5,3,1,2,6]    
heap_find_kth_num(array, 5)

```

#### Create a min_heap for a array 
```python

class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        if not A: return 
        n = len(A)
        index = n/2 - 1
        for i in xrange(index, -1, -1):
            self.heapify_min(A, i, n)
        return 
    
    def heapify_min(self, A, start, end):
        root = start
        while (2*root + 1) < end:
            i = 2 * root + 1
            if i + 1 < end and A[i+1] < A[i]:
                i = i + 1
            if A[i] < A[root]:
                A[i], A[root] = A[root], A[i]
            root = i 

```

* Time complexity:
* Heapify: O(lg n)
* Build-Heap: O(n)
    * [why build heap is O(n)](http://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf)
    * [stack flow](http://stackoverflow.com/questions/9755721/build-heap-complexity)
* Heap Sort: O(nlogn)
* Extract-Max: O(logn)

* 注意 heapify 只是建立一个最小堆，而并不是数组最后就是有序的，例如 下面这个例子，对于input array，after call
* the heapq.heapify(data) 我们建立了最小堆，但是数组最后的结果并不是有序的，倘若我们不用heapify实现，用自己的
* function实现，我们需要从数组的 length//2 到0开始遍历，假设为i, 对于每一个i，我们要保证它下面为最小堆
* heapify  为O(logn)，但是针对所有的O(n)一次建立heap，为O(n) 复杂度

```
import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

print 'random    :', data
heapq.heapify(data)
print 'heapified :'
show_tree(data)
$ python heapq_heapify.py

random    : [19, 9, 4, 10, 11, 8, 2]
heapified :

                 2
        9                 4
    10       11       8        19
------------------------------------
```


#### Heap use ```__cmp__```
##### How could we sort the string "abc" and "adef" (which are sorted in each string)?

```python
import random
from random import randint
import heapq

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

def merge_karray(files):
    '''
    @ input files list: [file1, file2, file3...]
    @ output:
    '''
    if not files: return None
    heap = []
    result = []
    k = len(files)
    for i in xrange(k):
        ele = files[i]
        if ele:
            heap.append((MyLine(ele), i))
    heapq.heapify(heap)

    while heap:
        element = heapq.heappop(heap)
        value, file_index = element[0], element[1]
        result.append(value.string)
    return result

if __name__ == '__main__':
    lines = []
    for i in xrange(5):
        lines.append('abc' + str(randint(1,200)))
        lines.append('efg' + str(randint(1,200)))
        lines.append('xyz' + str(randint(1,200)))
    print merge_karray(lines)

```

##### Uber phone interview
```python
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


```


* [Merge K sorted linked list](https://github.com/UmassJin/Leetcode/blob/master/Array/Merge_K_Sorted_Lists.py)
* [Merge K sorted array](https://github.com/UmassJin/Leetcode/blob/master/Experience/Merge_k_sorted_array.md)
* [Good Video about how to make max heap](https://www.youtube.com/watch?v=WsNQuCa_-PU)
* [Median in stream data](https://github.com/UmassJin/Leetcode/blob/master/Experience/Median_in_stream_data.py)
* [Find K closet points](https://github.com/UmassJin/Leetcode/blob/master/Experience/K_closet_points.py)
