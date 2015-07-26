### Definition
#### Atomic Operations 
      * An atomic operation is an operation that is carried out in a single execution step, without any chance that another thread gets control.

#### Mutual Exclusion
1. In computer science, mutual exclusion refers to the requirement of ensuring that no two concurrent processes are in their critical section at the same time; it is a basic requirement in concurrency control, to prevent race conditions.
2. Binary semaphores can provide mutual exclusion

#### Condition Variable
1. A condition variable is basically a container of threads that are waiting on a certain condition. 

2. A condition variable represents some condition that a thread can:
      * Wait on, until the condition occurs; or
      * Notify other waiting threads that the condition has occurred

3.  A condition variable is always associated with some kind of lock; this can be passed in or one will be created by default. 

4.  A condition variable has ```acquire()``` and ```release()``` methods that call the corresponding methods of the associated lock. It also has a ```wait()``` method, and ```notify()``` and ```notifyAll()``` methods. These three must only be called when the calling thread has acquired the lock, otherwise a RuntimeError is raised.

5. Three operations:
      * wait()
          The wait() method releases the lock, and then blocks until it is awakened by a notify() or notifyAll() call for the same condition variable in another thread. Once awakened, it re-acquires the lock and returns. It is also possible to specify a timeout.
      * notify()
      * notifyAll()
          
#### Details for Condition Variable
```python
# Consume one item
cv.acquire()
while not an_item_is_available():
    cv.wait()
get_an_available_item()
cv.release()

# Produce one item
cv.acquire()
make_an_item_available()
cv.notify()
cv.release()
```
* wait c, m, where c is a condition variable and m is a mutex (lock) associated with the monitor. This operation is called by a thread that needs to wait until the assertion P_c is true before proceeding. While the thread is waiting, it does not occupy the monitor. The function, and fundamental contract, of the "wait" operation, is to do the following steps:
* first:
      * 1.  release the mutex m
      * 2.  move this thread from the "ready queue" to c's "wait-queue" (a.k.a. "sleep-queue") of threads, and
      * 3.  sleep this thread.  (Context is synchronously yielded to another thread.)
* Second:
      * Once this thread is subsequently notified/signalled (see below) and resumed, then automatically re-acquire the mutex m.
* As a design rule, multiple condition variables can be associated with the same mutex, but not vice versa.

#### Producer Consumer using Condition Variable 

```python
# Reference:
# http://agiliq.com/blog/2013/10/producer-consumer-problem-in-python/
# https://en.wikipedia.org/wiki/Monitor_(synchronization)

'''
For consumer, we check if the queue is empty before consuming.
If yes then call wait() on condition instance.
wait() blocks the consumer and also releases the lock associated with the condition. 
This lock was held by consumer, so basically consumer loses hold of the lock.
Now unless consumer is notified, it will not run.
Producer can acquire the lock because lock was released by consumer.
Producer puts data in queue and calls notify() on the condition instance.
Once notify() call is made on condition, consumer wakes up. But waking up doesn't mean it starts executing.
notify() does not release the lock. Even after notify(), lock is still held by producer.
Producer explicitly releases the lock by using condition.release().
And consumer starts running again. Now it will find data in queue and no IndexError will be raised.
'''

import threading
import time
import random
from threading import Thread
from threading import Condition

queue = []
MAX_NUM = 10
condition = Condition()

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print "Queue is full, producer is waiting"
                condition.wait()
                print "Space in queue, Consumer notified the producer"

            num = random.choice(nums)
            queue.append(num)
            print "Produced", num
            condition.notify()  # http://www.eecs.harvard.edu/~mdw/course/cs61/mediawiki/images/7/7e/Lectures-semaphores.pdf
            '''
            Notice here: if we use 
            if len(queue) == 1:
               condition.notify() 
            will have the issue, since If two threads call consume(), then two threads call produce(),
            only one will wake up !
            we could use the above method or use
            if len(queue) == 1:
               condition.notifyAll()
            '''
            condition.release()
            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        while True:
            condition.acquire()
            if not queue:
                print "Nothing in the queue, consumer is waiting"
                condition.wait()
                print "Produce added something to queue, notified the consumer"
            num = queue.pop()
            print "Consumed: ", num
            condition.notify()
            condition.release()
            time.sleep(random.random())
            
def main():
    try:
        ProducerThread().start()
        ConsumerThread().start()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
```

