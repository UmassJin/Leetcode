'''
1. http://www.mitbbs.com/article_t/JobHunting/32005597.html
1) Implement a simple calculator (+,-,*,/);
    2) Implement "+1" for a large integer;
    3) How to match Ads to users;
    4) How to extract useful information from a forum webpage (list all 
kinds of useful signal you can think of)
    5) How to detect the duplicate HTML pages (large scale);
    6) Find all the paths between two places on Google map;
    7) Find the minimum window in a string which contains all the given 
characters;
    8) How to debug a random algorithm, i.e., for the same input, the 
output
can be different;
    9) Inverse a stack give three member functions (forgot details); 
prove 
why your algorithm is correct;
    10) Given the mask of ISP and a huge volume of IPs, find out the top 
1000 ISP which contains the maximum number of IPs;


2. http://www.mitbbs.com/article_t/JobHunting/32590583.html
发信人: zyeye (zyeye), 信区: JobHunting
标  题: G电面
发信站: BBS 未名空间站 (Tue Dec  3 21:45:01 2013, 美东)

估计是跪了 
简历题， 网站架构方面。 
第一道题 nondetermistic testing 怎么测试， 这个题卡住了 不知道怎么回答。
第二题： 有序数组中查找第一个出现的数，数组里面可能有重复。 做完之后写test 
case，如何设计test case， 考虑哪方面， 感觉还行。 
第三题： 就是这个题把我整跪了， binary semaphore 

def inc: 
  while True: 
      v = v + 1  //---A
     set(s)       // ---B

def disp: 
  while True: 
     wait(s)      //---C
       print v    //----D

求输出序列的可能情况 v 是shared value 初始为0 
s是binary semophore 初始为0。set(s) 置s为1，wait(s) unset s 并且blocking。 
第一问 0 是否能输出， 回答 不能，因为会blocking ， OK。 
第二问， 后面的情况，会输出什么样的递增数字， 我一想执行序列可能为 ABABCD， 
这样的话 有些number 就missing了，然后他问是否任意的都missing？ 我说是，然后
OK，他问我 能否重复出现数字，我回答如果重复的话 就是CDCD 就waiting了。。然后
我知道悲剧了，因为他给个例子。。 ABCABDCD， 这样的话就有两个重复，然后又问我
能否多次重复，我就抽自己嘴巴了，说能，然后就没时间了，后来发现其实是不能的，
最多重复两次

3. http://www.mitbbs.com/article_t1/JobHunting/32635481_0_1.html
发信人: liuwei7923 (superLancer), 信区: JobHunting
标  题: 求推荐准备面试的书籍，发G 电面面经
关键字: google 电面
发信站: BBS 未名空间站 (Thu Feb 27 10:43:52 2014, 美东)

刚经历了google的电面，深刻感到自己思路不够开阔，遇到没见过的题完全无从下手，
所以想请教版上的同学有什么书籍适合面试准备。 本人使用java，只做过leetcode和
cc150

闲话不说，上面经：
前两天面的。三哥面试官
面试开始，直接上题。给了一个Quack的类，里面有三个方法：
pop(): 随机从头或者尾扔出一个元素；
peek(): 随机看头或者尾的一个元素，peek()之后pop()的话一定会pop()出peek()的那
个元素；
push()：向尾部插入一个元素

问题是：给一个排序好的Quack,怎么把里面的元素原封不动的放到一个Array里面。
follow-up：如果quack里面有重复的元素，怎么处理

拿到题之后，完全没思路，基本是在面试官的指导下才做出来的。而且follow-up的题
目也没想到该怎么做。最后只写了没有重复元素的代码。


4. http://www.mitbbs.com/article_t1/JobHunting/32574909_0_1.html
发信人: CrazyCow (CrazyCow), 信区: JobHunting
标  题: 国内Google电面两轮 已挂
关键字: google,电面
发信站: BBS 未名空间站 (Mon Nov 11 12:42:55 2013, 美东)

10月17日，第一轮电面：
   第一题：上海的电话isTree(vector<pair<int,int> >& edges);  (离散化+dfs判环
判联通)
   第二题，               
     Given a 2D space of maximum size NxN which supports two operations :
     [1] void UPDATE(x,y,v) - sets the value of cell [x,y] to v
     [2] int QUERY(x1,y1,x2,y2) - returns sub-rectangle sum (x1,y1) to (x2,
y2)
      inclusive, and there is an infinite stream of such 2 types of 
operations which have to supported. How would you store the values for 
efficient updates and retrievals ? （二维线段树  说算法+分析复杂度）
    第一轮答得还可以。
10月30日，第二轮电面：(挂)
    美国的电话，面试官很nice：
    第一题。一个二叉树，节点值有正有负，求树中的任意路径的最大值。路径的值就
是路径经过点的值的和。然后我说dfs，面试官就让写代码  。 写代码一开始dfs的接
口声明有问题，期间停下来修改了一下，然后写完。被面试官查出1个bug。面试官提示
了，一开始找出了另外个bug；面试官又提示了一下，才找出了面试官想要我fix的bug
。杯具。
    第二题。给三个字符串，a，b，c。问a 和b 能不能组成c，且保证c 中a b 的字母
顺序不变。 一开始我给了一个没验证贪心的想法。然后面试官让我验证或举个反例。
我想贪心多数没戏，就又说了种dp的思路。面试官让我写下来。我写完之后，让我解释
了解释。然后突然悲催地发现我的解法是O(2^n)的。。面试后想想如果我的解法状态去
重后，就和普通的dp无异了。。  杯具  。。 然后就挂了。
    哎，悲伤，简单题目答成这样，白白浪费了这次机会。
    背景：国内渣本科毕业一年，有ACM竞赛经验。平常做算法题还可以，leetcode上
刷题也从没看过其他人的题解。还是把google电面想的太easy了，所以心态上有松懈。
而且加之早上起早有些困。。。 总之这些都是次要原因，主要还是因为太他妈挫了。

5. http://www.mitbbs.com/article_t/JobHunting/32634303.html
发信人: yw001 (肥猴), 信区: JobHunting
标  题: G onsite 面经
发信站: BBS 未名空间站 (Tue Feb 25 16:37:40 2014, 美东)

mountain view 两周前面的，今天电话来hiring committee没过。

（1） 中年白人： 先在手机上演示了一个game, 就是一个球从起点开始沿着通道，看
能不能滚到终点。不过有限制， 每次球一走到底要不到边界，要不到障碍物，中间不
能停留。 可以上下左右走，然后让写个function 给定起点， 终点，和图，判断是不
是solvable. 写出来了， 就是用BFS,有个小bug被指出。然后问复杂度， 问如何优化。
（2） 韩国人： a) 给一个dictionary, 再给一个set of coding string （g5, goo3,
goog2, go2le.........). return all string from dictionary that can be 
matched with the coding string. 要求尽量减少dictionary look up 次数。给了个
方法，但一直不满意复杂度。
                     （b)如何用Trie,   把问题(a)解决,要求写code 建一个Trie包
括所有字典词和coding string.不是很明白。。。凭感觉写了个。

（3） 阿三， 非常拽。。。 给一个dictionary, 一个string,找出dict 里能全部用
string里的letter 表示的所有最长的词。给了算法，死活不满意，不让我写code. 估
计被黑了。
  (4）阿三。 design google calendar .  要求分析如何存data, 如何invoke user 
created events, 如何handle 100000events per second, 然后要写了一部分thread 
safe 的code 实现如何invoke event.

(5)年轻白人： (a)leetcode 上的coin 题， 用DP. (b)给你一个password 假定6位， 
有个function 每call 一次就给你一个triplet 是password 里的随即三位，order不变
。比如google, 可能返回， ggl, goe, oog, ool, ........
问如何最有效破译这个密码，写code. 


6. http://www.mitbbs.com/article_t/JobHunting/32631467.html
发信人: goodbai (八段锦), 信区: JobHunting
标  题: 热腾腾g电面 已挂
发信站: BBS 未名空间站 (Fri Feb 21 00:20:19 2014, 美东)

同胞面试官，上来就gdoc做题。
2d array ＊代表障碍物 ＃代表货物 空白就是正常的路 
问 
如何找到一个点为出发点 能实现总共取货路径最短？ 每次只能拿一个货物，遇到障碍
需要绕开，拿到以后要放回出发点，然后再取另一个

＊＊＊＊＊＊
＊   ＃       ＊
＊  ＊＊＊  ＊
＊              ＊
＊     ＊＊   ＊
＊ ＃       ＃＊
＊＊ ＊＊＊＊

大牛们有什么好思路？我用的bfs，但因为之前讨论题目要求花了很久，没有写完。。
我还是太弱了，move on


7. http://www.mitbbs.com/article_t/JobHunting/32568289.html
发信人: xiaolongnv84 (一见若彤误终身), 信区: JobHunting
标  题: F, A, MS, QM, RF的OFFER和经历 -- Final update
发信站: BBS 未名空间站 (Fri Nov  1 14:55:43 2013, 美东)

昨天收到FB的电话，我的OFFER已经批下来了，这也意味着我的JOB HUNTING结束了，下
面是我这两个月来申请结果汇总：
Applications (7): Facebook, Google, Microsoft, Square, Twitter, Rocket Fuel,
Amazon
Offers (5): Facebook (accepted), Microsoft, Amazon, Rocket Fuel, Qualcomm (
return offer)
Rejections (3): Square, Twitter, Google

OFFER细节就不报了，上次看有人报MS的OFFER细节，结果引发口争，有人将其定性为
SHOW OFF。。。

在版上受益良多，我会陆续呈上各家公司的面试经历和面试题（FB的面试题除外），当
务之急是给LEETCODE捐点钱。

非大牛，版上互赞大牛的风气不可取。有二爷，半海和一帮真牛在这镇着，谁敢放肆！

============
个人背景
============
既然已经被不少朋友认出来了，就提供下背景信息吧。
我是2009入学的PHD＠ECE，今年11月刚毕业，研究方向是Wireless Sensor Networks和
Distributed Systems Design。在过去的四个暑假里，完成三个实习，每个大概14星期
。第二个暑假我没有实习，跑去加拿大和意大利游玩了。

更多信息，比如个人主页，可以站内信。

============
如何准备
============
1. 书籍：
B1. Introduction to Algorithms
B2. Algorithms (4th Edition) by Robert Sedgewick and Kevin Wayne
B3. Cracking the Coding Interview
B4. Programming Pearls
毫无疑问，B1是最重要的，其中的基本和中级算法章节我至少读了4遍，高级算法部分
间断地读了2遍。版上很多人非常推崇B3和LEETCODE （我后面会讲），却忽略了这本葵
花宝典。读这本书时，重点不是解上面的题或是背算法，最重要的是理解掌握各个算法
背后的设计思想。面试中遇到原题是你运气，大部分时候是没这种运气的。但是绝大部
分面试题的解题思想非常类似，无非是从各种排序算法，BST算法和基本图论算法中变
化的而来。微软的面试题4.1我从来没见过，好像这个版上也没讨论过，我也是现场灵
光一闪，发现其本质就是QUICKSORT算法，然后给出了最优答案。

B2与B1类似，都是大部头的书，确实需要点勇气的耐心去读。这本书中讨论了很多更为
实用的算法，更适合去解面试题。如果你有时间的话，一定要读一下，网上可以找到
PDF版本。B3可以看下，主要是看解题思路，上面的代码质量很一般。我是在刷完
LEETCODE几遍后，随手翻的。因为我已经把LEETCODE上的题刷得很熟了，所以这本书我
看得很快。B4感觉是个鸡肋，以前版上很多少推荐过，所以我也就看了看，发现这本书
实在是非常非常基础。如果你已经把B1看过两遍了，这本书就没必要了。

题外话，我从来不相信只靠刷题就能拿到FLGT的OFFER。这些顶级公司对个人能力的考
查还是很全面的，有时即便你全部答对了题，也不一定能拿到OFFER。况且现在不少面
试官已经知道LEETCODE这类的刷题网站（他们当中有些人以前就是这么刷进去的），他
们也会尽量避免出原题。当然，如果哪位国人哥哥想放水，出个原题让你水过，也是有
可能的。

话说我面试最怕国人，其次是日本人和韩国人。阿三就不用提了，我已经将他们划为抱
团阴狠的鼠类。

2. 在线资源
MITBBS
LEETCODE
TOPCODER
CAREERCUP
找工作的前一个月，我就开始MITBBS考古，看了不少题。后来在面试期间，基本上每天
早晨都会上来把前一天的所有关于面试的帖子看一遍。从开始感叹各位神人的答案，到
后来我也开始提供答案了。在我看来，LEETCODE是最好的在线训练网站。刷LEETCODE的
目的不是解上面的题，而是通过训练来熟练掌握B1中的算法设计思想，因为LEETCODE上
不少题的解题思想非常类似，还都是那些基本算法的变种。LEETCODE每道题我认真
地写了两遍，都是自己努力想答案，如果实在不行，才去看别人的解法。因为大部分题
是自己做出来的，所以印象非常深刻。到后来，我两三天就能快速地过一遍；随机挑个
题，我很快就能写出来。

TOPCODER上有非常好的TUTORIAL，讲得深入简出，非常值得认真读一下。我以前就一直
没太明白KMP算法，看过上面的TUTORIAL后，一切都明朗了，LEETCODE上的STRSTR那题
我也是用KMP算法解的。在面试RF时，一个阿三一上来就考这个STRSTR题，而且还很卑
鄙地把那个最基本的逐个比较的算法说出来了，意思是说你不能用这个基本算法解了，
然后那个SB一脸欠揍的得意表情。我当时就是现场用25分钟左右时间写了KMP算法，那
个SB又变成一脸失望的表情。面完那轮后，我后面心态就非常随意了，因为已经决定不
去这家充斥着阿三的公司了。

当我已经把LEETCODE做得非常熟了后，我就开始随机做TOPCODER上DIV1和DIV2的题了。
DIV3的题就不用看了，太难，不适合面试。在面每家公司前两天，我会去CAREERCUP把
这家公司前4页的题都看一下。只是看看，过过脑子既可，没有去写代码。

3. Design
总结贴：
http://blog.csdn.net/sigh1988/article/details/9790337

其它资源：
http://www.mitbbs.com/article_t/JobHunting/32498535.html
https://www.facebook.com/note.php?note_id=365915113919
https://www.facebook.com/video/video.php?v=432864835468
https://www.facebook.com/photo.php?v=572283147938&set=vb.9445547199&type=3&
permPage=1
http://vimeo.com/11280885

必看论文：
Google: Google File System, MapReduce, BigTable
Facebook: Cassandra
Amazon: Dynamo

其实读懂这5篇论文后，很多系统设计题就应该大概明白怎么做了，因为很多重要的设
计思想都在这些论文中。

============
Facebook
============
下面更新FB的面试经历吧，因为已经从了，所以不想说具体题目，只说我这个非典型经
历吧。
第一次和FB打交道是在今年２月份，当时我突然想在毕业前再去实习一次，于是网投了
FB的实习，没有找人REFER。一个月后收到HR的通知，安排面试。他家效率非常之高，
一周之内就搞定了两轮电面，进入PROJECT MATCH。可惜时间太晚了，没有MATCH上。

我今年９月向我老板确认我可以４年半毕业，于是开始申请工作。我直接发信给我上次
的那个HR，说我想申请正式职位，看她能不能安排下电面。她非常爽快地说，我们不用
浪费大家的时间了，电面就不用了，你直接来ONSITE吧。于是安排两周后电面。ONSITE
一共四轮，第一轮是PHD JEDI，主要是让我在白板上讲解的我DISSERTATION，最后问了
个无限数据处理的问题。第二轮和第三轮是CODING NINJA，每轮两个题目，可以有点小
BUG，但要能自己发现。最后一轮是DESIGN，主要是讨论设计思想，根据面试官提出的
种种问题进行改进。

一周后收到OFFER，可惜在那周的星期三我已经ACCEPT了微软的OFFER。话说微软很不自
信，三天两头催我做决定，最后说在周三之前必须做决定，大概是因为他们知道我还在
面FB吧。比较了两个OFFER，发现在考虑税收和LIVING COST下，FB的只多个两三W，我
不想为了这么点钱伤人品，于是发信给FB，说已经接了MS的OFFER，非常不好意思。不
过我明年会跳槽过来的。

然后FB的HR没理我，我想她们很少见过有为了MS的OFFER，拒掉FB的OFFER的傻B吧，还
是在FB给的钱多的情况下。三天后，突然接到HR的邮件，说面试我的几个人都强烈推荐
我，他们想再给我加一轮DESIGN面试，来决定是否要给我加工资。我一想还有这种好事
，于是就同意了，当天下午就SKYPE面试了。几天后收到新的OFFER，说如果我愿意拒掉
MS的，他们会把我的PACKAGE提高１２％。话说他们这么没有节操的硬抢，我也就没有
节操的同意了。。。

这个故事可以打消很多的关于反悔OFFER的顾虑。上次还有人担心拒人别家，从了FB的
话，FB知道后会收回OFFER。其实FB还是很喜欢抢人的，只要你有货。

============
Twitter
============
话说我和T家非常没有缘分。今年2月申请实习时，让我朋友REFER，结果他家HR连电面
都没有给，就把我给拒了。今年我换了另一个朋友REFER我，电面是拿到了，第一面就
挂了。电面先是一个LEETCODE原题，Palindrome Partitioning II ，我给了O(n^2)的
解法。然后是问LINUX里面BASH SHELL是如何实现的，运行一个命令时，系统有哪些步
骤，系统STACK是如何转换的。我对LINUX底层的东西不熟悉，第二部分答得不好，磕磕
碰碰的，然后就没有然后了。

============
Square
============
这家我是网投的，两天后拿到面试。电面有两轮，间隔两天：
1. 经典的小偷问题：一排房子，每个房子里有一定价值的东西，小偷不能偷相邻的两
个房间。即如果小偷光临了房间i, 那么就不能再偷房间i - 1和房间i + 1。要求返回
小偷能偷到东西的总价值的最大值。这是个经典DP问题，版上讨论过。
Sol: Suppose v[i] = the value of house i, and totally we have n houses.
f[0] = v[0], f[1] = v[1], f[i] = max{f[i - 1], f[i - 2] + v[i]} for i >= 2

A modified version of this problem is that all houses form a circle, whose
solution is very similar. We need to run DP twice.
1st: f[0] = v[0], f[1] = 0, f[i] = max{f[i - 1], f[i - 2] + v[i]} for i = 2,
3, ..., n - 2 ==> ans1 = f[n - 2]
2nd: f[0] = 0, f[1] = v[1], f[i] = max{f[i - 1], f[i - 2] + v[i]} for i = 2,
3, ..., n - 1 ==> ans2 = f[n - 1]
return max{ans1, ans2}

Sample code: https://gist.github.com/krisys/4089748
More explanation (Bad Neighbors): http://community.topcoder.com/tc?module=Static&d1=match_editorials&d2=tccc04_online_rd_4

2. 扑克牌问题：给一副扑克牌排序，先是按花色，同一花色按数字排序。主要是扑克
牌这个CLASS应该如何设计，如何表示花色和面值。我给出了他想要的JAVA enum表示法
，但我以前在JAVA中很少用enum，导致里面有些方法都忘记了。
FOLLOW-UP：现在你有一手牌，你要计算其分值，规则如下：如果两张牌相同，或这两
张牌的面值和为15，则计2分。ACE可以是1或者11.

这家公司对代码简洁度有着变态的要求，凡是能一行写出来的东西，绝不会让你写两行
代码，哪怕两行代码的版本更容易理解和维护。写完代码后，其余的时间全是在按他们
的要求简化压缩代码。最后代码的行数是减少了不少，可是可读性也是一样。第二面挂
掉，我觉得主要是用enum的时候，明显不熟。

============
Google
============
与FB类似，我在今年3月申请实习的时候，也过了前面两轮电面，进入HOST MATCH，最
后也没MATCH上，于是他们直接让我去ONSITE。我当时还没准备好正式找工作，就把
ONSITE推到了10月，也就是在FB面试的后面几天。面试一共四轮，全是CODING，只有一
个人稍微问了下我的研究内容，这点就明显没有FB给我的感觉好。

第一轮是个香港帅哥，人很好，这轮是我表现最好的一轮。题目如下：
1.1. Tokenize a string to words. Ignore any space and punctuator

1.2. Design an distributed file system to store files of TB size
Follow-up: How to find and store the top-k most frequent keywords among
documents stored on all Google servers

第二轮是个阿三，感觉很吊的样子，一副大爷样地坐在那里，让我很不爽。他就问了很
简单的一道题，然后就是不停地问我如何改进。
2. Given a list of words, find two strings S & T such that:
    a. S & T have no common character
    b. S.length() * T.length() is maximized
Follow up: how to optimize and speed up your algorithm

第三轮如下：

3.1 Design an interface that can convert both a sorted linked list and a
sorted array into a balanced binary search tree. Implement it in both bottom
-up and top-down approaches

3.2. (Leetcode 原题) Given a matrix of size m * n, matrix[i][j] stores the
number of carrots in cell (i, j). Now a rabbit starts from the left upper
corner and wants to reach the right below corner. It can only move either to
the right or below. Compute the maximum number of carrots that it can
collect along the way, and output that path.
Follow up: how many different ways are there?

第四轮就是个悲剧，一个更年期日本女人，英文听得让我想死。进来后没有任何问候，
连自我介绍都没有，坐下来就板着个脸开始问。整个过程中就是我在说，她没有任何回
应或是表情，我还不如去她们日本买个漂亮的充气娃娃来对着面试呢。这轮我从一开始
就很紧张，发挥得也不好，到最后快结束时才写出代码。这题其实想明白了，算法极简
单。只是我当时不知道怎地，居然卡在这上面了。
4. Given a byte array, which is an encoding of characters. Here is the rule:
    a. If the first bit of a byte is 0, that byte stands for a one-byte
character
    b. If the first bit of a byte is 1, that byte and its following byte
together stand for a two-byte character
Now implement a function to decide if the last character is a one-byte
character or a two-byte character
Constraint: You must scan the byte array from the end to the start.
Otherwise it will be very trivial.

============
Microsoft
============
一共五轮，过程没什么好讲的，标准流程，直接上题吧：

1.1. What are the two ways to implement hash tables? How to add, delete, and
lookup an key? How to deal with collision?

1.2. Given an integer, return the next prime number bigger than it.
Follow-up: If this function will be called frequently, how to optimize the
performance?

2.1. What's a full outer join in database? Implement a full outer join given
two tables.
Follow-up: If two tables are very big (i.e., no enough RAM to load them),
how to deal with it?

2.2. Given random() that can return 0 or 1 uniformly, implement random_new()
that can return 0 with 90%, and 1 with 10%.

3.1. Given an image represented by byte[][] image, return its mirror image.

3.2. Design a distributed LRU

4.1. Given an array [a1, a2, ..., an, b1, b2, ..., bn], transform it to [a1,
b1, a2, b2, ..., an, bn].
Requirement: time complexity O(nlogn), space complexity O(logn)
Sol: the base idea is to use quicksort techniques. Suppose the current array
is A, whose size is 2k.
1. Divide A into four segments: A = [A1 A2 B1 B2], where A1.size = B1.size =
k / 2, B1.size = B2.size = k - k / 2;
2. Swap A2 and B1, and we get A = [A1 B1 A2 B2]. In this step, we actually
need to rotate [A2 B1] to the right by k - k / 2 items. This can be done by
reversing [A2 B1] first, and then reversing [A2] and [B1] respectively.
3. Recursive on [A1 B1] and [A2 B2] respectively.

Example: A = [1 2 3 4 5 6 7 8 9 10]
A1 = [1 2], A2 = [3 4 5], B1 = [6 7], B2 = [8 9 10]
After 2nd step, A = [1 2 | 6 7 | 3 4 5| 8 9 10]
For the 3rd step, process [1 2 6 7] and [3 4 5 8 9 10] repectively

4.2. Design: suppose you have a cluster, and each machine in this cluster
has a large number of numbers. How can you find out the median of all the
numbers on all the machines.

5. Design: How to design a crawler?


============
Amazon
============
题目比较简单，感觉他家标准降低好多好多。。。

1. Given a string, find the longest palindromic substring

2. Given a binary tree, find the length of the longest path in the tree. A
path can start and end anywhere in the tree (i.e., not necessary from the
root to a leaf).

3. Given a large number of integers, return the largest K numbers. How to
process them using MapReduce?

4. Implement a priority queue: enQueue, getFront, deQueue

5. Given a set of points on a plane, and a list of circles centered at the
original point, find the ring containing the most number of points.

6. Design: You have a HTML page, which contains many strings describing
potions in a CSS file, how can to compress these strings to reduce the size
of the HTML page.
Follow-up: Users complain that your website becomes slow recently, how can
you find out the problems, and how to fix them?

7. Java OO concepts, dissertation and behavior questions from CC150.


8. http://www.mitbbs.com/article_t/JobHunting/32636739.html
发信人: tiantianyo (天天向上), 信区: JobHunting
标  题: 多家的面经
发信站: BBS 未名空间站 (Fri Feb 28 19:53:56 2014, 美东)

具体哪些公司就不提了，反正就是版上的那些大公司，把能记住的电面onsite题就混在
一块儿了。

1. anagram
2. OO design: candy bar
3. sort color
4. 给一个小写的string，例如“abcd” 输出所有大小写混合的组合
5. string to double
6. given a string words, find the shortest substring including all the given
key words
7. what is little/big endian, how to tell if one machine is little or big
endian machine？
8. power set
9. smart pointer
10. given a set of weighted intervals, find the set non-overlap weighted
intervals that has the biggest weight
11. two sum变形
12. serialize/deserialize binary tree, the leetcode solution is not accepted
by the interviewer, nor the inorder&preorder sequence method
13. design a data structure that can support: get element in O(1), delete
randomly in O(1)
14. how to swap the i-th and j-th bits of an integer
15. median of two sorted arrays - all possible solutions discussed
16. find the kth element from an unsorted array
17. valid number
18, given an unsorted integer array, find three integers can form a triangle
19. tell if two words are one-character different: replace/delete/insert
20. given an array of 32-bit integers, the array is already sorted according
to the most significant 28bits, sort the array in O(n)
21. return all the nodes on the deepest path of a BST O(n)
22. an array of float number, calculate the average value with a sliding
window, the window is moved with k steps every time. need to keep the
precision for float type: 1000000 + 0.01 = 1000000 (not wanted)
23. big integer operation and compare
24. generate maze
25. what is TCP, UDP, RTP, differences of them? what is RTP header? what is
DNS? Who owns DNS? What is the name of the organization that manages DNS?
Can a company own its own DNS? Describe how DNS works in very detailed way.
what will happen when you type google.com? How google deal with so many
requests per second? How to load balance the request? What is SSL? What is
the protocol/design mechanism of SSL? 

9. http://www.mitbbs.com/article_t/JobHunting/32636325.html
发信人: noaddiction (五行缺火), 信区: JobHunting
标  题: A onsite 4轮面筋
发信站: BBS 未名空间站 (Fri Feb 28 10:58:55 2014, 美东)

回馈下本版，长期潜水得到了很多帮助。

算法两题，一个是leetcode原题，判断两个tree node的lowest common ancestor.
另一个是directed graph, 代表work flows, 打印dependency sequence.
1->2->3
4->5《  （两个分别指向3，8的箭头）
6->7->8
task 3必须在1245都完成后才出现，task 8必须在4567都完成才出现。
sequence12453678是个解。
基本靠提示做的。3和8只有进来的edges, 当作root, 分别做post order tree
traversal
(不一定binary tree). 结果合并并且避免重复就可以了。

OO design题主要针对scalability。搞熟stateless, stateful conversation的差别,
partition, replica各自的好处就差不多了。我尽量把自己知道的知识都表达出来，只
要沾边的。比如，这个系统用name value database比sql更好。Optimistic lock和
pessimistic可以同时使用，用checked exception提供alternative work flow比
return null好，等等。

behavior问题主要靠以前工作经验。

10. http://www.mitbbs.com/article_t/JobHunting/32623475.html
发信人: xyf501 (Ivan), 信区: JobHunting
标  题: FLAG干货：
关键字: flag,面经
发信站: BBS 未名空间站 (Mon Feb 10 17:01:39 2014, 美东)

Linkedin

phone1：烙印
lowest common ancestor w/ and w/o parent pointer
phone2：国人
search in rotated sorted array

onsite:
1.两个国人
implement addInterval(start, end) and getcoverage(),
2.两个国人
talk projects and some behavior question
3.烙印
lunch, talk about technologies interest
4.亚裔，不确定是否国人
Manager, talked a lot of behavior questions, interest and projects
5.烙印
Design: tinyurl
6.烙印+小白
1.exclusive array, give an arr1, return a new arr2, arr2[i] is the
multiplication of all elements in arr1 except arr1[i]
2.boolean isMirrorTrees(tree1, tree2)/inplace convert a tree to its mirror
tree/create a new mirror tree
3.find the intersection of two linked list(do not use hashmap)


Amazon

phone1: 烙印
Given a list of test results (each with a test date, Student ID, and the
student’s Score), return the Final Score for each student. A student’s
Final Score is calculated as the average of his/her 5 highest test scores.
You can assume each student has at least 5 test scores.

phone2:白男
1.大数plusOne
2.给你一个按字母顺序排好的字典（但你不知道字母顺序,非英语），要求找出字母顺序
例：
单词顺序：
    wrt
    wrf
    er
    ett
    rftt
字母顺序：
    w,e,r,t,f

onsite:
1. 白男
class MagicNumber{
boolean isMagicNum(long num);
long nextMagic(long num){
    while(!isMagicNum(num)){
    num++;
}
return num;
}
}
consider a data structure to improve the nextMagic(long num)
2. 烙印
behavior questions and text editor design(insert, add, search, cut, paste)
3. 白男
大数加法 (int数组表示大数，每一个元素代表一个2^31进制数字)
4. 日本人manager
lunch interview:
    4.1 describe a time you are stressful to meet a deadline
    4.2 describe a time you feel most proud in your professional career
    4.3 what would you change in your past project if you have a chance
5. 白男
give API: List<Movie> getMovies(Actor a);  List<Actor> getActors(Movie m);
implement: int findDistance(Actor a, Actor b)
6. 白男
System design, open question, give your solution, describe pros and cons


Google
phone： 白男
1. remove duplicates of the array in place
2. 一道BFS题。具体是什么记不清了

on-site:

1. 白男
count islands in a m*n grid （一个联通的值为1的区域被视为一个island）
例：
    0011010
    0010010
    1000110
    0000001

    4 islands found in above grid
Design： copy and shuffle lines in a 8 GB file, memory limit 1 GB (you are
given multiple machines)
2.国人
void minMSwap(int[] num, int m), return the min array after m swaps， each
swap happens only between two adjacent elements([4,2,1,3], 2 return [1,4,2,3
] )
4,2,1,3
4,1,2,3
1,4,2,3
design a protocol to syncing gmail messages among different client apps

3.小白
give a list of <id, parent id, weight>, build the tree(not limited to a
binary tree), then update each node’s sum value(sum is the sum of all its
descendents’ weights)
int[] num incremental(大数加一)
design interface for memory cache

4. 国女
find a intersection to build office so that the sum of all employees’
commute distances is minimum. （the map is represented as a m*n grid, you
are given each employee’s coordination, they can only move in up-down and
left-right directions）

5. 白男manager
How to find median of unsorted integers in linear time
Design the system architecture(FE and BE) for above service in a distributed
system (find optimal office location).


FB
phone: 小白
word break, suffixtree

Onsite:
1. 越南人？
Talked the resume, project and behavior questions. lowest common ancestor
with parent pointer.
2. 白男
is valid binary search tree (handle edge case), if the tree size exist
memory limit, how to handle?
3. 白男
Design question, FB search
4. 国人
give a time, search in a log file. 需要自己提问需求，并考虑边界情况。
    00:23 *****
    00:24 *****
    00:56 *****
    01:02 *****

how to distribute the work to 10 servers?
5. 白男
Celebrity Problem

11. http://www.mitbbs.com/article_t/JobHunting/32622081.html
发信人: bainikolaus (bainikolaus), 信区: JobHunting
标  题: G面经 已挂
发信站: BBS 未名空间站 (Sat Feb  8 16:15:06 2014, 美东)

Update:

已挂

------------------------------------------------------------

昨天onsite完的，趁还记得上来写一下，面的不好，求bless。

一轮店面
第一题判断一个string的开头第一个字母是不是大写，两行代码就能写完，没有任何陷
阱。第二题让我用Java（因为我本来用python）写判断binary tree是不是bst。两个题
都很简单，然后还让我说一下自己做过的最challenging的一个project，整个面试不到
二十分钟就说问完了问我还有没有问题，我连忙问他为什么这么快是不是我什么地方做
错了他不愿继续问下去。答曰他在G工作七年多面了不下一百人，十分清楚哪些人去
onsite不是在浪费他们engineer的时间，觉得我没有问题。。。

过了一周果然hr说去onsite，由于我所在的城市有G的office，所以去那里面，早上三
轮然后吃午餐，下午再两轮，一共五轮

第一轮
给一个矩阵，每个格子上有三种可能，空房，阻碍物或者是保安，阻碍物不能进，空房
四个方向都能进，要写代码给每个空房标记其离最近的保安的距离，比如

000
BGG
B00

B表示障碍物，G表示保安，0表示空房，应该标记为

211
BGG
B11

我说扫一遍矩阵，然后遇到每个G就bfs整个矩阵, 他说不是optimal，optimal可以做到
O(N^2)。当时想不出，他说那就先按我那个想法写代码。写完就到时间了。后来回家后
就想到optimal的解法了，对所有G一起开始bfs就可以了。

第二轮
写一个函数生成满足下面三个条件的integer
1. 非负
2. 不能有重复数字
3. 递增，既后面产生的比前面产生的要大

我问要一次性全部生成所有数字还是每呼叫一次函数产生一个，他让我先写一次性产生
全部的，这个不难，backtracking，follow up是假设现在给一个符合条件的数字，如
789，返回下一个（比输入大但是最小的）数字，790。一开始我没思路，说很多edge 
case，然后多观察几个例子后发现有些规律，说出来后他说看起来不错，然后举了几个
例子让我模拟跑一遍，没有问题，他说ok，不用写code了，正好也到时间了

第三轮
问了一个Java的问题
假设有两个class，A和B，B是A的子类，
先有下面几句
A a = new A();
B b = new B();
List<A> la = new List<A>();
List<B> lb = new List<B>();
（反正就是建了A，B的各一个instance，list of A 和 list of B 各一个instance）
然后问下面四句哪句能过compiler，哪句不能：
a = b;
b = a;
la = lb;
lb = la;

答案是只有第一句能过，我一开始答1和3能过（我真心不熟Java，python里面的话啥能
过啊亲）。could use generic wild card
http://tutorials.jenkov.com/java-generics/wildcards.html


然后出了一道python generator的题，写代码，还有follow up，也要写代码，最后都
超出时间了。

中午吃饭, 下午接着面

第四轮
问我知不知道zip文件，我说用过但不知原理。他就说我们来讨论一下

假设一个文件压缩后的表示是

#3, #5, #6, 2 5, #8...

”#k“形式的代表这个数字k，两个数字“i j”形式的代表取前 i 个
数字做 j 长的 circular重复，像上面那个表示，前面3个都是表示单个数字，
然后 2 5表示取前2个数字 （既56），组成5个数字，不够的从头再取，所以就是56565
最后上面解压缩后应该为
3, 5, 6, 5, 6, 5, 6, 5, 8...

要我写的是压缩算法的代码。
我提出从头扫，一边一边用hashtable记下见过的number，每前进一位就检查hashtable
有没有符合当前数字模式的number出现过，然后他说还不错，写代码。一边写一边出现
bug，一边发现很多写代码前没考虑的东西，最后勉强算写完，时间也到了，他说这个
他也没写过，是在一篇paper上看到的算法，原算法跟我的有些不同，倒是都用了
hashtable。。。

第五轮
拿着我简历进来，说有人跟你谈过你的简历吗，我说没有，他表示万分惊讶，然后在我
简历上挑了一个research project让我说说，说完后用c++出了一个题，一个cipher类
，有一个member function是对输入加密，加密方法为对input的每16个Byte和一个
increasing counter做xor，这个increasing counter也是有16Byte，从00..01（前
15Byte都是0，最后1Byte是1）开始，还有一个要求，举例说：
第一个input 有20个Byte，前16个Byte就和00..01做xor，后4个Byte和00..02的前
4Byte做xor
然后之后再对第二个input加密的时候，对这个input的前12Byte用00..02的后12Byte（
即11个Byte 0，1个Byte 1）

然后让我写这个class

我问了一句要是couter的数用完了怎么办，他反问我这个counter有16Byte，多久会用
完。因为已经很累了，算错了好几次，中途我还说16乘以8等于64。。。反正在他逼迫
下我硬着头皮模拟算了一下，得出结果就是很久很久很久才会用完，不用担心。然后又
因为好久没写c或c++，还有真的很累，脑袋一片发麻，茫然不知如何下手，他看不下去
了就说那你就写一个能从小到大生成这个counter能表示的所有integer的函数吧，你要
对python熟一点的话就用Python，这个写完后有两个小bug，迅速改正过来，然后就到
时间了。问我还有没有问题，我就随便问了一下这个office有哪些project，然后就结
束了。


12.http://www.mitbbs.com/article_t/JobHunting/32625123.html
给一个SEQUENCE， 给一个 window size, 求 running average.

  constructor里给WINDOW SIZE， 实现一个 next(double input) interface 返回 
  the running average till input:

  For example:

  window size = 5;

  input: {1,2,3,4} output: 2.5
  input: {1,2,3}   output: 2
  input: {1,2,3,4,5} output: 3
  input: {1,2,3,4,5,6} output: 4


13.http://www.mitbbs.com/article_t/JobHunting/32586301.html
发信人: pdu (PigDuckUnited), 信区: JobHunting
标  题: G onsite面经
发信站: BBS 未名空间站 (Tue Nov 26 07:41:39 2013, 美东)

上周onsite了G，4轮。由于签了NDA，我就不透露题目细节了，但是会说下怎么准备可
以过。也麻烦不要站内我问题目细节，一律不回。

当前状态：hr说还有2个面试官没提交feedback，已经找我要了G的朋友名单做
reference
不知道是什么意思。是说当前已知的feedback还不错，有戏？

第一面：
问简历上的东西，很多想法相关的事情，面试官做了很多记录。
后来问了一个题，我觉得非常有意思，但是我答的很烂，在面试官再三提醒下，还是没
上正途。
后来面完的当天晚上，才幡然醒悟。。。推荐大家看下《集体智慧编程》，对面试会有
好处。另外面试的时候，实在想不出来，不妨换个思路。我一直到最后都以为是要考我
图论，实际上是考ML基础相关的。

第二面：
编码题：涉及到数据结构，比较简单的算法
推荐c++的同学把STL弄熟悉一点，面试的时候可以信手拈来。比如set, map, multi_
set, multi_map, next_permutation, sort, unique, heap, priority_queue, tr1::
unordered_map等等

第三面：
纯编码题，字符串处理，细心点就没事儿
另外还问了点简历上很基础的知识点，比如awk，bash，linux command等，用意应该是
确认你简历上不是瞎写的

第四面：
设计题
推荐上highscalability.com看看文章，理解下典型的web三层架构，load balance，
cache，storage等，还有离线处理，在线处理等，对前端js的ajax也最好了解一下。

总的来说，第一面没答出来的题，感觉是最有意思！整体都不难，要看临场发挥。
面试官都非常nice~~

14.http://www.mitbbs.com/article_t/JobHunting/32542339.html
发信人: milili (milili), 信区: JobHunting
标  题: Google, Facebook, Rocket Fuel面经及经验总结
发信站: BBS 未名空间站 (Sat Sep 28 18:53:20 2013, 美东)

找工作期间在本版潜水两个月，收益良多，发一下最近面经和经验作为回馈。
本人背景：美国不错学校电子PHD即将毕业，专业是EDA做电路设计算法优化。因为EDA
已经是一个很稳定的工业，没什么太大的前景，随想转到前沿的tech公司。本专业只投
了一家现在最大的公司，拿到offer。别的投了Google, Facebook, Rocket fuel, 
Twitter, Linkedin, Yahoo, Amazon, Box, Oracle. 除了box别的都找人refer了， 在
此感谢板上大哥们的热情帮忙. 除了GFR别的都没理我，可能背景差太大了。

因为之前是学算法的，mit算法书以前就看过两遍，基础还可以，前期8月份刷了遍
leetcode。然后9月初投出简历。两个星期刷Career cup 150， 最后面试期间一直查缺
补漏。到现在尘埃落定大概两个月。 最后GFR全挂，总结下惨痛经历：

1. Facebook电面

面试官做distributed cache infrastructure的，先问我最难的project，没怎么好好
准备过behavior，胡乱说了一通。但是因为做的是电路相关，非行内人士很难明白，讲
的也比较乱。最后估计起到了反效果。感觉如果不是有特别好的经历和体会的话（特别
对于fresh在校内没什么好相关项目经历的）这种最好长话短说想办法一笔带过，不然
可能起到反效果。

浪费了大几分钟开始第一题，leetcode原题，Valid Panlindrome
"A man, a plan, a canal: Panama" is a palindrome.

这题之前做过，也很简单，但当时太紧张出了一个很sb的bug，还是在面试官提示下找
到的。15行的代码出bug实在是不能犯的错误。另外在判断一个char是否letter的时候
没有另用函数把一堆&&写了两次，被批评不够简洁。

第二题，将1->2->3->4->5->6->7 变成 1->7->2->6->3->5->4，不能用额外空间

第一遍用了recursive很快解决，被指出用了stack额外空间，开始改iterative，最后
因为第一题浪费时间手忙脚乱没改完。说了一下大概思路草草收场，面完就知道不妙。
4天后被通知挂了。

总结： facebook非常重视coding的clean和bugfree。 这两题都没什么算法但是如果
coding不过硬第一遍很容易有bug，我感觉从这点上来讲面试官出题水品很高，死的心
服口服。 另外他家感觉比较看背景，phd onsite会有jedi面试问项目经验什么的，专
业差太大估计要超级牛才容易过。

2. Google电面

上来直接上题，题目有些绕。CSS里面表示颜色用
#abcdef (eg 0x1F2A3B) 这种形式， 每个字母代表四个bit (hex)，两个字母代表一种
原色
比如 ab = R, cd = G, ef = B (每种原色整个是0-255间的一个数字)
现在需要压缩空间改#abcdef 为 #xyz
实际上#xyz = #xxyyzz,所以减小一半，问怎么找到最好的压缩让
（ab-xx）^2 + (cd - yy)^2 + (ef - zz)^2 最小

这题其实数学上很简单因为三个维度是分开的，其实就是找#ab到#xx的压缩。

我当时的面试官是个asian可能是韩国人或abc，有点bitchy。我最开始说让我想一想，
才过了5秒钟他说不知道我在想什么让我在google doc上打，然后我就在上面打example
试图观察一下规律，他又阻止我说不用什么都打出来。完了我说了我的观察： a的权重
更大， x应该很接近a， 实际上 x = a, a - 1 , or a + 1。 然后他不置可否。可能
我说的不是很清楚，他又开始和我纠结我的变量名用得不好。因为他一直和我纠结这些
细节，我也没法安心思考，直接就开始写code，又拿不准函数input和output应该用什
么样的type和形式。这就是这种模糊提很麻烦的一个地方。面试官还是不给提示，我就
开始写但是code写的很乱。中途面试官没有任何提示。完了我说想move on到下一题他
说没时间了要我找bug。整个code写的很糟，因为没有分情况按 a > b 时 x = a, a- 1
， a < b时 x = a, a + 1这样来考虑所以变成了for loop非常乱。还剩5分钟时万念俱
灰面试官问我还可以怎么optimize已经没心思回答了跟他说”如果你想让我检查代码我
就看吧“开始有点顶撞他的意思。我电面这么多次第一次和面试官搞得这么僵心情非常
沮丧。最后草草收尾。3天后通知被挂。

心得体会：google电面其实是很松的，很容易过。电面没过打击很大，除了运气不好碰
到面试经验不丰富的面试官和模糊题外主要问题还在自己。因为题目并不难，就算和面
试官不和拍也应该避免干扰仔细思考认真写代码。特别是到后面十分钟我有点破罐子破
摔，这样给面试官映像肯定非常糟糕。因为面试的一个目的就是考验你是rise against
challenge还是crash under pressure。这点上我表现的非常失败。因为google家比较
看中算法算是我的强项，所以没能去成onsite非常可惜。

3. Rocket Fuel

网上交简历，当天收到hr回信，过两天和hr电话chat半个小时，主要问问背景和看你是
不是serious applicant。完了发来online test 5hour。我做的auto racer。没有
follow他的hints选了最优算法但是由于编不出balanced avl tree有个test case没过
，还是个给了电面，面试官是三哥，电面是之前有人贴过的ad query题，给出了大家讨
论的最优答案，又拓展到分布式系统。才说了半个小时面试官突然说时间到了问我有没
什么问题，我看他很急就说没问题就bye了。本来以为肯定挂了因为预定要一个小时，
结果过了两天recruiter说feedback very positive让我去onsite有点莫名其妙。

onsite中午和一个cmu毕业的topcoder 2000+的nb phd吃饭闲聊了一下，下午面了四个
人，三个三哥一个asian。两个big data infrastucture（最后端）的， 两个serving 
infrastrucre（中后端）的。所有题目在之前rocket fuel的帖子里或者leetcode都能
找到，除了一道挺有意思的题

给定一个n*n的board里面是0或1.算出里面独立0group的数量。比如

0 0 1 1 1
0 1 1 1 0
1 1 1 1 0
1 0 1 1 1
1 1 1 1 1

答案是3个group。我瞬间给出了一个BFS的O(n^2)答案，被指出需要visited数组的额外
空间。然后给了一个逐行扫描的算法相当tricky，我经过提示才想出来。面试完后第二
天被告知挂了。其实自我感觉还不错除了java multithreading答的不好。recruiter给
的反馈是总体还不错但有人指出我coding a bit messy。说另外还有一个不错的
candidate选了另外那个人，说我是pretty close。我自己猜测如果不是因为另外一个
人是三哥或美国人这种原因还是死在coding quality上，另外背景实在差的有点远。他
家要求最好一遍写出clean code。另外在onsite是建议code不要写太长，如果要超过一
黑板最好把里面主要部件都先用函数代替写出主要流程向面试官说明之后补充即可。

心得： onsite时因为很多题都见过经常迅速讲一下思路就开始coding，感觉交流不够
。面试的时候交流还是第一位的，如果跑上来就写代码写的再好面试官对你印象也未必
好（可能还会觉得你是练过的），因为他会把你当成未来的coworker所以交流的融洽是
很重要的。rf家的big data infrastructure全部是三哥，我觉得这也是我挂的一个原
因，建议申请ai optimization那些核心组，那才是他们家的精髓所在。rf没有之前提
的那些帖子那么乱但感觉还是不够正规，面试的时候不是很舒服，连schedule都不给你
,说好的面试官经常换人。

总体心得：coding不过硬会导致必然的失败。我之前就是觉得自己算法底子不错忽视了
coding，其实本末倒置。工作中coding才是最重要的，而且看了很多牛人的coding之后
才发现这个事情真的不是搬砖那么简单，同一个内容的程序coding好不好能差很多（再
加上clear和readability的考虑）。顶尖it公司要的不是average coder而是top coder
，所以以前仗着算法不错就满足于average的coding水品实在是很幼稚，以后一定会在
这方面加强锻炼。

个人还有些算法和advanced data structure的重点觉得没有在leetcode里面很好体现
的，总结如下:

1. 很多recursive容易的算法也要考虑iterative方法。因为掌握iterative代表你对问
题结构理解上升了一个高度。e.g. reverse linked list， tree traversal

2. i) top k (kth) elements: heap O(n+klogn), quickselect O(n) average O(n^2)
worst, median of medians O(n) worst. cons and pros.
Extension: what if all data can not fit into memory. heap size of k O(nlogk)
for single machine, many machines see 3.
ii) get median in data stream: max heap + min heap

3. kth element in many m machines: binary search, pick a pivot and see how 
many less and larger among all machines, then discard halves accordingly (
distributed quickselect)

if sorted in single machine: find smallest (k/m)th element among all 
machines and discard the less partition.

4. stack support O(1) getMin
   queue support O(1) getMin
e.g. k sliding window, most frequently clicked url in past 12 months.

5. reservoir sampling for infinite stream, generate random(1-7) with random(
1-5), card shuffle, string permute in place

6. data structure with O(1) insert, delete, getRandom, get: hashmap + array

LRU data structure: hashmap + doublelikedlist.

binary search tree with rank() (position of inserted or queried data)
(add treesize attribute for each node)

7. bit operation and bitset.
e.g. find missing number in large data, reverse binary number, 

8. java multi-threading, blocking queue, nonblocking queue, H20, philosophy 
dining, deadlock checking. 现在是个公司都问concurrency，一定要好好准备。

9. OOP: elevator design, parking lot design
distributed: large log file design, social network design, distributed cache
design ....


15.http://www.mitbbs.com/article_t/JobHunting/32575573.html
发信人: eastflag (Minifancy), 信区: JobHunting
标  题: 最新G 电面面经
关键字: G,电面
发信站: BBS 未名空间站 (Tue Nov 12 16:37:51 2013, 美东)

今天G的电面，应该是第一轮电面吧，因为题目比较简单。。。

对面是个女的，估计是SDE,先是简单问下为啥选Google，然后是两道题

1. 大数+1
这题好常见。。。

2. 对数组排序，使得a1<=a2>=a3<=a4>=...
也是很简单的O(n)，注意写的时候不用swap元素。。。

Google doc写的，大概花了30分钟，然后问了下有什么问题。。。


16. http://www.mitbbs.com/article_t/JobHunting/32608789.html
发信人: adsd (adsd), 信区: JobHunting
标  题: g电面
发信站: BBS 未名空间站 (Tue Jan 14 18:49:08 2014, 美东)

肯定跪了。
interface RateLimit {
    /** Sets the rate, from 1 to 1000000 queries per second */
    void setQPS(int qps);

    /** accept or reject a request, called when request is received */
    boolean allowThisRequest();
}

brief example:
server instantiates your object, calls setQPS(1)
at at time t, user1 makes a request, allowThisRequest() returns true
at time t+0.01 sec, user2 makes a request, allowThisRequest() returns false
at at time t+1, user4 makes a request, allowThisRequest() returns true
at time t+5 sec, user3 makes a request, allowThisRequest() returns true
写个class implement这个接口

String encode(List<String> input);
List<String> decode(String input);


17. http://www.mitbbs.com/article_t/JobHunting/32618057.html
发信人: qianquan (qianquan), 信区: JobHunting
标  题: 发个g的电面
发信站: BBS 未名空间站 (Sun Feb  2 00:05:08 2014, 美东)

上周面的，答得超级不好，估计跪了，发题攒下人品。。
1. implement java iterator interface
input : 11223344
output : 1223334444 （类似于count & say那题) 由于对iterator不熟直接跪掉

2. 
how to find median from 2 sorted array
then ask
how to find median from k sorted array...


18. http://www.mitbbs.com/article_t/JobHunting/32582727.html
电面题目：
一位国人大哥，先在这里谢过啦，时间刚好45分钟，吐槽下Google docs上写程序好蛋
疼，什么时候可以搞个可以支持Vim的编辑器吧。。。。
Assume some binary (each pixel is either black or white ) images, have same 
width and height, and the length is power of 2. Present it by quadtree: 
divide the image into quarters, each quarter can be all back, all white or 
mixed, subdivide the mixed ones… recurse.

+-------+---+---+
|         | F | F  |
|   T    +---+---+
|         | T | T  |
+---+--+---+---+
| F | T  |         |
+--+---+   F    |
| F | T  |         |
+--+- +------ --+

a) how to present this image

struct TreeNode {
    TreeNode* upperLeft;
    TreeNode* downLeft;
    TreeNode* upperRight;
    TreeNode* downRight;
    int size;
    bool pixel;
    TreeNode(bool p, int s): pixel(p), size(s), upperLeft(NULL), downLeft(
NULL), upperRight(NULL), downRight(NULL){}
};

TreeNode* copy( TreeNode* root) {
    if( !root)
        return NULL;
    TreeNode* r = new TreeNode( root->pixel, root->size);
    r->upperLeft = copy( root->upperLeft);
    r->upperRight = copy( root->upperRight);
    r->downLeft = copy( root->downLeft);
    r->downRight = copy( root->downRight);
    return r;
}

b) count all the black pixels of this image

int getBlackPixels( TreeNode* root) {
    if(!root) 
        return 0;
    if( !root->upperLeft) {
        if( root->pixel)
            return root->size * root->size;
    }
    int sum = 0;
    sum += getBlackPixels( root->upperLeft);
    sum += getBlackPixels( root->downLeft);
    sum += getBlackPixels( root->upperRight);
    sum += getBlackPixels( root->downRight);
    return sum;
}

c) merge two image( actually it's to "and" two image with same size since 
all pixels are boolean)

TreeNode* merge( const TreeNode* image1, const TreeNode* image2) {
    if( !image1->upperLeft && !image2->upperLeft) {
        return new TreeNode(image1->pixel && image2->pixel, image1->size);
}
    if( !image1->upperLeft) {
        return mergeHelper(image1, image2);
    }
    if( !image2->upperLeft) {
        return mergeHelper(image2, image1);
    }
    TreeNode* root = new TreeNode(image1->pixel, image1->size);
    root->upperLeft = merge( image1->upperLeft, image2->upperLeft);
    root->upperRight = merge( image1->upperRight, image2->upperRight);
    root->downLeft = merge( image1->downLeft, image2->downLeft);
    root->downRight = merge( image1->downRight, image2->downRight);
    return root;
}

    
TreeNode* mergeHelper( TreeNode* image1, TreeNode* image2) {
        
        if( !image1->pixel) {
                        return new TreeNode(image1->pixel, image1->size);
        }
        return copy(image2);
}












19. http://www.mitbbs.com/article_t/JobHunting/32300077.html
发信人: Michelle85 (Michelle), 信区: JobHunting
标  题: 发个google的面试题
发信站: BBS 未名空间站 (Thu Jan 10 14:52:46 2013, 美东)

刚收到消息，悲剧了，意料之中，不过我也还ok，还有其他公司move on吧，可能今年
准备的还是不够，希望能对其他找工作的人有帮助。

一共三题，有一道是c++的基础题，那个很简单，基本你要是会c++应该就会写。

另外两道题
1 第一道题，是说你知道(n&(n-1))得出什么结果吗？
  这个好答，我当时说这个我见到过，是看一个数是不是2^n，然后他问，除了这个之
外，还可以用在别的地方吗？然后他问了这个之后，我主要是不知道他要问的point在
哪。。。最后兜兜转转地跟他聊了很多，结果最后终于知道，他要的答案是，“n&(n-1
)”改变最后一位不是0的数字。I mean,这个我未必不知道，但是他问我还可以用来做
什么的时候，我确实不知道他想要什么答案，因为这个可能可以用在很多情况下

2 第二道题，以1/(2^n)的概率返回1，其它的时候返回0，题目应该假设有个函数可以
生成1或者0，以1/2的概率
  我当时想了一下，最intuitive的想法是先产生一个数，num = 1<<n，然后 result =
(double)num * rand();
  当时写的时候没有把num转化成double，这是一个bug，并且我觉得这个bug其实是不
应该的，也是个很关键的bug。 然后他不满意，我也知道，我说n很大的时候num会
overflow，这个时候有两种解决方式，一种是用BigInt，还有一种用divide and 
conque，举了个例子，如果int是16位的话，那么n大于16的时候，就不断地divide and
conque，直到小于16为止。

第二题我觉得可以这样来做。

假设有个函数f以1/2的概率产生1和0

记i=1，用f产生一个数字。如果是0的话，停止

如果是1的话，记i=2，继续用函数f产生是1或者0。如果是0停止，如果是1继续这个迭
代步骤，直到i=n。


'''
