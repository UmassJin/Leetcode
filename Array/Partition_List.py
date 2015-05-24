'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if not head: return None
        head1 = ListNode(0)
        head2 = ListNode(0)
        lower = head1
        higher = head2
        
        while head:
            if head.val < x:
                lower.next = head
                head = head.next
                lower = lower.next
                lower.next = None
            else:
                higher.next = head
                head = head.next
                higher = higher.next
                higher.next = None
        
        lower.next = head2.next
        return head1.next 
        
#         if not head: return None
#         dummy = ListNode(0)
#         dummy.next = head
#         lower = cur = dummy
        
#         while cur.next:
#             if cur.next.val >= x:
#                 cur = cur.next
#             else:
#                 tmp = cur.next
#                 cur.next = cur.next.next
#                 tmp.next = lower.next
#                 lower.next = tmp 
#                 lower = lower.next
#         return dummy.next 

# # The above method does not work
# # Test Case: 1) [2,1], 2; [1], 2; [1,3,2], 3
