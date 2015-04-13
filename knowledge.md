## C language 

#### [Understanding "extern" keyword in C] (http://www.geeksforgeeks.org/understanding-extern-keyword-in-c/)
1. Declaration can be done any number of times but definition only once.
2. “extern” keyword is used to extend the visibility of variables/functions().
3. Since functions are visible through out the program by default. The use of extern is not needed in function declaration/definition. Its use is redundant.
4. When extern is used with a variable, it’s only declared not defined, not allocate any memory. 
5. As an exception, when an extern variable is declared with initialization, it is taken as definition of the variable as well.

#### [Little and Big Endian Mystery] (http://www.geeksforgeeks.org/little-and-big-endian-mystery/)

Little and big endian are two ways of storing multibyte data-types ( int, float, etc). 
* In little endian machines, last byte of binary representation of the multibyte data-type is stored first. 
* On the other hand, in big endian machines, first byte of binary representation of the multibyte data-type is stored first.

* In big endian, the most significant byte is stored at the memory address location with the lowest address This is akin to left-to-right reading order Little endian is the reverse: the most significant byte is stored at the address with the highest address

#### [Memory Layout of C Programs] (http://www.geeksforgeeks.org/memory-layout-of-c-program/)
A typical memory representation of C program consists of following sections.

1. Text segment
   Often Read-Only 
2. Initialized data segment
   * Initialized data segment, usually called simply the Data Segment. 
   * A data segment is a portion of virtual address space of a program, which contains the global variables and static variables that are initialized by the programmer.
   * Not Read-Only
3. Uninitialized data segment --> "bss" Segment
   * For instance a variable declared static int i; would be contained in the BSS segment.
   * For instance a global variable declared int j; would be contained in the BSS segment.
4. Stack
  * The stack area traditionally adjoined the heap area and grew the opposite direction; 
    when the stack pointer met the heap pointer, free memory was exhausted.
  * Stack, where automatic variables are stored, along with information that is saved each time a function is called. Each time a function is called, the address of where to return to and certain information about the caller’s environment, such as some of the machine registers, are saved on the stack. 
5. Heap
  * The Heap area is managed by malloc, realloc, and free, which may use the brk and sbrk system calls to adjust its size (note that the use of brk/sbrk and a single “heap area” is not required to fulfill the contract of malloc/realloc/free; they may also be implemented using mmap to reserve potentially non-contiguous regions of virtual memory into the process’ virtual address space).

![pic](http://www.geeksforgeeks.org/wp-content/uploads/Memory-Layout.gif)

#### [Memory](http://stackoverflow.com/questions/79923/what-and-where-are-the-stack-and-heap)
* Process is on Heap memory.
* Thread is on Stack memory.
* Stack is faster while heap is slower
* stackoverflow for stack while heap is for memory leak

#####Compare
| Stack | Heap |
| --- | --- |
| Stored in computer RAM just like the heap. | Stored in computer RAM just like the stack. |
| Variables created on the stack will go out of scope and automatically deallocate. | Variables on the heap must be destroyed manually and never fall out of scope. The data is freed with delete, delete[] or free |
| Much faster to allocate in comparison to variables on the heap. | Slower to allocate in comparison to variables on the stack. |
| Implemented with an actual stack data structure. | Used on demand to allocate a block of data for use by the program. |
| Stores local data, return addresses, used for parameter passing | Can have fragmentation when there are a lot of allocations and deallocations |
| Can have a stack overflow when too much of the stack is used. (mostly from infinite (or too much) recursion, very large allocations) | In C++ data created on the heap will be pointed to by pointers and allocated with new or malloc |
| Data created on the stack can be used without pointers. | Can have allocation failures if too big of a buffer is requested to be allocated. |
| You would use the stack if you know exactly how much data you need to allocate before compile time and it is not too big. | You would use the heap if you don't know exactly how much data you will need at runtime or if you need to allocate a lot of data.|
| Usually has a maximum size already determined when your program starts | Responsible for memory leaks |

#####[Memory Leak](http://en.wikipedia.org/wiki/Memory_leak)
A memory leak may happen when an object is stored in memory but cannot be accessed by the running code.

######[Cause of Memory Leak](http://www.lshift.net/blog/2008/11/14/tracing-python-memory-leaks/)
* Some low level C library is leaking
* Your Python code have global lists or dicts that grow over time, and you forgot to remove the objects after use
* There are some reference cycles in your app


#####Stack (Memory)
When a function calls another function which calls another function, this memory goes onto the stack An int (not a pointer to an int) that is created in a function is stored on the stack
#####Heap (Memory)
When you allocate data with new() or malloc(), this data gets stored on the heap

The JVM divided the memory into following sections:

* Heap
* Stack
* Code
* Static

This division of memory is required for its effective management.

* The code section contains your bytecode.
* The Stack section of memory contains methods, local variables and reference variables.
* The Heap section contains Objects (may also contain reference variables).
* The Static section contains Static data/methods.

Of all of the above 4 sections, you need to understand the allocation of memory in Stack & Heap the most, since it will affect your programming efforts

* When a method is called , a frame is created on the top of stack.
* Once a method has completed execution , flow of control returns to the calling method and its corresponding stack frame is flushed.
* Local variables are created in the stack
* Instance variables are created in the heap & are part of the object they belong to.
* Reference variables are created in the stack.


####Thread and Process
A __process__ can be thought of as an instance of a program in execution Each process is an in- dependent entity to which system resources (CPU time, memory, etc ) are allocated and each process is executed in a separate address space One process cannot access the variables and data structures of another process If you wish to access another process’ resources, inter-process communications have to be used such as pipes, files, sockets etc

A __thread__ uses the same stack space of a process A process can have multiple threads A key difference between processes and threads is that multiple threads share parts of their state Typically, one allows multiple threads to read and write the same memory (no processes can directly access the memory of another process) However, each thread still has its own registers and its own stack, but other threads can read and write the stack memory

A thread is a particular execution path of a process; when one thread modifies a process resource, the change is immediately visible to sibling threads
