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

#### [Memory Layout of C Programs] (http://www.geeksforgeeks.org/memory-layout-of-c-program/)
A typical memory representation of C program consists of following sections.

1. Text segment
2. Initialized data segment
3. Uninitialized data segment
4. Stack
5. Heap

![pic](http://www.geeksforgeeks.org/wp-content/uploads/Memory-Layout.gif)
