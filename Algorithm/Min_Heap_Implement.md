####Good Reference
*[Heapify in Python](http://interactivepython.org/runestone/static/pythonds/Trees/heap.html)

*[Heap Sort](http://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/Sorting/heapSort.htm)

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
* Time complexity:
* Heapify: O(lg n)
* Build-Heap: O(n)
* Heap Sort: O(nlogn)
* Extract-Max: O(logn)

* [Merge K sorted linked list](https://github.com/UmassJin/Leetcode/blob/master/Array/Merge_K_Sorted_Lists.py)
* [Merge K sorted array](https://github.com/UmassJin/Leetcode/blob/master/Experience/Merge_k_sorted_array.md)
* [Good Video about how to make max heap](https://www.youtube.com/watch?v=WsNQuCa_-PU)
