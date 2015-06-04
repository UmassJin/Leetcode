##Table of Content
####[1. Dynamic Programming](#dp)
####[2. DFS & Backtracking](#dfs-backtracking)
####[3. Data Structure](#data-structure)
####[4. Math](#math)
####[5. Two Pointer](#two-pointer)
####[6. Matrix Graph](#matrix-graph)
####[7. String](#string)
####[8. Tree](#tree)
####[9. Linked list](#linked-list)
####[10. Bit Manupulation](#bit-manupulation)
####[11. Greedy (Search from Two Side)](#greedy)
####[12. Bucket](#bucket)
-----------------------

####[1. Rectangle Serious](#rectangle-serious)
####[2. Sum Serious](#sum-serious)
####[3. Permutation Serious](#permutation-serious)
####[4. Array Interval Serious](#array-interval-serious)
####[5. Rotate Serious](#rotate-serious)
####[6. Merge Serious](#merge-serious)
####[7. Sudoku Serious](#sudoku-serious)
####[8. Parentheses Serious](#parentheses-serious)
####[9. Duplicate Serious](#duplicate-serious)
####[10. Stock Serious](#stock-serious)
####[11. Interview Questions not in Leetcode](#interview-questions-not-in-leetcode)
####[12. Python Buildin Function Usage](#python-buildin-function-usage)

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

  1. 最大值/最小值
  2. 有无可行解
  3. 求方案个数(如果需要列出所有方案，则一定不是动规，因为全部方案为指数级别复杂度，所有方案需要列出时往往用递归)
  4. 给出的数据不可随便调整位置

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

* 这道题目有两个解法，一个是from top to bottom，一个是from bottom to top
* from top to bottom: 我们需要每line从后往前遍历，否则新的数会覆盖原来的数
* from bottom to top: 对于每行，不需要从后往前遍历，不会覆盖原来的数

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
* 在实际的面试中，如果直接被问到了jump game2的问题，需要考虑是否可以跳到最后一步，如果可以再看最小跳的个数是多少
* 还需要清楚会不会有负数，如果有负数，怎么处理
* 在Jump Ganme2中，注意把maxNextAval 给maxReachableDis, 不是maxNextAval - 1 

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

######[Unique Binary Search Trees](./Array/Tree.py)
* state: ```dp[i]``` 表示how many unique BST for the number i 
* function: ```dp[i] += dp[k-1] * dp[i-k]  1 <= k <= i ```
* initialize: ```dp[0] = 1, dp[1] = 1```
* answer: ```dp[n]```



######[Longest Increasing Subsequence 最长上升子序列](Experience/Longest_Increasing_Subsequence.md) [(Not in Leetcode)](http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/)
* state: ~~```dp[i]```表示前i个数字中最长的LIS长度(错误)~~ ```dp[i]```表示第i个数字结尾的LIS长度(正确)
* function: ```dp[i] = max(dp[j]+1, j<i and a[j] <= a[i])```
* initialize: ```dp[0..n-1] = 1```
* answer: ```max(dp[0..n-1])```
任何一个位置都可能为开始, 所以所有都要初始化为1, 因为最少LIS是1


