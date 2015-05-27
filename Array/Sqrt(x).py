'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

#解题思路：实现开平方函数。这里要注意的一点是返回的时一个整数。通过这一点我们可以看出，
#很有可能是使用二分查找来解决问题的。这里要注意折半查找起点和终点的设置。起点i=1；终点j=x/2+1；
# 因为在(x/2+1)^2 > x，所以我们将折半查找的终点设为x/2+1。

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x < 0: return -1
        if x == 0: return 0
        l = 1; r = x/2+1
        
        while l <= r:
            mid = (l + r)/2
            
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                r = mid - 1
            else:    
                l = mid + 1
        return r


# Reference: http://www.cnblogs.com/zuoyuan/p/3775852.html
# Reference: http://blog.csdn.net/linhuanmars/article/details/20089131
