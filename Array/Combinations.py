```
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        def combine_helper(n, k, start, depth, subres):
            if depth == k: 
                result.append(subres)
                return
            for i in xrange(start, n+1):
                combine_helper(n, k, i+1, depth+1, subres+[i])
            
        if n == 0 or k == 0: return [[]]    
        result = []
        combine_helper( n, k, 1, 0, [])
        return result 
