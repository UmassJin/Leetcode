'''
Offer:
=====
背景：非cs PhD+两年半经验
申请了Amazon，FB 和 G。
A家Rejected：1st 电面遇三哥，被黑
f家Offer：        ~24w/year + 5w sign on
g家Offer：       ~25w/year + 3.5w sign on
两个Offer都很好，很难选择，最后去了狗。

FB 是板上的大哥帮我内推的，人非常非常好，很热心，很可惜最后没去，特别特别的
感谢他。
G家是哥们内推的，帮忙收集了很多准备材料，有问必答。
最感谢的是，老婆，岳父，岳母，提供充足的后期保障，说实话，照顾宝宝比什么写码
刷题，累得多。


面经：
====
A家电面：
-----------
     三哥，出了5道题，30分钟全部搞定，还是被黑了。当时没有经验，应该面试完后
立刻投诉。出结果后才向HR投诉，未果。
     1 given 2 strings，can you construct str1 using chars in str2？
     2 binary tree inorder traversal，both recursively and iteratively
     3 erase given value item in linked list 
     4 how to debug memory leak in c++?
     5 design a parking lot.

F家：
-------
电面：
     华人大哥: 一个数组里有多个最大值，等概率随机返回其中一个最大值的index，
要求one pass。LC 的 permutations

Onsite：
     1 国人大哥（人很好，放我的水）： merge k sorted lists, best time to buy
and sell stock。
     2 印度经理： 背景+behavior+一个编程：code base在某个版本开始有bug，找到
这个版本。
     3 老美： LC 的 minimum window substring, decode ways。
     4 中东人： LC的valid palindrome。 给1， 2， 5面值的纸币，有多少种组合凑
出100 块钱。
     5 三哥：设计题，传输10G的data到5个data center，每个data center 有1000的
节点。三哥从问背景就开始找茬，面试过程中要求解gossip protocol的微分方程， 被
黑。
     面试完，立刻投诉三哥，因为所有其他面试官都给了strong recommend，于是加
面设计题
     6. 老美（高级别，大牛人）：设计iPhone Find Friends 的后端。Geohashing +
DHT解之

F家的面试官水平都很高， 都很乐意和你讨论他们的project， 当然如果你很恰当的给
出comment，会给你加分不少。
设计题问得很细，比如DHT如何实现，单机的Hash table如何实现能节省内存， 如何做
concurrency control，如何实现mutex之类的。
三哥中有好人也有坏人，坏人不少，好人也很多，不用遇到三哥就紧张。万一被坏三哥
黑了，不要影响心情，继续完成好接下来的面试，你很有可能拿到加面的机会。

G家：
--------
因为签了NDA就不细说了。感谢一个浙大的国人大哥，面试的时候给了很多引导。


面试准备：
========
F家的算法：
----------------
    1. F家的题基本上都是Leetcode 的原题和变种。把leetcode的题研究透就OK了。
    2. 跟F家的HR 聊过， 如果你想拿到面试官的strong recommendation, 需要在一
轮面试中做完两道题。每题15-17分钟完成，包括和面试官讨论，写代码，以及写test 
case 的时间， 同时尽量bug free， 不一定要optimal solution。 
    3. 时间很紧，所以要多练习白板码，多练习在白板上跑test case。写多了就会发
现，白板码上写出bug的概率比用电脑写低很多， 因为白板上可以通过图表的形式很直
观的跑test case， 很容易发现bug。
    4. 面试的时候，自己带fine tip marker， 比粗的笔写代码快很多。

G家的算法：
--------------
    1. G家的题库很大，而且经常换新题，我面试的时候一道都没有见过，所以刷题用
处不大。
       G家的题基本上都是经典算法的变种。如果对经典算法很熟练，面试的时候很快
就可以想到解法。
   2. 复习经典算法，推荐看一下Sedgewick 教授的算法书。http://algs4.cs.princeton.edu/home/
        相比算法导论，我更推荐这本书，因为这本书的算法是用Java而不是伪代码实
现的，而且代码写的非常简洁而优雅。
        Sedgewick教授的书里没有 DP专门的章节，看看算法导论作为补充。
    3. G家喜欢考各种tree：prefix tree，augmented binary search tree (with 
rank and select APIs), segment tree，binary index tree （1D and 2D), 
interval tree, kd tree, quad tree. 
    4. G家喜欢考几何题，推荐：
           topcoder的教程：http://help.topcoder.com/data-science/competing-in-algorithm-challenges/algorithm-tutorials/
           Sedgwick的介绍几何算法（sweep line之类）的video：https://www.
youtube.com/watch?v=Igr6yONkpIQ
    5. G家关于设计棋类游戏的AI的题，基本上都可以用MinMax 算法解决: http://neverstopbuilding.com/minimax
    6. G家和F家都会考 Thread-Safe data structure和 Threading Pool，推荐阅读C
++ concurrency in action的第六章和第九章 http://www.manning.com/williams/

系统设计：
     1. 我基本没有web development的经验。和我一样0经验的同学可以先上一门课，
推荐Reddit Cofounder 开的web development
的课( 讲义和课程project都非常好）：https://www.udacity.com/course/viewer#!/c
-cs253/ 
     2. 对于distributed system不了解的同学，推荐coursera上的Cloud Computing 
Concept：https://www.coursera.org/course/cloudcomputing
     3. 系统设计里边，最重要的部分是Data Storage和Data processing。
         Data storage包含：
              a. Distributed File System: 推荐看一下GFS的paper和FB Haystack 
Photo storage的paper
              b. NoSQL Data storage: 推荐看一下Big Table的paper，了解一下
Cassandra 的架构：Cloud Computing Concept的课有讲
              c. Memcache
         Data processing：
              看一下Map-Reduce的paper。了解一下Map-Reduce能解决什么问题。如
何做job scheduling等等。

     4. 板上大牛收集的题库：https://www.evernote.com/shard/s21/sh/c2035c38-
1a80-4fd4-8c93-8ca0ad9ffb48/35079ac1bf5ae3ea
         大多数题，解题的时候，按三步走：
               a. 如果数据量小，如何在单机上实现。
               b. 如果数据量大，如何sharding data，如何实现scalability
               c. Fault tolerance，考虑有node failure和message loss的时候这
么处理。
    

最后，祝大家都有好offer。



所以这里我觉得比较有用的准备方法是，在弄明白一个design之前，先要做好几个准备

1. 先把一个process或者一个系统是怎么工作的搞清楚，这里是指，design一个
service需要cpu，memory，disk，network等等很多component协调工作，这些东西分别
都在什么时候用到，为什么要有这些东西，分别有什么特点。
相信大家都很熟悉有一篇文章叫做The numbers eveyone should know，在没有这篇文
章基础上的design都是瞎扯。

2. 要清楚这个design到底是为了解决什么问题，use case是什么，design一个系统根
本上讲是为了解决一个存在的problem，这个problem会有general的要求，比如latency
，比如throughput，比如load，比如哪种操作比较频繁，比如有没有consistency要求
，是不是reactive，是不是需要highly available，等等等等，这样跟第1点相结合才
能明白瓶颈可能在哪里，哪些东西可以tradeoff，进而才会有design的solution

3. knowledge base的储备要尽量够，操作系统，distributed system，concurrency这
些东西很难啃，我也曾经自学过几个大学的distributed system公开课，很多同学想绕
过这些走捷径，但是越难的东西就越有价值。知识量不够不是问题，看一点补充一点，
只要能坚持下来，到了一个时间点基本上还是可以有质变的。


FB 高频题
1 sort colors, O(n)时间, O(1)空间.      https://leetcode.com/problems/sort-colors/
2 One Edit Distance, Given two strings S and T, determine if they are both one edit distance apart.       https://leetcode.com/problems/one-edit-distance/
3 A set of points(x, y), 返回前k个离原点最近的点, 用k-selection 或者堆（代码见附件）
4 Flatten Binary Tree to Linked List   https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
5 Remove Element 将一个01随机数列中，把1全部移到左边，要求移动次数最少


'''


