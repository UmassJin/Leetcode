


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
# Recursion: TLE, O(n^2)
class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree_1(self, A):
        if not A: return None
        return self.buildTree(A, 0, len(A)-1)
        
    def buildTree(self, A, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(A[start])
        
        maxvalue = max(A[start: end+1])
        max_index = A.index(maxvalue)
        
        root = TreeNode(maxvalue)
        root.left = self.buildTree(A, start, max_index-1)
        root.right = self.buildTree(A, max_index+1, end)
        
        return root 
        
    
    def maxTree(self, A):

        stack = []
        for num in A:
            newnode = TreeNode(num)
            while stack and (stack[-1].val <= newnode.val):
                left_neighbor = stack.pop()
                left_neighbor.right = newnode.left
                newnode.left = left_neighbor
            stack.append(newnode)
        
        pre = None
        while stack:
            cur = stack.pop()
            cur.right = pre 
            pre = cur
        
        return pre
        
        
        
        
