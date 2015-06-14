##### [Reference](http://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem)

* semaphore_items 表示现在有多少资源可以用
* semaphore_room 表示现在有多少space可以存放资源
* 

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

# Polling Solution: Nultiple-Producer Multiple-Consumer
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


### Producer-consumer 
#### Variables 

```python
mutex = Semaphore(1) # mutex provides exclusive access to the buffer
items = Semaphore(0) # When items is positive, it indicates the number of items in the buffer
                     # When it is negative, it indicates the number of consumer threads in queue.
local event    # event is a local variable, which in this context means that each thread has its own version.
```

#### Version 1




