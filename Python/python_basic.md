###Data Structures 
####1. Tuples 
* A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The only difference is that tuples can't be changed i.e., tuples are immutable and tuples use parentheses and lists use square brackets.
* It is not possible to assign to the individual items of a tuple, however it is possible to create tuples which contain mutable objects, such as lists.

##### Definition:
```python
# A tuple consists of a number o fvalues seperated by commas 
>>> t = 123,4456,'hello'
>>> t
(123, 4456, 'hello')
# Tuples may be nested 
>>> t1 = 123,234,(234,90,'world')
>>> t1
(123, 234, (234, 90, 'world'))
# Tuples are immutable:
>>> t1[0] = 999
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
# But tuple can contain mutable objects 
>>> t2 = [1,2,3],[1,3,2]
>>> t2
([1, 2, 3], [1, 3, 2])
>>> type(t2)
<type 'tuple'>
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```
* The statement t = 12345, 54321, 'hello!' is an example of tuple packing: the values 12345, 54321 and 'hello!' are packed together in a tuple. The reverse operation is also possible:
```python
>>> t = 12345, 54321, 'hello!'
>>> x,y,z = t
>>> x
12345
>>> y
54321
>>> z
'hello!'
>>> type(t)
<type 'tuple'>
>>> type(x)
<type 'int'>
>>> type(z)
<type 'str'>
```
* Access Values in Tuples: t[0], t[1:3]
* Can not change the value in tuple or delete/modify any element in tuple, but create a new tuple as following
```python
>>> t
(12345, 54321, 'hello!')
>>> t1
(123, 234, (234, 90, 'world'))
>>> t2 = t+t1
>>> t2
(12345, 54321, 'hello!', 123, 234, (234, 90, 'world'))
>>> type(t2)
<type 'tuple'>
```
* Delete the whole tuple: ```del t2```

##### Basic Tuple operations:
Tuples respond to the + and * operators much like strings; they mean concatenation and repetition here too, except that the result is a new tuple, not a string.
In fact, tuples respond to all of the general sequence operations we used on strings in the prior chapter :

| Python Expression	| Results	| Description
|---|:---:|:---:|
| len((1, 2, 3)) |	3 |	Length
| (1, 2, 3) + (4, 5, 6)	| (1, 2, 3, 4, 5, 6) |	Concatenation
| ('Hi!',) * 4	| ('Hi!', 'Hi!', 'Hi!', 'Hi!')|	Repetition
| 3 in (1, 2, 3) |	True|	Membership
| for x in (1, 2, 3): print x,|	1 2 3 |	Iteration

##### Build-in Tuple function 
|SN	| Function with Description
|---|:---|
1	| cmp(tuple1, tuple2)
  | Compares elements of both tuples.
2	| len(tuple)
  | Gives the total length of the tuple.
3	| max(tuple)
  | Returns item from the tuple with max value.
4	| min(tuple)
  | Returns item from the tuple with min value.
5	| tuple(seq)
  | Converts a list into tuple.

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
Usage: [String to Integer (atoi)] (../Array/String_to_Integer.py) ;
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

##### 1) zip(iterable,..)
This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The returned list is truncated in length to the length of the shortest argument sequence. When there are multiple arguments which are all of the same length, zip() is similar to map() with an initial argument of None. With a single sequence argument, it returns a list of 1-tuples. With no arguments, it returns an empty list.

The left-to-right evaluation order of the iterables is guaranteed. This makes possible an idiom for clustering a data series into n-length groups using zip(*[iter(s)]*n).

zip() in conjunction with the * operator can be used to unzip a list:
```python
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> zipped
[(1, 4), (2, 5), (3, 6)]
# Note: here is not (1,4),(1,5),(1,6),(2,4)....
>>> x2, y2 = zip(*zipped)
>>> x == list(x2) and y == list(y2)
True
```
Usage 
[Reverse Words in a StringII](../Array/Reverse_Words_in_a_StringII.py)

