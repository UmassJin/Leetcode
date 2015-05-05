## Lock
Locks have 2 states: locked and unlocked. 2 methods are used to manipulate them: acquire() and release(). Those are the rules:

if the state is unlocked: a call to acquire() changes the state to locked.
if the state is locked: a call to acquire() blocks until another thread calls release().
if the state is unlocked: a call to release() raises a RuntimeError exception.
if the state is locked: a call to release() changes the state to unlocked().


#### [Reference](http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/)
