'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head or k == 0: return head
        size = 1
        fast = head
        while fast.next:
            size +=1 
            fast = fast.next
        fast.next = head
        k = k % size
        tmp = size - k 
        while tmp > 0:
            fast = fast.next
            tmp -= 1
        head = fast.next
        fast.next = None
        return head
