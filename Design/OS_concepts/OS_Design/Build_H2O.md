#### Requirement
* If an oxygen thread arrives at the barrier when no hydrogen threads are present, it has to wait for two hydrogen threads.
* If a hydrogen thread arrives at the barrier when no other threads are present, it has to wait for an oxygen thread 
and another hydrogen thread.

#### Barrier

```python
import threading
from threading import BoundedSemaphore

class Barrier:
    def __init__(self):
        turnstile = BoundedSemaphore(0)
        turnstile2 = BoundedSemaphore(1)
        mutex = BoundedSemaphore(1)
        self.count = 0

    def barrier(self):
        mutex.wait()
            self.count += 1
            if self.count == n:
                turnstile2.wait()
                turnstile.signal()
        mutex.signal()

        turnstile.wait()
        turnstile.signal()

        # critical point

        mutex.wait()
            self.count -= 1
            if self.count == 0:
                turnstile.wait()
                turnstile2.signal()
        mutex.signal()
        
        turnstile2.wait()
        turnstile2.signal()
        
```
