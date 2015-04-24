##Table of Content
####[1. C Language](#c-language)
####[2. Operation System](#operation-system)
####[3. Network](#network)

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

#### [How to write C functions that modify head pointer of a Linked List?](http://www.geeksforgeeks.org/how-to-write-functions-that-modify-the-head-pointer-of-a-linked-list/)

#### [Delete a given node in Linked List under given constraints](http://www.geeksforgeeks.org/delete-a-given-node-in-linked-list-under-given-constraints/)


## Operation System 

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

#### [Inter-Process communications] (http://en.wikipedia.org/wiki/Inter-process_communication)
* Sharing information; for example, web servers use IPC to share web documents and media with users through a web browser.
* Distributing labor across systems; for example, Wikipedia uses multiple servers that communicate with one another using IPC to process user requests.[2]
* Privilege separation; for example, HMI software systems are separated into layers based on privileges to minimize the risk of attacks. These layers communicate with one another using encrypted IPC.
* Approaches: File, Signal, Socket, Message queue, Pipe, Semaphore, Shared memory.

##### [Network Socket](http://en.wikipedia.org/wiki/Network_socket)


## Network
#### [what happens when you type in a URL in browser](http://stackoverflow.com/questions/2092527/what-happens-when-you-type-in-a-url-in-browser)
[The other analysis](http://www.quora.com/What-are-the-series-of-steps-that-happen-when-an-URL-is-requested-from-the-address-field-of-a-browser)

1. browser checks cache; if requested object is in cache and is fresh, skip to #9
2. browser asks OS for server's IP address
3. OS makes a DNS lookup and replies the IP address to the browser(host/dig)
4. browser opens a TCP connection to server (this step is much more complex with HTTPS)
5. browser sends the HTTP request through TCP connection
6. browser receives HTTP response and may close the TCP connection, or reuse it for another request
7. browser checks if the response is a redirect (3xx result status codes), authorization request (401), error (4xx and 5xx), etc.; these are handled differently from normal responses (2xx)
8. if cacheable, response is stored in cache
9. browser decodes response (e.g. if it's gzipped)
10. browser determines what to do with response (e.g. is it a HTML page, is it an image, is it a sound clip?)
11. browser renders response, or offers a download dialog for unrecognized types

####Transmission Control Protocol (TCP)
1. Transmission Control Protocol (TCP) is a connection oriented protocol, which means the devices should open a connection before transmitting data and should close the connection gracefully after transmitting the data.
2. Transmission Control Protocol (TCP) assure reliable delivery of data to the destination.
3. Transmission Control Protocol (TCP) protocol provides extensive error checking mechanisms such as flow control and acknowledgment of data.
4. Sequencing of data is a feature of Transmission Control Protocol (TCP).
5. Delivery of data is guaranteed if you are using Transmission Control Protocol (TCP).
6. Transmission Control Protocol (TCP) is comparatively slow because of these extensive error checking mechanisms
7. Multiplexing and Demultiplexing is possible in Transmission Control Protocol (TCP) using TCP port numbers.
8. Retransmission of lost packets is possible in Transmission Control Protocol (TCP).

####User Datagram Protocol (UDP)

1. User Datagram Protocol (UDP) is Datagram oriented protocol with no overhead for opening, maintaining, and closing a connection.
2. User Datagram Protocol (UDP) is efficient for broadcast/multicast transmission.
3. User Datagram protocol (UDP) has only the basic error checking mechanism using checksums.
4. There is no sequencing of data in User Datagram protocol (UDP) .
5. The delivery of data cannot be guaranteed in User Datagram protocol (UDP) .
6. User Datagram protocol (UDP) is faster, simpler and more efficient than TCP. However, User Datagram protocol (UDP) it is less robust then TCP
7. Multiplexing and Demultiplexing is possible in User Datagram Protcol (UDP) using UDP port numbers.

There is no retransmission of lost packets in User Datagram Protcol (UDP).

#### [VLAN](http://www.cisco.com/c/en/us/td/docs/ios/12_2/switch/configuration/guide/fswtch_c/xcfvl.html#wp1003443)
* A VLAN is a switched network that is logically segmented on an organizational basis, by functions, project teams, or applications rather than on a physical or geographical basis. For example, all workstations and servers used by a particular workgroup team can be connected to the same VLAN, regardless of their physical connections to the network or the fact that they might be intermingled with other teams. Reconfiguration of the network can be done through software rather than by physically unplugging and moving devices or wires.
* A VLAN can be thought of as a broadcast domain that exists within a defined set of switches. A VLAN consists of a number of end systems, either hosts or network equipment (such as bridges and routers), connected by a single bridging domain. The bridging domain is supported on various pieces of network equipment; for example, LAN switches that operate bridging protocols between them with a separate bridge group for each VLAN.
* VLANs are created to provide the segmentation services traditionally provided by routers in LAN configurations. VLANs address scalability, security, and network management. Routers in VLAN topologies provide broadcast filtering, security, address summarization, and traffic flow management. None of the switches within the defined group will bridge any frames, not even broadcast frames, between two VLANs. 
 
#### [How to troubleshoot a ping failure ?](http://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/asr9k_r4-0/troubleshooting/guide/tr40asr9kbook/tr40con.pdf)

##### IGP (Interior Gateway Protocol)
* An Interior Gateway Protocol (IGP) is a type of protocol used for exchanging routing information between gateways (commonly routers) within an Autonomous System (for example, a system of corporate local area networks). This routing information can then be used to route network-level protocols like IP.
* Interior gateway protocols can be divided into two categories: distance-vector routing protocols and link-state routing protocols. Specific examples of IGP protocols include Open Shortest Path First (OSPF), Routing Information Protocol (RIP) and Intermediate System to Intermediate System (IS-IS).

##### [ARP (Address Resolution Protocol)](http://en.wikipedia.org/wiki/Address_Resolution_Protocol)