##### Good DP Practices and Reference
[DP Practives Problems.clemson.edi](http://people.cs.clemson.edu/~bcdean/dp_practice/)

[G4G: Variations of the LIS Problem](http://www.geeksforgeeks.org/dynamic-programming-set-14-variations-of-lis/)

[G4G: Box Stacking Problem](http://www.geeksforgeeks.org/dynamic-programming-set-21-box-stacking-problem/)


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

######[Unique Binary Search Trees.py](./Array/Unique_Binary_Search_Trees.py)
* status: result[i]: the number of unique BST for a sequence of length i.
* initialize: result[0]= 1; result[1] = 1, only one combination to construct a BST out of a sequence 
* function: 
  ```
  result[n] = F(1,n) + F[2,n] +...F[n,n]   
  
  F[i, n]:  # the number of unique BST, where the number i is the root of BST, and the sequence ranges from 1 to n.
  
  F[i, n] = result[i-1] * result[n-i]  1<= i <= n
  
  result[n] = result[0]*result[n-1] + result[1]*result[n-2]+..+result[n-1]*result[0]
  ```
* result: result[n]

-----

####3. Two Sequences DP 40%
* state: ```dp[i][j]```代表了第一个sequence的前i个数字/字符配上第二个的sequence的前j个...
* function: ```dp[i][j] =``` 研究第i-1个和第j-1个的匹配关系
* initialize: ```dp[i][0], dp[0][j]```
* answer: ```dp[len(s1)][len(s2)]```
* 复杂度一般为O(m*n)

######[Longest Common Subsequence](./Experience/Longest_Common_Subsequence.py) [(Not in Leetcode)](http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/)
* state: ```dp[i][j]```表示前i个字符配上前j个字符的LCS的长度
* function:  

  ```python
  dp[i][j] = dp[i-1][j-1] + 1           # if a[i-1] == b[j-1]
           = max(dp[i][j-1],dp[i-1][j]) # if a[i-1] != b[j-1]
  ```
* initialize: ```dp[i][0] = 0, dp[0][j] = 0```
* answer: ```dp[M][N]```

######[Longest Common Substring](./Experience/Longest_Common_Substring.py) [(Not in Leetcode)](http://www.geeksforgeeks.org/longest-common-substring/)
* state: ```dp[i][j]```表示前i个字符配上前j个字符的LCS的长度(一定以第i个和第j个结尾的LCS)
* function:  

  ```python
  dp[i][j] = dp[i-1][j-1] + 1 # if a[i-1] == b[j-1]
           = 0                # if a[i-1] != b[j-1]
  ```
* initialize: ```dp[i][j] = 0, dp[0][j] = 0```
* answer: ```max(dp[0...len(a)][0...len(b)])```

######[Longest Common Prefix](https://github.com/UmassJin/Leetcode/blob/master/Array/Longest_Common_Prefix.py)

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

  这道题可以作为两个字符串DP的典型：
  两个字符串：
  先创建二维数组存放答案，如解法数量。注意二维数组的长度要比原来字符串长度+1，因为要考虑第一个位置是空字符串。
  然后考虑dp[i][j]和dp[i-1][j],dp[i][j-1],dp[i-1][j-1]的关系，如何通过判断S.charAt(i)和T.charAt(j)的是否相等来看看如果移除了最后两个字符，能不能把问题转化到子问题。
  最后问题的答案就是dp[S.length()][T.length()]
  还有就是要注意通过填表来找规律

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

######[Regular Expression Matching](./Array/Regular_Expression_Matching.py)
* state: ```dp[i][j]``` 表示```s[0:i-1]```是否能和 ```p[0:j-1]```匹配
* initialize:  ``` dp[0][0] = True ```
* function: 
```python
dp[i][j] =  dp[i-1][j-1] and s[i-1] == p[j-1]  if p[j-1] != '.' and p[j-1] != '*'
            dp[i-1][j-1]                  if p[j-1] == '.'
            dp[i][j-1]  or dp[i][j-2]     if p[j-1] == '*' 匹配0个或者1个元素 
            匹配0个元素，即消去p[j-2]，此时p[0: j-1] = p[0: j-3]
            匹配1个元素，此时p[0: j-1] = p[0: j-2]
            dp[i-1][j] and (s[i-1] = p [j-2] or p[j-2] == '.')
```
* answer: ```dp[M][N]```
* Reference: [Leetcode artical](http://articles.leetcode.com/2011/09/regular-expression-matching.html)
*            [Reference 1 ] (http://bangbingsyb.blogspot.com/2014/11/leetcode-regular-expression-matching.html)
*            [Reference 2 ] (http://www.aichengxu.com/view/14420)

Compare with [Wildcard Matching](./Array/Wildcard_Matching.py)
* There is dp solution for Wildcard Matching, need to recall!!

######Wildcard Matching 
* '?' Matches any single character.
* '*' Matches any sequence of characters (including the empty sequence).
* isMatch("ab", "?*") → true
* isMatch("aab", "c*a*b") → false
* Example  ```isMatch("abebdcd","?b*cd")``` → True
*    a-->'?'; b-->b; '*'-->'ebd';'cd'-->'cd'
* Example ```isMatch("abebdcbd","?b*cd")``` → False
*    a-->'?';b--:>b; 'ebd'-->'*';'c'-->'c';'b'-->'d' --> False
* Example ```isMatch('acbb','*b')``` -> True
* Example ```isMatch('acbcb','*b')``` -> True
* Example ```isMatch("abedsfsf","a*ff")``` -> False
* Example ```isMatch("abf","ab*f")``` -> True
* 对于wildcard matching 来说，```'*'```可以match到空的或者任意长度的string，所以```"abedsfsf","a*f"```就为True，
* 但是```isMatch("abedsfsf","a*ff")``` 为False， 因为fsf 与ff 不match

######Regular Expression Matching 
* '.' Matches any single character.
* '*' Matches zero or more of the preceding element.

* ```isMatch("ab", ".*")``` → true
* '.*' could match any strng, since * means zero or more of the preceding element, so here maybe 0 or more '.'
* ```isMatch("aab", "c*a*b")``` → true 
* here is true since c maybe have 0 times 
* Example ```isMatch('acbb','*b')``` -> False
* Example ```isMatch('acbcb','*b')``` -> False
* Example ```isMatch('bb', '*')``` -> False
* 注意regular expression 中，```*``` 表示match zero或者more of the preceding element, 所以对于```'acbb','*b', * ```match 为空，result is false, 而对于wildcard matching, ```*```match 空或者任意长度string, 不一定是preceding，所以为true 

-----

####4. Interval DP
* state: ```dp[i][j]``` 代表从i到j这一段区间...
* function: ```dp[i][j] = max/min/sum(dp[i][k], dp[k+1][j])```
* initialize: ```dp[i][i] = ?```
* answer: ```dp[1][n]```

######[Merge Stone 石子归并](http://wikioi.com/problem/1048/)

######[Coin Game](Experience/Coin_game.md)
* state: dp[i][j] the maximum value user can collect from ith coin to jth coin
* function: dp[i][j] = Vi + min( dp[i+2][j], dp[i+1][j-1]) 
*                   = Vj + min( dp[i+1][j-1], dp[i][j-2])
* base: if i == j: dp[i][j] = Vi
* base: if j == i + 1: dp[i][j] = max(Vi, Vj)
* Result: dp[0][n-1]

######[Minimum insertions to form a palindrome](Experience/Min_Insert_Palin.md)
* state: dp[i][j] meanings the min number for the string[i:j]
* initialize: 
* function: dp[i][j] = dp[i-1][j+1] if string[i] == string[j]
*                    = min(dp[i][j-1], dp[i+1][j])+1 else
* result: dp[0][length-1]


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

##DFS Backtracking 
主要想法是先搜索到不能再底层然后再往上走

#### Reference
* [全面解析回溯法](http://www.cnblogs.com/wuyuegb2312/p/3273337.html)

#####复杂度问题
* 组合的话就是O(n^2)
* 排列的话就是(n!)

#####[Palindrome Partitioning](./Array/Palindrome_Partitioning.py)
* Add the recursion function, palindrome_helper function 
* From the first letter, go through each substr, check whehter this is the palindrome and whether
  the rest part of string is palindrome 
* For loop we go through the input string should from [1 : length+1]
* when pass the string to the bottom recursion, should pass strlist + [rest_string]

#####[Letter Combinations of a Phone Number](./Array/Letter_Combinations_of_a_Phone_Number.py)
* 注意容易犯的错误，对于每一个digit 不需要for loop！例如'23', 否则会出现 3 3 组合的情况！
* Use the recursion and iteration two methods 
* Iteration: the initialization should use [''] rather than []
 
#####[Subset I and II](./Array/subset1&2.py)
* Need to first sort the input array 
* Backtracking Sample: subset_helper(sublist, start, S), start used to record the start index and also the depth
* [Subset BIT 求解方法](http://www.cnblogs.com/yuzhangcmu/p/4211815.html)
* BIT 解法在于，对于给定的序列, ```example S = [1,2,3]```, the length of the combination is ```2 ^ len(S)```
* ```{} <--> 000; {1} <--> 001; {2} <--> 010;; {1,2} <--> 011``` and so on 

#####[Combinations](.//Array/Combinations.py)

#####[N-Queens](./Array/N_Queens.py)
* 注意要check对角线！！

#####[N-QueensII](./Array/N_QueensII.py)
* 注意要用self.result to update the value !!


#####[Sudoku Solver](./Array/sudoku_solver.py)
* 几个容易犯错的地方
* 1. 思路是，一次从```board
* [0][0]```开始走起，如果发现```'.'```则一次填入1到9之间数字的任意一个
* 2. 然后进行check在同一行或者同一列中是否有一样的
* 3. 注意在check 的时候，不能将```board[i][cal] == board[i][j]```直接check，因为可能是自己等于自己的情况！
* 4. 注意同一个九宫格的check，```board[(i/3)*3+p][(j/3)*3+q] == tmp```,p和q分别从0遍历到2
* 5. 注意如果返回false，要将```board[i][j]```重新设置为```'.'```
* 6. 在最后注意所有条件都满足时，返回True 

-----

##Data Structure
##### Stack 
#####[Longest Valid Parentheses](./Array/Longest_Valid_Parentheses.py)
* Use two methods to solve the problem
* First, use the Stack to record the "(", maintain the variable "last", record the last unusage ')'
* Second, iterarate the string for two times, from start to end and from end to start 

#####[Min Stack](https://github.com/UmassJin/Leetcode/blob/master/Array/Min_Stack.py)
* 用两个list来实现，list1里面存所有元素，list2里面存最小元素
* 注意，当x <= list2[-1], push 到list2里面，不是 '<', test case: push0,push1,push0,getmin,pop,getmin
* 最开始的想法是，用list1存所有元素，并且按照由大到小，最小的元素永远在top，用list2实现这个功能，但是这个
* 方法会超时! 每次push x的时候，都要把大的元素依次拿出，再放入，耗费时间.

##### Hashtable 
#####[Anagrams](./Array/Anagrams.py)
* Save the SORTED string as the key in the dictionary 
* Save each string as the value (put into a list), then push them into the list 
* Use the ''.join and list.extend instead of list.append 

##### Use the Hashtable and two pointers to solve the following problems 
#####[Minimum Window Substring](./Array/Minimum_Window_Substring.py)
* 1. Use two hashtable, one is save the char anc count in the T, and one used for find when search in S
* 2. Use two pointer, first move the right pointer, when we find all the chars in T in the S, stop
* 3. Then move the left pointer, skip the useless char and duplicate chars 
* 4. Then keep moving the right pointer, till the end 

#####[Substring with Concatenation of All Words ] (./Array/Substring_with_Concatenation_of_All_Words.py)

#####[Longest Substring with At Most Two Distinct Characters](./Array/Longest_Substring_with_At_Most_Two_Distinct_Characters.py)
* Use the hashtable to save the char and count number
* keep the count to check the distinguish chars
* Note: we use the while not the if to check count > 2


#####[Longest Substring Without Repeating Characters ](./Array/Longest_Substring_Without_Repeating_Characters.py)
* Use the hashtable to record the index of the character
* Update the start pointer when hit the repeat character


#####[Longest Palindromic Substring](./Array/Longest_Palindromic_Substring.py)(需要回看！！)

#####[Rotate Array](./Array/Rotate_Array.py)
* Note: nums[:] not the nums!!

##### Array
######[Search in rotated array I && II](Array/search%20in%20rotated%20array1&2.py) [注意算法实现的不同点！]
* Note: 注意边界条件：while left <= right:   ====> left need to <= right, test case [1], 1
* after we check if target == A[mid] or not, we need to check if A[mid] >= left or A[mid] <= right, not A[mid] > target, since we need to find where is the roated
* Check A[mid] >= left: test case: [3,1], 0 ; [1], 0 
* target >= A[left], target <= A[right]
* If there is the duplicate allowed in the array, then A[mid] only compare with A[left]
* test case:  
  ```
  A[mid] < A[right]: [3,1,1], 3; 
  A[mid] <= A[right]:[1,1,3,1], 3
  A[mid] <= A[left]: [3,1], 1
  ```

* I: O(logn), II: O(n)
 
######[Find Minimum in Rotated Sorted Array](Array/find%20min%20in%20rotated%20array1%262.py)
* I: O(logn)
* II: O(n)
  1. 注意在每次left或者right移动的时候，都需要check minval和另一边的最小值
  2. 在每次循环之后，都要check minval和num[mid]的最小值！
 
#####[Find kth max element in unsorted array](./Algorithm/Max_Heap_Implement.md)

#####[Longset Consecutive Sequence](./Array/Longset_Consecutive_Sequence.py)
* Whenever a new element n is inserted into the map, do two things:
* See if n - 1 and n + 1 exist in the map, and if so, it means there is an existing sequence next to n. Variables left and right will be the length of those two sequences, while 0 means there is no sequence and n will be the boundary point later. Store (left + right + 1) as the associated value to key n into the map.
* Use left and right to locate the other end of the sequences to the left and right of n respectively, and replace the value with the new length.
* 注意这里不是update左右邻居的值，而是update左右临界的数值

#####[Maximum Gap](https://github.com/UmassJin/Leetcode/blob/master/Array/Maximum_Gap.py)
* 注意题目详细解释和注释


#####[Find Peak Element](https://github.com/UmassJin/Leetcode/blob/master/Array/Find_Peak_Element.py)
* 注意recursion的比较条件

-----

##Math 
#####[Palindrome Number](./Array/Palindrome_Number.py)
* Since the requirement is DO NOT use the extra space, should not transfer the number to string 
* Use the math method to compare the first number and last number
* Then in the next step, reduce this two numbers
* Note: after we compare the first digit and last digit in the input number, we should first run
* x = x % div, then x / 10, can not do the opposite, test case: 11

#####[Add Binary](./Array/Add_Binary.py)
* 解题思路:
* Go through the number a and b from the last digit 
* Have two variables: one is bit: sum %2, one is carry sum/2
* Insert the bit into result, check the last carry value 

#####[Plus One](./Array/Plus_One.py)
* Note the details: check carry, and if last carry == 1 or not 

#####[Print Five](./Experience/Print_Five.md)[Note in Leetcode]
#####[Rotated Mirror Number](./Experience/Rotated_Mirror_Number.md)[Not in Leetcode]

Compare the above questions:
* Both use the recursion to resolve the problem
* For the "Print Five", we will recursivly add the number and check if it larger than input number or length is longer, then check if there is number '5' exist in the number
* For the "Mirror Number", we will recursivly add the number in the front and the end of input, and also check if this number larger than input or length is longer, need to handle the single number "1,2,3,4..."

#####[Reverse Integer](https://github.com/UmassJin/Leetcode/blob/master/Array/Reverse_Integer.py)
* 注意，在处理interger的时候，必须考虑到两点:
* 1) 正负号的问题，在处理integer 的时候，我们需要去掉符号
* 2) max integer 和 min integer 的问题，需要考虑到最大最小数值

#####[Divide Two Integers](https://github.com/UmassJin/Leetcode/blob/master/Array/Divide_Two_Integers.py)
* 注意题目的思路，用<<1 和 >>1
* 这里的 max int and min int range有点奇怪，需要check


#####[Pow(x,n)](https://github.com/UmassJin/Leetcode/blob/master/Array/pow(x%2Cy).py)
* Solution 1: 二分法
* 优点是代码简洁，缺点是没有考虑到overflow的情况

* Solution 2: bit manipulation 
* 就是把n看成是以2为基的位构成的，因此每一位是对应x的一个幂数，然后迭代直到n到最高位。
* 比如说第一位对应x，第二位对应x*x,第三位对应x^4,...,第k位对应x^(2^(k-1))
* 这里做很多边界的检查
* 1) n < 0 or n > 0, if n < 0, whether 1/x will overflow 
* 2) whether x < 0 or x > 0, if n 为奇数，并且x < 0, result < 0
* Reference: http://blog.csdn.net/linhuanmars/article/details/20092829

#####[Sqrt(x,n)](https://github.com/UmassJin/Leetcode/blob/master/Array/Sqrt(x).py)
* 解题思路：实现开平方函数。这里要注意的一点是返回的时一个整数。通过这一点我们可以看出，
* 很有可能是使用二分查找来解决问题的。这里要注意折半查找起点和终点的设置。起点i=1；终点j=x/2+1；
* 因为在(x/2+1)^2 > x，所以我们将折半查找的终点设为x/2+1。

##### 数值计算总结
* 一般来说数值计算的题目可以用两种方法来解，一种是以2为基进行位处理的方法，另一种是用二分法。
* 需要考虑的两个主要方面，1. positive number or negative number 
* 2. overflow: whether larger than the max_Int or smaller than the min_Int 
* 3. ```max_Int: 1 << 32 -1, min_Int -1 << 32```

-----

##Two Pointer
#####[Valid Palindrome](./Array/Valid_Palindrome.py)
* Pyhon: isalnum()
* lower()
* no need to check len at the beginning 
* condition: left < right, not the left <= right, since if left == right, which means they point to the same number, return True

#####[Trapping Rain Water](./Array/Trapping_Rain_Water.py)
Solution1
* Idea: go through the array from left to the right, find the maximum left value
* And then go through the array from the right to the left, find the maximum right value
* for the each value A[i], the max value could contain should be min(left_max, right_max) - A[i]

Solution2
* Always maintain two pointers, leftmax and rightmax
* compare through beginning and end of the array, update the leftmax and rightmax
* if leftmax < rightmax: leftmax-A[i], left+=1 update result 
* else: rightmax-A[i], right-= 1, update result,

#####[Container With Most Water](./Array/Container_With_Most_Water.py)
* Check from the beginning and end, find the minimum (left, right)*(right-left), udpate max
* if height[left] < height[right]: update left
* else: update right 

#####[Search Insert Position](./Array/Search_Insert_Position.py)
* Note: the while loop condition !
* Last the return value is start !

#####[Search for a Range](./Array/Search_for_a_range.py)
#####[Remove Element](./Array/Remove_Element.py)

## Matrix Graph
#####[Set Matrix Zeroes](./Array/Set_Matrix_Zeroes.py)
    1. 最优化解的方案精华在于：第一遍扫描从row = 0, cal = 1开始，如果[row][0]==0, 标记first_cal = 0
    2. 第二遍从底层到高层扫描，if matrix[row][0] or matrix[0][cal] == 0, set as 0, 注意cal 从lengthcal 到 1
    3. 最后判断first_cal 是否为0，设置第一行所有元素为0
    
#####[Number of Islands](./Array/Number_of_Islands.py)

#####[Spiral Matrix](./Array/Spiral%20Matrix1%262.py)
    1. 题目的难点在于，在每次改动matrix之后，matrix的长度和每行的长度都会变化
    2. 不能用简单的check 还有pop() 来做，因为每一次pop之后长度又变化了
    3. 注意：list = [[3]] --> pop() 之后为[[]]，此时list的长度为1!!
    4. 第一次和第三次加入result的时候需要将整个matrix[i] pop出来，不然会出错！

#####[Search in 2D matrix](./Array/Search_in_2D_matrix.py)
    1. ```m = len(matrix); n = len(matrix[0])```
    2. ```matrix[x][y] ==> a [x*n + y]```
    3. ```a[x] ==> matrix[x/n][x%n] ```
    
-----

###String 
#####[Implement strStr()](./Array/Implement_strStr().py)
* Note: [KMP algorithm](http://blog.csdn.net/v_july_v/article/details/7041827)

#####[String to Integer (atoi)] (./Array/String_to_Integer.py)
* 思路: 注意去除前后空格，注意第一个字符是sign, 注意最大最小值的比较 
* Coding Note:
* 1）str.strip()
* 2）imin, imax = (-1<<31)/2, (1<<31)/2-1, use this method to get the max/mix value
* 3) Learn to use enumerate() function 
* 4) 容易出错的地方: 
*    a) 在check sign为"-"的时候，也要注意check "+"
*    b) 在check max_int, min_int的时候，注意用sign*result 

#####[Wildcard Matching] (./Array/Wildcard_Matching.py)
Reference: [思路解析] (http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html)
* Definiton of '?' and '*', '?' could match any single char, '*' match any sequqnce of chars 
* Example isMatch("abebdcd","?b*cd") → True
    a-->'?'; b-->b; '*'-->'ebd';'cd'-->'cd'
* Example isMatch("abebdcbd","?b*cd") → False
    a-->'?';b--:>b; 'ebd'-->'*';'c'-->'c';'b'-->'d' --> False
*  We need the variable 'ss', since for the example isMatch("hi","*?")

#####[Compare Version Numbers] (./Array/Compare_Version_Numbers.py)
* Use str.split('.')
* Use Build-in function [all()](https://docs.python.org/2/library/functions.html#all)
* 思路：先把version split based on '.'，倘若首个数字可以比较出大小，则返回1 或者 －1，否则，继续比较下个字母，如果接下来的字母都为0，则返回0，否则返回1 或者 －1
* 注意最后判断长度如果相等且数字相等，返回0

#####[Count and Say] (./Array/Count_and_Say.py)
* 思路: use the helper function to get the new result string from the old one
* Go through the string one time and use the curr to record the current character and amount value 
* [Prove the count should less than 10] (https://leetcode.com/discuss/6762/how-to-proof-the-count-is-always-less-than-10)

#####[Simplify Path] (./Array/Simplify_Path.py)
* Use a stack to store the path 
* Initialization is: stack = ['/'], used for the example '/..'
* first split the input string based on the '/'
* If input char is '.' or '/' or '', continue, if '..', pop the value in stack
* Check the '/' at last if len(stack)>1, delete the last '/'

#####[Restore IP Addresses] (./Array/Restore_IP_Address.py)
* Use the DFS
* 基本思路，将i从1到4遍历，for example: '255255312'，则依次取2, 25, 255...必须每次check i< len(s)
* 例如 '1111', 最后取 111, 1， 当i再增大时，已经超过s的长度！
* corner case: ip should not be 001, 000, should consider the "010010"-->'0.1.0.010' case
* ip number should be in [0,255]

#####[Reverse Words in a StringII](./Array/Reverse_Words_in_a_StringII.py)
* 1) enumerate usage
* 2) zip usage 
* 3) reverse the whole string and then reverse each word 