#### Queue

```python

'''
In place of list, we are using a Queue instance(hereafter queue).
queue has a Condition and that condition has its lock. You don't need to bother about Condition and Lock if you use Queue.
Producer uses put available on queue to insert data in the queue.
put() has the logic to acquire the lock before inserting data in queue.
Also put() checks whether the queue is full. If yes, then it calls wait() internally and so producer starts waiting.
Consumer uses get.
get() acquires the lock before removing data from queue.
get() checks if the queue is empty. If yes, it puts consumer in waiting state.
get() and put() has proper logic for notify() too. Why don't you check the source code for Queue now?
'''

from threading import Thread
import time
import random
from Queue import Queue

queue = Queue(10)

class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print "Produced", num
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print "Consumed", num
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()
```

####  Sequential Outputting using CV
one thread output odd number, one thread output even number 


```python
import threading
import time
import random
from threading import Thread
from threading import Condition

condition = Condition()
isodd = True     

class EvenThread(Thread):
    def run(self):
        global isodd
        for i in xrange(2, 11, 2):
            condition.acquire()
            if isodd:
                condition.wait()
            print "even, i: ", i
            isodd = True
            condition.notify()
            condition.release()    
            time.sleep(random.random())
            
class OddThread(Thread):
    def run(self):
        global isodd
        for i in xrange(1, 10, 2):
            condition.acquire()
            if not isodd:
                condition.wait()
            print "odd, i: ", i
            isodd = False
            condition.notify()
            condition.release()
            time.sleep(random.random())

def main(): 
        OddThread().start()
        EvenThread().start()

if __name__ == '__main__':   
    main()
  
```

#### Daemon Thread 
* Daemons are only useful when the main program is running, and it's okay to kill them off once the other non-daemon threads have exited. Without daemon threads, we have to keep track of them, and tell them to exit, before our program can completely quit. By setting them as daemon threads, we can let them run and forget about them, and when our program quits, any daemon threads are killed automatically.

* Usually our main program implicitly waits until all other threads have completed their work. However, sometimes programs spawn a thread as a daemon that runs without blocking the main program from exiting. Using daemon threads is useful for services where there may not be an easy way to interrupt the thread or where letting the thread die in the middle of its work without losing or corrupting data. To designate a thread as a daemon, we call its setDaemon() method with a boolean argument. The default setting for a thread is non-daemon. So, passing True turns the daemon mode on.
```python
d = threading.Thread(name="daemon", target=daemon)
d.setDaemon(True)

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
```

* Reference: 
* [Reference solution for producer consumer in CV](http://agiliq.com/blog/2013/10/producer-consumer-problem-in-python/)
* http://pymotw.com/2/threading/ 


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


#### Spin Lock
* [Spin Lock](http://stackoverflow.com/questions/5869825/when-should-one-use-a-spinlock-instead-of-mutex)
* [Spin Lock wiki](https://en.wikipedia.org/wiki/Spinlock)

#### Virtual Memory
[Virtual Memory](http://www.tutorialspoint.com/operating_system/os_virtual_memory.htm)

#### Reference:
* [Python Synchronized](http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/)
* [Different Lock vs RLock](http://stackoverflow.com/questions/22885775/what-is-the-difference-between-lock-and-rlock)
* [thread.start and thread.join](http://stackoverflow.com/questions/19138219/use-of-threading-thread-join)
* [Python Synchronized1](http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/)
* [Python Synchronized2](http://effbot.org/zone/thread-synchronization.htm)
* [Python Synchronized3](http://theorangeduck.com/page/synchronized-python)
