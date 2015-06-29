'''
发信人: peking2 (clojure), 信区: JobHunting
标  题: 我的面试题总结
发信站: BBS 未名空间站 (Sat Oct 26 19:32:12 2013, 美东)

好多人问，我就发到这里吧。

面试题的构成和分类

首先声明一下，这里的面试题主要所指数据结构和算法的题目，题目的分析集中在
Leetcode上面的题目上。


我认为一道面试题由以下几个方面组成的

Question

Data structure in question

Data structure in solution

Algorithm in solution

Coding


题目：非常关键，一个题目通常有一些相应的变形题目，同一个题目可能有不同的要求
。比如时间复杂度，空间复杂度的要求，比如recursive,
iterative的要求。而根据题目的变形与要求，可能会极大的影响到你能够采取的数据
结构和算法。


问题中的数据机构：问题中有可能带数据结构，有可能没有数据结构，有可能是可以自
定义数据结构


解决方案中的数据结构：可以是in-place的，也就是利用已有的数据结构，也可能是创
建新的数据结构。新的数据结构跟已有的数据结构没有必然的联系，而很多问题都是一
题多解，可能采取不同的数据结构。


算法：一般来说，当解决方案中的数据结构确定以后，算法也就确定了。同样，一旦解
决方案的算法确定，相应的数据结构也就确定了。这两个没有先后的关系，但解决方案
中的数据结构和算法具有非常紧密的联系。


代码：非常关键。代码就是解决方案的数据结构和算法的实现了。目前来看，题目，数
据结构和算法在面试中出现的类型比较固定，因此代码的好坏则是拉开面试者水平的一
个有效手段。这也是为什么F，G如此看中代码的质量了。我发现上面几点比较容易突击
，但是写代码的功力还是需要实打实的积累的。


总结面试题目的关键就是要把面试题目进行分类之后分析。由于面试题目由以上几个部
分组成并且混杂在一起，因此怎样合理的分类就变得非常的困难。其实Careercup150的
分类就比较好，它是这样进行分类的。

数据结构：Arrays and Strings, Linked Lists, Stacks and Queues, Trees and
Graphs

算法：Bit Manipulation, Mathematics and Probability, Recursion and
Dynamic Programming, Sorting and Searching

但是我感觉这样分类比较适合初级阶段学习，并不适合系统地对面试题目进行分析。我
其实目前也没有什么特别好的idea，想跟着感觉先来，可能慢慢就能悟出更多了。


Peking2面试题总结(2) - Two/Three pointers
简称two pointers吧。大概把分类粗略的搞了一遍（http://leetcode.cloudfoundry.com/),
发现利用two pointers解决的题目数量很大。two pointers我指的是一类题，而不一定
是真正的two pointers,
比如可能是three pointers, 也可能不是pointer， 而是index。这类题基本上就是发
生在array,
string, linked
list这三种数据结构上，是一种基本的算法和编程技巧，同样超高频率的出现，可以说
是面试必遇的题。

two pointers常常和其他的算法混杂起来出现。比如binary search本身也可以归类为
two
pointers的。如果这样算的话，Leetcode上边1/4的题目都跟它相关。因此，two
pointers是必须熟练掌握的基本编程技巧。


Two pointers大概分三种类型

1. 两个pointers从头往后走：感觉绝大多数的linked
list的题目都涉及到这个操作，当然还有array。这类题目很多时候又可以称为sliding
window。

Implement strStr()

Longest Substring Without Repeating Characters

Minimum Window Substring

Remove Duplicates from Sorted Array &
II

Remove Duplicates from Sorted List & II

Remove Element

Remove Nth Node From End of List

Reverse Linked Llist II

Rotate List

Substring with Concatenation of All Words

Swap Nodes in Pairs
2.
两个pointers从两头往中间走：一般面试出现的的都是singly linked list,
因此这类题主要是array题。

3Sum

3Sum Closest

4Sum

Container With Most Water

Sort Colors

Trapping Rain Water

Two Sum

Binary search (will discuss it in a separate section)
3.
两个pointers控制两个不同的数组或链表：一般出现在跟merge相关的题目上。

Add Binary

Add Two Numbers

Merge Sorted Array

Merge Two Sorted Lists

Multiply Strings

Partition List


Peking2面试题总结(3) - Permutation and Combination
基本题，但是非常重要。面试中碰到任何一题一点也不奇怪。PIE,
CC150和Leetcode都不约而同地包含了这类题。把这些题目做熟是必须的。基本上来说
这类题的解法都是DFS，程序的大体框架非常类似，只是根据题目的要求代码稍作修改
。当然每道题也有不同的解法，但是你应该根据自己的喜好把这类题目的解决方案统一
化。熟悉了这类题目以后对于DFS(will
be discussed in a separate section)
的理解会非常深刻。基本上一般的DFS的题目应该没什么问题了。

无论是排列还是组合，这类题都有一个变形，就是要求不能有重复的输出。PIE和CC150
都没有提到相应的解法，大家应该很好的体会一下。如果没有相应的准备，属于面试的
时候比较容易跪的题目。


Permutation

输入没有重复：Permutations, CC150 9.5, PIE Chapter7 Permutations of a
String
输入有重复，输出不能有重复：Permutations
II


Next Permutation: 经典算法，背吧

Permutation Sequence: 非常有意思的题目


Combination

纯粹的subset

输入没有重复：Subsets, CC150 9.4, PIE Chapter7 Combinations of a
String
输入有重复，输出不能有重复：Subsets
II


需要满足一定要求的组合

一个元素只能取一次(输入没有重复): Combinations

一个元素可以取多次(输入没有重复): Combination Sum, CC150
9.8
一个元素只能取一次(输入有重复，输出不能有重复）:
Combination Sum II


Gray Code: 具有subset的序列特点 （考虑CC150 9.4 Solution#2:
Combinatorics)


Peking2面试题总结(4) - 数据结构和算法

下边是我认为面试中常见的数据结构和算法，以Java的类库作为标准。


数据结构

Array, ArrayList

String, StringBuffer

LinkedList

HashMap, HashSet

Stack and Queue

Tree:

BT: binary tree

BST: binary search tree,

Balanced BST (red-black tree): TreeMap, TreeSet

Trie: prefix tree

Heap: PriorityQueue
Grpah


注意：

Array和Linkedlist是最最基本的数据结构，因为他们可以构造很多其他的数据结构，
比如String
(C语言里String就是字符数组），HashMap, Stack和Queue
(Java里Queue就是LinkedList实现了Queue的interface;
Ruby里stack和queue都是array）, 以及Heap。

Heap is a tree logically, but array physically.

HashMap, Stack and
Queue通常不会出现在问题里的数据结构中，因此一般作为solution的数据结构。但是
面试中也常会让你实现这三种数据结构，另外就是CC150的3.2和3.5都是典型的Stack和
Queue的题。Leetcode中并不涵盖这些内容，这几种数据结构在Leetcode中都是作为
solution数据结构出现的
(没有的原因是这些题目不太适合OJ，因此需要单独练习）。

目前Leetcode还不包含graph的题型



算法

Sort: quick sort, merge sort, count sort, heap sort, bucket sort,
radix sort, external sort, K selection etc.

Merge: 2 array/list merge, k-way merge, interval merge
etc.

Binary search:

Stack:

Recursion and Iteration:

DFS：pre-order, in-order, post-order for trees

BFS: 需要用Queue

DP: Top down and bottom up

Greedy:

Toposort: 需要用Queue


注意：

Leetcode并没有包含各种sort算法，而通常面试很少让你直接去实现sort算法，但是大
部分的相关编程技巧是包含在很多题目当中的,
比如quick sort的two pointers。

Merge跟sort是紧密相关的，单独拿出来是因为有很多这个类型的题目，需要一起总结
。Merge操作的对象基本都是已经排好序的。

Stack虽说是数据结构，但是一般出现在solution里，因此代表了一类算法

Toposort面试作为难题也很有可能遇到，目前Leetcode还没有包括进去


Peking2面试题总结(5) - Binary search and divide and conquer

玩竞赛对面试不利的一个地方就是面试经常遇到的数据结构比如LinkedList, Tree, 和
算法Binary
search，竞赛很少涉及到，因此一直心里都感觉到有些不安。

Binary search非常tricky，虽说道理简单，但是面试的时候却很容易出bug，因此总结
一下是必须的。假设i=0,
j=A.length-1, 我做了一下LeetCode上的所有binary
search的题目，发现了以下几点值得注意。


终止条件不同 i<=j, i<j

mid的上下取向不同 i+(j-i)/2, j-(j-i)/2

如何合理分半

分半的时候取=mid, mid-1, or mid+1


Search a 2D Matrix： 这是一道普通的binary search。终止条件i<=j,
mid取向i+(j-i)/2, 分半的时候=mid-1 or mid+1。

Search for a Range：这道题需要终止条件i<j,
mid取向两种都需要用到，分半的时候需要用到=mid。我发现一般＝mid的时候，终止条
件往往是i<j,
不然会有死循环。


如何合理分半：下边这几道题都很tricky，分半的时候都有各自的特点，很不容易一次
写对。需要多多练习和体会。

Search in Rotated Sorted Array

Search in Rotated Sorted Array II

Median of Two Sorted Arrays


还有一个有趣的现象就是很多数学相关的题目也是通过binary search来解决的：

Divide Two Integers：这题没做过面试也容易跪

Pow(x, n)

Sqrt(x)：其实算是一道典型的binary
search题目，不过里边包括了几个tricky的地方，很难一次写对


总的来说，LeetCode上边的这些binary
search的题目cover的还比较全面，而且题目全部是面试高频题，需要练习一次写对。



Peking2面试题总结(6) - Linked List




首先LeetCode上几乎所有的Linked list的题目都可以用two pointers来解决，或者会
用到two
pointers这个基本编程技巧。因此two pointers跟linked list是紧密相关的。因为two
pointers以前已经总结过了，就不多讲了。


其次，因为LinkedList和Array/ArrayList一样都具备有List的特性，因此很多题目都
出现在了两种数据结构上，或者说很多题目都是可以把这两种数据结构互换的。比如：

Add Two Numbers

Convert Sorted List to Binary Search
Tree

Insert Interval

Merge Intervals

Merge k Sorted
Lists

Merge Two Sorted
Lists

Remove Duplicates from Sorted
List

Remove Duplicates from Sorted List
II


第三，LinkedList的题目大多自然而然使用iteration来解决的，但是我发现有些时候
iteration比较容易出bug，换成recursion实现更容易。面试的时候万一iteration卡住
可以换换recursion的思路。


第四，dummy head非常有用，可以使代码简洁很多，并且容易写bug
free的code。这个技巧可以大量使用。


第五，今天做了一遍LinkedList的题目，发现两个地方容易出bug。一是two pointers
loop完之后常常会有一个收尾的工作，比如Add Two
Numbers需要处理carrier>0的情况。二是在swap了nodes之后，新的tail需要把next置
空，不然就出现死循环了。

面试题总结(7) - Tree

一直没有总结Tree，这次想总结一下结果却发现没有什么太多可以总结的。Leetcode上
tree的题目还是比较全面的。我做了一遍发现基本上跑不出三个套路：

1. Recursive DFS

2. Iterative DFS

3. BFS


有些tree的题目比较tricky一些，但是最终解法还是逃不出这三个套路，所以我觉得面
试的时候代码的质量就变得更加的重要了。因为没有什么太多总结的，下边就随便聊一
下了。

Leetcode上graph的题目涉及的很少，不过从算法和coding来说DFS，BFS完全适用于
tree和graph。因此，把tree的题目练好了，graph的多数题目应该也不会有什么问题才
对。当然graph涉及的算法比tree还是要多的，比如shortest
path,
toposort等等，但是DFS,BFS还是基本中的基本。因此做Leetcode上的tree的题目也相
当于练习了graph的题目了。


由于Tree的题目比较多，我感觉一些可以skip掉，如果时间不充裕的话。或者做一遍即
可，不需要反复练习。这些题目或者太简单，或者面试不太可能碰到。

Balanced Binary Tree

Binary Tree Level Order Traversal II


Maximum Depth of Binary Tree

Minimum Depth of Binary Tree

Same Tree

Symmetric Tree

Unique Binary Search Trees

Unique Binary Search Trees II


Pre-order, In-order, Post-order traversal
需要会recursive和iterative的两种实现方式。可惜Leetcode上只包含了In-order，有
些遗憾。


Tree的serialization/deserialization也是常常被考到的题目，这个Leetcode目前还
没有包含，当然套路还是DFS/BFS。


LinkedList和Binary Tree相互转换的题目。

Convert Sorted List to Binary Search Tree

Flatten Binary Tree to Linked List
(这题原题在CC150是一道双向链表题，不知道Leetcode上怎么改单向了。双向链表应该
更复杂一些，大家要注意一下）

'''
http://www.mitbbs.co.nz/article_t/JobHunting/32564237.html
