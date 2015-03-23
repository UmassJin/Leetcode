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
