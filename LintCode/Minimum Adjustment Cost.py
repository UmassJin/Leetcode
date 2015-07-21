'''
Given an integer array, adjust each integers so that the difference of every adjacent integers are not greater than a given number target.

If the array before adjustment is A, the array after adjustment is B, you should minimize the sum of |A[i]-B[i]|

Have you met this question in a real interview? Yes
Example
Given [1,4,2,3] and target = 1, one of the solutions is [2,3,2,3], the adjustment cost is 2 and it's minimal.

Return 2.

Note
You can assume each number in the array is a positive integer and not greater than 100.
'''

def min_adjust_cost(array, target):
    '''
    @args:
    @return:
    @raise error:
    '''
    if not array:
        return None
    n = len(array)
    s = 100
    dp = [[(1 << 31)-1 for _ in xrange(s+1)] for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(1, s+1):
            if i == 0:
                dp[i][j] = abs(array[i] - j)
            else:
                for k in xrange(max(1, j-target), min(s,j+target)+1):
                    dp[i][j] = min(dp[i][j], abs(j-array[i])+dp[i-1][k])
    result = (1 << 31) -1
    for i in xrange(1, s+1):
        result = min(result, dp[n-1][i])
    return result

test = [1, 4, 2, 3]
print min_adjust_cost(test, 1)


# Reference: http://www.cnblogs.com/yuzhangcmu/p/4153927.html
# https://github.com/algorhythms/LintCode/blob/master/Minimum%20Adjustment%20Cost.py
