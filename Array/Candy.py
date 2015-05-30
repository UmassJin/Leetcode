'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candy = [1 for i in xrange(len(ratings))]
        length = len(ratings)
        
        # 第一遍从左边往右边扫描，找出左边需要的最大的糖果数目
        for i in xrange(1, length):
            if ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1
        
        ＃第二遍从右边往左边扫描，找出右边所需要的最大的糖果数目，
        # 当i比右边rating大，而且candy小于等于的时候，加candy
        for i in xrange(length-2,-1,-1):       
            if ratings[i+1] < ratings[i] and candy[i+1] >= candy[i]:
                candy[i] = candy[i+1] + 1
        
        return sum(candy)  
        
        
class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        if not ratings: return 0
        n = len(ratings)
        left = [1 for i in xrange(n)]

        for i in xrange(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        
        result = left[n-1]
        for i in xrange(n-2, -1, -1):
            right = 1
            if ratings[i] > ratings[i+1]:
                 right = left[i+1] + 1
            result += max(right, left[i])
            left[i] = right
        return result 
  
# 基本思路就是进行两次扫描，一次从左往右，一次从右往左。第一次扫描的时候维护对于每一个小孩左边所需要最少的糖果数量，
# 存入数组对应元素中，第二次扫描的时候维护右边所需的最少糖果数，并且比较将左边和右边大的糖果数量存入结果数组对应元素中。
# 这样两遍扫描之后就可以得到每一个所需要的最最少糖果量，从而累加得出结果。方法只需要两次扫描，所以时间复杂度是O(2*n)=O(n)。
# 空间上需要一个长度为n的数组，复杂度是O(n)。
