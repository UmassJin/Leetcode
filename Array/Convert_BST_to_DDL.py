'''
#### Flatten BST to (Doubly) linked list
1. Leetcode上面的原题是to single, 但是traversal是pre-order
2. 这里的doubly用的方法是in-order traversal, pre-order也是一样的思路
3. [网上](http://cslibrary.stanford.edu/109/TreeListRecursion.html)的题目还有点差别是要变成Circular Doubly Linked List
4. 稍微注意一下return的问题, 这两种recursion的方法都没有return值, 所以如果需要找head的话还得再处理下
5. 千万记得这里需要用到global declaration

#####Flatten思路
1. 最方便的方法还是用recursion
2. 先弄清需要的是preorder, inorder还是postorder的顺序
3. 选择对应order的traversal模板, 重要的一点是要把
   ```python
   left = root.left
   right = root.right
   ```
   提前存好，因为进行flatten之后可能会破坏树的结构，这步做好之后，XXXorder traversal的方法都是一样的了
4. 记得```global head, last```然后对```last```进行操作
   * Singly Linked List - 记得重置```last.left = None, last.right = root```
   * Doubly Linked List - 如果```last.right = root, root.left = last```
     这里有一点点差别就是如果是preorder的话，```head.left = None```需要单独处理下
5. ```last = root```更新```last```
6. ```head```就是初始设为None, 第一个需要处理的node就赋为```head```就行了

Good Reference: 
http://articles.leetcode.com/2010/11/convert-binary-search-tree-bst-to.html
http://cslibrary.stanford.edu/109/TreeListRecursion.html

'''
# Convert BST to the Circular Double linked list 
# The most important thing for converting is the header pointer,
# The first node, previous pointer pointer to the last element 
# The last node, next pointer pointer to the first element 

# In-order convert 
def BST_DDL(root):
    pre = [None], head = [None]
    BSTToDDL(root, pre, head)
    return head

def BSTToDDL(node, pre, head):
    if not node: return
    BSTToDDL(node.left, pre, head)# Use the recursion for the in-order traverse 

    node.left = pre[0]
    if pre[0]:
        pre[0].right = node
    else:
        head[0] = node # Current node (smallest element) is head of the list if previous node is None

    # as soon as the recursion ends, the head's left pointer 
    # points to the last node, and the last node's right pointer
    # points to the head pointer.
    right = node.right # Need to SAVE the right pointer here since after flatten, the pointer changes! 
    head[0].left = node
    node.right = head[0]

    pre[0] = node
    BSTToDDL(right, pre, head)

# Convert BST to the Double linked list 
# In-order convert 
def inorder_doubly_flatten(root):
    global last   # Use the global ! 
    global head
    if not root: return
    inorder_doubly_flatten(root.left)
    if last:
        last.right = root    # update the previous and next pointer for each node 
        root.left = last
    last = root   # Always update the last 
    if not head:
        head = root
    inorder_doubly_flatten(root.right)


# Since the python does not support transfer the reference
# So here we use the list to keep update the value
# instead of use the global variable 
def inorder_doubly_flatten(root):
    last = [None]
    head = [None]
    inorder_ddl_helper(root, last, head)
    return head[0]

def inorder_ddl_helper(root, last, head):
    if not root: return
    inorder_ddl_helper(root.left, last, head)

    if last[0]:
        last[0].right = root  # update the previous and next pointer for each node 
        root.left = last[0]
    last[0] = root 
    if not head[0]:
        head[0] = root     # Always update the last 
        
    inorder_ddl_helper(root.right, last, head)


# Convert BST to the Double linked list 
# Pre-order convert
def preorder_doubly_flatten(root):
    if not root: return
    global last
    global head

    if not head:
        head = root
    if last:
        last.right = root
        root.left = last
    else:
        root.left = None  # Note here!!! this is not the circlal double linked list!!  
    last = root

    preorder_doubly_flatten(left)
    preorder_doubly_flatten(right)
