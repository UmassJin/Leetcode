From [Career Cup](http://www.careercup.com/question?id=5359122669109248) Pinterest

Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. You need to output the minimum number of words. For example, 

input: ```"aaaisaname" dict: ("a", "aaa", "is", "name")```

output: ```"aaa is a name"```

Wrong output: ```"a a a is a name"```

```python
def print_min_num_words(string, dic):
    length = len(string)
    if length == 0: return

    dp = [ length for i in xrange(length+1)]
    dp[0] = 0
    for i in xrange(1, length+1):
        if string[:i] in dic:
            dp[i] = 1

        for j in xrange(i): # Note: here we recursive in the range [0:i], compare with word_break.md
            if string[j:i] in dic:
                dp[i] = min(dp[i], dp[j]+1)

    print "min num words: %d",  dp[length]
    print "dp: ", dp
    cur = dp[length]
    last = length
    res = []
    for i in range(length)[::-1]: 
        # Here we could use range(length)[::-1], but could not use for xrange !!
        # since the range() return the list, but xrange() return the object !!                         
        print "i: %d, dp[i]: %d, cur: %d" %(i, dp[i], cur)
        if dp[i] == cur - 1:
            res.insert(0, string[i:last])
            print "res: ", res
            last = i
            cur -= 1
    print res

str1 = "aaaisaname"
d = ["a", "aaa", "is", "name"]
print_min_num_words(str1, d)
```

Output:

```python
[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python min_num_words.py 
min num words: %d 4
dp:  [0, 1, 2, 1, 10, 2, 3, 10, 10, 10, 4]
i: 9, dp[i]: 10, cur: 4
i: 8, dp[i]: 10, cur: 4
i: 7, dp[i]: 10, cur: 4
i: 6, dp[i]: 3, cur: 4
res:  ['name']
i: 5, dp[i]: 2, cur: 3
res:  ['a', 'name']
i: 4, dp[i]: 10, cur: 2
i: 3, dp[i]: 1, cur: 2
res:  ['is', 'a', 'name']
i: 2, dp[i]: 2, cur: 1
i: 1, dp[i]: 1, cur: 1
i: 0, dp[i]: 0, cur: 1
res:  ['aaa', 'is', 'a', 'name']
['aaa', 'is', 'a', 'name']
```

