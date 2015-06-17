Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    
    # Recursion
    # Sort the array at first, then use the recursion to find 
    # the result, Time O(n^2)
    # 96ms
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.result = []
        self.dfs(candidates,target,0,[])
        return self.result 
        
    def dfs(self,candidates,target,start,reslist):
        length = len(candidates)
        if target == 0: 
            return self.result.append(reslist)
        
        for i in xrange(start,length):
            if target < candidates[i]:return 
            self.dfs(candidates,target-candidates[i],i,reslist+[candidates[i]])
        
        
    # DFS, not sort array (220ms)
    def combinationSum(self, candidates, target):
        self.result = []
        self.dfs(candidates,0,target,[])
        return self.result
        
    def dfs(self,can,cursum,target,res):
        if cursum > target: return 
        if cursum == target: 
            self.result.append(res)
            return 
        for i in xrange(len(can)):
            if not res or res[len(res)-1] <= can[i]:
                self.dfs(can,cursum+can[i],target,res+[can[i]])


For the combination_sum2, just change the start index from i to the i+1

Time Complexity: T(n) = T(n-1) + 1 = O(n) ？
