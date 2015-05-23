'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head or not head.next: return None
        slow = head; fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None 

# 注意test case: [1] 有cycle 和没有cycle的情况，我们需要check head.next == None or not
# 不一定fast and slow的相遇点就是交点，分析
# http://www.cnblogs.com/zuoyuan/p/3701877.html
