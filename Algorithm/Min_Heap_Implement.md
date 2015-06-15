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

* [Merge K sorted linked list](https://github.com/UmassJin/Leetcode/blob/master/Array/Merge_K_Sorted_Lists.py)
* [Merge K sorted array](https://github.com/UmassJin/Leetcode/blob/master/Experience/Merge_k_sorted_array.md)
* [Good Video about how to make max heap](https://www.youtube.com/watch?v=WsNQuCa_-PU)
