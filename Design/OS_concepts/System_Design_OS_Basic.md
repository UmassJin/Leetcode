##Table of Content
####[1. Process](#process)
####[2. Process Synchronization](#process-synchronization)
####[3. Semaphores](#semaphores)
####[4. Monitor](#monitor)
####[5. Static Numbers](#static-numbers)
####[6. Relational SQL vs NoneSQL](#relationalsqlvsnonesql)

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

![pic](https://cloud.githubusercontent.com/assets/9062406/7449415/8d6808bc-f1ea-11e4-9b14-3f147f0f0d18.png)

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

#### [Read/Write Lock](http://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock)
##### Read-preferring RW locks 
* allow for maximum concurrency, but can lead to write-starvation if contention is high. This is because writer threads will not be able to acquire the lock as long as at least one reading thread holds it. Since multiple reader threads may hold the lock at once, this means that a writer thread may continue waiting for the lock while new reader threads are able to acquire the lock, even to the point where the writer may still be waiting after all of the readers which were holding the lock when it first attempted to acquire it have released the lock.

##### Write-preferring RW locks 
* avoid the problem of writer starvation by preventing any new readers from acquiring the lock if there is a writer queued and waiting for the lock. The writer will then acquire the lock as soon as all readers which were already holding the lock have completed.[3] The downside is that write-preferring locks allows for less concurrency in the presence of writer threads, compared to read-preferring RW locks. Also the lock is less performant because each operation, taking or releasing the lock for either read or write, is more complex, internally requiring taking and releasing two mutexes instead of one.This variation is sometimes also known as "write-biased" readers-writer lock.

##### Unspecified priority RW locks 
* does not provide any guarantees with regards read vs. write access. Unspecified priority can in some situations be preferable if it allows for a more efficient implementation.[citation needed]


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
* [wiki page](http://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem)

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

#### Callback 
* Definition: a callback is a piece of executable code that is passed as an argument to other code, which is expected to call back (execute) the argument at some convenient time. 

## [Monitor](http://en.wikipedia.org/wiki/Monitor_%28synchronization%29)
* a monitor is a synchronization construct that allows threads to have both mutual exclusion and the ability to wait (block) for a certain condition to become true. Monitors also have a mechanism for signalling other threads that their condition has been met. 
*  A condition variable is basically a container of threads that are waiting on a certain condition.

#### [参考Implement EventManager](https://github.com/UmassJin/Leetcode/blob/master/Design/OS_concepts/Implement_EventManager.md)


## Static Numbers
#### [Facebook](http://newsroom.fb.com/company-info/)
* 1.44 billion active user per month
* 1.25 billion mobile user per month
* 936 million daily active user per day (远大于Monthly因为monthly的active user不能重复计算)
* 798 million mobile daily active users on average for March 2015


####程序内
* 一个char是1 byte, 一个int/float/long是4 bytes, 一个double是 8 bytes
* 1 Million = 10^6, 1 Million char = 1MB, 1 Million int = 4MB, 1 Million double = 8MB
* 1 Billion = 10^9, 1 Billion char = 1GB, 1 Billion int = 4GB, 1 Million double = 8GB
* 综上所述，假设8G电脑很普通，一般来说如果不提memory size的话无论什么type都能放下，如果说了memory size就要对比下了
* We choose quicksort over mergesort as mergesort requires O(n) space. Quicksort uses O(logn) space.
* MD5 digest size 128 bits = 16 bytes
* SHA-1 digest size 160 bits = 20 bytes
* Max Email address = 254 char = 254 bytes

| Things| 1 | 1 Thousand(2^10) | 1 Million(2^20) | 1 Billion(2^30) |
| :---: | ---: | ---: | ---: | ---: |
| byte | byte | KB | MB | GB |
| char | 1 byte | 1 KB | 1 MB | 1 GB |
| int/float/long | 4 byte | 4 KB | 4 MB | 4 GB |
| double | 8 byte | 8 KB | 8 MB | 8 GB |
| MD5 | 128 bits = 16 bytes| 16 KB | 16 MB | 16 GB |
| SHA-1 | 160 bits = 20 bytes | 20 KB | 20 MB | 20 GB |
| Email | 254 chars = 254 bytes | 254 KB | 254 MB | 254 GB |
| IP Address(IPv4) | 2**8 * 4 = 4 bytes | 4 KB | 4 MB | 4 GB |
| IP Address(IPv6) | 128 bits = 16 bytes | 16 KB | 16 MB | 16 GB |

####Computer
* SSD 50~200MB/s
* DRAM 2-20GB/s

####Note
1. 所有IP是能放进内存的，因为一共2^32个ip地址


#### [Hierarchy of Storage](http://en.wikipedia.org/wiki/Computer_data_storage#Primary_storage)
* register
* cache
* main memory (The main memory (the "RAM") in personal computers is Dynamic random-access memory (DRAM))
* Above are volatile storage, loses its contents when the power to the device is removed.
* solic-state disk
* magnetic disk
* optical disk
* magnetic tapes


##### A millisecond(ms), 1 microsecond(μs), , A nanosecond (ns)
* 1s = 1000 ms 
* 1 ms = 1000 μs
* 1 μs = 1000 ns

#### Architectural view of the storage hierarchy
![pic](https://cloud.githubusercontent.com/assets/9062406/8048464/633deccc-0e06-11e5-95cd-c026b09d648d.png)


## Relational SQL vs NoneSQL
* NoSQL
  * MongoDB(Document)
  * Google Big Table (Column)
  * Cassandra (Column)
  * HBase (Column)
  * Amazon DynamoDB(Key-Value Eventually Consistent)
  * Redis(Key-Value RAM)
  * MemcacheDB(Key-Value RAM)
* Eventually Consistent
* Pros:
  * Scalable
  * Flexible
  * It’s Administrator-Friendly
  * It’s Cost-Effective and Open-Source
  * The Cloud’s the Limit
* Cons:
  * A General Lack of Maturity
  * Performance and Scaling > Consistency - Performance and Scaling is good, lack of Consistency

