#### Suffix Array interview question
首先定义了suffix string 或者说suffix arrary, 如果有个数组是 ```int[] text = {10, 20, 30, 25}```, 那么   
```
           suffix[0] = {10, 20, 30, 25}
           suffix[1] = {20, 30, 25}
           suffix[2] = {30, 25}
           suffix[3] = {25}
```
如果对这些数组进行lexical order 的排序，我们可以得到 ```suffix[0] < suffix[1] < suffix[3] < suffix[2]``` 问题是:
```     
  input: int[] text. 1point 3acres 
  output: int[] suffix_array_order. 

  e.g.
  input: int[] text = {10, 20, 30, 25}
  output: int[] suffix_array_order = {0, 1, 3, 2}
```

#### [解法一：暴力解法](http://www.geeksforgeeks.org/suffix-array-set-1-introduction/)
* 首先求出所有的prefix
* 然后对做sorting，最快的sorting算法是O(nlogn), 每个长度为n，所以totally 算法复杂度是O(n^2logn)

#### [解法二](http://algorithmsandme.com/2015/01/suffix-array/)






* 第二题： input:  int[] text, int[] subText
*              output: boolean isExist;.1point3acres
* 检查text数组中有没有一个subarray 是subText。要求时间小于O(N^2)， N == text.length;
* 这里假设我们有了第一题的 suffix_array_order.
* (做法是binary search)



#### Reference:
* [GeeksForGeeks Tutorial] (http://www.geeksforgeeks.org/suffix-array-set-1-introduction/)
* [Introduction pdf] (http://www.cs.jhu.edu/~langmea/resources/lecture_notes/suffix_arrays.pdf)
