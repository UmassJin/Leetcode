Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
For example, given s = "aab",
Return
  [
    ["aa","b"],
    ["a","a","b"]
  ]
  
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if len(s) == 0 or len(s) == 1:
            return [[s]]
        str_list = []
        result = []
        self.get_partition(s, str_list, result)
        return result
    
    def get_partition(self,s, str_list, result):
        if len(s) == 0:
            result.append(str_list)
            
        for i in xrange(1,len(s)+1):  # Note: here should be 1 to len(s) + 1
            substr = s[:i]
            if (self.is_palindrome(substr)):
                self.get_partition(s[i:], str_list + [substr], result) 
                # Note: Here we pass str_list + [substr] instead of [str_list,substr]
        
    def is_palindrome(self, s): 
        i = 0; j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True   


# Time Complexity: O(n^2)
