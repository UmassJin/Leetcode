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
        result = []
        self.partition_helper(s, result, [])
        return result 
        
    def partition_helper(self, s, result, sublist):
        if len(s) == 0:
            result.append(sublist); return
        for i in xrange(1, len(s)+1):  # Note: here should be 1 to len(s) + 1
            if self.is_palindrome(s[:i]):
                self.partition_helper(s[i:], result, sublist + [s[:i]])
                 # Note: Here we pass str_list + [substr] instead of [str_list,substr]
    def is_palindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            return False 
            
# Time Complexity: O(n^2)
