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

>>> type(object)  # 3) 
<type 'type'>
>>> object.__class__  # 4) 
<type 'type'>
>>> object.__bases__
()

>>> type.__class__
<type 'type'>
>>> type.__bases__
(<type 'object'>,)

>>> isinstance(object, object)
True
>>> isinstance(type, object)
True

```

* 1), 2) The names of the two primitive objects within Python. Earlier type() was introduced as a way to find the type of an object (specifically, the __class__ attribute). In reality, it is both an object itself, and a way to get the type of another object.
* 3), 4) Exploring <type 'object'>: the type of <type 'object'> is <type 'type'>. We also use the __class__ attribute and verify it is the same as calling type()
* 个人理解：每一个class, 包括class 的instance都是object，例如我们定义 ```i = 2; i = int(2) ```,实际上是定义了int class 的一个instance i, 所以type(i) 相当于 ```i.__class__() ```返回的是 ```type 'int'```. 对于object来说, type(object)是一个type，所以object.__class__是type，而对于type来说，它的type就是它本身，所以它本身的class就是type. 但是它的bases是建立在object上面的，所以在python里面，type和object是相辅相成的。
* These two objects are primitive objects in Python. We might as well have introduced them one at a time but that would lead to the chicken and egg problem - which to introduce first? These two objects are interdependent - they cannot stand on their own since they are defined in terms of each other.

#### 5. Type Object 
* Type and classes are readlly the SAME in Python !!
* Class is Type, Type is Class ! 
* Type objects share the following traits:
      * They are used to represent abstract data types in programs. For instance, one (user defined) object called User might represent all users in a system, another once called int might represent all integers.
      * They can be subclassed. This means you can create a new object that is somewhat similar to exsiting type objects. The existing type objects become bases for the new one.
      * They can be instantiated. This means you can create a new object that is an instance of the existing type object. The existing type object becomes the __class__ for the new object.
      * The type of any type object is <type 'type'>.
      * They are lovingly called types by some and classes by others.

#### 6. Type Or Non-type Test Rule 
##### If an object is an instance of <type 'type'>, then it is a type. Otherwise, it is not a type !! 
* Summarize: 
      1. <type 'object'> is an instance of <type 'type'>.
      2. <type 'object'> is a subclass of no object.
      3. <type 'type'> is an instance of itself.
      4. <type 'type'> is a subclass of <type 'object'>.
      5. There are only two kinds of objects in Python: to be unambiguous let's call these types and non-types. Non-types could be called instances, but that term could also refer to a type, since a type is always an instance of another type. Types could also be called classes, and I do call them classes from time to time.

* For example:

```python
>>> list
<type 'list'>  # the build-in <type 'list'> object
>>> list.__class__  # it's type is <type 'type'>
<type 'type'>
>>> list.__bases__
(<type 'object'>,)
>>> tuple.__class__, tuple.__bases__ 
(<type 'type'>, (<type 'object'>,))
>>> dict.__class__, dict.__bases__
(<type 'type'>, (<type 'object'>,))
>>>
>>> mylist = [1,2,3]
>>> mylist.__class__  # the type of the mylist here is the 'list'
<type 'list'>
```

* 个人理解，对于build-in type比如list，tuple来说，实际上是curate

####  [Class Inheritance](https://docs.python.org/2/tutorial/classes.html#multiple-inheritance)
####  [What's metaclass ?](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python)

