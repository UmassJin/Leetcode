#Reference: http://articles.leetcode.com/2010/11/convert-binary-search-tree-bst-to.html

# 30) Convert BST to the Circular Double linked list 
# The most important thing for converting is the header pointer,
# The first node, previous pointer pointer to the last element 
# The last node, next pointer pointer to the first element 

# In-order convert 
def BST_DDL(root):
    pre = None, head = None
    BSTToDDL(root, pre, head)
    return head

def BSTToDDL(node, pre, head):
    if not node: return
    BSTToDDL(node.left, pre, head)# Use the recursion for the in-order traverse 

    node.left = pre
    if pre:
        pre.right = node
    else:
        head = node # Current node (smallest element) is head of the list if previous node is None

    # as soon as the recursion ends, the head's left pointer 
    # points to the last node, and the last node's right pointer
    # points to the head pointer.
    right = node.right # Need to SAVE the right pointer here since after flatten, the pointer changes! 
    head.left = node
    node.right = head

    pre = node
    BSTToDDL(node.right, pre, head)

# Convert BST to the Double linked list 
# In-order conver 
def inorder_doubly_flatten(root):
    global last
    global head
    if not root: return
    inorder_doubly_flatten(root.left)
    if last:
        last.right = root
        root.left = last
    last = root
    if not head:
        head = root
    inorder_doubly_flatten(root.right)

def preorder_doubly_flatten(root):

