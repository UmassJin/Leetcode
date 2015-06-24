'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''

# Good Analysis: http://blog.csdn.net/kenden23/article/details/14106137

    def canCompleteCircuit(self, gas, cost):
        total = 0; sum = 0
        n = len(gas)
        j = -1
        
        for i in xrange(n):
            sum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if sum < 0:
                j = i
                sum = 0
                
        if total < 0: 
            return -1
        return j + 1


class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    # Time out 
    def canCompleteCircuit(self, gas, cost):
        total = 0; sum = 0
        n = len(gas)
        j = 0
        
        for i in xrange(n):
            sum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if sum < 0:
                j = i + 1
                sum = 0
                
        if total < 0: 
            return -1
        return j 
 
'''
1. 几点注意的地方
a. 从i开始，j是当前station的指针，sum += gas[j] – cost[j] （从j站加了油，再算上从i开始走到j剩的油，走到j+1站还能剩下多少油）
b.如果sum < 0，说明从i开始是不行的。那能不能从i..j中间的某个位置开始呢？既然i出发到i+1是可行的， 又i~j是不可行的， 从而发现i+1~ j是不可行的。
c. 以此类推i+2~j， i+3~j，i+4~j 。。。。等等都是不可行的
d. 所以一旦sum<0，index就赋成j + 1，sum归零。
e. 最后total表示能不能走一圈。

倘若在i处gas[i]-cost[i] < 0, 则从 i + 1 开始
倘若total (gas[i] - cost[i]) < 0, 则一定不存在起始点

# Reference: http://www.cnblogs.com/yuzhangcmu/p/4179228.html
'''
