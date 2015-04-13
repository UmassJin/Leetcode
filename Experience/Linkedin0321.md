1. K closest points:
  Find the K closest points to the origin in a 2D plane, given an array containing N points.
2.Maximum Sum/Production Subarray --> Check the answer in Array/
3.Pow(x,n)
4 Text Justification
5.Valid Number
6.Implement List/Stack/MaP
7.Isomorphic
8.Implement Read/Write Lock for HashMap/Buffer/etc

1. Print a N x M matrix in diagonal from the upper left to lower right. 
However, with the following caveat. It's easy to just show the 
input and expect output.

matrix:
a b c
d e f g
h i j k

output:
aej
bfk
cg
di
h 

2.  given an arrya of numbers see if you can get to index with   0 in it from an 
index by jumping through the array using the values in the array. So if you have 
[1,2,1,0,3] you can get to 0, from 0 by jumping 0, you can get to 0 from 3, by 
jumping 3 index down to 2 and then jumping 2 index up to 0... 

3. There were two problems to solve: A) Write a job scheduler. 
Input : list of jobs with dependencies. Output: list of jobs to be executed according 
to dependencies.
B) Count calendar days. Input: list of ranges [start,end], a range represent days i.e. 
[1,4] means days from 1 to day 4. Output: Total days included in the list of ranges. 
Answer was 1)Sort list, 2)Merge overlapping ranges and 3) Count/Sum the days of the 
resulting non-overlapping ranges.  

选址建房子。图论的题，意思是给一个matrix，上面有一堆商店，每个商店有建房子需要的材料，要求找到建房子最佳的地址，使到每家商店的距离之和最短，matrix里面还包含不能走的格子。要求先设计类后给算法。

BST构建，插入，删除, return the next node;. more info on 1point3acres.com

给一个array of 硬币，第i次翻面所有i的倍数的位置的硬币，（第0次，第1次全翻，第2次翻2, 4, 6, ...）输出最后结果。要求O(n logn)解法。. visit 1point3acres.com for more.

cypher graphics equivalent, 判断两个string是不是cypher graphics equivalent，并证明cypher graphics equivalent是否symmetric和transitive。
cypher graphics equivalent是指，比如说ABC和DEF就cypher graphics equivalent，因为A=>D, B=>E, D=>F。ABC和ADD就不是。

给一个disordered array，判断是否有两个数相等。
给一个disordered array和一个int dist，判断是否有两个数相等且距离小于dist。
给一个disordered array和一个int targe和一个int dist，判断是否有两个数a, b使 Math.abs(a-b) <= target。且a, b的index距离小于dist。


####[FaceBook 面经](http://www.mitbbs.com/article_t/JobHunting/32760941.html)
都不难，非常注重代码的速度跟简洁性。不过俺已挂。大家加油。
电面
Clone graph
onsite
1. 一个manager 先聊behavior， 然后做了一个小题
    isOneEditDistance 判断两个string是不是只差一个编辑距离。
2. 3Sum 变体，每个数字可以重复用。
3. System design设计手机上读取photo feeds的app。
    功能： 读取好友的最近图片
               阅览好友的相册
    要求： 满足功能的同时减少对手机的能耗。
4. (1) 一维度向量相乘。每个向量很长，billion个数字。
    (2) 多线程 reader 跟 writer 的经典问题。
加面
1. 求 LCA 两种情况，有parent结点跟没有parent的结点的情况都要回答。
2. search in rotated sorted array LC原题。
    decode ways LC原题。


#### [Pinterest 面经](http://www.mitbbs.com/article_t/JobHunting/32570751.html)
电面：
1. 给一个矩阵如下：
a b c d
e f g h
i j k l
m n o p

要求按如下方式打印：
a f k p
b g l
c h
d
e j o
i n 
m

2. 设计题：
如果要给每个Pin加上一个price tag，怎么去evaluate这是否work？
（1） A/B testing -> 可以有好几种，讨论优劣性
（2） metrics to monitor -> click rate, impression, return user ratio, etc

上门：
1. 假设Pinterest的更新系统只能显示3条更新，怎么设计？更新可以是：用户评论、
加新的pin，repin等等，一共可能有一千多种。讨论各种方法的优劣性
回答：a ranking problem...

2. 给如下的数据格式：
<start_time, end_time, value>
比如有一组数据：
1, 3, 100
2, 4, 200
5, 6, 300
。。。
这些数据时间点可能有重合。在时间段2~3之间，value的和是100+200 = 300. 找出这
组数据中最高的value和。
回答1： 用一个数组，每个cell代表一个timestamp，然后扫一遍数据，increment相应
的cell。-》 面试官：时间连续怎么办？有没有更好的办法。
答案：把数据变成：<type, time, value>；然后按照时间排序。如果是start_time,就
+value，不然就-value：
int sum = 0;
int max = 0;

// sort by time

while(have more lines) {
    if(type is start) sum += value;
    else sum -= value;
    if(sum > max) max = sum;
}
return max;

3. 设计一个数据结构支持O(1)的insert， remove， find random（老题）

4. java arraylist里如果满了，怎么办？为什么？
答： make a new copy, size double. 原因是：double size的时候需要拷贝原来的n
个数据，当当前这个长度为2*n的arraylist再满的时候，至少还需要插入n个数据，这
样平均每个数据的cost是在O(1)级别的

5. 怎么做weighted random sampling？（老题）

6. 有产生5的随机数，怎么生成7的？（老题）

7. 怎么去找log中的异常？outlier detection


