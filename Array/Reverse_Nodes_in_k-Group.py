'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
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
    def reverseKGroup(self, head, k):
        if not head or k == 1: return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy; cur = dummy
        num = 0
        
        while cur.next:
            cur = cur.next 
            num += 1
        
        while num >= k:
            cur = pre.next
            for i in xrange(k-1):
                tmp = pre.next
                pre.next = cur.next
                cur.next = cur.next.next
                pre.next.next = tmp 
            
            pre = cur
            num -= k
        
        return dummy.next 
        
  # https://leetcode.com/discuss/20923/simple-python-solution-one-pass-no-additional-space-109ms
  # https://leetcode.com/discuss/21301/short-but-recursive-java-code-with-comments
  # https://leetcode.com/discuss/39901/python-o-n-time-o-1-space-recursive-solution
