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

#####[Minimum Path Sum](./Array/Minimum_Path_Sum.py)
* state: ```dp[x][y]```表示从起点走到x,y的minimum path sum
* function: ```dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + grid[x][y]```
* initialize: ```dp[0][0] = grid[0][0], dp[x][0] = dp[x-1][0] + grid[x][0], dp[0][y] = dp[0][y-1] + grid[0][y]```
* answer: ```dp[M-1][N-1]``
