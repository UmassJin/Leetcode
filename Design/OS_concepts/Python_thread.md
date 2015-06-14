## Lock
Locks have 2 states: locked and unlocked. 2 methods are used to manipulate them: acquire() and release(). Those are the rules:

if the state is unlocked: a call to acquire() changes the state to locked.
if the state is locked: a call to acquire() blocks until another thread calls release().
if the state is unlocked: a call to release() raises a RuntimeError exception.
if the state is locked: a call to release() changes the state to unlocked().

#### Creating Threads
```python
>>> import threading
>>> def function(x,y,z):
...     print x, y, z
... 
>>> thread = threading.Thread(target=function, args=[1,2,3])
>>> thread.start()
1 2 3
```
The other way 
```
class Thread(threading.Thread):
    def __init__(self, t, *args):
         threading.Thread.__init__(self, target=t, args=args)
         self.start()

thread = Thread(function, 1, 2, 3)
threads = [Thread(function, i, i, i) for i in range(10)]
```


#### Semaphore

```
import threading

class Semaphore(threading._Semaphore):
    wait = threading._Semaphore.acquire
    signal = threading._Semaphore.release
    
mutex = Semaphore()
mutex.wait()
mutex.signal()
```


#### [Reference](http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/)