#####[Roman to Integer] (./Array/Roman_to_Integer.py)
* 1)  According to the rules from wiki:
     A number written in Arabic numerals can be broken into digits. For example, 1903 is composed of 1 (one thousand), 
     9 (nine hundreds), 0 (zero tens), and 3 (three units). To write the Roman numeral, each of the non-zero digits should 
     be treated separately. In the above example, 1,000 = M, 900 = CM, and 3 = III. Therefore, 1903 = MCMIII.[4]
* 2) The symbols "I", "X", "C", and "M" can be repeated three times in succession, but no more. (They may appear more than          three times if they appear non-sequentially, such as XXXIX.) "D", "L", and "V" can never be repeated.[5][6]
* 3) "I" can be subtracted from "V" and "X" only. "X" can be subtracted from "L" and "C" only. "C" can be subtracted from "D"       and "M" only. "V", "L", and "D" can never be subtracted[6]
     'IV' --> 4; 'IX' --> 9; 'XI' --> 11
* 4) [Roman to Integer table] (http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm)
* 5) Only one small-value symbol may be subtracted from any large-value symbol.[7]

#####[Text_Justification] (./Array/Text_Justification.py)
* Notes:
* 1. 很好的思路，use cur_len + len(word) + len(res) 去判断
* 2. extra_space 去除了每个单词之间必须有的空格
     each_extra 加上了每个单词之间必须有的空格
     rest_spaces 除了每个单词之间必须有的空格和多余的空格，还剩下多少空格需要填补
