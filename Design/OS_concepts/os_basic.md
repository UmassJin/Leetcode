
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
