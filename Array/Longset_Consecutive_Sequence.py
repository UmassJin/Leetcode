Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        table = {}
        n = len(num)
        result = 0
        for i in xrange(n):
            left = 0; right = 0
            if num[i] not in table:
                if (num[i]-1) in table:
                    left = table[num[i]-1]
                if (num[i]+1) in table:
                    right = table[num[i]+1]
                isum = left + right + 1
                table[num[i]] = isum
                
                table[num[i]-left] = isum
                table[num[i]+right] = isum
                
                result = max(isum, result)
        return result 

# 注意这里的corner case： [1,2,0,1] 不光要更新当下的数值可以组成
# maximum consecutive array 的最大长度，还要更新 起点和终点的值！记住不是左右邻居的值，而是起点和终点
# Use left and right to locate the other end of the sequences to the left and right of n respectively, and replace the value with the new length.

# Corner Case 
# Input:	[0,3,7,2,5,8,4,6,0,1]
# Output:	7
# Expected:	9
