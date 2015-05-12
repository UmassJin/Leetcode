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

    # 第三遍做题思路总结：这里需要用到两个dictionary，一个用来存储有多少个元素在T里面，一个用来
    # 判断是否找到，注意这里的思路，不能对left pointer and right pointer 做while循环，
    # 在找到所有的元素之后或者遍历到结尾之后在移动left
    # Test case: 'a', 'a'; 'a', 'b'; 'ab', 'b'


# The following is the wrong answer !!!
    # def minWindow(self, s, t):
    #     if not s or not t: return None
    #     if len(t) > len(s): return ""
        
    #     idict = {}
    #     slow = 0; fast = 0
    #     count = 0; 
    #     result = ""
    #     minlen = len(s)
        
    #     for char in t:
    #         if char not in idict:
    #             idict[char] = 1
    #             count += 1
    #         else:
    #             idict[char] += 1
                
    #     for i, char in enumerate(s):
    #         while fast < len(s) and slow <= fast:
    #             if char not in idict:
    #                 fast += 1
    #             else:
    #                 if idict[char] > 0:
    #                     idict[char] -= 1
    #                     if idict[char] == 0:
    #                         count -= 1
    #                 if count > 0:
    #                     fast += 1
    #                 else:
    #                     if minlen >= (fast-slow+1):
    #                         result = s[slow:fast+1]
    #                         minlen = len(result)
                        
    #                     if s[slow] in idict:
    #                         if idict[s[slow]] == 0:
    #                             count += 1
    #                         idict[s[slow]] += 1
    #                     slow += 1
        
    #     return result 
        
