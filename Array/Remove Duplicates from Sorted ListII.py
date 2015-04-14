Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head 
        dummynode = ListNode(0)
        dummynode.next = head
        p = dummynode 
        temp = p.next
        
        while temp:
            while temp.next and temp.next.val == temp.val:
                temp = temp.next
            
            if p.next != temp:
                p.next = temp.next
                temp = p.next 
            else:
                p = p.next
                temp = temp.next
        return dummynode.next 
