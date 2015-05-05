##### [Reference](http://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem)
```
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
        semaphore_room.wait()
        ibuffer[in] = item
        in = (in + 1) % buffersize
        semaphore_items.signal()

    def consume(self):
        semaphore_items.wait()
        item = buffer[out]
        out = (out + 1) % buffersize
        semaphore_room.signal()
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
        semaphore_room.wait()
        _mutex.wait()
        ibuffer[in] = item
        in = (in + 1) % buffersize
        _mutex.signal()
        semaphore_items.signal()

    def consume(self):
        semaphore_items.wait()
        _mutex.wait()
        item = buffer[out]
        out = (out + 1) % buffersize
        _mutex.signal()
        semaphore_items.signal()
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


