'''
Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000) and an query list. For each query, give you an integer, return the number of element in the array that are smaller that the given integer.

Have you met this question in a real interview? Yes
Example
For array [1,2,7,8,5], and queries [1,8,5], return [0,4,2]

Note
We suggest you finish problem Segment Tree Build and Segment Tree Query II first.

Challenge
Could you use three ways to do it.

Just loop
Sort and binary search
Build Segment Tree and Search.
'''

class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that 
             are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        if not queries: return []
        if not A: return [0 for i in xrange(len(queries))]
        A.sort()
        n = len(A)
        result = []
        
        for i in xrange(len(queries)):
            if len(A) == 0 or A[-1] < queries[i]:  # Here we check if the A[-1] is larger than the queries[i]
                result.append(len(A))
                continue 
            
            left = 0; right = n-1
            subres = 0
            
            while left < right - 1: # Here we need to seperate left, right, could not use left <= right
                mid = (left + right) / 2
                if queries[i] > A[mid]:
                    left = mid 
                elif  queries[i] <= A[mid]:
                    right = mid 
    
            if A[left] >= queries[i]: subres = left
            elif A[right] >= queries[i]: subres = right
            else: subres = right + 1
            result.append(subres)
        return result 
