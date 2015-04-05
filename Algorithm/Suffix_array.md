* Reference:
* [GeeksForGeeks Tutorial] (http://www.geeksforgeeks.org/suffix-array-set-1-introduction/)
* [Introduction pdf] (http://www.cs.jhu.edu/~langmea/resources/lecture_notes/suffix_arrays.pdf)

* Face interview experience: 
*    首先定义了suffix string 或者说suffix arrary
*    如果有个数组是 ```int[] text = {10, 20, 30, 25}```
*    那么   
*           suffix[0] = {10, 20, 30, 25}
*           suffix[1] = {20, 30, 25}
*           suffix[2] = {30, 25}
*           suffix[3] = {25}
* 如果对这些数组进行lexical order 的排序，我们可以得到
* suffix[0] < suffix[1] < suffix[3] < suffix[2]. 
* 问题是：. more info on 1point3acres.com
*    input: int[] text. 1point 3acres 
*    output: int[] suffix_array_order. 
* e.g.
* input: int[] text = {10, 20, 30, 25}
* output: int[] suffix_array_order = {0, 1, 3, 2}
* 第二题： input:  int[] text, int[] subText
*              output: boolean isExist;.1point3acres
* 检查text数组中有没有一个subarray 是subText。要求时间小于O(N^2)， N == text.length;
* 这里假设我们有了第一题的 suffix_array_order.
* (做法是binary search)

