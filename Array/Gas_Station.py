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
    def canCompleteCircuit_1(self, gas, cost):
        n = len(gas)
        
        for i in xrange(n):
            left = 0
            for j in xrange(n):
                k = (i+j)%n
                left = left + (gas[k] - cost[k])
                if left < 0 : 
                    break
            if j == n: return i
            i += j + 1
        return -1
 
