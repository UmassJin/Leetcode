## DP 
注：转自cyandterry的总结，并加以适量修改

###模板
* 状态 state: 灵感, 创造力, 储存小规模问题的结果
* 转移方程 transfer function: 状态之间的联系, 怎么通过小的状态来算大的状态
* 初始化 initialization: 最极限的小状态是什么
* 答案 answer: 最大的那个状态是什么

###Clues
1. Cannot sort, or swap
2. Satisfy:
  * Find a maximum/minimum result
  * Decide whether something is possible or not
  * Count all possible solutions(Doesn't care about solution details, only care about the count or possibility)

###Types of DP
####1. Matrix DP 20% (Triangle, Unique Path, ...)
* state: ```dp[x][y]```表示从起点走到坐标 (x,y) 的xxx
* function: 研究下一步怎么走
* initialize: 起点
* answer: 终点
* 复杂度一般为O(n^2)

#####[Triangle](./Array/Triangle.py)
* status: ```dp[x][y]```表示从bottom走到top每个坐标的最短路径
* function: ```dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]```
* initialize: ```dp[-1][j] = triangle[-1][j]```
* answer: ```dp[0][0]``` (比较奇怪，因为是由下至上)

#####[Unique Path](./Array/Unique-Path-1%262.py) 
* state: ```dp[x][y]```表示从起点走到 (x,y) 的path数
* function: ```dp[x][y] = dp[x-1][y] + dp[x][y-1]``` | ```if 障碍, dp[x][y] = 0```
* initialize: ```dp[0][y] = 1, dp[x][0] = 1```
* answer: ```dp[M-1][N-1]```

#####[Minimum Path Sum](./Array/MinimumPathSum.py)
* state: ```dp[x][y]```表示从起点走到x,y的minimum path sum
* function: ```dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + grid[x][y]```
* initialize: ```dp[0][0] = grid[0][0], dp[x][0] = dp[x-1][0] + grid[x][0], dp[0][y] = dp[0][y-1] + grid[0][y]```
* answer: ```dp[M-1][N-1]``

-----

####2. One Sequence DP 40%
* state: ```dp[i]```表示前i个位置/数字/字母，以第i个为...
* function: ```dp[i] = dp[j] ...j``` 是i之前的一个位置
* initialize: ```dp[0] = ...```
* answer: ```dp[N-1]```
* 复杂度一般为O(n^2)

######[Climbing Stairs](./Array/ClimbingStairs.py)
* state: ```dp[i]```表示爬到前i个台阶时的方法数
* function: ```dp[i] = dp[i-1] + dp[i-2]```
* initialize: ```dp[0] = 1, dp[1] = 2```
* answer: ```dp[N-1]```

######[Jump Game](./Array/JumpGame.py) | [Jump Game II](./Array/JumpGameII.py)
* state: ```dp[i]```表示能否跳到第i个位置O(n^2) (还有一种O(n)的dp, 见方法2) | dp[i]表示跳到这个位置最少需要多少步.
* function: ```dp[i] = for j in (i-1 ... 0) if dp[j] and j能跳到i)``` | ```min(dp[j] + 1, j < i and j能跳到i)```
* initialize: ```dp[0] = True``` | ```dp[0] = 0```
* answer: ```dp[N-1]```

######[Palindrome Partitioning II](./Array/Palindrome_PartitioningII.py)
* state: ```dp[i]```表示从s[0]到s[i]的子串中回文的数目是多少
* function: ```dp[i] = min( dp[j]+1, j<i and j+1 ~ i 这一段是一个palindrome```) (这里需要用另外一个数组来储存是否是palindrome))
* initialize: ```dp[0] = N-1```最少N-1次cut就行了
* answer: ```dp[N]-1```(这里有些不一样，用回文的数目减去1得到min cut数目)
* There is the other good answer, need to understand 

######[Word Break](./Array/word_break.py)
* state: ```dp[i]```表示前i-1个字符能否被完美切分
* function： ```dp[i] = for j in (i-1 ... 0) if dp[j] and j ~ i是一个字典中的单词)```
* initialize: ```dp[0] = True```
* answer: ```dp[N]``` (这里也是比较特殊，因为是i-1个字符，不能从0算起)

  注意j的枚举 -> 枚举单词长度
  O(NL) N: 字符串长度  L:最长单词的长度

######[Word Break II](./Array/word_breakII.py)
* Combine the DFS and DP 

######[Longest Increasing Subsequence 最长上升子序列](./Interviews/Longest_Increasing_Subsequence.py) [(Not in Leetcode)](http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/)
* state: ~~```dp[i]```表示前i个数字中最长的LIS长度(错误)~~ ```dp[i]```表示第i个数字结尾的LIS长度(正确)
* function: ```dp[i] = max(dp[j]+1, j<i and a[j] <= a[i])```
* initialize: ```dp[0..n-1] = 1```
* answer: ```max(dp[0..n-1])```
任何一个位置都可能为开始, 所以所有都要初始化为1, 因为最少LIS是1

######[Decode Ways](./Array/Decode_Ways.py)
* state: ```dp[i]```表示前i-1个数字的DW
* function:  
  ```python
  dp[i]   = 0        # if A[i] == 0 and A[i-1] not in [1,2]
         += dp[i-1]  # if A[i] != 0
         += dp[i-2]  # if 10 <= int(A[i-2:i]) <= 26
  ```
* initialize: ```dp[0] = 1```
* answer: ```dp[N]``` (这里比较特殊，因为是前i-1个数字，且dp[0]只是作为一个起始数字来的)

-----

####3. Two Sequences DP 40%
* state: ```dp[i][j]```代表了第一个sequence的前i个数字/字符配上第二个的sequence的前j个...
* function: ```dp[i][j] =``` 研究第i-1个和第j-1个的匹配关系
* initialize: ```dp[i][0], dp[0][j]```
* answer: ```dp[len(s1)][len(s2)]```
* 复杂度一般为O(m*n)

######[Longest Common Subsequence](./Interviews/Longest_Common_Subsequence.py) [(Not in Leetcode)](http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/)
* state: ```dp[i][j]```表示前i个字符配上前j个字符的LCS的长度
* function:  

  ```python
  dp[i][j] = dp[i-1][j-1] + 1           # if a[i-1] == b[j-1]
           = max(dp[i][j-1],dp[i-1][j]) # if a[i-1] != b[j-1]
  ```
* initialize: ```dp[i][0] = 0, dp[0][j] = 0```
* answer: ```dp[M][N]```

######[Longest Common Substring](./Interviews/Longest_Common_Substring.py) [(Not in Leetcode)](http://www.geeksforgeeks.org/longest-common-substring/)
* state: ```dp[i][j]```表示前i个字符配上前j个字符的LCS的长度(一定以第i个和第j个结尾的LCS)
* function:  

  ```python
  dp[i][j] = dp[i-1][j-1] + 1 # if a[i-1] == b[j-1]
           = 0                # if a[i-1] != b[j-1]
  ```
* initialize: ```dp[i][j] = 0, dp[0][j] = 0```
* answer: ```max(dp[0...len(a)][0...len(b)])```

######[Edit Distance](./Array/Edit_Distance.py)
* state: dp[i][j] a的前i个字符配上b的前j个字符最少要用几次编辑使得他们相等
* function:  

  ```python
  dp[i][j] = dp[i-1][j-1]                                    # if a[i] == b[j]
           = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])) + 1  # if a[i] != b[j]
  ```
* initialize: ```dp[i][0] = i, dp[0][j] = j```
* answer: ```dp[M][N]```

######[Distinct Subsequence](./Array/Distinct_Subsequences.py)
* state: ```dp[i][j]```表示T的前i-1个字符和S的前j-1个字符的DS个数
* function:  

  ```python
  dp[i][j] = dp[i][j-1] + dp[i-1][j-1] # if T[i-1] == S[j-1]
           = dp[i][j-1]                # if T[i-1] != S[j-1]
  ```
* initialize: ```dp[i][0] = 0, dp[0][j] = 1```
* answer: ```dp[M][N]```

  大概意思就是， 因为算的是S的子串和T匹配的方法， 所以一旦S[:j-1]和T[:i]有x种匹配方法时  
  S[:j]必定也至少和T[:i]有x种匹配方法，但尤其当S[j-1]==T[i-1]的时候，需要再加上S[:j-1]和T[:i-1]的匹配方法数  
  注意分清M,i和N,j对应T和S，这个很特殊因为必须是S的子串和T相同

######[Interleaving String](./Array/Interleaving_String.py)
* state: ```dp[i][j]```表示s1的前i个字符配上s2的前j个字符在s3的前i+j个字符是不是IS
* function:  

  ```python
  dp[i][j] = True  # if dp[i-1][j] and s1[i-1] == s3[i-1+j]
           = True  # if dp[i][j-1] and s2[j-1] == s3[i+j-1]
           = False # else
  ```
* initialize: ```dp[0][0] = True```
* answer: ```dp[M][N]```
* Better Solution: check later https://leetcode.com/discuss/19973/8ms-c-solution-using-bfs-with-explanation

-----

####4. Interval DP
* state: ```dp[i][j]``` 代表从i到j这一段区间...
* function: ```dp[i][j] = max/min/sum(dp[i][k], dp[k+1][j])```
* initialize: ```dp[i][i] = ?```
* answer: ```dp[1][n]```

######[Merge Stone 石子归并](http://wikioi.com/problem/1048/)

-----

####5. Tree DP
######Binary Tree Maximum Path Sum

-----

####6. States Compressing DP(不需要知道)
####7. Knapsack


###总结

####复杂度
直接看循环嵌套层数

####关于取dp[N]还是dp[N-1]还有dp[N]-1
1. 首先先分析dp维度，Matrix和Two Sequence dp都是二维，One Sequence是一维
2. Matrix dp一般都是初始(0,0)跳到(M-1,N-1)所以取的是```dp[M-1][N-1]```
3. 如果dp[i]或者dp[i][j]表示前i个什么的时候，需要以N/MN作为结尾，主要原因是这种情况下前0个字符串是没有意义的，至少从1开始，所以取dp的时候也是从dp[1]开始才有意义，所以dp[i]的含义是前i-1个东西的性质，而```dp[0] or dp[0][0]```需要强制赋值
4. 至于dp[N] - 1纯粹是因为Palindrome题目比较特殊，实际我们算的cut-1才是结果

####已知dp问题然后回问满足dp条件的结果
一般这种情况就是根据已知的dp matrix和结论，从最后开始往前回溯，满足的就挑进去，不满足的就不放来解决.

-----

###DFS & Backtracking 
主要想法是先搜索到不能再底层然后再往上走
#####复杂度问题
* 组合的话就是O(n^2)
* 排列的话就是(n!)


#####[Palindrome Partitioning](./Array/Palindrome_Partitioning.py)
* Add the recursion function, palindrome_helper function 
* From the first letter, go through each substr, check whehter this is the palindrome and whether
  the rest part of string is palindrome 
* For loop we go through the input string should from [1 : length+1]
* when pass the string to the bottom recursion, should pass strlist + [rest_string]

-----

###Data Structure
##### Stack 
#####[Longest Valid Parentheses](./Array/Longest_Valid_Parentheses.py)
* Use two methods to solve the problem
* First, use the Stack to record the "("
* Second, iterarate the string for two times, from start to end and from end to start 
