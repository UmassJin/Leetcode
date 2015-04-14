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

######[Regular Expression Matching](./Array/Regular_Expression_Matching.py)
* state: ```dp[i][j]``` 表示```s[0:i-1]```是否能和 ```p[0:j-1]```匹配
* initialize:  ``` dp[0][0] = True ```
* function: 
```python
dp[i][j] =  dp[i-1][j-1] and s[i-1][j-1]  if p[j-1] != '.' and p[j-1] != '*'
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
######Wildcard Matching 
* '?' Matches any single character.
* '*' Matches any sequence of characters (including the empty sequence).
* isMatch("ab", "?*") → true
* isMatch("aab", "c*a*b") → false
* Example  ```isMatch("abebdcd","?b*cd")``` → True
*    a-->'?'; b-->b; '*'-->'ebd';'cd'-->'cd'
* Example ```isMatch("abebdcbd","?b*cd")``` → False
*    a-->'?';b--:>b; 'ebd'-->'*';'c'-->'c';'b'-->'d' --> False

######Regular Expression Matching 
* '.' Matches any single character.
* '*' Matches zero or more of the preceding element.

* ```isMatch("ab", ".*")``` → true
* '.*' could match any strng, since * means zero or more of the preceding element, so here maybe 0 or more '.'
* ```isMatch("aab", "c*a*b")``` → true 
* here is true since c maybe have 0 times 


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

#####[Letter Combinations of a Phone Number](./Array/Letter_Combinations_of_a_Phone_Number.py)
* Use the recursion and iteration two methods 
* Iteration: the initialization should use [''] rather than []
 


-----

###Data Structure
##### Stack 
#####[Longest Valid Parentheses](./Array/Longest_Valid_Parentheses.py)
* Use two methods to solve the problem
* First, use the Stack to record the "(", maintain the variable "last", record the last unusage ')'
* Second, iterarate the string for two times, from start to end and from end to start 

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


-----

###Math 
#####[Palindrome Number](./Array/Palindrome_Number.py)
* Since the requirement is DO NOT use the extra space, should not transfer the number to string 
* Use the math method to compare the first number and last number
* Then in the next step, reduce this two numbers


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

-----

###Two Pointer
#####[Valid Palindrome](./Array/Valid_Palindrome.py)
* Pyhon: isalnum()
* lower()
* no need to check len at the beginning 
* condition: left < right, not the left <= right, since if left == right, which means they point to the same number, return True

#####[Trapping Rain Water](./Array/Trapping_Rain_Water.py)
* Idea: go through the array from left to the right, find the maximum left value
* And then go through the array from the right to the left, find the maximum right value
* for the each value A[i], the max value could contain should be min(left_max, right_max) - A[i]

#####[Search Insert Position](./Array/Search_Insert_Position.py)
* Note: the while loop condition !
* Last the return value is start !

#####[Search for a Range](./Array/Search_for_a_range.py)
#####[Remove Element](./Array/Remove_Element.py)

### Matrix/Graph
#####[Set Matrix Zeroes](./Array/Set_Matrix_Zeroes.py)
#####[Number of Islands](./Array/Number_of_Islands.py)

-----

###String 
#####[Implement strStr()](./Array/Implement_strStr().py)
* Note: [KMP algorithm](http://blog.csdn.net/v_july_v/article/details/7041827)

#####[String to Integer (atoi)] (./Array/String_to_Integer.py)
* 思路: 注意去除前后空格，注意第一个字符是sign, 注意最大最小值的比较 
* Coding Note:
* 1）str.strip()
* 2）imin, imax = -1<<31, (1<<31)-1, use this method to get the max/mix value
* 3) Learn to use enumerate() function 

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
* Use Build-in function all() 

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

#####[Restore IP Addresses] (./Array/Restore_IP_Addresses.py)
* Use the DFS
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
* [Remove Duplicates from Sorted List](./Array/Remove%20Duplicates%20from%20Sorted%20List.py) [Keep the Dup node]
* [Remove Duplicates from Sorted List II](./Array/Remove%20Duplicates%20from%20Sorted%20ListII.py) [Remove the Dup node]
* Use two pointers, create a dummy node which point to the header 
* Use the while loop to find the last duplicate node, then make the ```p.next = temp.next```
* Otherwise, ```p = p.next, temp = temp.next ```
* [Remove duplicates from an unsorted linked list](Experience/Remove_duplicates_from_unsorted_linked_list.md)
* [Remove duplicates from an unsorted linked list with given value](Experience/Remove_duplicates_from_unsorted_linked_list_given_value.md) [not use dummyheader]

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
| [Implete Min Stack](./Experience/Implete_min_stack.md) | Stack |

## Design Pattern
* Blocking Queue (回看！)

## Other useful Reference
* [Bash Prompt HOWTO](http://tldp.org/HOWTO/Bash-Prompt-HOWTO/index.html)
* [C faq](http://c-faq.com/)
