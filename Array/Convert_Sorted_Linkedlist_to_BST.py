Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        fast = slow = head
        pre = None 
        while (fast and fast.next):
            fast = fast.next.next
            pre = slow
            slow = slow.next 
 
        root = TreeNode(slow.val)
        right = slow.next
        pre.next = None 
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right)
        return root 

# test case: [0], only one node
# test case: [], empty linked list
# test case: [1,2], two nodes 
