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
# Time complexity: T(n) = 2T(n/2) + O(n) = O(nlogn)
# test case: [0], only one node
# test case: [], empty linked list
# test case: [1,2], two nodes 

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def get_size(self, head):
        self.current = head 
        size = 0
        while head:
            size += 1
            head = head.next 
        return size 
    
    def sortedListToBST(self, head):
        if not head: return head
        size = self.get_size(head)
        return self.sortedListToBST_helper(size)
    
    def sortedListToBST_helper(self,size):
        if size <= 0: return None
        left = self.sortedListToBST_helper(size/2)
        
        root = TreeNode(self.current.val)
        self.current = self.current.next 
        
        right = self.sortedListToBST_helper(size - 1 - size/2)
        root.left = left
        root.right = right
        return root 

# Here we get the size at first, then the time complexity is T(n) = 2T(n/2) + O(1)--> O(n) + O(logn) = O(n)
