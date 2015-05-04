
## Process
#### Independent process and cooperating process 
* A process is cooperating if it can affect or be affected by the other processes executing in the system.
* Cooperating processes require an interprocess communication (IPC) mechanism that will allow them to exchange data and information. 
* Advantage for the cooperation process: Information sharing, Computation speedup, Modularity, Convenience 
* There are two fundamental models of interprocess communication: shared memory and message passing.

##### Shared memory vs Message passing 
| Share memory | Message passing |
| --- | --- |
| More faster, since message-passing systems are typically implemented using system calls thus require the more time-consuming task of kernel intervention | Message passing is useful for exchanging smaller amounts of data, because no conflicts need be avoided.|
|In shared-memory systems, system calls are required only to establish shared memory regions. Once shared memory is established, all accesses are treated as routine memory accesses, and no assistance from the kernel is required | easier to implement in a distributed system than shared memory | 

##### Shared memory 

＊ To allow producer and consumer processes to run concurrently, we must have available a buffer of items that can be filled by the producer and emptied by the consumer. This buffer will reside in a region of memory that is shared by the producer and consumer processes.

＊ Two types of buffers can be used. The unbounded buffer places no practical limit on the size of the buffer. The consumer may have to wait for new items, but the producer can always produce new items. The bounded buffer assumes a fixed buffer size. In this case, the consumer must wait if the buffer is empty, and the producer must wait if the buffer is full.

##### Message-Passing Systems
* Use the mailbox 

####[ Google Chome Multi-process architecture](https://www.chromium.org/developers/design-documents/multi-process-architecture)
* Browser process
* Renderer process
* plug-in process 


## Process Synchronization

#### [The Critical-Section Problem](http://www.geeksforgeeks.org/g-fact-70/)

* Each process has a segment of code, called a critical section, in which the process may be changing common variables, updating a table, writing a file, and so on. 
* No two processes are executing in their critical sections at the same time. The critical-section problem is to design a protocol that the processes can use to cooperate.
* A solution to the critical-section problem must satisfy the following three requirements:
   1. Mutual exclusion. If process Pi is executing in its critical section, then no other processes can be executing in their critical sections.
   2. Progress. If no process is executing in its critical section and some processes wish to enter their critical sections, then only those processes that are not executing in their remainder sections can participate in deciding which will enter its critical section next, and this selection cannot be postponed indefinitely.
   3. Bounded waiting. There exists a bound, or limit, on the number of times that other processes are allowed to enter their critical sections after a process has made a request to enter its critical section and before that
request is granted.

#### [Atomic Operation](http://www.geeksforgeeks.org/g-fact-57/)
Hardware support: atomic operations (test-and-set, compare-and-swap, fetch-and-add etc.)

#### Mutex Locks
* A process must acquire the lock before entering a critical section; it releases the lock when it exits the critical section. The acquire()function acquires the lock, and the release() function releases the lock

#### Spinlock
* The main disadvantage of the implementation given here is that it requires busy waiting. While a process is in its critical section, any other process that tries to enter its critical section must loop continuously in the call to acquire(). In fact, this type of mutex lock is also called a spinlock because the process “spins” while waiting for the lock to become available.
* Spinlocks do have an advantage, however, in that no context switch is required when a process must wait on a lock, and a context switch may take considerable time. Thus, when locks are expected to be held for short times, spinlocks are useful. They are often employed on multiprocessor systems where one thread can “spin” on one processor while another thread performs its critical section on another processor.
* 好处，当credical section 比较短，适合spinlock, 因为 no conext switch is required.

## [Semaphores](http://en.wikipedia.org/wiki/Semaphore_%28programming%29)
##### Two types
* Semaphores which allow an arbitrary resource count are called counting semaphores, while semaphores which are restricted to the values 0 and 1 (or locked/unlocked, unavailable/available) are called binary semaphores

