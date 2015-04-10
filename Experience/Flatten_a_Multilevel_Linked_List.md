[G4G](http://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/)
Given a linked list where in addition to the next pointer, each node has a child pointer, 
which may or may not point to a separate list. These child lists may have one or more children 
of their own, and so on, to produce a multilevel data structure, as shown in below figure.
You are given the head of the first level of the list. Flatten the list so that all the nodes 
appear in a single-level linked list. You need to flatten the list in way that all nodes at first
level should come first, then nodes of second level, and so on.

Each node is a C struct with the following definition.

![pic](https://github.com/UmassJin/Python-Study/blob/master/img/flattenList.png)

