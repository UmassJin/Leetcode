Problem statement: Consider a row of n coins of values v1 . . . vn, where n is even. We play a game against an opponent by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first.

Note: The opponent is as clever as the user.

Let us understand the problem with few examples:

    1. 5, 3, 7, 10 : The user collects maximum value as 15(10 + 5)

    2. 8, 15, 3, 7 : The user collects maximum value as 22(7 + 15)


* [G4G](http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/)


```python
# state: dp[i][j] the maximum value user can collect from ith coin to jth coin
# function: dp[i][j] = Vi + min( dp[i+2][j], dp[i+1][j-1]) 
#                   = Vj + min( dp[i+1][j-1], dp[i][j-2])
# base: if i == j: dp[i][j] = Vi
# base: if j == i + 1: dp[i][j] = max(Vi, Vj)
# Result: dp[0][n-1]

def game_dp(array):
    if not array: return 0
    length = len(array)
    
    dp = [[0 for j in xrange(length)]for i in xrange(length)]
    for gap in xrange(length):
        i = 0; j = gap; 
        while j < length:
            x =0; y = 0; z = 0
            if i + 2 <= j:
                x = dp[i+2][j]
            if i + 1 <= j-1:
                y = dp[i+1][j-1]
            if i <= j - 2:
                z = dp[i][j-2]
            dp[i][j] = max(array[i] + min(x,y), array[j] + min(y,z))
            print "dp[%d][%d]: %d" %(i,j,dp[i][j])
            i += 1; j += 1
    return dp[0][length-1]

array = [8,15,3,7]
print game_dp(array)

  0  1  2   3
0 8 15  11  22
1   15  15  18
2        3   7
3            7

```
