Given a Singly Linked List, write a function to delete the node which has given value. 

Your function must follow following constraints: 
* 1) It must accept pointer to the start node as first parameter and node to be deleted as second parameter i.e., pointer to head node is not global. 
* 2) It should not return pointer to the head node. 
* 3) It should not accept pointer to pointer to head node.

[G4G](http://www.geeksforgeeks.org/delete-a-given-node-in-linked-list-under-given-constraints/)

[Solution using C](https://github.com/UmassJin/Leetcode/blob/master/Experience/April/0413Arista.md)

```python
#! /usr/bin/env python

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# should not use the dummy pointer, which pointer to the head 
def delete_node_given_constraints(head, number):
   if not head: return None
   while head.val == number:
        if not head.next:
            print "Only head is the target number!"
            del head
            # how could we delete the head here ??
            return
        head.val = head.next.val
        head.next = head.next.next

   prev = head
   while prev.next:
       if prev.next.val != number:
           prev = prev.next
       else:
           prev.next = prev.next.next


def print_linkedlist(head):
    while head:
        print head.val,
        head = head.next
    print "\n"

node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(2)
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(8)
node7 = ListNode(2)
node8 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
print_linkedlist(node1)
delete_node_given_constraints(node1, 3)
print_linkedlist(node1)
delete_node_given_constraints(node1, 2)
print_linkedlist(node1)

node9 = ListNode(2)
node10 = ListNode(2)
node11 = ListNode(2)
node9.next = node10
node10.next = node11
print_linkedlist(node9)
delete_node_given_constraints(node9,2)
print_linkedlist(node9)
```
