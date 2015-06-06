#### What do you consider aside from Big-O time complexity?
##### 1. constant factor (e.g. selection sort/insertion sort)
    * selection sort: O(n^2/2); insertion sort: O(n^2/4)
    
##### 2. how large is N (e.g. quick sort + insertion sort)
    * sometimes we need to combine quick sort and insertion sort
##### 3. special constraint (e.g. O(nk) insertion sort for k-sorted array)    
##### 4. space’s implications on performance (memory hierarchy)
##### 5. memory access pattern (e.g. top-k problem, linked-list/array)
    * for example, top-k problem, we could have two methods
    * 1) create a N-max heap, and choose each max valuse in the top root, O(klogN + N)
    * 2) create a k-min heap, and for each value in the rest array, update heap, O((N-k)logN + N)
    * 3) even through the second time complexity is larger than the first one, we still chosse second one since it has less memory access. 
##### 6. bottleneck/hotspot profiling 
##### 7. trade accuracy for performance (e.g. sliding window average)
    * For example: we have the streaming data, need to calculate sliding window average 
    * let's say the sliding windwo size is 5, have one request came in, we calculate 5 numbers average.
    * we could use the buffer which size is 5 ,  O(k) 的复杂度
    * Optimization, we could calculate use new_average = (old_average * 5 - old + new ) / 5 ==> O(1) 
    * But the above optimization method has one problem, since the streaming data maybe is the floating data, 
      so (a + b) + c != a + (b + c), after many datas, there will be a large error 误差
    * 解决方法: we could calculate the 5 numbers average when arrival 1000th number, then use O(1) to continue to calculate. 
    
##### 8. compiler options
##### 9. * pipeline, super-scalar, branch prediction
##### 10. parallelism (e.g. matrix multiplication)


#### Number everyone need to know
![pic](https://cloud.githubusercontent.com/assets/9062406/7668842/0a028a40-fc05-11e4-9af5-75250c22e655.png)

* Network 比disk, SSD 都要快，但是它在建立TCP connection的时候，会有round trip latency, 例如发送2KB data very fast,
* 但是如果从加州send到欧洲，会有round trip latency


###[Big O](http://bigocheatsheet.com/)
* Time Complexity - The amount of time needed to finish the task
* Space Complexity - The amount of memory needed to store values/variables

#####[Master Method](http://www.cs.cornell.edu/courses/cs3110/2012sp/lectures/lec20-master/lec20.html)
```T(n) = aT(n/b) + f(n)```
* 其中a是每次每次recursion有几次call, b是recursion的长度变为原来的n/b
* 结论分三种情况讨论，需要对比T(n-1)的复杂度和f(n)的复杂度  
  T(n-1)复杂度算法是 O(T)= n ^ (loga/logb)， f(n)的一般比较直观，O(f) = n ^ x, 所以变形为比较loga/logb和x的大小
  * 前者大, 则结论是O(T)
  * 两者一样大, 则结论是 O(n^x * logn)
  * 后者大, 则结论是O(f)

####[Duke大法](http://www.cs.duke.edu/~ola/ap/recurrence.html)
#####步骤
1. 写出Master Method方程
2. 写出base case T(1) = ??
3. 将递推式转化为通项式

| Recurrence | Algorithm    | Big-O Solution |
| --- | :---: | :---: |
| T(n) = T(n/2) + O(1) | Binary Search | O(log n) |
| T(n) = T(n-1) + O(1) | Sequential Search | O(n) |
| T(n) = 2 T(n/2) + O(1) | tree traversal | O(n) |
| T(n) = T(n-1) + O(n) | Selection Sort (other n2 sorts) | O(n^2) |
| T(n) = 2 T(n/2) + O(n) | Mergesort (average case Quicksort) | O(n log n) |
| T(n) = n * T(n-1) + O(n) | | O(n!) |
