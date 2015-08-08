##Table of Content
####[1.Strings ](#strings)
####[2.Lists ](#lists)
####[3.Tuples ](#tuples)
####[4.Set](#set)
####[5.Dictionary](#dictionary)
####[6.Basic Knowledge](#basic-knowledge)
####[7.Class Related Knowledge (Important!!)](#class-related-knowledge)
####[8.Sort and Sorted](#sort-and-sorted)
####[9.Collections](#collections)
####[10. Iterator and Generator](#iterator-and-generator)
####[11. Print in format](#print-format)
####[12. File Operation](#file-operation)
####[13. Time Complexity](#time-complexity)
####[14. Decorator](#decorator)
------------------------------------------------------------


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
＊注意区分这里
```python
>>> buf4 = ['']*4
>>> buf4
['', '', '', '']
>>> buf4[0]
''
>>> id(buf4[0])
4334310664   # --> here all the buf4[0] to buf4[3] are the same address, but since the string is immutable
>>> id(buf4[1])
4334310664
>>> id(buf4[2])
4334310664
>>> id(buf4[3])
4334310664
>>> buf4[0] = buf4[0] + 'hello'  #--> so here acturally we add the new string as buf4[0]
>>> buf4
['hello', '', '', '']
>>> id(buf4[0])
4335488384     #---> note: here the address of buf4[0] is different with buf4[1] to buf4[3]
>>> id(buf4[1])
4334310664
>>> id(buf4[2])
4334310664
>>> id(buf4[3])
4334310664

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


| Python Expression |	Definition | Results	| Description
|:---|:---| :---|:---|
| string | str_test = 'abc' | 'abc' | immutable
| list	| list_test = [a,b,c] | [a,b,c]  | mutable
| tuple | tuple_test = 1,2,3 | (1,2,3)  | immutable
| set | set_test =set(['a','b','c']) | python 2.7: set(['a', 'b', 'c']), |
|     | set_test = set('hello') | python 3.4: {'h', 'e', 'l', 'l', 'o'} | mutable
| dict | dict_test = {'a': 1, 'b': 2} | {'a': 1, 'b': 2} | mutable 

* 7) Count

```
>>> string = "hi how are you?"
>>> string.count('h')
2
>>> string.count('y')
1
>>> string.count('i')
1
>>> string.count('b')
0
>>> 
>>> string.count(3)           # Will have errors here !
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected a character buffer object


>>> list = [1,2,3,4,5,6]
>>> list.count(1)
1
>>> list.count(8)
0
>>> list.count('a')
0                              # No errors here !
>>> list.count('b')
0
```

##Strings
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

#### [String Operations example](http://www.tutorialspoint.com/python/python_strings.htm)
* String could use "+" as Concatenation. 

#### Compare reverse the string and reverse the list

```python
>>> str = 'abcdefg'
>>> str[::-1]
'gfedcba'
>>> str = str[::-1]
>>> str
'gfedcba'
>>> strlist = ['a','b','c','d']
>>> strlist.reverse()
>>> strlist
['d', 'c', 'b', 'a']
>>> 
>>> strlist = ['abcdef']
>>> strlist.reverse()
>>> strlist
['abcdef']

```


#### Check Empty 
```
>>> s = ""
>>> not s
True
>>> s = "   "
>>> not s
False
```

* We could use the < and > compare the integer string

```
>>> s1 = '123'
>>> s2 = '321'
>>> s1 > s2
False
>>> s2 > s1
True
>>> 
>>> 
>>> s1 = 'a123'
>>> s2 = '123'
>>> s1 > s2
True
>>> s2 > s1
False
```


##### Reference
* [Think in Python] (http://www.greenteapress.com/thinkpython/html/thinkpython009.html)
* [Tutorial: String Method] (https://docs.python.org/2/library/stdtypes.html#string-methods)
* [Tutorial: String Formatting Operations](https://docs.python.org/2/library/stdtypes.html#string-formatting)

##Lists
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

[Compare link](http://blog.csdn.net/u010141025/article/details/41866281)
    
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
>>> list1 = [1,2]
>>> list2 = [3,4]
>>> str = 'aga'
>>> list1.extend(list2)
>>> list1
[1, 2, 3, 4]
>>> 
>>> list1.extend(str)  # 还可以extend string
>>> list1
[1, 2, 3, 4, 'a', 'g', 'a']
>>> dict
{'ABDEFS': 1}
>>> list1.extend(dict)  # 还可以extend dict 
>>> list1
[1, 2, 3, 4, 'a', 'g', 'a', 'ABDEFS']
>>> 
>>> tuple = 'ab','cd'
>>> tuple
('ab', 'cd')
>>> list1.extend(tuple)  # 还可以extend tuple
>>> list1
[1, 2, 3, 4, 'a', 'g', 'a', 'ABDEFS', 'ab', 'cd']

```
* list.insert(index, x)
* list.remove(x)
* 注意：如果在list里面没有x，那么用remove会出错！
```
>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> print t
['a', 'c']

>>> ilist 
['abd', '..', 'c', 'hello']
>>> ilist.remove('')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
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
Check the LC [Rotate Array](./Array/Rotate_Array.py)

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


##Tuples 
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

## Set 
##### Definition
* A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
* Mutable 
* Create a empty set: 
```a = set() ```
```
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> fruit = set(basket)               # create a set without duplicates
>>> fruit
set(['orange', 'pear', 'apple', 'banana'])
>>> 'orange' in fruit                 # fast membership testing
True
>>> 'crabgrass' in fruit
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')             # s is string type
>>> b = set('alacazam')
>>> a                                  # unique letters in a
set(['a', 'r', 'b', 'c', 'd'])
>>> a - b                              # letters in a but not in b
set(['r', 'd', 'b'])
>>> a | b                              # letters in either a or b
set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
>>> a & b                              # letters in both a and b
set(['a', 'c'])
>>> a ^ b                              # letters in a or b but not both
set(['r', 'd', 'b', 'm', 'z', 'l'])
>>> set_test = set()
>>> t = 123,456,789                   # t is tuple type 
>>> set_test = set(t)
>>> set_test
set([456, 123, 789])
>>> type(t)
<type 'tuple'>
>>>
>>> dict = {'a':1,'b':2}                 # dict is the dictionary type 
>>> set_test = set(dict)
>>> set_test
set(['a', 'b'])

