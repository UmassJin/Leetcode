#### Remove duplicates from an unsorted linked list
Write a removeDuplicates() function which takes a list and deletes any duplicate nodes from the list. The list is not sorted.

For example if the linked list is 12->11->12->21->41->43->21 then removeDuplicates() should convert the list to 12->11->21->41->43.


[G4G](http://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/)

```python
def delete_duplicate_node_unsorted(head):
    if not head: return
    hashtable = {}
    hashtable[head.val] = 1
    cur = head
    while cur.next:
        if cur.next.val not in hashtable:
            hashtable[cur.next.val] = 1
        else:
            cur.next = cur.next.next
        cur = cur.next
    return head

```
