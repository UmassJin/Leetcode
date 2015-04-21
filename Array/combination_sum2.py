Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        if not candidates: return None
        candidates.sort()
        self.result = []
        self.combi_helper(candidates, target, 0, [])
        return self.result
    
    def combi_helper(self, candidates, target, start, reslist):
        if target == 0:
            if reslist not in self.result:
                self.result.append(reslist)
        
        for i in xrange(start, len(candidates)):
            if candidates[i] > target: return 
            self.combi_helper(candidates, target-candidates[i], i+1, reslist + [candidates[i]])
        
