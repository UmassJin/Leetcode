#### Problem
* 1. Any number of readers can be in the critical section simultaneously.
* 2. Writers must have exclusive access to the critical section.
* 3. a writer cannot enter the critical section while any other thread (reader or writer) is there, and while the writer is there, no other thread
may enter.

```python

import threading
from threading import BoundedSemaphore


'''
The First one turn on the light and the last one turn off.

lock takes one parameter, a semaphore that it will check and possibly hold.
If the semaphore is locked, the calling thread blocks on semaphore and all
subsequent threads block on self.mutex. 

When the semaphore is unlocked,
the first waiting thread locks it again and all waiting threads proceed.
'''

class Lightswitch:
    def __init__(self):
        self.counter = 0
        self.mutex = BoundedSemaphore(1)

    def lock(self, semaphore):
        self.mutex.wait()
            self.counter += 1
            if self.counter == 1:
                semaphore.wait()
        self.mutex.signal()

    def unlock(self, semaphore):
        self.mutex.wait()
            self.counter -= 1
            if self.counter == 0:
                semaphore.signal()
        self.mutex.signal()

# This version works fine, but maybe the writers starve problem 


class ReadWrite:
    def __init__(self):
        _mutex = BoundedSemaphore(1)
        roomEmpty = BoundedSemaphore(1)
        #self.readers = 0
        readLightswitch = Lightswitch()

    def read(self):
        readLightswitch.lock(roomEmpty)
        # critical session
        readLightswitch.unlock(roomEmpty)

    def writers(self):
        roomEmpty.wait()
        # Critical section 
        roomEmpty.signal()


# Version 2
# use the turnstile to aviod the starve writer
# If a writer gets stuck in the turnstile it has the ect of forcing 
# the readers to queue at the turnstile.
'''
When the last reader leaves, it signals roomEmpty, unblocking the waiting
writer. The writer immediately enters its critical section, since none of the
waiting readers can pass the turnstile.
When the writer exits it signals turnstile, which unblocks a waiting thread,
which could be a reader or a writer. Thus, this solution guarantees that at least
one writer gets to proceed, but it is still possible for a reader to enter while
there are writers queued.
'''
class ReadWrite:
    def __init__(self):
        _mutex = BoundedSemaphore(1)
        roomEmpty = BoundedSemaphore(1)
        turnstile = BoundedSemaphore(1)
        readswitch = Lightswitch()

    def read(self):
        turnstile.wait()
        turnstile.signal()

        readLightswitch.lock(roomEmpty)
            # critical session
        readLightswitch.unlock(roomEmpty)

    def writers(self):
        turnstile.wait()
            roomEmpty.wait()
            # Critical section 
        turnstile.signal()

        roomEmpty.signal()

  
  
