'''
Give you an integer array (index from 0 to n-1, where n is the size of this array)，find the longest increasing continuous subsequence in this array. (The definition of the longest increasing continuous subsequence here can be from right to left or from left to right)

Have you met this question in a real interview? Yes
Example

For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.

For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.

Note
O(n) time and O(1) extra space.
'''

class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        if not A: return 0
        n = len(A)
        longestinc = 1
        longestdec = 1
        result = 1
        pre = A[0]
        
        for num in A[1:]:
            if num > pre:
                longestinc += 1
                pre = num
                result = max(result, longestinc)
                longestdec = 1
                
            elif num < pre:
                longestdec += 1
                pre = num
                result = max(result, longestdec)
                longestinc = 1
        return result 
            
                
