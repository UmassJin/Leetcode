#### Singleton
* Singleton has one purpose: to return the same instance every time it is instanced, like a sort of object-oriented global variable. 
So we need to build a class that does not work like standard classes, which return a new instance every time they are called.


#### Reference:
* [Introduce the metaclass and singleton](http://lgiordani.com/blog/2014/09/01/python-3-oop-part-5-metaclasses/#.VWs59mRVhHw)
* [Different Methods to implement Singleton](http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python)

##### Code:
import threading 

class Solution:
    __lock = threading.Lock()
    __obj = None
    # @return: The same instance of this class every time
    @classmethod
    def getInstance(cls):
        if not cls.__obj:
            with cls.__lock:
                if not cls.__obj:
                    cls.__obj = cls()
        return cls.__obj