```
* The input parameter should only be list or the string, tuple, the iterate type
```
>>> set_test = set('a','b','c')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set expected at most 1 arguments, got 3
```

##### 注意set的不同定义

* 如果我们要把'hi','hello'放在同一个set里面，不能直接用set('hi')

```python
>>> 
>>> t = set('hi')  ＃如果这么定义，会分开成两个字母！
>>> 
>>> t
set(['i', 'h'])
>>> 
>>> 
>>> list = ['hi','hello']
>>> s = set(list)   ＃ 通过list来定义
>>> s
set(['hi', 'hello'])
>>> 
>>> 
>>> p = {'hi','hello'}  ＃ 可以用大括号来初始化set！
>>> p
set(['hi', 'hello'])
>>> type(p)
<type 'set'>
>>> type(s)
<type 'set'>
>>> type(t)
<type 'set'>
>>> 
>>> 
>>> q = set('hi','hello')  # 注意，set只能有一个input parameter
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: set expected at most 1 arguments, got 2
>>> 

```

##### Operation
add(elem)
Add element elem to the set.

remove(elem)
Remove element elem from the set. Raises KeyError if elem is not contained in the set.

discard(elem)
Remove element elem from the set if it is present.

pop()
Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.

clear()
Remove all elements from the set.

```
>>> string = 'hello world'
>>> testset = set(string)
>>> testset
{'h', 'o', ' ', 'w', 'r', 'l', 'd', 'e'}
>>> testset.add('h')
>>> testset
{'h', 'o', ' ', 'w', 'r', 'l', 'd', 'e'}
>>> testset.add('b')
>>> testset
{'h', 'b', 'o', ' ', 'w', 'r', 'l', 'd', 'e'}
>>> testset.remove('h')
>>> testset
{'b', 'o', ' ', 'w', 'r', 'l', 'd', 'e'}
>>> testset.pop()
'b'
>>> testset.discard('b')
>>> testset
{'o', ' ', 'w', 'r', 'l', 'd', 'e'}
>>> testset.discard('e')
>>> testset
{'o', ' ', 'w', 'r', 'l', 'd'}
>>> testset.remove('e')  # ---> remove will raise the error if there is no member, but discard will not 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'e'
```
* Reference [Tutorial: set] (https://docs.python.org/2/library/stdtypes.html#frozenset)

##Dictionary 
#### Definition 
* dictionary: ```{key:value; key:value }```
* Indexed by keys, which can be any immutable type; strings and numbers can always be keys.
* Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. 
* You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().
* It is best to think of a dictionary as an unordered set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.
* The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.
* The keys() method of a dictionary object returns a list of all the keys used in the dictionary, in arbitrary order (if you want it sorted, just apply the sorted() function to it). To check whether a single key is in the dictionary, use the in keyword.


``` python
>>> words = {'a':1,'b':2}   # String as keys
>>> words
{'a': 1, 'b': 2}

>>> words = {(1,2,3):'hi',(1,2,3):'world'}  # Tuple as keys 
>>> words
{(1, 2, 3): 'world'}    # If there are multiple values map to the same key, will overwrite the first one

>>> words = {[1,2,3]:'hi',[1,2,3]:'world'}   # List can not as keys 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```
* More ways to create the dictionary 

```python
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e
True
```
* In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
```
>>>
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

* When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

```
>>>
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}
```
* The order of the key-value pairs is not the same. In fact, if you type the same example on your computer, you might get a different result. In general, the order of items in a dictionary is unpredictable.

```
>>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> print eng2sp
{'one': 'uno', 'three': 'tres', 'two': 'dos'}
```

#### [Some operations](https://docs.python.org/2/library/stdtypes.html#dict)
```
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'guido': 4127, 'irv': 4127, 'jack': 4098}
>>> tel.keys()
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
```
 * The in operator uses different algorithms for lists and dictionaries. For lists, it uses a search algorithm, as in Section 8.6. As the list gets longer, the search time gets longer in direct proportion. For dictionaries, Python uses an algorithm called a hashtable that has a remarkable property: the in operator takes about the same amount of time no matter how many items there are in a dictionary. I won’t explain how that’s possible, but you can read more about it at http://en.wikipedia.org/wiki/Hash_table.

```python
>>> d = {}
>>> for i in xrange(3):
...     d.setdefault(i, [])
... 
[]
[]
[]
>>> d
{0: [], 1: [], 2: []}
>>> 