##### Implementation
* Counting semaphores are equipped with two operations, historically denoted as V (also known as signal) and P (or wait). Operation V increments the semaphore S, and operation P decrements it.
* A simple way to understand wait and signal operations is:
  1. wait: If the value of semaphore variable is not negative, decrements it by 1. If the semaphore variable is now negative, the process executing wait is blocked (i.e., added to the semaphore's queue) until the value is greater or equal to 1.   Otherwise, the process continues execution, having used a unit of the resource.
  2. signal: Increments the value of semaphore variable by 1. After the increment, if the pre-increment value was negative (meaning there are processes waiting for a resource), it transfers a blocked process from the semaphore's waiting queue to the ready queue.
* Code:
```
typedef struct{ 
   int value;
   struct process *list; 
} semaphore;

wait(semaphore *S) { 
      S->value--;
      if (S->value < 0) {
         add this process to S->list;
         block();
      }
}

signal(semaphore *S) { 
      S->value++;
      if (S->value <= 0) {
            remove a process P from S->list; 
            wakeup(P);
      }
}
```

* The list of waiting processes can be easily implemented by a link field in each process control block (PCB). Each semaphore contains an integer value and a pointer to a list of PCBs. One way to add and remove processes from the list so as to ensure bounded waiting is to use a FIFO queue, where the semaphore contains both head and tail pointers to the queue.
* It is critical that semaphore operations be executed atomically !
   1. This is a critical-section problem; and in a single-processor environment, we can solve it by simply inhibiting interrupts during the time the wait() and signal() operations are executing. This scheme works in a single-processor environment because, once interrupts are inhibited, instructions from different processes cannot be interleaved. Only the currently running process executes until interrupts are reenabled and the scheduler can regain control.
   2. In a multiprocessor environment, interrupts must be disabled on every pro- cessor. Otherwise, instructions from different processes (running on different processors) may be interleaved in some arbitrary way. Disabling interrupts on every processor can be a difficult task and furthermore can seriously diminish performance. Therefore, SMP systems must provide alternative locking tech- niques—such as compare and swap() or spinlocks—to ensure that wait() and signal() are performed atomically.


##### [Example: Producer/consumer problem](http://en.wikipedia.org/wiki/Semaphore_%28programming%29)

##### [Difference between Semaphore and Mutex](http://www.geeksforgeeks.org/mutex-vs-semaphore/)
* [Wiki](http://en.wikipedia.org/wiki/Semaphore_%28programming%29)
* Mutexes have a concept of an owner. Only the process that locked the mutex is supposed to unlock it. If the owner is stored by the mutex this can be verified at runtime.
* Mutexes may provide priority inversion safety. If the mutex knows its current owner, it is possible to promote the priority of the owner whenever a higher-priority task starts waiting on the mutex.
* Mutexes may also provide deletion safety, where the process holding the mutex cannot be accidentally deleted.

##### [Priority Inversion](http://en.wikipedia.org/wiki/Priority_inversion)

##### More Example about the Semaphore
##### Semaphore 实现 Signaling， 保证B到达之后，A才能到达
```
Semaphore bArrived(0);
-----------------------

B1
bArrived.signal();

---------------------

bArrived.wait()
A1
````

##### Semaphore 实现mutex
```
Semaphore mutex(1);

-------------------
mutex.wait();
B1
mutex.signal();

--------------------
mutex.wait();
A1
mutex.signal();

```

### [Deadlock](http://en.wikipedia.org/wiki/Deadlock)
＊ In an operating system, a deadlock is a situation which occurs when a process or thread enters a waiting state because a resource requested is being held by another waiting process, which in turn is waiting for another resource held by another waiting process. If a process is unable to change its state indefinitely because the resources requested by it are being used by another waiting process, then the system is said to be in a deadlock.

#### Deadlock Condition
##### 1. Mutual Exclusion: 
At least one resource must be held in a non-shareable mode.[1] Only one process can use the resource at any given instant of time.
##### 2. Hold and Wait or Resource Holding: 
A process is currently holding at least one resource and requesting additional resources which are being held by other processes.
##### 3. No Preemption: 
a resource can be released only voluntarily by the process holding it.
##### 4. Circular Wait: 
A process must be waiting for a resource which is being held by another process, which in turn is waiting for the first process to release the resource. In general, there is a set of waiting processes, P = {P1, P2, ..., PN}, such that P1 is waiting for a resource held by P2, P2 is waiting for a resource held by P3 and so on until PN is waiting for a resource held by P1

