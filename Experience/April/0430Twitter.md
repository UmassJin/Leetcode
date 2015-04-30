```
Input: the string "I want to count the frequency of the words in the input"
Output:
'I......1'
'want...1'
'the....3'
```

注意输出的格式可以用:
line = 12
print ele + '.'* (line - len(ele)) 
