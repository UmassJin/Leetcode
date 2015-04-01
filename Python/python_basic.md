###[Sequence Types - str, unicode, list, tuple, bytearray, buffer, xrange] (https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange)
* 1) There are seven sequence types: strings, Unicode strings, lists, tuples, bytearrays, buffers, and xrange objects.
* 2) For other containers see the built in dict and set classes, and the collections module.
* 3) 仔细阅读link 中tutorial 这部分！

* 4) Values of n less than 0 are treated as 0 (which yields an empty sequence of the same type as s). Note also that the copies are shallow; nested structures are not copied. This often haunts new Python programmers; consider:
```python
>>>
>>> lists = [[]] * 3
>>> lists
[[], [], []]
>>> lists[0].append(3)
>>> lists
[[3], [3], [3]]
>>> id(lists[1])
4302991816   # ---> the address are the same
>>> id(lists[0])
4302991816
>>> id(lists[2])
4302991816
```
* 5) What has happened is that ```[[]]``` is a one-element list containing an empty list, so all three elements of ```[[]] * 3``` are (pointers to) this single empty list. Modifying any of the elements of lists modifies this single list. You can create a list of different lists this way:
```python
>>>
>>> lists = [[] for i in range(3)]
>>> id(lists[0])
4302992008    # --->  the address are different 
>>> id(lists[1])
4302992200
>>> id(lists[2])
4302991624
>>> lists[0].append(3)
>>> lists[1].append(5)
>>> lists[2].append(7)
>>> lists
[[3], [5], [7]]
```

``` s[i:j:k]  # slice of s from i to j with step k``` 
* 6) The slice of s from i to j with step k is defined as the sequence of items with index ```x = i + n*k such that 0 <= n < (j-i)/k```. In other words, the indices are ```i, i+k, i+2*k, i+3*k``` and so on, stopping when j is reached (but never including j). If i or j is greater than len(s), use len(s). If i or j are omitted or None, they become “end” values (which end depends on the sign of k). Note, k cannot be zero. If k is None, it is treated like 1.

####1. Strings
##### Definition 
Creat string simply by enclosing characters in quotes. Python treats single quotes the same as double quotes.

##### String slices
* The operator [n:m] returns the part of the string from the “n-eth” character to the “m-eth” character, including the first but excluding the last.
* If we want to get the ith char in the string, the i should not larger than length-1
* But for the string slices, we could use larger than length, since return the empty string '' as following example 
```
>>> string1 = 'hello'
>>> string2 = "world"
>>> string1
'hello'
>>> string2
'world'
>>> string1[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> string1[:6]
'hello'
>>> string1[6:]
''
```

##### String are immutable 
* It is tempting to use the [] operator on the left side of an assignment, with the intention of changing a character in a string. For example:
```
>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
TypeError: 'str' object does not support item assignment
```
* The “object” in this case is the string and the “item” is the character you tried to assign. For now, an object is the same thing as a value, but we will refine that definition later. An item is one of the values in a sequence.
* The reason for the error is that strings are immutable, which means you can’t change an existing string. The best you can do is create a new string that is a variation on the original:
```
>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> print new_greeting
Jello, world!
```

##### Reference
* [Think in Python] (http://www.greenteapress.com/thinkpython/html/thinkpython009.html)
* [Tutorial: String Method] (https://docs.python.org/2/library/stdtypes.html#string-methods)
* [Tutorial: String Formatting Operations](https://docs.python.org/2/library/stdtypes.html#string-formatting)

####2. Lists
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
* strings --> list: ```new_list = list(strings)```
* list --> string: ```new_string = ' '.join(list)```
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

##### Objects and values
* To check whether two variables refer to the same object, you can use the is operator.
* In the string example, Python only created one string object, and both a and b refer to it.
* In the list example, two list have the same value, but different object 
* If use the ```a=b```, list a and list b will have the same address and same value 
* In this case we would say that the two lists are equivalent, because they have the same elements, but not identical, because they are not the same object. If two objects are identical, they are also equivalent, but if they are equivalent, they are not necessarily identical.

```python
>>> a = 'good'
>>> b = 'good'
>>> id(a)
4302757088
>>> id(b)
4302757088
>>> a is b
True
>>> a = [1,2,3]
>>> b = [1,2,3]
>>> id(a)
4302991496
>>> id(b)
4302987208
>>> a is b
False
```

* slicing, s[1:2], based on the 0, include the 1 and exclude 2 
* s == t, equal if all of the characters are the same. s is t ? no guarantee. 
* t = s[:]  # list slices ALWAYS make copies 
* slicing mutable objects ALWAYS makes new objects (list)
  slicing immutable objects entirely MAY or MAY NOT make a new object (tuple)
* t =s   assignments in python NEVER make copies. The association of a variable with an object is called a reference. In this example, there are two references to the same object.An object with more than one reference has more than one name, so we say that the object is aliased.
    
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

##### List Arguments 
* When you pass a list to a function, the function gets a reference to the list. If the function modifies a list parameter, the caller sees the change. For example, delete_head removes the first element from a list:
```
def delete_head(t):
    del t[0]
```
Here’s how it is used:
```
>>> letters = ['a', 'b', 'c']
>>> delete_head(letters)
>>> print letters
['b', 'c']
```
* The parameter t and the variable letters are aliases for the same object. 
* It is important to distinguish between operations that modify lists and operations that create new lists. For example, the append method modifies a list, but the + operator creates a new list:
```
>>> t1 = [1, 2]
>>> t2 = t1.append(3)
>>> print t1
[1, 2, 3]
>>> print t2
None

>>> t3 = t1 + [4]
>>> print t3
[1, 2, 3, 4]
```
* This difference is important when you write functions that are supposed to modify lists. For example, this function does not delete the head of a list:
```
def bad_delete_head(t):
    t = t[1:]              # WRONG!
```
* The slice operator creates a new list and the assignment makes t refer to it, but none of that has any effect on the list that was passed as an argument.
* An alternative is to write a function that creates and returns a new list. For example, tail returns all but the first element of a list:
```
def tail(t):
    return t[1:]
```
This function leaves the original list unmodified. Here’s how it is used:
```
>>> letters = ['a', 'b', 'c']
>>> rest = tail(letters)
>>> print rest
['b', 'c']
```

##### Debugging
* Careless use of lists (and other mutable objects) can lead to long hours of debugging. Here are some common pitfalls and ways to avoid them:

1) Don’t forget that most list methods modify the argument and return None. This is the opposite of the string methods, which return a new string and leave the original alone.
* If you are used to writing string code like this:
```word = word.strip()```
* It is tempting to write list code like this:
```t = t.sort()           # WRONG!```
* Because sort returns None, the next operation you perform with t is likely to fail.

* Before using list methods and operators, you should read the documentation carefully and then test them in interactive mode. The methods and operators that lists share with other sequences (like strings) are documented at http://docs.python.org/2/library/stdtypes.html#typesseq. 
* The methods and operators that only apply to mutable sequences are documented at http://docs.python.org/2/library/stdtypes.html#typesseq-mutable.

2) Pick an idiom and stick with it.
* Part of the problem with lists is that there are too many ways to do things. For example, to remove an element from a list, you can use pop, remove, del, or even a slice assignment.
* To add an element, you can use the append method or the + operator. Assuming that t is a list and x is a list element, these are right:

```
t.append(x)
t = t + [x]
And these are wrong:
t.append([x])          # WRONG!
t = t.append(x)        # WRONG!
t + [x]                # WRONG!
t = t + x              # WRONG!
```
* Try out each of these examples in interactive mode to make sure you understand what they do. Notice that only the last one causes a runtime error; the other three are legal, but they do the wrong thing.

3) Make copies to avoid aliasing.
* If you want to use a method like sort that modifies the argument, but you need to keep the original list as well, you can make a copy.
```
orig = t[:]
t.sort()
```
* In this example you could also use the built-in function sorted, which returns a new, sorted list and leaves the original alone. But in that case you should avoid using sorted as a variable name!


