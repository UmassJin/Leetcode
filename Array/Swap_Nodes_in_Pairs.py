'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head or not head.next: return head
    
        dummy = ListNode(0)
        dummy.next = head
        head1 = dummy
        
        while head1 and head1.next:
            p = head1.next
            if p.next:
                head1.next = p.next
                p.next = p.next.next
            else:
                break
            head1.next.next = p
            head1 = p 
            
        return dummy.next