#This method returns the key value available in the dictionary and if given key is not available then it will return provided default value.


>>> dic = {'name':'jerry','id':'123','female':'yes'}
>>> dic
{'name': 'jerry', 'female': 'yes', 'id': '123'}
>>> dic.get('name')
'jerry'
>>> 
>>> dic.get('word')
>>> 
>>> dic.get('word',[])
[]
>>> 


```

```
>>> 'one' in eng2sp
True
>>> 'uno' in eng2sp
False
```

####  Explain why the key can not be the mutable type, like list
* Lists can be values in a dictionary, as this example shows, but they cannot be keys. Here’s what happens if you try:

```
>>> t = [1, 2, 3]
>>> d = dict()
>>> d[t] = 'oops'
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: list objects are unhashable
```

* I mentioned earlier that a dictionary is implemented using a hashtable and that means that the keys have to be hashable.
* A hash is a function that takes a value (of any kind) and returns an integer. Dictionaries use these integers, called hash values, to store and look up key-value pairs.
* This system works fine if the keys are immutable. But if the keys are mutable, like lists, bad things happen. For example, when you create a key-value pair, Python hashes the key and stores it in the corresponding location. If you modify the key and then hash it again, it would go to a different location. In that case you might have two entries for the same key, or you might not be able to find a key. Either way, the dictionary wouldn’t work correctly.
* That’s why the keys have to be hashable, and why mutable types like lists aren’t. The simplest way to get around this limitation is to use tuples, which we will see in the next chapter.


#### [Collections.defaultdict!](https://docs.python.org/2/library/collections.html#collections.defaultdict)

```python
>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```
##### When each key is encountered for the first time, it is not already in the mapping; so an entry is automatically created using the default_factory function which returns an empty list. The list.append() operation then attaches the value to the new list. When keys are encountered again, the look-up proceeds normally (returning the list for that key) and the list.append() operation adds another value to the list. This technique is simpler and faster than an equivalent technique using dict.setdefault():

```python
>>> d = {}
>>> for k, v in s:
...     d.setdefault(k, []).append(v)
...
>>> d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

```


#### [Collections OrderedDict!](https://docs.python.org/2/library/collections.html#ordereddict-objects)
##### 1) An OrderedDict is a dictionary subclass that remembers the order in which its contents are added. A regular dict does not track the insertion order, and iterating over it produces the values in an arbitrary order. In an OrderedDict, by contrast, the order the items are inserted is remembered and used when creating an iterator.

```
import collections

print 'Regular dictionary:'
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v

print '\nOrderedDict:'
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print k, v

$ python collections_ordereddict_iter.py

Regular dictionary:
a A
c C
b B
e E
d D

OrderedDict:
a A
b B
c C
d D
e E


```

##### 2) A regular dict looks at its contents when testing for equality. An OrderedDict also considers the order the items were added.

```
import collections

print 'dict       :',
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = {}
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

print 'OrderedDict:',

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = collections.OrderedDict()
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

$ python collections_ordereddict_equality.py

dict       : True
OrderedDict: False

