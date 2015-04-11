safes = [2, 5, 4, 10, 7, 2, 6, 8, 1, 10] x x x x x

Given an array of numbers, choose the numbers that cannot become neighbor to each other, find out the largest sum

Note: Three ways of solutions:

```python
# 3 ways to resolve this problem
# First, DP
# State: dp[i] means the max none close sum from 0...to..i
# Initialization: dp[0] = 0, dp[1] = max(dp[0], dp[1])
# Function: dp[i] = (dp[i-2]+nu[i], dp[i-1])
# Result: dp[n-1]
def find_largest_none_close_sum(A):
    length = len(A)
    dp = [0 for i in xrange(length)]
    dp[0] = A[0]
    
    for i in xrange(1, length):
        if i == 1:
            dp[1] = max(A[0],A[1])
        else:
            dp[i] = max((dp[i-2]+A[i]), dp[i-1])
    return dp[length-1]

# Greedy
def find_largest_none_close_sum_1(A):
    a = 0 
    b = 0 
    for i in xrange(len(A)):
        if i % 2 == 0:
            a = max(a+A[i], b)
        else:
            b = max(b+A[i], a)
    return max(a, b)

# The other dp
def find_largest_none_close_sum_2(A):
    length = len(A)
    value = [0,0]
    if not A: return 0
    value[0] = A[0]
    for i in xrange(1, length):
        if i == 1:
            value[1] = max(A[0],A[1])
        else:
            tmp = value[1]
            value[1] = max(A[i]+value[0], value[1])
            value[0] = tmp
    return value[1]        
                                        

num = [2, 5, 4, 10, 7, 2, 6, 8, 1, 10]
print "result1: ", find_largest_none_close_sum(num)
print "result2: ", find_largest_none_close_sum_1(num)
print "result3: ", find_largest_none_close_sum_2(num)                                        

```
