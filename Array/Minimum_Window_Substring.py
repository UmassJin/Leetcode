Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

# More efficient answer, ONLY need one dict 
# https://leetcode.com/discuss/20053/three-concise-implemetation-according-leetcode-oj-discuss
import collections 

class Solution:
    def minWindow(self, s, t):
        m = len(s); n = len(t)
        if m == 0 or n == 0 or m < n: return ""
        idict = collections.defaultdict(int)
        for i in xrange(n):
            idict[t[i]] += 1
        left = 0; count = 0
        minlen = (1<<31) - 1; minindex = 0
        for right in xrange(m):
            idict[s[right]] -= 1
            if idict[s[right]] >= 0:
                count += 1
            while count == n:
                if right - left + 1 < minlen:
                    minlen = right - left + 1
                    minindex = left
                idict[s[left]] += 1
                if idict[s[left]] > 0:
                    count -= 1
                left += 1
        if minlen == (1<<31) - 1: return ""
        return s[minindex:minindex+minlen]
        

# The other answer 
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow_1(self, s, t):
        m = len(s); n = len(t)
        if m == 0 or n == 0 or m < n: return ""
        idict = {char: t.count(char) for char in t}
        left, right = 0, 0
        result = ''
        minwindow = (1<<31) - 1
        while right <= m:
            if all(map(lambda x: True if x <= 0 else False, idict.values())):
                if minwindow > right - left:
                    minwindow = right - left
                    result = s[left:right]
                if s[left] in idict:
                    idict[s[left]] += 1
                left += 1
            else:
                if right == m: break
                if s[right] in idict:
                    idict[s[right]] -= 1
                right += 1    
        return result 

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
            if found[S[r]] <= required[S[r]]:  # 注意这里count可以用来统计t的长度
                count += 1
            
            if count == lengtht:  # 这里不能用while
                while l < r:      # 这里要判断l < r
                    if S[l] not in required:
                        l += 1
                        continue
                    if found[S[l]] > required[S[l]]:
                        found[S[l]] -= 1
                        l += 1
                        continue 
                    break    # 注意这里的break!!! 非常重要！！！
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
