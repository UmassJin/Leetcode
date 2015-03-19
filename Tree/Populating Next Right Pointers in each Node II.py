class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None: return
        dummy = TreeNode(0)
        cur = root
        while cur:
            ptr = dummy
            dummy.next = None
            while cur:
                if cur.left:
                    ptr.next = cur.left
                    ptr = ptr.next
                if cur.right:
                    ptr.next = cur.right
                    ptr = ptr.next
                cur = cur.next
            cur = dummy.next
        return