* 3. 注意思想，如何加上多余的空格
* 4. after one loop, the res need to clean
* 5. Add the last word, for example here is "example", could not add into the first line,
     add into the next line 
* 6. 最后是一定会append多余的一行的,没必要再check了, 直接append, 但是这里需要用
     ' '.join, not the ''.join
* 7. 需要check长度为1，因为在下面计算中len(res)-1

#####[Scramble String] (./Array/Scramble_String.py)
* Condition: 
* 1) length_s1 != length_s2
* 2) s1 == s2, s1与s2完全相等
* 3) sorted(s1) 与 sorted(s2)是不是相等
* 4) 比较s1[:i] s2[:i] and s1[i:],s2[i:]
# 5) 比较s1[:i], s2[length_s2-i:] and s1[i:],s2[length_s2:-i]


-----

###[Tree](./Array/Tree.py)
* The resolution for each question have two methods: recursion and iteration 
* [x] Binary Tree Inorder Traversal
* [x] Binary Tree Preorder Traversal
* [x] Binary Tree Postorder Traversal
* [x] Binary Tree Level Order Traversal
* [x] Binary Tree Level Order Traversal II
* [x] Binary Tree Zigzag Level Order Traversal

_____

* [x] Construct Binary Tree from Preorder and Inorder Traversal
* [x] Construct Binary Tree from Inorder and Postorder Traversal

