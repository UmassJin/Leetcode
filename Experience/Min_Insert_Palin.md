Given a string, find the minimum number of characters to be inserted to convert it to palindrome.

Before we go further, let us understand with few examples:
```
    ab: Number of insertions required is 1. bab
    aa: Number of insertions required is 0. aa
    abcd: Number of insertions required is 3. dcbabcd
    abcda: Number of insertions required is 2. adcbcda which is same as number of insertions in the substring bcd(Why?).
    abcde: Number of insertions required is 4. edcbabcde
```

Let the input string be str[l……h]. The problem can be broken down into three parts:

* 1. Find the minimum number of insertions in the substring str[l+1,…….h].
* 2. Find the minimum number of insertions in the substring str[l…….h-1].
* 3. Find the minimum number of insertions in the substring str[l+1……h-1].

[G4G](http://www.geeksforgeeks.org/dynamic-programming-set-28-minimum-insertions-to-form-a-palindrome/)

```python
def min_insert_pali(string):
    return pali_helper(string, 0, len(string)-1)
    
def pali_helper(string, left, right):
    if left == right: return 0
    if right == left + 1:
        if string[left] == string[right]:
            return 0
        else:
            return 1
    if left > right: return 1<<32
    
    if string[left] == string[right]:
        return pali_helper(string, left+1, right-1)
    else:
        return min(pali_helper(string, left, right-1), \
                pali_helper(string, left+1, right))+1
        
input_str = "geeks"  
print min_insert_pali(input_str)


# state: dp[i][j] meanings the min number for the string[i:j]
# initialize: 
# function: dp[i][j] = dp[i-1][j+1] if string[i] == string[j]
#                    = min(dp[i][j-1], dp[i+1][j])+1 else
# result: dp[0][length-1]

def pali_dp(string):
    n = len(string)
    dp = [[0 for j in xrange(n)] for i in xrange(n)]
    
    for gap in xrange(1,n):
        i = 0; j = gap;
        while j < n:
            if string[i] == string[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i+1][j])+1
            i += 1; j += 1
    return dp[0][n-1]

input_str = "geeks"
print pali_dp(input_str)
```
