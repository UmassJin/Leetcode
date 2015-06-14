### Asynchronous, without the condition variable 

##### Note: Minimize critical section 
##### This solution is not the asychronous 

```python
# Version 1
class EventManager:
    def __init__(self):
        self._trigger = False
        self.register_callbacks_ = []

    def RegisterForEvent(self, callback_func_):
        if _trigger:
            callback_func_()
        else:
            register_callbacks_.append(callback_func_)

    def TriggerEvent(self):
        _trigger = True
        size = len(register_callbacks_)
        for i in xrange(size):
            register_callbacks_[i]

g_em = EventManager()
def thread1():
    g_em.RegisterForEvent(callback1)
def thread2():
    g_em.RegisterForEvent(callback2)
def thread3():
    g_em.TriggerEvent()
def thread4():
    g_em.RegisterForEvent(callback3)
def thread5():
    g_em.RegisterForEvent(callback4)


# 1. First problem: Race on the vector 
# In the multithreading scenario, if there are two threads call the 
# RegisterForEvent at the same time, then these two threads will 
# save the callback_func_ saved into the same position 

# Version 2
# Event Manager shared by all threads
# Event Manager is thread-safe, can not have any collition 
from threading import Thread, Lock

class EventManager:
    def __init__(self):
        self._mutex = Lock() # Add the mutex to lock the registered_callbacks
        self._trigger = False
        self.register_callbacks_ = []

    def RegisterForEvent(self, callback_func_):
        if _trigger:
            callback_func_()
        else:
            _mutex.acquire() # _mutex.lock() # No race on the vector
            register_callbacks_.append(callback_func_)
            _mutex.release() # _mutex.unlock()

    def TriggerEvent(self):
        _trigger = True
        size = len(register_callbacks_)
        for i in xrange(size):
            register_callbacks_[i]


# 2. Second problem: Register and Trigger happened at the same time
# Scenario: if there is one callback check the trigger, find _trigger is False
# Then trigger_event happened, trigger all the callbacks, 
# So the callback which happened at the same time will be lost, will be never excute 

from threading import Thread, Lock


class EventManager:
    def __init__(self):
        self._mutex_callbacks = Lock() # Add the mutex to lock the registered_callbacks
        self._mutex_trigger = Lock() # Add the mutex to prevent the callback lose 

        self._trigger = False
        self.register_callbacks_ = []

    def RegisterForEvent(self, callback_func_):
        _mutex_trigger.acquire() # _mutex_trigger.lock()
        if _trigger:
            callback_func_()
        else:
            _mutex_callbacks.acquire() # _mutex.lock() # No race on the vector
            register_callbacks_.append(callback_func_)
            _mutex_callbacks.release() # _mutex.unlock()
        _mutex_trigger.release() # _mutex_trigger.unlock()

    def TriggerEvent(self):

        _mutex_trigger.acquire() # _mutex_trigger.lock()
        _trigger = True
        _mutex_trigger.release() # _mutex_trigger.unlock()

        # Read here could not add the lock, since when we release the mutex_trigger
        # then RegisterForEvent coming, this time the _trigger is True 
        size = len(register_callbacks_)
        for i in xrange(size):
            register_callbacks_[i]

# 3. Third problem: after the TriggerEvent has done, then all the next
# EventManager will be serialized, will do one at one time, 
# The other problem is in the RegisterForEvent inside, maybe call the RegisterForEvent again
# Python do not have the reader_writer lock, need to implement 
# https://majid.info/blog/a-reader-writer-lock-for-python/
# http://code.activestate.com/recipes/577803-reader-writer-lock-with-priority-for-writers/

from threading import Thread, Lock

class EventManager:
    def __init__(self):
        self._mutex_callbacks = Lock() # Add the mutex to lock the registered_callbacks
        self._mutex_trigger = Lock() # Add the mutex to prevent the callback lose 

        self._trigger = False
        self.register_callbacks_ = []

    def RegisterForEvent(self, callback_func_):
        ## Change to the reader_lock() here, which means could have multiple readers
        ## But only have one writer !! 
        _mutex_trigger._reader_lock() # _mutex_trigger.lock()
        if _trigger:
            callback_func_()
        else:
            _mutex_callbacks.acquire() # _mutex.lock() # No race on the vector
            register_callbacks_.append(callback_func_)
            _mutex_callbacks.release() # _mutex.unlock()
        _mutex_trigger._reader_unlock() # _mutex_trigger.unlock()

    def TriggerEvent(self):

        _mutex_trigger.acquire() # _mutex_trigger.lock()
        _trigger = True
        _mutex_trigger.release() # _mutex_trigger.unlock()

        # Read here could not add the lock, since when we release the mutex_trigger
        # then RegisterForEvent coming, this time the _trigger is True 
        size = len(register_callbacks_)
        for i in xrange(size):
            register_callbacks_[i]

 ```                          

### Synchronous, with the condition variable 

```
# In the python, we should use the _cv.acquire() instead of
# create the other mutex = Lock()
from threading import Thread, Lock, Condition

class EventManager:
    def __init__(self):
        self._mutex = Lock()
        self._cv = Condition()
        
    def RegisterForEvent(self):
        _mutex.acquire()
        _cv.wait(_mutex)
        _mutex.release()
        callback_func()
        
    def TriggerEvent(self):
        _cv.notify_all()

    
# Problem 1: after trigger event, then when the register callback
# will wait forever 
# Version 2: add the bool _wait to check whether need to wait 
from threading import Thread, Lock, Condition
        
class EventManager:
    def __init__(self):
        self._mutex = Lock()
        self._cv = Condition()
        bool _wait = True
    
    def RegisterForEvent(self):
        _mutex.acquire()
        while _wait:   # Here we use the while instead of the if ! 
            _cv.wait(_mutex) # Unblock the _mutex, add to the block list, sleep
        _mutex.release()
        
        callback_func()
        
    def TriggerEvent(self):
        _mutex.acquire()
        _wait = False
        __mutex.release()
        
        _cv.notify_all()

```

