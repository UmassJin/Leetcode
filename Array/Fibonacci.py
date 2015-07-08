'''
Reference
Analysis: http://tech-queries.blogspot.com/2010/09/nth-fibbonacci-number-in-ologn.html
Python: http://stackoverflow.com/questions/12338802/how-efficient-is-this-python-code-for-the-fibonacci-sequence
G4G: http://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
Wiki: https://en.wikipedia.org/wiki/Fibonacci_number
'''


# Fn = Fn-1 + Fn-2
# F0 = 0 and F1 = 1 

def fib_dp(n):
    dp = [0 for i in xrange(n+1)]
    dp[0] = 0
    dp[1] = 1
    
    for i in xrange(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


def fib_dp2(n):
    dp1 = 0; dp2 = 1
    for i in xrange(2, n+1):
        tmp = dp2
        dp2 = dp1 + dp2
        dp1 = tmp
    return dp2

def fib_logn(n):
    if n < 2: return n
    m = [[1,1],[1,0]]
    return matrix_exp(m, n)[0][0]

def matrix_exp(A, n):
    if n == 0:
        return [[1,0],[0,1]]
    if n % 2 == 1:
        return multiply(A, matrix_exp(A, n-1))
    else:
        sq = matrix_exp(A, n//2)
        return multiply(sq, sq)
        
def multiply(matrix1, matrix2):
    result = [[0,0],[0,0]]
    result[0][0] = matrix1[0][0]*matrix2[0][0] + matrix1[0][1]*matrix2[1][0]
    result[0][1] = matrix1[0][0]*matrix2[0][1] + matrix1[0][1]*matrix2[1][1]
    result[1][0] = matrix1[1][0]*matrix2[0][0] + matrix1[1][1]*matrix2[1][0]
    result[1][1] = matrix1[1][0]*matrix2[0][1] + matrix1[1][1]*matrix2[1][1]
    return result

n = 9
print fib_dp(n)
print fib_dp2(n)
print fib_logn(n)
