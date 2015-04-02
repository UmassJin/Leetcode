You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from 
robbing each of them is that adjacent houses have security system connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob_1(self, num): 
        a = 0
        b = 0
        for i in xrange(len(num)):
            if i % 2 == 0:
                a = max(a+num[i],b)
            else:
                b = max(b+num[i],a)
        return max(a,b)
    
    def rob(self, num):
        length = len(num)
        if length == 0: return 0
        if length == 1: return num[0]
        value = [0,0]
        value[0] = num[0]
        value[1] = max(num[0],num[1]) # value[1] always keep the largest sum
        for i in xrange(2,length):
            tmp = value[1]
            value[1] = max(num[i] + value[0],value[1])
            value[0] = tmp # value[0] keep the previous largest sum
        return value[1]
