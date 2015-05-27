Implement pow(x, n).


class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}

# Solution 1: 二分法
# 优点是代码简洁，缺点是没有考虑到overflow的情况
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            n = -n
            x = 1/x
        if n % 2 == 1:
            return self.myPow(x*x, n/2)*x
        if n % 2 == 0:
            return self.myPow(x*x, n/2)

# Solution 2: bit manipulation 
# 就是把n看成是以2为基的位构成的，因此每一位是对应x的一个幂数，然后迭代直到n到最高位。
# 比如说第一位对应x，第二位对应x*x,第三位对应x^4,...,第k位对应x^(2^(k-1))
# 这里做很多边界的检查，
# 1) n < 0 or n > 0, if n < 0, whether 1/x will overflow 
# 2) whether x < 0 or x > 0, if n 为奇数，并且x < 0, result < 0

    def myPow(self, x, n):
        max_int = (1<<32)/2-1
        min_int = (-1<<32)/2
        
        if n == 0 : return 1
        if n == 1: return x
        result = 1
        if n < 0:
            if 1/x <= max_int or x <= (-1/max_int):
                x = 1/x
            else:
                return max_int
        
        n = abs(n)
        positive = True
        if n%2 == 1 and x < 0:
            positive = False
        
        x = abs(x)
        while n > 0:
            if n & 1 == 1:
                if result*x > max_int:
                    return max_int
                result *= x
            
            x *= x
            n = n >> 1
        
        if positive: return result
        else: return -result 


# Reference: Pow(x,n) http://blog.csdn.net/linhuanmars/article/details/20092829
# Reference: Sqrt(x) http://blog.csdn.net/linhuanmars/article/details/20089131
