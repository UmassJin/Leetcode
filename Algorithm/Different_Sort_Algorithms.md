##Table of Content
####[1. Bubble Sort](#bubble-sort)
####[2. Selection Sort](#selection-sort)
####[3. Insertion Sort](#insertion-sort)
####[4. Shell Sort](#shell-sort)
####[5. Merge Sort](#merge-sort)
####[6. Quick Sort](#quick-sort)
####[7. Heap Sort](#heap-sort)


## Bubble Sort
##### 介绍：
* 冒泡排序的原理非常简单，它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。

###### 步骤：
    * 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    * 对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。
    * 针对所有的元素重复以上的步骤，除了最后一个。
    * 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。


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


#### Reference
* [Algorithm Sort Summary](http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/)
