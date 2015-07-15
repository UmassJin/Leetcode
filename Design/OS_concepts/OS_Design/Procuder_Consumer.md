##### [Reference](http://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem)

* semaphore_items 表示现在有多少资源可以用
* semaphore_room 表示现在有多少space可以存放资源
* _mutex 表示防止多个thread同时修改数值

```python
import random
import time
import threading
from threading import Thread
from threading import Semaphore
from threading import BoundedSemaphore

MAX_SIZE = 10
mutex = threading.Lock()
semaphore_room = BoundedSemaphore(MAX_SIZE)
semaphore_items = Semaphore(0)  # Here we can not use the BoundedSemaphore!
queue = []

class Producer(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            semaphore_room.acquire()
            print "room has space: ",
            with mutex:
                num = random.choice(nums)
                queue.append(num)
                print "produced: ", num
            semaphore_items.release()
            time.sleep(random.random())

class Consumer(Thread):
    def run(self):
        global queue
        while True:
            semaphore_items.acquire()
            with mutex:
                item = queue.pop()
                print "consume item: ", item
            semaphore_room.release()
            time.sleep(random.random())
        
Producer().start()
Consumer().start()

```

```python
from threading import BoundedSemaphore

# Singal-Producer Single-Consumer 
class Buffer:
    def __init__(self):
        semaphore_items = BoundedSemaphore(0)
        semaphore_room = BoundedSemaphore(buffersize)

        buffersize = 10
        self.ibuffer = [0 for in in xrange(buffersize)]
        in = 0
        out = 0

    def produce(self, item):
        semaphore_room.wait()  # 注意， 这里是room.wait()
        ibuffer[in] = item
        in = (in + 1) % buffersize
        semaphore_items.signal() # 注意，这里是items.signal()

    def consume(self):
        semaphore_items.wait()  # 注意，这里是items.wait()
        item = buffer[out]
        out = (out + 1) % buffersize
        semaphore_room.signal()  # 注意，这里是 room.signal()
        return out

# Multiple-Producer Multiple-Consumer
class Buffer:
    def __init__(self):
        semaphore_items = BoundedSemaphore(0)
        semaphore_room = BoundedSemaphore(buffersize)
        _mutex = BoundedSemaphore(1)

        buffersize = 10
        self.ibuffer = [0 for in in xrange(buffersize)]
        in = 0
        out = 0

    def produce(self, item):
        semaphore_room.wait()  # 注意， 这里是room.wait()
        _mutex.wait()
        ibuffer[in] = item
        in = (in + 1) % buffersize
        _mutex.signal()
        semaphore_items.singal()  # 注意，这里是items.signal()
        
        
    def consume(self):
        semaphore_items.wait()   # 注意，这里是items.wait()
        _mutex.wait()
        item = buffer[out]
        out = (out + 1) % buffersize
        _mutex.signal()
        semaphore_room.signal()  # 注意， 这里是room.signal()
        return out

# Polling Solution: Multiple-Producer Multiple-Consumer
class Buffer:
    def __init__(self):
        buffersize = 10
        self.ibuffer = [0 for in in xrange(buffersize)]
        in = 0
        out = 0

    def produce(self, item):
        while (((in + 1) % buffersize) == out):
            sched_yield()

        ibuffer[in] = item
        in = (in + 1) % buffersize

    def consume(self):
        while in == out:
            sched_yield()

        item = buffer[out]
        out = (out + 1) % buffersize
        return out

```



