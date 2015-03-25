## DP 

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

######[Word Break](./Array/word_breakII.py)
* Combine the DFS and DP 

######[Longest Increasing Subsequence 最长上升子序列](./Interviews/Longest_Increasing_Subsequence.py) [(Not in Leetcode)](http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/)
* state: ~~```dp[i]```表示前i个数字中最长的LIS长度(错误)~~ ```dp[i]```表示第i个数字结尾的LIS长度(正确)
* function: ```dp[i] = max(dp[j]+1, j<i and a[j] <= a[i])```
* initialize: ```dp[0..n-1] = 1```
* answer: ```max(dp[0..n-1])```
任何一个位置都可能为开始, 所以所有都要初始化为1, 因为最少LIS是1

######[Decode Ways](./Leetcode/Decode_Ways.py)
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

###DFS
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
