Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
       positive = (dividend < 0) is (divisor < 0)
       
       dividend = abs(dividend)
       divisor = abs(divisor)
       result = 0
       
       while dividend >= divisor:
           tmp = divisor
           k = 0
           while dividend >= tmp:
               dividend -= tmp
               result += 1<<k
               tmp = tmp << 1
               k += 1
       if not positive: 
            result = -result 
       
       return min(max((-1<<32)/2, result), (1<<32)/2-1)
       #return min(max(-2147483648, result), 2147483647)
           
# 被除数:dividend/除数:divisor，13/3:  13是被除数，3是除数
# 两种思路：
# 第一个思路是：从大到小，将divisor<<1,记录下做移的次数，一直到靠近dividend,然后再依次>>1,除以2
# 第二个思路是: 从小到大，如above code，我们先从最小的算起，然后result依次 += 1<<k, 直到dividend >= tmp, 然后再从tmp = divisor算起
# http://yucoding.blogspot.com/2013/01/leetcode-question-28-divide-two-integers.html
# http://zjalgorithm.blogspot.com/2014/11/leetcode-divide-two-integers.html
