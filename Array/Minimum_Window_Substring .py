Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

# Reference: http://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/

class Solution:
    # @return a string
    def minWindow(self, S, T):
        lengths = len(S)
        lengtht = len(T)
        if lengtht > lengths: return ""
        
        required = {}
        found = {}
        result = ''
        count = 0  # calculate whether there is enough char in T present in S 
        l = 0
        
        for char in T:
            required[char] = required.get(char,0) + 1
            found[char] = 0
        
        for r in xrange(lengths):
            if S[r] not in required:
                continue 
            
            found[S[r]] += 1
            if found[S[r]] <= required[S[r]]: 
                count += 1
            
            if count == lengtht:
                while l < r:
                    if S[l] not in required:
                        l += 1
                        continue
                    if found[S[l]] > required[S[l]]:
                        found[S[l]] -= 1
                        l += 1
                        continue 
                    break
                if len(result) == 0 or len(result) > (r-l+1): 
                    result = S[l:r+1]
        
        return result 

    # Note
    # 1. Prepare for wo dict
    # 2. Skip chars that we don't care, increase right bound
    # 3. If current window contains all the chars we want(counter == M), stop and resize left bound
    # 4. Skip chars that we don't care. If extra chars in found > wanted, skip them
    # 5. break here
    # 6. Calculate the current size
