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
        if not head or k < 2: return head
        
        next_head = head
        for i in xrange(k-1): # Note 1) 
            next_head = next_head.next
            if not next_head:
                return head
        ret = next_head
        
        current = head
        while next_head:
            tail = current 
            prev = None
            for i in xrange(k):
                if next_head:
                    next_head = next_head.next
                _next = current.next
                current.next = prev
                prev = current 
                current = _next
            tail.next = next_head or current  # 注意这里必须是next_head or current 
            # test case: [1,2,3,4] 2; [1,2,3] 2
            #tail.next = current
        return ret
        
  # 这题的解题思路是，先把next_head 找到第k个节点(Note 1), 然后 ret = next_head, 这个ret将是新的header
  # 然后将tail 始终指向链表的头部，当reverse done的时候，指向next_head，如果next_head不为空
  # https://leetcode.com/discuss/20923/simple-python-solution-one-pass-no-additional-space-109ms
