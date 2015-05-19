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


#### Reference
* [Algorithm Sort Summary](http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/)
