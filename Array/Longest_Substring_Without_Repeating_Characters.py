Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = 0
        length = 0
        table = {}
        for i, char in enumerate(s):
            if char in table:
                start = max(start,table[char]+1)
            table[char] = i
            length = max(length, i-start+1)
        return length 
    
    # O(n) time, O(n) space
    def lengthOfLongestSubstring(self, s):
        idict = {}
        result = 0
        start = 0
        for i, char in enumerate(s):
            if char not in idict:
                idict[char] = i
            else:
                start = max(start, idict[char]+1) #注意这里必须是max(start,idict[char]+1), test case: 'abba'
                idict[char] = i    #注意这里，不管char是不是在idict里面，都需要update i的值，例如test case 'dddd', 'dedv'
            result = max(result, i-start+1)
        return result 
    
    def lengthOfLongestSubstring_1(self, s):
        start = 0
        maxlen = 0
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = -1
        for i in range(len(s)):
            if dict[s[i]] != -1:
                while start <= dict[s[i]]:
                    dict[s[start]] = -1
                    start += 1
            if i - start + 1 > maxlen: maxlen = i - start + 1
            dict[s[i]] = i
        return maxlen
        
# First solution is better
# For example, if the string is 'abcdbd', so when we go through till the second 'b', the start should be 
# start from 'c', and then calculate the distinct letters.
# we use the hashtable to save the index! Not the times that letter appeared !
# start = max(start,table[char]+1) not start = table[char] + 1
