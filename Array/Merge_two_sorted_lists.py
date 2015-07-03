'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together 
the nodes of the first two lists.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists_1(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        
        dummy1 = ListNode(0)
        pre = dummy1 
        
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            elif l1.val >= l2.val:
                pre.next = l2 
                l2 = l2.next
            pre = pre.next
        
        if l1:
            pre.next = l1

        if l2:
            pre.next = l2
 
        return dummy1.next
        
        
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b
