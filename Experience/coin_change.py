'''
*[G4G] (http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/)
* Similar to CC150, good questions !
* Several ways to ask 1. How many ways? 2. What are the ways? 3. Minimum coin number?
'''

# s: means {1,2,3}, list of coins
# m: how many kinds of coins provided 
# n: total sum  

# For example: (1,2,3) sum: 5, how many ways:

# Recursion:
def coin_change(s, m, n):
    if n == 0:
        return 1  # Note: if n==0, means there is 1 solution already !
    if n < 0:
        return 0
    if m <= 0 and n > 0:
        return 0
    return coin_change(s, m-1, n) + coin_change(s, m, n-s[m-1])

# DP
# state: dp[i][j]: how many ways use j coins and sum is i 
# initialization: dp[0][j] = 1 # if n==0, means there is 1 solution already !
# function: dp[i][j] = dp[i][j-1] + dp[i-S[j]][j] if j >=1 and i-S[j] >= 0
def coin_change_dp(s, m, n):
    dp = [[0 for j in xrange(m)] for i in xrange(n+1)]
    for i in xrange(m):
        dp[0][i] = 1
        
    for i in xrange(1, n+1):
        for j in xrange(m):
            x = 0; y = 0
            if i - s[j] >= 0:
                x = dp[i-s[j]][j]
            if j >= 1:
                y = dp[i][j-1]
            dp[i][j] = x + y
    return dp[n][m-1]

test = [2,3,5,6]
print "coin_change: ", coin_change(test, 4, 10)
print "coin_change_dp: ", coin_change_dp(test, 4, 10)


# Optimization 
# table[i] will be storing the number of solutions for
# value i. We need n+1 rows as the table is consturcted
# in bottom up manner using the base case (n = 0)

def coin_change_optimize(s, m, n):
    '''
    @ args:
    s: coin array
    m: how many coins totally
    n: how much need to change
    @ total change options 
    @ return: min number
    '''
    dp = [0 for i in xrange(n+1)]
    dp[0] = 1
    for i in xrange(m):
        for j in xrange(s[i],n+1):
            dp[j] += dp[j-s[i]]
    return dp[n]
 
test1 = [2,3,5,6]
print "coin_change: ", coin_change_optimize(test1, 4, 10)
