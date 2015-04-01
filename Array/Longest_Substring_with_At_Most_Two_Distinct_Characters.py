Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
For example, Given s = “eceba”,
T is "ece" which its length is 3.

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstringTwoDistinct(self, s):
        table = {} 
        l = 0; count = 0
        result = 0
        if len(s) < 2: return len(s)
        for r, char in enumerate(s):
            table[char] = table.get(char,0) + 1
            if table[char] == 1: # new char 
                count += 1
                while count > 2:
                    table[s[l]] -= 1
                    if table[s[l]] == 0: count-=1
                    l += 1
            result = max(result, r-l+1)
        return result 

# Use the hashtable to save the char and count number
# keep the count to check the distinguish chars
# Note: we use the while not the if to check count > 2
