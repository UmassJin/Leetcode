###Data Structures 
####1. Lists
* A list is a sequence of values. In a string, the values are characters; in a list, they can be any type. The values in a list are called elements or sometimes items.

##### Definition:
* There are several ways to create a new list; the simplest is to enclose the elements in square brackets ([ and ])
```python
[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit']
# Could have different types in one list 
['spam', 2.0, 5, [10, 20]]
# empty list
empty = []
```
* A list within another list is nested. 

##### Lists are mutable:
* ```numbers[1] = 5```
* Any integer expression can be used as an index.
* If you try to read or write an element that does not exist, you get an IndexError.
* If an index has a negative value, it counts backward from the end of the list.

##### Traversing a list
```Python
for cheese in cheeses:
    print cheese

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
```    
* Use the enumerate 
```python
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
>>> for i, char in enumerate(list):
...    print ("i: ", i)
...    print ("char: ", char)
... 
i:  0
char:  12
i:  1
char:  56
i:  2
char:  good
```

##### List Operations
| Python Expression |	Results	| Description
|:---|:---|:---|
| len([1, 2, 3])	| 3 |	Length
| [1, 2, 3] + [4, 5, 6]	 | [1, 2, 3, 4, 5, 6]	| Concatenation
| ['Hi!'] * 4 | 	['Hi!', 'Hi!', 'Hi!', 'Hi!']	| Repetition
| 3 in [1, 2, 3]	|True	| Membership
| for x in [1, 2, 3]: print x,|	1 2 3	| Iteration

* slicing, s[1:2], based on the 0, include the 1 and exclude 2 
* s == t, equal if all of the characters are the same. s is t ? no guarantee. 
* t = s[:]  # list slices ALWAYS make copies 
* slicing mutable objects ALWAYS makes new objects (list)
  slicing immutable objects entirely MAY or MAY NOT make a new object (tuple)
* t =s   assignments in python NEVER make copies 
    
```python
>>> s = t
>>> s
[10, 20, 30, 40, 50, 60]
>>> t
[10, 20, 30, 40, 50, 60]
>>> id(s)
4493599448
>>> id(t)
4493599448
>>> p = t[:]
>>> id(p)
4493789160
>>> id(t)
4493599448

>>> tuple1 = 'abd','dfaf'
>>> tuple1
('abd', 'dfaf')
>>> tuple2 = tuple1[:]
>>> tuple2
('abd', 'dfaf')
>>> id(tuple2)
4302721352
>>> id(tuple1)
4302721352
>>> tuple3 = tuple1
>>> id(tuple3)
4302721352
>>> id(tuple1)
4302721352

```
    
##### List Methods
* list.append(x)
```
>>> t = ['a', 'b', 'c']
>>> t.append('d')
>>> print t
['a', 'b', 'c', 'd']
```
* list.extend(list2)
```
>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> print t1
['a', 'b', 'c', 'd', 'e']
```
* list.insert(index, x)
* list.remove(x)
```
>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> print t
['a', 'c']
```
* list.pop([i]): by default, it pop the last element in the list 
```
>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> print t
['a', 'c']
>>> print x
b
```
* list.index(x)
```
>>> list
[12, 56, 'good']
>>> 
>>> list.index(56)
1
```
* list.count(x)
```
>>> list
[12, 56, 'good']
>>> 
>>> list.count(12)
1
```
* list.sort()
```
>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> print t
['a', 'b', 'c', 'd', 'e']
```
* list.reverse()
```
[66.25, -1, 333, 1, 1234.5, 333]
>>> a.reverse()
>>> a
[333, 1234.5, 1, 333, -1, 66.25]
```
* del element 
```
>>> t = ['a', 'b', 'c']
>>> del t[1]
>>> print t
['a', 'c']
```

##### List and strings
* strings --> list: new_list = list(strings)
* list --> string: new_string = ' '.join(list)
* A string is a sequence of characters and a list is a sequence of values, but a list of characters is not the same as a string. To convert from a string to a list of characters, you can use list:
```python
>>> s = 'spam'
>>> t = list(s)
>>> print t
['s', 'p', 'a', 'm']
```
* Because list is the name of a built-in function, you should avoid using it as a variable name. I also avoid l because it looks too much like 1. So that’s why I use t.
The list function breaks a string into individual letters. If you want to break a string into words, you can use the split method:
```
>>> s = 'pining for the fjords'
>>> t = s.split()
>>> print t
['pining', 'for', 'the', 'fjords']
```
* An optional argument called a delimiter specifies which characters to use as word boundaries. The following example uses a hyphen as a delimiter:
```
>>> s = 'spam-spam-spam'
>>> delimiter = '-'
>>> s.split(delimiter)
['spam', 'spam', 'spam']
```
* join is the inverse of split. It takes a list of strings and concatenates the elements. join is a string method, so you have to invoke it on the delimiter and pass the list as a parameter:
```
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> delimiter.join(t)
'pining for the fjords'
```
* In this case the delimiter is a space character, so join puts a space between words. To concatenate strings without spaces, you can use the empty string, '', as a delimiter.

##### Objects and valuse



####2. Tuples 
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

##### Advantage 
* Tuple 比 list 操作速度快。如果您定义了一个值的常量集，并且唯一要用它做的是不断地遍历它，请使用 tuple 代替 list。
* 如果对不需要修改的数据进行 “写保护”，可以使代码更安全。使用 tuple 而不是 list 如同拥有一个隐含的 assert 语句，说明这一数据是常量。如果必须要改变这些值，则需要执行 tuple 到 list 的转换 (需要使用一个特殊的函数)。
* 还记得我说过 dictionary keys 可以是字符串，整数和 “其它几种类型”吗？Tuples 就是这些类型之一。Tuples 可以在 dictionary 中被用做 key，但是 list 不行。实际上，事情要比这更复杂。Dictionary key 必须是不可变的。Tuple 本身是不可改变的，但是如果您有一个 list 的 tuple，那就认为是可变的了，用做 dictionary key 就是不安全的。只有字符串、整数或其它对 dictionary 安全的 tuple 才可以用作 dictionary key。

##### Reference
* http://www.tutorialspoint.com/python/python_tuples.htm
* https://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences
* http://woodpecker.org.cn/diveintopython/native_data_types/tuples.html


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