##### Using lists as Stacks
```
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```
##### Using lists as Queues
```
>>> queue = ['hi','how','are','you']
>>> queue
['hi', 'how', 'are', 'you']
>>> queue.append('world')
>>> queue
['hi', 'how', 'are', 'you', 'world']
>>> queue.pop(0)
'hi'
>>> queue
['how', 'are', 'you', 'world']
```
Or
```
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

##### [Functional Programming Tools] (https://docs.python.org/2/tutorial/datastructures.html#functional-programming-tools)
* ```map(function,sequence)```
* ```filter(function, sequence)```
* ```reduce(function, sequence)```
```
>>> def f(x,y): return x*y
... 
>>> map(f, range(3))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes exactly 2 arguments (1 given)
>>> map(f, range(3),range(5))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in f
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
>>> map(f, range(3),range(3))
[0, 1, 4]
```
#####[List Comprehensions] (https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions)
```
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

##### [Nested List Comprehensions] (https://docs.python.org/2/tutorial/datastructures.html#nested-list-comprehensions)
```
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
>>> zip(*matrix)
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```


####3. Tuples 
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

### Basic knowledge 
####1. Use enumerate 
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

####2. Two methods to get the random list
```python
random.shuffle(a_tot)    #get a randomized list
a_1 = a_tot[0:1300]     #pick the first 1300
a_2 = a_tot[1300:]      #pick the last 200

new_t = random.sample(a_tot,len(a_tot))    #get a randomized list
a_1 = new_t[0:1300]     #pick the first 1300
a_2 = new_t[1300:]      #pick the last 200
```
####3. String Method 
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


####4. Build-in function
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
True`
```
``` python
>>> x = [1,2,3]
>>> y = [4,5,6]
>>> zipped = zip(x,y)
>>> zipped
[(1, 4), (2, 5), (3, 6)]
>>> id(x)
4335495864
>>> id(y)
4335495720
>>> a,b = zip(*zipped)
>>> a
(1, 2, 3)
>>> b
(4, 5, 6)
>>> id(a)
4335414080
>>> id(b)
4335287104
>>> y == list(b)
True
```

Usage 
[Reverse Words in a StringII](../Array/Reverse_Words_in_a_StringII.py)

####5. Difference between ```range()``` and ```xrange()```
*  ```xrange(start, stop[, step])```
* This function is very similar to range(), but returns an xrange object instead of a list. This is an opaque sequence type which yields the same values as the corresponding list, without actually storing them all simultaneously. The advantage of xrange() over range() is minimal (since xrange() still has to create the values when asked for them) except when a very large range is used on a memory-starved machine or when all of the range’s elements are never used (such as when the loop is usually terminated with break).
```
=>>> a = range(0,10)
>>> print a 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(a)
<type 'list'>
>>> a = xrange(0,10)
>>> a
xrange(10)
>>> type(a)
<type 'xrange'>
```
* But for the python 3.4, there is NO xrange, only range, return range 
```python
>>> a = range(0,10)
>>> type(a)
<class 'range'>
>>> x = xrange(0,10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'xrange' is not defined
```

#### 6. Reference
[What's new in Python 3](https://docs.python.org/3/whatsnew/3.0.html)

