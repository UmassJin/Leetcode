[G4G] (http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/)

Similar Question [Min Num to Composite Words](./Min_Num_to_Composite_Words.md)

Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details.
This is a famous Google interview question, also being asked by many other companies now a days.

Consider the following dictionary 
```
{ i, like, sam, sung, samsung, mobile, ice, cream, icecream, man, go, mango}
```

```python
Input:  ilike
Output: Yes 
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung" or "i like sam sung".
```

```python
# Determine whether the string could break into words in the dictionary 
# DP
# Status: dp[i] means the str[0,i-1] could segmented into dictionary
# Initializaiton: dp[0] = True
# Function: dp[i] = True, if str[:i] in dict 
#           for j in xrange(i+1, length+1), dp[j] = True if string[i:j] in dict 
# Result: dp[length] 
def word_break(string, dic):
    length = len(string)
    if length == 0: return True
    dp = [False for i in xrange(length+1)]
    dp[0] = True
    for i in xrange(1, length+1):
        if string[:i] in dic:
            dp[i] = True 
        if dp[i]:
            for j in xrange(i+1, length+1):
                if not dp[j] and string[i:j] in dic:
                    dp[j] = True
            if dp[j]: return True
    return False 

str1 = "ilikesamsung"
str2 = ""
str3 = "ilikelikeimangoiii"
str4 = "samsungandmangok"
dic = {"mobile","samsung","sam","sung","man","mango","icecream","and","go","i","like","ice","cream"}
print word_break(str1, dic)
print word_break(str2, dic)
print word_break(str3, dic)
print word_break(str4, dic)


```
