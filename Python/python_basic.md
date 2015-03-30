####1. Array
Spiral Matrix

####2. Use enumerate 
```python
enumerate(sequence,start=0)
seasons = ['a','b','c','d']
for idx, ele in enumerate(seasons):
    print "idx: %d, ele: %s" %(idx, ele)
Output:
idx: 0, ele: a
idx: 1, ele: b
idx: 2, ele: c
```

####3. Two methods to get the random list
```python
random.shuffle(a_tot)    #get a randomized list
a_1 = a_tot[0:1300]     #pick the first 1300
a_2 = a_tot[1300:]      #pick the last 200

new_t = random.sample(a_tot,len(a_tot))    #get a randomized list
a_1 = new_t[0:1300]     #pick the first 1300
a_2 = new_t[1300:]      #pick the last 200
```
####4. String Method 
#####Remove the leading chars or the 
######1) str.lstrip([chars])
Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix; rather, all combinations of its values are stripped:
```python
>>> '   spacious   '.lstrip()
'spacious   '
>>> 'www.example.com'.lstrip('cmowz.')
'example.com'
```

######2) str.rstrip([chars])
Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped:
```python
>>> '   spacious   '.rstrip()
'   spacious'
>>> 'mississippi'.rstrip('ipz')
'mississ'
```

######3) str.strip([chars])
Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped:
```python
>>> '   spacious   '.strip()
'spacious'
>>> 'www.example.com'.strip('cmowz.')
'example'
```
Usage: [String to Integer (atoi)] (../Array/String_to_Integer.py)
[Simply Path](../Array/Simplify_Path.py)


####5. Build-in function
##### 1) all(iterable)
Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:
```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

