```
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
```

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        result = []
        ilist = []
        factor = 1
        
        for i in xrange(1, n+1):
            ilist.append(i)
        for i in xrange(1, n+1):
            factor *= i
        
        k -= 1
        while n > 0:
            factor = factor / n
            index = k / factor 
            result.append(str(ilist[index]))  
            # Here, ''.join(result), result must be the string list ! 
            # result = ['1','2','3']
            ilist.remove(ilist[index])
            k %= factor 
            n -= 1
        
        return ''.join(result) 

# For the permutation of n, the total amount is n!
# so we could seperate into n group, each group has (n-1)! 
# if we want to get the kth permutation, k/(n-1)! is the index 
# among current n groups, need to mention here, k = 1,2,3,4....
# but index is based on 0, so here we use k-1, then k/(n-1)!
# then we delete that member in the list, k = k % (n-1)!
# n -= 1; factor = factor / n
