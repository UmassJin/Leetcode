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
