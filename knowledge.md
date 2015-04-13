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

![pic](http://4.bp.blogspot.com/_IEmaCFe3y9g/SO3GGEF4UkI/AAAAAAAAAAc/z7waF2Lwg0s/s1600-h/lb.GIF)

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