-----

* [x] Same Tree
* [x] Balanced Binary Tree
* [x] Symmetric Tree
* [x] Maximum Depth of Binary Tree
* [x] Minimum Depth of Binary Tree

####Binary Search Tree
* [x] Convert Sorted Array to Binary Search Tree
* [x] Unique Binary Search Trees
* [x] Unique Binary Search Trees II
* [x] Validate Binary Search Tree
* [x] Recover Binary Search Tree
* [x] Binary Search Tree Iterator 
* [x] [Search a range in BST](./Experience/Search_A_Range_in_BST.md)

####类Tree(以tree作为Data Structure的题目)
* [x] Path Sum
* [x] Path Sum II
* [x] Populating Next Right Pointers in Each Node
* [x] Populating Next Right Pointers in Each Node II
* [x] Sum Root to Leaf Numbers
* [x] Flatten Binary Tree to Linked List
* [x] [Convert BST to the (Circal) Doubled Linked List](./Array/Convert_BST_to_DDL.py) （Important!回看！）
* [x] Binary Tree Right Side View
* [x] Convert Sorted List to Binary Search Tree 
* [x] Binary Tree Maximum Path Sum  （follow question: print out all the path! think about it ! the result may include the root node or not ! ! ）
* [ ] Binary Tree Upside Down 

