Given a set of distinct integers, S, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    # Recursion 
    def subsets(self, S):
        def dfs(depth, start, result_list):
            result.append(result_list)
            if depth == len(S): return
            for i in xrange(start, len(S)):
                dfs(depth+1, i+1, result_list +[S[i]])
    
        result = []
        result_list = []
        S.sort()
        dfs(0,0, result_list)    
        return result
    
    # Recursion Method 2 
    def subsets(self,S):
        if not S: return [[]]
        else:
            S.sort()
            pre_subsets = self.subsets(S[1:])
            return pre_subsets +  [[S[0]]+elem for elem in pre_subsets]

    # Iteration 
    def subsets(self, S):        
        result = []
        if S == []:
            return []
        S.sort()
        for i in xrange(len(S)):
            result_list = []
            result_list.append([S[i]])
            j = i +1
            while j < len(S):
                for k in xrange(len(result_list)):
                    result_list.append(result_list[k]+[S[j]])
                j = j + 1
            result = result + result_list
        result.insert(0,[])
        
        return result    

Subset II
Given a collection of integers that might contain duplicates, S, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        def dfs(depth, start, valuelist):
            if valuelist not in res:
                res.append(valuelist)
            if depth == len(S): return
            for i in range(start, len(S)):
                dfs(depth+1, i+1, valuelist+[S[i]])
        S.sort()
        res = []
        dfs(0, 0, [])
        return res
        
    def subsetsWithDup(self, S):
        if not S: return [[]]
        else:
            S.sort()
            pre_subset = self.subsetsWithDup(S[1:])
            for ele in pre_subset:
                if [S[0]] + ele not in pre_subset:
                    pre_subset = pre_subset + [[S[0]] + ele]
            return pre_subset

        
        
    # Method2, Iteration
    # if S[i] is same to S[i - 1], then it needn't to be added 
    # to all of the subset, just add it to the last l subsets 
    # which are created by adding S[i - 1]
    def subsetsWithDup(self, S):
        S.sort()
        result = [[]]
        
        for i in xrange(len(S)):
            if i == 0 or S[i] != S[i-1]:
                l = len(result)
            for j in xrange(len(result)-l,len(result)):
                result.append(result[j]+[S[i]])
        return result
