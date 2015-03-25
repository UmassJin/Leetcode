Given a string s and a dictionary of words dict, add spaces in s to construct 
a sentence where each word is a valid dictionary word.
Return all such possible sentences.
For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].
A solution is ["cats and dog", "cat sand dog"].

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak_1(self, s, dict):
        n = len(s)
        A = [None]*n
        i = n-1
        
        while i >= 0:
            if s[i:n] in dict:
                A[i] = [n]
            else:
                A[i] = []
                
            for j in xrange(i+1,n):
                if A[j] and s[i:j] in dict:
                    A[i].append(j)
        
            i -=1            
        
        path_list = [[0]]
        res = []
        
        while path_list: 
            new_list = []
            for list in path_list:
                if list[-1] == n:
                    temp = [ s[list[i]:list[i+1]] for i in xrange(len(list)-1) ]
                    res.append(" ".join(temp))
                else:
                    for j in A[list[-1]]:
                        new_list.append(list+[j])
                
            path_list = new_list
        return res
    
    # Use the recursion and DFS    
    # Note: 
    # 1) Use the DFS combined with DP for the issue
    # 2) DP: dp[i] get the True/False check if s[:i] could cut the word or not  
    # 3) DFS: go though the string from the end to start, for example "catsenddog"
    #    first find the "dog", then check "catsend" for the corresponding word 
    def wordBreak(self, s, dict):
        self.result = []
        dp = self.word_break_dp(s,dict)
        self.dfs_word_break(len(s)+1,s,dict,[],dp)
        return self.result 
        
    def word_break_dp(self,s,dict):
        length = len(s)
        dp = [False for i in xrange(length+1)]
        dp[0] = True
        for i in xrange(1,length+1):
            for j in xrange(i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
                    break
        return dp 
    
    def dfs_word_break(self,end,s, dict, strlist, dp):
        if end == 0: self.result.append(' '.join(strlist))
        for i in xrange(end):
            if dp[i] and s[i:end] in dict:
                strlist.insert(0,s[i:end])
                self.dfs_word_break(i,s,dict,strlist,dp)
                strlist.pop(0)
        
        
        
