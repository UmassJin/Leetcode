##Table of Content
####[1. Bubble Sort](#bubble-sort)
####[2. Selection Sort](#selection-sort)
####[3. Insertion Sort](#insertion-sort)
####[4. Shell Sort](#shell-sort)
####[5. Merge Sort](#merge-sort)
####[6. Quick Sort](#quick-sort)
####[7. Heap Sort](#heap-sort)


## Bubble Sort
##### Introduction：
* 冒泡排序的原理非常简单，它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。

##### Procedure：
    * 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    * 对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。
    * 针对所有的元素重复以上的步骤，除了最后一个。
    * 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

##### Optimization:
    * 优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。用一个标记记录这个状态即可。
    ＊优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序，不用再排序了。因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。

##### Code:

```python
def bubble_sort(array):
    length = len(array)
    for i in xrange(length):
        for j in xrange(1,length-i):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array


def bubble_sort2(array):
    length = len(array)
    for i in xrange(length):
        flag = 1
        for j in xrange(1,length-i):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                flag = 0
        if flag:
            break
    return array

def bubble_sort3(array):
    length = len(array)
    k = length
    for i in xrange(length):
        flag = 1
        for j in xrange(1,k):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                k = j 
                flag = 0
        if flag:
            break
    return array 
```

##### Time Complexity 
    * Best: O(n), the input array already in the sort condition
    * Worst: n + (n-1) + (n-2) +.. 1 = O(n^2/2)
    * Average: O(n^2/2)



## Selection Sort
##### Introduction：
      * 选择排序无疑是最简单直观的排序。它的工作原理如下。
##### Procedure：
      * 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
      * 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
      * 以此类推，直到所有元素均排序完毕

##### Code:

```
def selection_sort(array):
    length = len(array)
    for i in xrange(length):
        imin = i
        for j in xrange(i, length):
            if array[j] < array[imin]:
                imin = j
        array[imin], array[i] = array[i], array[imin]
    return array

```

##### Time Complexity 
    * Best: O(n^2/2)  
    * Worst: n + (n-1) + (n-2) +.. 1 = O(n^2/2) 
    * Average: O(n^2/2)


## Insertion Sort
##### Introduction:
    * 插入排序的工作原理是，对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    
##### Procedure:
    1. 从第一个元素开始，该元素可以认为已经被排序
    2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
    3. 如果被扫描的元素（已排序）大于新元素，将该元素后移一位
    4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
    5. 将新元素插入到该位置后
    6. 重复步骤2~5


##### Code:

```python
def insertion_sort(array):
    length = len(array)
    for i in xrange(1,length):
        if array[i] < array[i-1]:
            tmp = array[i]
            index = i
            for j in xrange(i-1,-1,-1):
                if tmp < array[j]:
                    array[j+1] = array[j]
                    index = j
            array[index] = tmp
    return array

```

##### Attribute:
    * 交换操作和数组中导致的数量相同
    * 比较次数>=倒置数量，<=倒置的数量加上数组的大小减一
    * 每次交换都改变了两个顺序颠倒的元素的位置，即减少了一对倒置，倒置数量为0时即完成排序。
    * 每次交换对应着一次比较，且1到N-1之间的每个i都可能需要一次额外的记录(a[i]未到达数组左端时)

##### Time Complexity:
    * 最坏情况下需要~N^2/2次比较和~N^2/2次交换，最好情况下需要N-1次比较和0次交换。
    * 平均情况下需要~N^2/4次比较和~N^2/4次交换


## [Merge Sort](http://algs4.cs.princeton.edu/22mergesort/)
##### 核心：将两个有序对数组归并成一个更大的有序数组。通常做法为递归排序，并将两个不同的有序数组归并到第三个数组中。
##### [Merge Sort Wiki](http://en.wikipedia.org/wiki/Merge_sort)

##### Procudure:
      * 先将array二分化为n/2, n/2，递归一直到每个数组的长度为<=1:
      * Merge: Go through each part of two array, 依次比较，然后找出最小的数，直到两个数组都为， 或者其中一个数组为0，再拷贝另一个数组即可.
      
##### Code:

```python
def merge_sort(array):
    if len(array) <= 1: return array

    mid = len(array)/2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    array = merge(left, right)
    return array

def merge(larray, rarray):
    result = []
    lstart = 0
    rstart = 0

    while lstart < len(larray) and rstart < len(rarray):
        if larray[lstart] < rarray[rstart]:
            result.append(larray[lstart])
            lstart += 1
        else:
            result.append(rarray[rstart])
            rstart += 1

    if lstart < len(larray):
        result += larray[lstart:]

    if rstart < len(rarray):
        result += rarray[rstart:]

    return result
```

##### Time Complexity:
      * T(n) = 2T(n/2) + n  --> O(nlogn)
      * [Master Theorem](http://en.wikipedia.org/wiki/Master_theorem)


## Quick Sort


#### Reference
* [Algorithm Sort Summary](http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/)
* [Different Sort - Git](http://yuanbin.gitbooks.io/algorithm/content/basics_sorting/merge_sort.html)