```

##### 3) 注意，在用key, value pair 定义的时候，the order of the key in the OrderedDict is fix, for the following example:

```
>>> from collections import OrderedDict
>>> spamher = OrderedDict(s=6, p=5, a=4, m=3, h=2, e=1, r=0)
>>> spamher
OrderedDict([('h', 2), ('m', 3), ('r', 0), ('s', 6), ('p', 5), ('a', 4), ('e', 1)])
>>> 
>>> list(spamher.keys())
['h', 'm', 'r', 's', 'p', 'a', 'e']
>>> 
>>> spamher = OrderedDict([('s', 6), ('p', 5), ('a', 4), ('m', 3), ('h', 2), ('e', 1), ('r', 0)])
>>> list(spamher.keys())
['s', 'p', 'a', 'm', 'h', 'e', 'r']
>>> 
```

#### 4) [popitem()](http://www.cnblogs.com/abeen/archive/2011/10/10/2205640.html)
* popitem(True): like stack，从queue的尾部弹出
* popitem(False): like queue, 从queue的头部弹出

```
>>> d = OrderedDict([(x,0) for x in range(10)])
>>> d.items()
[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0)]
>>> d.popitem()
(9, 0)
>>> d.popitem()
(8, 0)
>>> d.items()
[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
>>> d.popitem(last=True)
(7, 0)
>>> d.popitem(last=True)
(6, 0)
>>> d.items()
[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
>>> d.popitem(last=False)
(0, 0)
>>> d.popitem(last=False)
(1, 0)
>>> d.items()
[(2, 0), (3, 0), (4, 0), (5, 0)]
>>>
```

#### Reference:
* [Tutorial: Dictionaries](https://docs.python.org/2/tutorial/datastructures.html#dictionaries)
* [Think in Python: Dictionaries] (http://www.greenteapress.com/thinkpython/html/thinkpython012.html)


##Basic knowledge 
####1. Looping Techniques
##### a) Enumerate 
* When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

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
##### b) zip
* To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

```
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print 'What is your {0}?  It is {1}.'.format(q, a)
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```
##### c) reversed()
* To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.

```
>>> for i in reversed(xrange(1,10,2)):
...     print i
...
9
7
5
3
1
```

##### d) sorted()
* To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.

```
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print f
...
apple
banana
orange
pear
```



##### e) Iteritems()
* When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the iteritems() method.

```
>>> dict_test
{'world': 56, 'hello': 23}
>>> for k, v in dict_test.iteritems():
...     print k, v
... 
world 56
hello 23

>>> for k, v in enumerate(dict_test):
...     print k,v
... 
0 world
1 hello
```

##### f) Make a copy
* To change a sequence you are iterating over while inside the loop (for example to duplicate certain items), it is recommended that you first make a copy. Looping over a sequence does not implicitly make a copy. The slice notation makes this especially convenient:

```
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words[:]:  # Loop over a slice copy of the entire list. words[:] will make a copy, s = word will not! 
...     if len(w) > 6:
...         words.insert(0, w)
...
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
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

##### 2) zip(iterable,..)
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
>>>
>>> x = [1,2,3]
>>> y = [4,5,6]
>>> z = [7,8,9]
>>> zipped = zip(x,y,z)
>>> zipped
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
>>> z = [7,8]
>>> zipped = zip(x,y,z)
>>> zipped
[(1, 4, 7), (2, 5, 8)]
```

Usage 
[Reverse Words in a StringII](../Array/Reverse_Words_in_a_StringII.py)

##### 3) divmod 
* Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division. With mixed operand types, the rules for binary arithmetic operators apply. For integers, the result is the same as (a // b, a % b). For floating point numbers the result is (q, a % b), where q is usually math.floor(a / b) but may be 1 less than that. In any case q * b + a % b is very close to a, if a % b is non-zero it has the same sign as b, and 0 <= abs(a % b) < abs(b).

```python
'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
'''
>>> divmod(10,10)
(1, 0)
>>> 
>>> 
>>> divmod(12,10)
(1, 2)

```



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

#### 6. Global variables 
* In the previous example, known is created outside the function, so it belongs to the special frame called ```__main__```. Variables in ```__main__``` are sometimes called global because they can be accessed from any function. Unlike local variables, which disappear when their function ends, global variables persist from one function call to the next.

*It is common to use global variables for flags; that is, boolean variables that indicate (“flag”) whether a condition is true. For example, some programs use a flag named verbose to control the level of detail in the output:

```
verbose = True

def example1():
    if verbose:
        print 'Running example1'
```
* If you try to reassign a global variable, you might be surprised. The following example is supposed to keep track of whether the function has been called:

```
been_called = False

def example2():
    been_called = True         # WRONG
```    

* But if you run it you will see that the value of been_called doesn’t change. The problem is that example2 creates a new local variable named been_called. The local variable goes away when the function ends, and has no effect on the global variable.
* To reassign a global variable inside a function you have to declare the global variable before you use it:

```
been_called = False

def example2():
    global been_called 
    been_called = True
```

* The global statement tells the interpreter something like, “In this function, when I say been_called, I mean the global variable; don’t create a local one.”
* Here’s an example that tries to update a global variable:
```
count = 0

def example3():
    count = count + 1          # WRONG
If you run it you get:
UnboundLocalError: local variable 'count' referenced before assignment
```

* Python assumes that count is local, which means that you are reading it before writing it. The solution, again, is to declare count global.

```
def example3():
    global count
    count += 1
```
*If the global value is mutable, you can modify it without declaring it:
```
known = {0:0, 1:1}

def example4():
    known[2] = 1
```

* So you can add, remove and replace elements of a global list or dictionary, but if you want to reassign the variable, you have to declare it:

```
def example5():
    global known
    known = dict()
```

#### 7. [More on Conditions] (https://docs.python.org/2/tutorial/datastructures.html#more-on-conditions)important!

#### 8. ['_' meaning in the for loop](http://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python)
* '_' has 3 main conventional uses in Python:

1) To hold the result of the last executed statement in an interactive interpreter session. This precedent was set by the standard CPython interpreter, and other interpreters have followed suit

2) For translation lookup in i18n (imported from the corresponding C conventions, I believe)

3) As a general purpose "throwaway" variable name to indicate that part of a function result is being deliberately ignored

#### 9. [Numeric Types - int, float, long, complex](https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex)
*[Numbers](https://docs.python.org/2/tutorial/introduction.html#numbers)

##### plain integers
* Plain integers (called integers) are implemented using long in C, which gives them at least 32 bits of precision. 
* ```sys.maxint``` is always set to the maximum plain integer value for the current platform, the ```minimum``` value is ```-sys.maxint - 1```

```
>>> sys.maxsize
9223372036854775807
>>> sys.maxint
9223372036854775807
>>> type(sys.maxsize)
<type 'int'>
>>> type(sys.maxint+1)
<type 'long'>

>>> -sys.maxsize-1
-9223372036854775808
>>> -sys.maxint-1
-9223372036854775808
>>> type(-sys.maxsize-1)
<type 'int'>
>>> type(-sys.maxsize-2)
<type 'long'>
```


##### long integers
* Long integers have unlimited precision
* [MAX value for long integer](http://stackoverflow.com/questions/9860588/maximum-value-for-long-integer)

##### [floating point numbers](https://docs.python.org/2/library/sys.html#sys.float_info)
* Floating point numbers are usually implemented using double in C
* [How the FLOAT number in memory in C?](http://stackoverflow.com/questions/6910115/how-to-represent-float-number-in-memory-in-c)

##### complex numbers

#### 10. Multiple Assignment! [Important!!] 
##### [First Missing Positive](./Array/First%20Missing%20Positive.py)

```python
a, b = 1, 2
while b < 10:
    print "b: ", b
    a, b = a + b, a
    print "after a: %d b: %d" %(a,b)
    a = a + 1
    print "after2 a: %d b: %d" %(a,b)

# Output:    
b:  2
after a: 3 b: 1
after2 a: 4 b: 1
b:  1
after a: 5 b: 4
after2 a: 6 b: 4
b:  4
after a: 10 b: 6
after2 a: 11 b: 6
b:  6
after a: 17 b: 11
after2 a: 18 b: 11
```
* Note: here, a+b first assign to the a, so a = 3 and then a assign to b, b = 1, right now,
the value of a does not change!
* But then if we do the a = a + 1, the a has change to 3!!!
* Check the multiple assignment in the above leetcode question 
* [Tutorial](https://docs.python.org/2/tutorial/introduction.html#first-steps-towards-programming).)

#### 11. [Yield](http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python)
```python
def generator():
    for i in xrange(3):
        print "i: ", i
        yield i*1
        
test = generator()
print(test)
for j in test:
    print "j: ", j

Output:
[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python yield.py 
<generator object generator at 0x107a10b40>
i:  0
j:  0
i:  1
j:  1
i:  2
j:  2
```

#### 12. Reverse the List 

```
>>> list = [1,2,3,4,5]
>>> list[::-1]
[5, 4, 3, 2, 1]
>>> list[:2:-1]
[5, 4]
>>> list[:2:1]
[1, 2]
>>> list[:-2:1]
[1, 2, 3]
>>> list[:-2:-1]
[5]
>>> list[:2:-1]
[5, 4]
>>> list[:-2:-1]
[5]

>>> for i in xrange(-5,-1,-1):
...     print i 
... 
>>> 
>>> for i in xrange(-5,-1,1):
...     print i 
... 
-5
-4
-3
-2
>>> 
>>> for i in xrange(5,1,1):
...     print i 
... 
>>> for i in xrange(5,1,-1):
...     print i 
... 
5
4
3
2
```

#### 13. [Lambda usage](http://www.secnetix.de/olli/Python/lambda_functions.hawk)
##### Python supports a style of programming called functional programming where you can pass functions to other functions to do stuff

##### [Usage Example](https://github.com/UmassJin/Leetcode/blob/master/Array/Evaluate_Reverse_Polish_Notation.py)

##### Format 

```python
def func(x): return x**2
print func(6)

g = lambda x: x **2   # Do not need to include "return" statement 
print g(8)
```

##### [With ```map(), filter() and reduce() ```](http://www.python-course.eu/lambda.php)
1. map(func, seq)
```
>>> Celsius = [39.2, 36.5, 37.3, 37.8]
>>> Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
>>> print Fahrenheit
[102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]
>>> C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
>>> print C
[39.200000000000003, 36.5, 37.300000000000004, 37.799999999999997]
>>> 

>>> a = [1,2,3,4]
>>> b = [17,12,11,10]
>>> c = [-1,-4,5,9]
>>> map(lambda x,y:x+y, a,b)
[18, 14, 14, 14]
>>> map(lambda x,y,z:x+y+z, a,b,c)
[17, 10, 19, 23]
>>> map(lambda x,y,z:x+y-z, a,b,c)
[19, 18, 9, 5]
```

2. filter(function, seq)
```python
>>> fib = [0,1,1,2,3,5,8,13,21,34,55]
>>> result = filter(lambda x: x % 2, fib)
>>> print result
[1, 1, 3, 5, 13, 21, 55]
>>> result = filter(lambda x: x % 2 == 0, fib)
>>> print result
[0, 2, 8, 34]
>>>   
```

3. reduce(function, seq)

If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:
* At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
* In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
* Continue like this until just one element is left and return this element as the result of reduce()

#### 14. [Why we do not need to specific type in Python?](http://stackoverflow.com/questions/2489669/function-parameter-types-in-python)

#### 15. [AND operation] (https://docs.python.org/2/reference/expressions.html#boolean-operations) 
* In the context of Boolean operations, and also when expressions are used by control flow statements, the following values are interpreted as false: False, None, numeric zero of all types, and empty strings and containers (including strings, tuples, lists, dictionaries, sets and frozensets). All other values are interpreted as true. 
* The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.
* (Note that neither and nor or restrict the value and type they return to False and True, but rather return the last evaluated argument. This is sometimes useful, e.g., if s is a string that should be replaced by a default value if it is empty, the expression s or 'foo' yields the desired value. Because not has to invent a value anyway, it does not bother to return a value of the same type as its argument, so e.g., not 'foo' yields False, not ''.)
* For example
```python
>>> liveHR = [1,2,3,4,5]
>>> len(liveHR)
5
>>> len(liveHR) and liveHR[-1]
5
>>> liveHR[-1]
5
>>> len(liveHR) and liveHR[1]
2
>>> len(liveHR) and liveHR[2]
3
>>> len(liveHR) and liveHR[3]
4
>>> len(liveHR) and liveHR[0]
1
>>> s = []
>>> len(s)
0
>>> len(s) and liveHR[0]
0
>>> 
>>> len(s) and liveHR[1]
0
>>> len(s) and liveHR[2]
0
>>> s = [1]
>>> len(s) and liveHR[2]
3
>>> len(s) and liveHR[1]
2
>>> 
>>> 
>>> liveHR[1] and len(s)
1
>>> liveHR[3] and len(s)
1
```

#### 16. Reference

* [What's new in Python 3](https://docs.python.org/3/whatsnew/3.0.html)
* [Tutorial: Python Build-in function](https://docs.python.org/2/library/functions.html#)
* [Tutorial: Data Structure](https://docs.python.org/2/tutorial/datastructures.html#sets)
* http://blog.csdn.net/u010141025/article/details/41866281

## Class Related Knowledge
#### 1. Basic concepts in OOP: Abstraction, Polymorphism, Encapsulation, Inheritance 
    * The abstraction is simplifying complex reality by modeling classes appropriate to the problem. The polymorphism is the process of using an operator or function in different ways for different data input. The encapsulation hides the implementation details of a class from other objects. The inheritance is a way to form new classes using classes that have already been defined.

#### 2. Class Attributes
* Basic configuration

```python
#!/usr/bin/python

# initialize.py


class Cat:
   def __init__(self, name):
      self.name = name


missy = Cat('Missy')
lucky = Cat('Lucky')

print missy.name
print lucky.name
```
* In this code example, we have a Cat class. The special method __init__() is called automatically right after the object has been created. Each method in a class definition begins with a reference to the instance object. It is by convention named self. There is nothing special about the self name. We could name it this, for example. The name is the argument. The value is passed during the class instantiation.

* The atributes can be assigned dynamically, not just during initialization. This shows the next example.

```python
#!/usr/bin/python

# dynamic.py

class Dynamic:
   pass

d = Dynamic()
d.name = "Dynamic"
print d.name

# Output:
$ ./dynamic.py 
Dynamic
```
* So far, we have been talking about the instance attributes. In Python there are also so called class object attributes. Class object attributes are same for all instances of a class.

```python
# cat.py

class Cat:
   species = 'mammal'

   def __init__(self, name, age):
      self.name = name
      self.age = age


missy = Cat('Missy', 3)
lucky = Cat('Lucky', 5)

print missy.name, missy.age
print lucky.name, lucky.age

print Cat.species
print missy.__class__.species   # Two ways to access the class object attributes
print lucky.__class__.species
```

#### 3. Class Methods
* In Python, we can call methods in two ways. There are bounded and unbounded method calls.
* [bound, unbound, static](http://stackoverflow.com/questions/114214/class-method-differences-in-python-bound-unbound-and-static)

```python

class Methods:
   def __init__(self):
      self.name = 'Methods'

   def getName(self):
      return self.name


m = Methods()

print m.getName()   # Bounded method call
print Methods.getName(m) # Unbounded method call 
```

* [Special Methods](http://zetcode.com/lang/python/oop/)


```python

#!/usr/bin/python

# book.py

class Book:
   def __init__(self, title, author, pages):
      print "A book is created"
      self.title = title
      self.author = author
      self.pages = pages

   def __str__(self):
      return "Title:%s , author:%s, pages:%s " % \
              (self.title, self.author, self.pages)

   def __len__(self):
      return self.pages

   def __del__(self):
      print "A book is destroyed"


book = Book("Inside Steve's Brain", "Leander Kahney", 304)

print book  
# The print keyword calls the __str__() method. This method should return an informal string representation of an object.

print len(book)
# The len() function invokes the __len__() method. In our case, we print the number of pages of our book.

del book
# The del keyword deletes an object. It calls the __del__() method.
```

#### 4. Object and Type
##### 1. Everything is an object 
* Any classes that we define are objects, and of course, instances of those classes are objects as well.

``` python
>>> two = 2  # 1
>>> type(two)  # 3
<type 'int'>
>>> two.__class__  # 3 
<type 'int'>
>>> 
>>> type(type(two))
<type 'type'>
>>> type(two).__class__ 
<type 'type'>
>>> int
<type 'int'>
>>> type(int)
<type 'type'>
>>>  
>>> i = int(3)  # 2
>>> type(i)
<type 'int'>
>>> type(3)
<type 'int'>
>>> i.__class__
<type 'int'>
```
* Note 1), 2), we create the python in_build int instance, the type of these instance is 'int' 
* Note 3), In Python, the type of an object is represented by the class used to build the object: that is, in Python the word type has the same meaning of the word class.

``` python
>>> object  # 1) 
<type 'object'>
>>> type    # 2) 
<type 'type'>

>>> type(object)  3) 
<type 'type'>
>>> object.__class__  4) 
<type 'type'>
>>> object.__bases__
()

>>> type.__class__
<type 'type'>
>>> type.__bases__
(<type 'object'>,)
```

* 1), 2) The names of the two primitive objects within Python. Earlier type() was introduced as a way to find the type of an object (specifically, the __class__ attribute). In reality, it is both an object itself, and a way to get the type of another object.
* 3), 4) Exploring <type 'object'>: the type of <type 'object'> is <type 'type'>. We also use the __class__ attribute and verify it is the same as calling type()



####  [Class Inheritance](https://docs.python.org/2/tutorial/classes.html#multiple-inheritance)
####  [What's metaclass ?](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python)


## Memory Leak 
* [Tracking Python Memory Leak](http://www.lshift.net/blog/2008/11/14/tracing-python-memory-leaks/)
* Memory Leak Scenario 
 1. some low level C library is leaking
 2. your Python code have global lists or dicts that grow over time, and you forgot to remove the objects after use
 3. there are some reference cycles in your app

* [Different Method](http://python.dzone.com/articles/diagnosing-memory-leaks-python)


## Sort and Sorted 
#### Python lists have a built-in sort() method that modifies the list in-place and a sorted() built-in function that builds a new sorted list from an iterable.

#### Sorted 
```python
sorted(data, cmp=None, key=None, reverse=False) 
```

* data是待排序数据，可以使List或者iterator
* cmp和key都是函数，这两个函数作用与data的元素上产生一个结果，sorted方法根据这个结果来排序。 
* cmp(e1, e2) 是带两个参数的比较函数, 返回值: 负数: e1 < e2, 0: e1 == e2, 正数: e1 > e2. 默认为 None, 即用内建的比较函数. 
* key 是带一个参数的函数, 用来为每个元素提取比较值. 默认为 None, 即直接比较每个元素. 通常, key 和 reverse 比 cmp 快很多, 因为对每个元素它们只处理一次; 而 cmp 会处理多次.

```python
>>> students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10),]  
>>> 
>>> sorted(students, key = lambda student: student[2])
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(students, cmp = lambda x,y: cmp(x[2], y[2]))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> 
>>> from operator import itemgetter, attrgetter
>>> sorted(students, key = itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(students, key = itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
>>> 
>>> d = {'data1':3, 'data2':1, 'data3':2, 'data4':4} 
>>> sorted(d.iteritems(), key=itemgetter(1), reverse = True)
[('data4', 4), ('data1', 3), ('data3', 2), ('data2', 1)]
>>> sorted(d, key=itemgetter(1))
['data4', 'data1', 'data3', 'data2']
>>> sorted(d.iteritems(), key=itemgetter(1))
[('data2', 1), ('data3', 2), ('data1', 3), ('data4', 4)]

>>> num1
[8, 7, 6, 5]
>>> 
>>> 
>>> num1[:4].sort()
>>> num1
[8, 7, 6, 5]  # 注意这里num1不会改变，因为num1[:4]是给num1进行了copy，然后再sort copy之后的list，不是原来的list !
>>> num1[:].sort()
>>> num1
[8, 7, 6, 5]
>>> p = num1[:3]
>>> p.sort()
>>> p
[6, 7, 8]

```
#### Example
* [Create Largest Number](https://github.com/UmassJin/Leetcode/blob/master/Array/Create_Largest_Number.py)

##### String Sort
* 对于string来说，不能用strs.sort(), 但是可以用sorted(strs), 返回一个string的list
* 

```
>>> 
>>> strs = 'hello'
>>> sorted(strs)
['e', 'h', 'l', 'l', 'o']
>>> 
>>> 
>>> strs.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'sort'
>>> strs
'hello'
>>>
# 与list相比较，list可以用sorted() 和list.sort()，后者是in-space sort, 前者是返回一个新的list
>>> list = [1,3,7,2,4,5]
>>> list.sort()
>>> list
[1, 2, 3, 4, 5, 7]
>>> 
>>> 
>>> list = [1,3,7,2,4,5]
>>> sorted(list)
[1, 2, 3, 4, 5, 7]
>>> 
>>> list
[1, 3, 7, 2, 4, 5]
```

#### Related Leetcode Questions
* [Create Largest Number](https://github.com/UmassJin/Leetcode/blob/master/Array/Create_Largest_Number.py)

#### Reference
* [Sorted and Sorted 详解](http://gaopenghigh.iteye.com/blog/1483864)
* [Python Tutorial](https://wiki.python.org/moin/HowTo/Sorting)


## Collections 
### [Collections Counter](http://pymotw.com/2/collections/counter.html)
#### Initializing
```
import collections

print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print collections.Counter({'a':2, 'b':3, 'c':1})
print collections.Counter(a=2, b=3, c=1)

$ python collections_counter_init.py
Counter({'b': 3, 'a': 2, 'c': 1})
Counter({'b': 3, 'a': 2, 'c': 1})
Counter({'b': 3, 'a': 2, 'c': 1})
```

#### Update 
```

import collections

c = collections.Counter()
print 'Initial :', c

c.update('abcdaab')
print 'Sequence:', c

c.update({'a':1, 'd':5})
print 'Dict    :', c


$ python collections_counter_update.py
Initial : Counter()
Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
Dict    : Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})
# The count values are increased based on the new data, rather than replaced. In this example, the count for a goes from 3 to 4.

```

#### Arithmetic

```
import collections

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print 'C1:', c1
print 'C2:', c2

print '\nCombined counts:'
print c1 + c2

print '\nSubtraction:'
print c1 - c2

print '\nIntersection (taking positive minimums):'
print c1 & c2

print '\nUnion (taking maximums):'
print c1 | c2

$ python collections_counter_arithmetic.py

C1: Counter({'b': 3, 'a': 2, 'c': 1})
C2: Counter({'a': 2, 'b': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 1, 't': 1})

Combined counts:
Counter({'a': 4, 'b': 4, 'c': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 1, 't': 1})

Subtraction:
Counter({'b': 2, 'c': 1})

Intersection (taking positive minimums):
Counter({'a': 2, 'b': 1})

Union (taking maximums):
Counter({'b': 3, 'a': 2, 'c': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 1, 't': 1})

```

## Iterator and Generator
### Introduction
```python
class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
```        
* The __iter__ method is what makes an object iterable. Behind the scenes, the iter function calls __iter__ method on the given object.
* The return value of __iter__ is an iterator. It should have a next method and raise StopIteration when there are no more elements.
* Check the following link for more information

#### yield
#### Two usages in Google interview experience 

#### Reference
* http://anandology.com/python-practice-book/iterators.html
* https://docs.python.org/3/tutorial/classes.html#iterators


## [Print Format](https://docs.python.org/2/tutorial/inputoutput.html)
* This example demonstrates the str.rjust() method of string objects, which right-justifies a string in a field of a given width by padding it with spaces on the left. There are similar methods str.ljust() and str.center(). These methods do not write anything, they just return a new string. If the input string is too long, they don’t truncate it, but return it unchanged; this will mess up your column lay-out but that’s usually better than the alternative, which would be lying about a value. (If you really want truncation you can always add a slice operation, as in x.ljust(n)[:n].)

```python
>>> for x in range(1, 11):
...     print repr(x).rjust(2), repr(x*x).rjust(3),
...     # Note trailing comma on previous line
...     print repr(x*x*x).rjust(4)
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

>>> for x in range(1,11):
...     print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

## File Operation 

```python
        fullname = os.path.join(self.dirname, key)
        try:
            with open(fullname) as f:
                return f.read()
        except IOError:
            raise KeyError(key)
```


## Time Complexity

#### 1000 in dict.keys(): O(n)
#### 1000 in dict: O(1)

* d.keys() returns a list which is a copy of the dict keys, not a view. Constructing that list takes O(n), as does the lookup, which uses list.__contains__ i.e. iterating the keys.
her hand, key in d essentially calls

* d.__contains__(key)
* The method dict.__contains__ is implemented efficiently with an O(1) hash lookup on the dict keys. This is precisely the raison d'être for the dict data structure, and it is the same reason you get a fast O(1) lookup when you access a dict with d[key].

* In summary, key in d.keys() is never appropriate in python 2.

## Space usage 
#### When the empty dictionay is created, it started with 8 slots(hash, key, value), looks details in the following link
http://stackoverflow.com/questions/327311/how-are-pythons-built-in-dictionaries-implemented

#### Reasign the size when there are 2/3 full in dictionary 

Good Video about the dictionary:
https://www.youtube.com/watch?v=C4Kc8xzcA68

#### Reference
* [Python time complexity wiki](https://wiki.python.org/moin/TimeComplexity)
* http://stackoverflow.com/questions/24540975/why-does-key-in-d-keys-finish-in-on-time-while-key-in-d-finishes-in-o1?lq=1



## Decorator

```python
>>> def outer1():
...     def inner1():
...             print "inside inner1"
...     return inner1()
... 
>>> foo = outer1()
inside inner1
>>> 
>>> def outer():
...     x = 1
...     def inner():
...             print x
...     return inner()
... 
>>> foo = outer()
1
>>> foo = outer()
1

>>> import random
>>> random.random()
0.6539368726060638
>>> 
>>> 
>>> def outer():
...     x = random.random()
...     def inner():
...             print x
...     return inner()
... 
>>> outer()
0.0717367602537
>>> 
>>> outer()
0.40143942734
>>> outer()
0.134812035114
>>> outer()
0.280289368236
>>> 

```

#### Reference
* [12 步骤搞定Decorator](http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=209540854&idx=1&sn=0b7a85228126842a493adb1ff44c57bb&scene=5#rd)
