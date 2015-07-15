### Definition
#### Atomic Operations 
     * An atomic operation is an operation that is carried out in a single execution step, without any chance that another thread gets control.

#### Mutual Exclusion
     * In computer science, mutual exclusion refers to the requirement of ensuring that no two concurrent processes are in their critical section at the same time; it is a basic requirement in concurrency control, to prevent race conditions.
     * Binary semaphores can provide mutual exclusion

#### Condition Variable
     * A condition variable is basically a container of threads that are waiting on a certain condition. 
     * A condition variable represents some condition that a thread can:
          * Wait on, until the condition occurs; or
          * Notify other waiting threads that the condition has occurred
     * A condition variable is always associated with some kind of lock; this can be passed in or one will be created by default. 
     * A condition variable has ```acquire()``` and ```release()``` methods that call the corresponding methods of the associated lock. It also has a ```wait()``` method, and ```notify()``` and ```notifyAll()``` methods. These three must only be called when the calling thread has acquired the lock, otherwise a RuntimeError is raised.
     * Three operations:
          * wait()
          * notify()
          * notifyAll()
          
#### spin-waiting
     * a mutex is used to protect the critical sections of code and busy-waiting is still used, with the lock being acquired and released in-between each busy-wait check

#### Semaphore
     * A semaphore has an internal counter rather than a lock flag, and it only blocks if more than a given number of threads have attempted to hold the semaphore. 
     * The counter is decremented when the semaphore is acquired, and incremented when the semaphore is released. If the counter reaches zero when acquired, the acquiring thread will block. When the semaphore is incremented again, one of the blocking threads (if any) will run
     * Python’s threading module provides two semaphore implementations:
            * the Semaphore class provides an unlimited semaphore which allows you to call release any number of times to increment the counter. 
            * To avoid simple programming errors, it’s usually better to use the BoundedSemaphore class, which considers it to be an error to call release more often than you’ve called acquire.
     * Counting semaphores can represent a resource with multiple instances (e.g. solving producer/consumer problem)
     * Binary semaphores can provide mutual exclusion (solution of critical section problem)

#### Conditions for a good Mutex solution
      * No two processes may be simultaneously inside their critical regions.
      * No assumptions may be made about speeds or the number of CPUs.
      * No process running outside its critical region may block other processes.
      * No process should have to wait forever to enter its critical region.


### Python Thread Code
#### Lock 用法
```
import threading
lock = threading.Lock()
lock.acquire()
    shared resource  
lock.release()

# For proper operation, it’s important to release the lock even if something goes wrong when accessing the resource. You can use try-finally for this purpose:

lock.acquire()
try:
    ... access shared resource
finally:
    lock.release() # release lock, no matter what
    
# use with statement
with lock:
    access share resource
```

#### Two kinds of Lock: ```threading.Lock() and threading.RLock()```
* RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。
* 注意：如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的锁。

```
>>> lock1 = threading.Lock()
>>> 
>>> lock1.acquire()
True
>>> lock1
<thread.lock object at 0x10e2191b0>
>>> lock1.acquire(0)  # can not acquire multiple times for the same lock 
False
>>> lock1
<thread.lock object at 0x10e2191b0>
>>> 
>>> rlock = threading.RLock()
>>> rlock.acquire()
True
>>> rlock.acquire()
1
>>> rlock
<_RLock owner='MainThread' count=2>
>>> rlock.acquire()
1
>>> rlock
<_RLock owner='MainThread' count=3>  # could acquire multiple times for the same lock, 
>>> rlock.release()                  # but need to release it the same times with acquire 
>>> rlock
<_RLock owner='MainThread' count=2>
>>> rlock.release()
>>> rlock
<_RLock owner='MainThread' count=1>
>>> rlock.release()
>>> rlock
<_RLock owner=None count=0>
```


#### Semaphore
```python
import threading

semaphore = threading.BoundedSemaphore(5)
semaphore.acquire() # decrements the counter
... access the shared resource
semaphore.release() # increments the counter


class Semaphore(threading._Semaphore):
    wait = threading._Semaphore.acquire
    signal = threading._Semaphore.release
    
mutex = Semaphore()
mutex.wait()
mutex.signal()
```



#### Lock
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




#### Reference:
* [Python Synchronized](http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/)
* [Different Lock vs RLock](http://stackoverflow.com/questions/22885775/what-is-the-difference-between-lock-and-rlock)
* [thread.start and thread.join](http://stackoverflow.com/questions/19138219/use-of-threading-thread-join)
* [Python Synchronized1](http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/)
* [Python Synchronized2](http://effbot.org/zone/thread-synchronization.htm)
* [Python Synchronized3](http://theorangeduck.com/page/synchronized-python)