#### Basic Tree question not in Leetcode
* [x] Find the leaf nodes number in the tree
* [x] Find the nodes number in k level 
* [x] [Find the common ancestry in Binary Tree I && II ](./Experience/Lowest_Common_Ancestor_in_Binary_Tree.md) (Three different questions!) 
* [x] [Find the common ancestry in BST ](./Experience/Lowest_Common_Ancestor_in_Binary_Tree.md) (Three different questions!) 

#### Algorithm related to Tree/Graph
* Red-Black Tree 
* Reference: [G4G] (http://www.geeksforgeeks.org/red-black-tree-set-2-insert/), [透彻了解红黑树](http://blog.csdn.net/v_JULY_v/article/details/6105630)
* Tries
* Suffix Tree
* Optimal Binary Seach Tree
* Morris Traversal Algorithm for Tree 
* Minimum Spanning Tree
* [Clone Graph] (Array/Clone_Graph.py)

## Linked List
#####[Remove Duplicates from Sorted List](./Array/Remove%20Duplicates%20from%20Sorted%20List.py) [Keep the Dup node]
#####[Remove Duplicates from Sorted List II](./Array/Remove%20Duplicates%20from%20Sorted%20ListII.py) [Remove the Dup node]
  1. Use two pointers, create a dummy node which point to the header 
  2. Use the while loop to find the last duplicate node, then make the ```p.next = temp.next```
  3. Otherwise, ```p = p.next, temp = temp.next ```
#####[Remove duplicates from an unsorted linked list](Experience/Remove_duplicates_from_unsorted_linked_list.md)
#####[Remove duplicates from an unsorted linked list with given value](Experience/Remove_duplicates_from_unsorted_linked_list_given_value.md) [not use dummyheader]

#####[Partition List](https://github.com/UmassJin/Leetcode/blob/master/Array/Partition_List.py)
* 注意：不能用最初会想到的指针的方法做！
* Test Case: [1],2; [2,1],2; [1,3,2], 3

#####[Reverse Linked List II](https://github.com/UmassJin/Leetcode/blob/master/Array/Reverse_Linked_ListII.py)
* 注意指针的用法！

#### Can Binary Search be used for linked lists ? [Skip Lists](http://www.geeksforgeeks.org/skip-list/)



## Bit Manupulation
##### [Gray Code](./Array/Gray_Code.py)

##### [Reverse Bits](https://github.com/UmassJin/Leetcode/blob/master/Array/Reverse_Bits.py)

## Greedy

### [两次扫描](http://blog.csdn.net/linhuanmars/article/details/20888505)
* 两次扫描算是一种常见的技巧，从两边各扫描一次得到我们需要维护的变量，通常适用于当前元素需要两边元素来决定的问题，
* Trapping Rain Water还可以用从两边到中间的方法
* 这种两边往中间夹逼的方法也挺常用的，它的核心思路就是向中间夹逼时能确定接下来移动一侧窗口不可能使结果变得更好，所以每次能确定移动一侧指针，直到相遇为止。这种方法带有一些贪心，用到的有Two Sum，Container With Most Water，都是不错的题目。

##### [Trapping Rain Water](https://github.com/UmassJin/Leetcode/blob/master/Array/Trapping_Rain_Water.py)
* 基本思路就是维护一个长度为n的数组，进行两次扫描，一次从左往右，一次从右往左。第一次扫描的时候维护对于每一个bar左边最大的高度是多少，存入数组对应元素中，第二次扫描的时候维护右边最大的高度，并且比较将左边和右边小的最大高度（我们成为瓶颈）存入数组对应元素中。这样两遍扫描之后就可以得到每一个bar能承受的最大水量，从而累加得出结果。这个方法只需要两次扫描，所以时间复杂度是O(2*n)=O(n)。空间上需要一个长度为n的数组，复杂度是O(n)。
* 另一种方法，相对不是那么好理解，但是只需要一次扫描就能完成。基本思路是这样的，用两个指针从两端往中间扫，在当前窗口下，如果哪一侧的高度是小的，那么从这里开始继续扫，如果比它还小的，肯定装水的瓶颈就是它了，可以把装水量加入结果，如果遇到比它大的，立即停止，重新判断左右窗口的大小情况，重复上面的步骤。这里能作为停下来判断的窗口，说明肯定比前面的大了，所以目前肯定装不了水（不然前面会直接扫过去）。这样当左右窗口相遇时，就可以结束了，因为每个元素的装水量都已经记录过了。

##### [Candy](https://github.com/UmassJin/Leetcode/blob/master/Array/Candy.py)
* 基本思路就是进行两次扫描，一次从左往右，一次从右往左。第一次扫描的时候维护对于每一个小孩左边所需要最少的糖果数量，存入数组对应元素中，第二次扫描的时候维护右边所需的最少糖果数，并且比较将左边和右边大的糖果数量存入结果数组对应元素中。这样两遍扫描之后就可以得到每一个所需要的最最少糖果量，从而累加得出结果。方法只需要两次扫描，所以时间复杂度是O(2*n)=O(n)。空间上需要一个长度为n的数组，复杂度是O(n)。

## Bucket 
##### [Contains Duplicate III](https://github.com/UmassJin/Leetcode/blob/master/Array/Contains%20Duplicate%20III.py)
* 注意对bucket的理解
* 注意不能单纯的用 if m 判断，因为m == None 的时候，return False, if m == 0, also return False 

## Rectangle Serious 
* [Largest Rectangle in Histogram](./Array/Largest-Rectangle-in-Histogram.py)
  1. Use the stack to record the height of each index i, if height[i] > stack[-1], stack.append(height[i])
  2. If height[i] <= stack[-1], 需要计算以stack[-1]为高度的最大的面积

* [Maximal Rectangle](./Array/Maximal_Rectangle.py)
  1. Analysis: maintain a row length of Integer array H recorded its height of '1's, 
     and scan and update row by row to find out the largest rectangle of each row.
  2. [The other DP solution](https://leetcode.com/discuss/20240/share-my-dp-solution) !!! [回看！]

## Sum Serious
* [2sum](./Array/2sum.py) O(nlogn)
* [3sum](./Array/3Sum.py) O(nlogn + n^2)
* [3sum closet](./Array/3sum_closet.py) 
* [4sum](./Array/4sum.py) 
  1. The better way is O(n^2) complexity, first we calculate the two sum and save it into the directory
  2. Then we search the array one more time, to check if the target - num[p] - num[q] in the directory
  3. Note: Last check! q < queue[0], which will delete the wrong and duplicate answer !!
* [Conclusion](http://tech-wonderland.net/blog/summary-of-ksum-problems.html):
  1. 结果中需要去掉重复出现的set，例如[[-1,-1,0,1],0] ==> [-1,0,1]
  2. 对于3sum来说，i从0开始，j从i+1开始，k从length-1开始，在移动的时候，可以check是否相等，避免重复
      ```python
      if num[i] > num[i-1]
      while j < k and num[j] == num[j-1]: j += 1
      while j < k and num[k] == num[k+1]: k -= 1
      ```
  3. [ksum](./Array/ksum.py):     
* [Combination Sum](./Array/combination_sum1.py) 
  1. Use the backtrack algorithm, 先将array sort一下
  2. O(n^2)
  3. 注意边界条件的分析
* [Combination Sum2](./Array/combination_sum2.py)
  1. 注意check duplicate answers ! check case [1,1], target = 1 !

## Permutation Serious 
##### [PermutationsI](./Array/PermutationsI.py)

##### [PermutationsII](./Array/PermutationsII.py)
* 注意：用一个previous去检测之前是否已经用过这个数字

##### [Permutation Sequence](./Array/Permutation_sequence.py)
* 注意这里巧妙的方法
* 或者我们也可以用recursion做，先初始化[1,2,3...n],再依次找到每一个permutation

## Array Interval Serious
* [Insert Interval](./Array/Insert_Interval.py)
  1. Search from the start of the array, find the first interval in the input which end > newinterval.start 
  2. then compare the interval.start with the newinterval.end ! note, not compare the interval.end with newinterval.end
     since maybe add the duplicate interval
  3. the newend need to initialize as the newinterval.end 
  4. at last, if i < length, need to add the left interval in the input intervals 
* [Merge Interval](./Array/Merge_Intervals.py)

## Rotate Serious
######[Search in rotated array I && II](Array/search%20in%20rotated%20array1&2.py) [注意算法实现的不同点！]
* Note: 注意边界条件：while left <= right:   ====> left need to <= right, test case [1], 1
* after we check if target == A[mid] or not, we need to check if A[mid] >= left or A[mid] <= right, not A[mid] > target, since we need to find where is the roated
* Check A[mid] >= left: test case: [3,1], 0 ; [1], 0 
* target >= A[left], target <= A[right]
* If there is the duplicate allowed in the array, then A[mid] only compare with A[left]
* test case:  
  ```
  A[mid] < A[right]: [3,1,1], 3; 
  A[mid] <= A[right]:[1,1,3,1], 3
  A[mid] <= A[left]: [3,1], 1
  ```

* I: O(logn), II: O(n)
 
######[Find Minimum in Rotated Sorted Array](Array/find%20min%20in%20rotated%20array1%262.py)
* I: O(logn)
* II: O(n)
  1. 注意在每次left或者right移动的时候，都需要check minval和另一边的最小值
  2. 在每次循环之后，都要check minval和num[mid]的最小值！
 
######[Rotate Image](./Array/Rotate_Image.py)
* 先将matrix沿着对角线颠倒翻转，注意x从0到n-1, y从i+1到n
* 再将每一行reverse过来


## Merge Serious 
######[Merge K Sorted Array](./Experience/Merge_k_sorted_array.md)
######[Merge K sorted linked list](https://github.com/UmassJin/Leetcode/blob/master/Array/Merge_K_Sorted_Lists.py)


## Sudoku Serious
#####[Sudoku Solver](./Array/sudoku_solver.py)
* 几个容易犯错的地方
* 1. 思路是，一次从```board[0][0]```开始走起，如果发现```'.'```则一次填入1到9之间数字的任意一个
* 2. 然后进行check在同一行或者同一列中是否有一样的
* 3. 注意在check 的时候，不能将```board[i][cal] == board[i][j]```直接check，因为可能是自己等于自己的情况！
* 4. 注意同一个九宫格的check，```board[(i/3)*3+p][(j/3)*3+q] == tmp```,p和q分别从0遍历到2
* 5. 注意如果返回false，要将```board[i][j]```重新设置为```'.'```
* 6. 在最后注意所有条件都满足时，返回True 

#####[Valid Sudoku](./Array/Valid_Sudoku.py)
* 1. 注意 在check行还有列的时候，必须用if, elif, if and elif, 不是if, elif, elif, elif


## Parentheses Serious
##### [Generate Parentheses](./Array/Generate_Parentheses.py)
* Use the backtracking algorithm
* First check the '(' amount 
* Then check the ')' amount, Note: here we should use the 'if' not the 'elif' !!
* if '(' amount and ')' amount is equal to 0, patch into the result

##### [Valid_Parentheses](./Array/Valid_Parentheses.py)
* Use the stack to check whether there is valid parentheses
* Note: we need to check the length of the stack in the end ! In case '(' is more than ')'

##### [Longest_Valid_Parentheses](./Array/Longest_Valid_Parentheses.py)

## Duplicate Serious 
##### [Remove duplicate from sorted array](./Array/Remove_duplicate_from_sorted_array.py)

##### [Remove duplicate from sorted arrayII](./Array/Remove_duplicate_from_sorted_arrayII.py)
* Note: we need to update nums[slow] every time ! 

## Stock Serious 
##### [Best Time to Buy and Sell Stock IV](https://github.com/UmassJin/Leetcode/blob/master/Array/Best%20Time%20to%20Buy%20and%20Sell%20Stock%20IV.py)(回看！)
##### [Best Time to Buy and Sell Stock I & II & III](https://github.com/UmassJin/Leetcode/blob/master/Array/Best-Time-to-Buy-and-Sell-Stock1%262%263.py)


## Interview Questions not in Leetcode
| Question | Type |
|:---|:---|
| [coin change](./Experience/coin_change.md) (Good Questions!!) | Dynamic Programming |
| [Word Break] (./Experience/Word_Break.md) | Dynamic Programming |
| [Min Num to Composite Words](./Experience/Min_Num_to_Composite_Words.md) | Dynamic Programming |
| [Consecutive Subarray] (./Experience/Consecutive_Subarray.md) | Two Pointer/KMP |
| [Flattening a Linked List] (./Experience/%20Flattening_a_Linked_List.md) | Linked list |
| [Flatten a Multilevel Linked List] (./Experience/Flatten_a_Multilevel_Linked_List.md) | Linked list |
| [Count_zeros_in_Factorial] (./Experience/Count_zeros_in_Factorial.md) | Math |
| [Print Five](./Experience/Print_Five.md) | Math |
| [Rotated Mirror Number](./Experience/Rotated_Mirror_Number.md) | Math |
| [Absolute Minimum] (./Array/Absolute_minimum.md) | Math | 
| [Time Angle](./Experience/Time_angle.md) | Math | 
| [Delete node in BST] (./Experience/Delete_node_in_BST.md) | Tree | 
| [Search A Range in BST](./Experience/Search_A_Range_in_BST.md) | Tree | 
| [Largest None Close Sum](./Experience/Largest_none_close_sum.md) | Array | 
| [Find K Closest Element to Target](./Experience/Find_K_Closest_Ele_to_Target.md) | Array | 
| [Alternating Positive N Negative](./Array/Alternating_Positive_N_Negative.md) | Array | 
| [Print Matrix](./Experience/Print_Matrix.md) | Array | 
| [Sort by Stack](./Experience/Sort_By_Stack.md) | Array |
| [Find kth max element in unsorted array](./Algorithm/Max_Heap_Implement.md) | Array | 
| [Implete Min Stack](./Experience/Implete_min_stack.md) | Stack |
| [Find_Order_of_Char_in_Sorted_Dict](./Experience/Find_Order_of_Char_in_Sorted_Dict.md)[Good Question!!] | Sort | 

## Python Buildin Function Usage
#### 1. ord('A')
#####[Excel Sheet Column Number](https://github.com/UmassJin/Leetcode/blob/master/Array/Excel%20Sheet%20Column%20Number.py)

#### 2. chr(65) --> 'A'
#####[Excel Sheet Column Title](https://github.com/UmassJin/Leetcode/blob/master/Array/Excel%20Sheet%20Column%20Title.py)

#### 3. divmod(), list.index(), string.replace(), string.rstrip()
#####[Fraction To Recurring Decimal](https://github.com/UmassJin/Leetcode/blob/master/Array/Fraction-to-Recurring-Decimal.py)

#### 4. str.isdigit()
#####[Evaluate Reverse Polish Notation](https://github.com/UmassJin/Leetcode/blob/master/Array/Evaluate_Reverse_Polish_Notation.py)
* 注意: str.isdigit() 不能判断负数

```python
>>> s = '-1'
>>> i = int(s)
>>> i
-1
>>> s.isdigit()
False
>>> 
>>> 
>>> s = '1'
>>> s.isdigit()
True
```

## Design Pattern
* Blocking Queue (回看！)

## Other useful Reference
* [Bash Prompt HOWTO](http://tldp.org/HOWTO/Bash-Prompt-HOWTO/index.html)
* [C faq](http://c-faq.com/)

## 注意编程过程中出现过的失误细节
* 注意变量名称，不要拼写错误
* 注意在two pointer时候,边界条件是left < right, 还是left <= right
* 一些corner case的处理，比如说input为空，只有一个input，[1],0 或者[0],1的情况
* 注意如果用class，不要丢掉self，定义的function后面有冒号，
* 对于数字的处理的时候，首先要判断是否有符号，是否可能为负数，在处理数字的时候同样需要注意
* 对于数字的处理，还需要考虑到max_int 和 min_int, 注意float('inf')和float('-inf')的用法
* 在对string处理的时候，可以提问的点: 是否允许duplicate ? 是否允许order changes ?  是否允许change the original string ?
