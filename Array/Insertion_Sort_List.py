Sort a linked list using insertion sort.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head
            
        dummy = ListNode(0)
        dummy.next = head 
        current = head
        
        while current.next:
            if current.next.val < current.val:
                pre = dummy
                while pre.next.val < current.next.val:
                    pre = pre.next
                temp = current.next
                current.next = temp.next
                temp.next = pre.next 
                pre.next = temp
            else:
                current = current.next 
            
        return dummy.next 

# In order to skip the Time Limited Exceed, we did not scan through the head every time
# Only we check if the current.next.val < current.val, we need to insert
