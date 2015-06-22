### Static Method
* 定义 staticmethod在一个类中，有时你可能需要写一个属于这个类的方法，但是这些代码完全不会使用到实例对象本身，
这个例子中，如果把_mix_ingredients作为非静态方法同样可以运行，但是它要提供self参数，而这个参数在方法中根本不会被使用到
* 类对象和实例都可以调用静态方法
* 好处:
    * 1. Python不再需要为Pizza对象实例初始化一个绑定方法，绑定方法同样是对象，但是创建他们需要成本，而静态方法就可以避免这些
    * 2. 可读性更好的代码，看到@staticmethod我们就知道这个方法并不需要依赖对象本身的状态。
    * 3. 可以在子类中被覆盖，如果是把mix_ingredients作为模块的顶层函数，那么继承自Pizza的子类就没法改变
         pizza的mix_ingredients了如果不覆盖cook的话。

```python
class Pizza(object):
   @staticmethod
   def mix_ingredients(x, y):
       return x + y
   def cook(self):
       return self.mix_ingredients(self.cheese, self.vegetables)
```

```python
class Pizza(object):
   def __init__(self, cheese, vege ):
        self.cheese = cheese
        self.vegetables = vege

   @staticmethod
   def mix_ingredients(x, y):       
       return x + y

   def cook(self):
       return self.mix_ingredients(self.cheese, self.vegetables)

class Test(Pizza):
    def cook(self):
        print "cook2"
    
p1 = Pizza(2,6)
p2 = Test(2,6)
print p1.cook()
print p2.cook() 
```

```
class Date:
  def __init__(self, month, day, year):
    self.month = month
    self.day   = day
    self.year  = year

  def display(self):
    return "{0}-{1}-{2}".format(self.month, self.day, self.year)

  @staticmethod
  def millenium(month, day):  # 定义一个staticmethod，我们不需要给定self，
    return Date(month, day, 2000)

new_year = Date(1, 1, 2013)               # Creates a new Date object
millenium_new_year = Date.millenium(1, 1) # also creates a Date object. 

# Proof:
print new_year.display()           # "1-1-2013"
print millenium_new_year.display() # "1-1-2000"

print isinstance(new_year, Date) # True
print isinstance(millenium_new_year, Date) # True


print "DateTime"

class DateTime(Date):
  def display(self):
      return "{0}-{1}-{2} - 00:00:00PM".format(self.month, self.day, self.year)

  #@staticmethod
  #def millenium(month, day):
  #    print "this is DateTime method"  
  #    return DateTime(12,12,1988)

datetime1 = DateTime(10, 10, 1990)
datetime2 = DateTime.millenium(10, 10)

print isinstance(datetime1, Date) # True
print isinstance(datetime1, DateTime) # True
print isinstance(datetime2, DateTime) 
# False, here if we did not re-write the millenium method, return Date instance, if re-write, return DateTime method 
print isinstance(datetime2, Date)  # True

datetime1.display() # returns "10-10-1990 - 00:00:00PM"
datetime2.display()
```

### Class Method
* 类方法不是绑定到对象上，而是绑定在类上的方法。
* 无论你用哪种方式访问这个方法，它总是绑定到了这个类身上，它的第一个参数是这个类本身（记住：类也是对象）。

* 应用:
    * 什么时候使用这种方法呢？类方法通常在以下两种场景是非常有用的：
    * 工厂方法：它用于创建类的实例，例如一些预处理。如果使用@staticmethod代替，那我们不得不硬编码Pizza类名在函数中，
    这使得任何继承Pizza的类都不能使用我们这个工厂方法给它自己用。
    * 调用静态类：如果你把一个静态方法拆分成多个静态方法，除非你使用类方法，否则你还是得硬编码类名。
    使用这种方式声明方法，Pizza类名明永远都不会在被直接引用，继承和方法覆盖都可以完美的工作。

```
class Pizza(object):
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegetables())


class Test(Pizza):
    pass

print Pizza.from_fridge
print Test.from_fridge

[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python classmethod2.py 
<bound method type.from_fridge of <class '__main__.Pizza'>>
<bound method type.from_fridge of <class '__main__.Test'>>
```


#### Refereence
http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner
http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=208412350&idx=1&sn=f71cf671bfb23c3ecd915cc602df43fd&scene=5#rd
