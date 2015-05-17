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
