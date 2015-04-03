#! /usr/bin/env python

class tree_node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def create_minimum_BST(datalist, start, end):
    if end < start:
        return None
    mid = (start + end) / 2
    n = tree_node(datalist[mid])
    n.left = create_minimum_BST(datalist, start, mid-1)
    n.right = create_minimum_BST(datalist, mid+1, end)
    return n

# DFS: use the stack to implement 
# BFS: use the queue to implement 
# 1) Inorder Recursive 
def in_order_traverse_rec(root):
    result = []
    in_order_rec(result,root)
    return result

def in_order_rec(result,root):
    if not root: return
    in_order_rec(result, root.left)
    result.append(root.val)
    in_order_rec(result, root.right)

# 2) Inorder Iterative (DFS)
def in_order_traverse_iter(root):
    stack = []; result = []
    node = root
    while True:
        while node:
            stack.append(node)
            node = node.left

        if not stack: break
        node = stack.pop()
        result.append(node.val)
        node = node.right
    return result

# 3) Preorder Recursive 
def preorder_traverse_rec(root):
    result = []
    pre_order_rec(result,root)
    return result

def pre_order_rec(result,root):
    if not root: return
    result.append(root.val)
    pre_order_rec(result, root.left)
    pre_order_rec(result, root.right)

# 4) Preorder Iterative (DFS)
def preorder_traverse_iter(root):
    stack = [root]; result = []
    while stack: # Use while ! 
        node = stack.pop()
        if node: # check if node !
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return result

# 5) Postorder Recursive
def postorder_traverse_rec(root):
    result = []
    post_order_rec(result,root)
    return result

def post_order_rec(result,root):
    if not root: return
    post_order_rec(result, root.left)
    post_order_rec(result, root.right)
    result.append(root.val)

# 6) Postorder Iterative (DFS)
def postorder_traverse_iter(root):
    stack = [root]; result = []

    if not root: return result # Note: Check!
    while stack:
        node =stack.pop()
        result.insert(0,node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result

# 7) Level Traversal from top to bottom, recursion 
def levelOrder_rec(root):
    result = []
    level_order(root, 0, result)
    return result

def level_order(node, level, result):
    if node:                        # Note: here if check !
        if len(result) < level + 1: # Note: the condition here 
            result.append([])
        result[level].append(node.val)
        level_order(node.left, level+1, result)
        level_order(node.right, level+1, result)
  
# 8) Level Traversal from top to bottom, iteration  
def levelOrder_iter(root):
    result = [];queue=[root]
    if not root: return result

    while queue:
        sublist = []
        length = len(queue)
        for i in xrange(length):  # Note: here we need to iterate each element in queue
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            sublist.append(node.val)
        result.append(sublist)
    return result

# 9) Level Traversal from bottom to top, recursion 
def levelOrderBottom_rec(root):
    result = []
    if not root: return result  # Note: check the root = None !!
    level_bottom_rec(root, result, 0)
    return result

def level_bottom_rec(root, result, level):
    if root:
        if len(result) < level + 1:
            result.insert(0,[])
        result[len(result)-level-1].append(root.val)
        level_bottom_rec(root.left, result, level+1)
        level_bottom_rec(root.right, result, level+1)

# 10) Level Traversal from bottom to top, iteration  
def levelOrderBottom_iter(root):
    queue = [root]; result = []
    if not root: return result

    while queue:
        qlist = []
        length = len(queue)
        for i in xrange(length):
            node = queue.pop(0)
            qlist.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.insert(0, qlist)
    return result

# 11) Find the Minimum Depth of the tree, recursion
def minDepth_rec(root):
    if not root: return 0
    if (root.left and not root.right):
        return minDepth_rec(root.left)+1
    if (not root.left and root.right):
        return minDepth_rec(root.right)+1
    return min(minDepth_rec(root.left),minDepth_rec(root.right))+1

# 12) Find the Minimum Depth of the tree, iteration 
def minDepth_iter(root):
    queue = []; depth = 0
    if not root: return depth
    queue.append((root,1))

    while queue:
        node, depth = queue.pop(0)
        if node.left: queue.append((node.left,depth+1))
        if node.right:queue.append((node.right,depth+1))
        if not node.left and not node.right:
            return depth

# 13) Find the Maximum Depth of the tree, recursion
def maxDepth_rec(root):
    if root == None:
        return 0
    if (root.left != None and root.right == None):
        return maxDepth_rec(root.left) + 1
    if (root.left == None and root.right != None):
        return maxDepth_rec(root.right) + 1
    return max(maxDepth_rec(root.left), maxDepth_rec(root.right))+1

# 14) Find the Maximum Depth of the tree, iteration
def maxDepth_iter(root):
    queue = []; depth = 0
    if not root: return depth
    queue.append((root,1))

    while queue:
        node, depth = queue.pop(0)
        if node.left: queue.append((node.left,depth+1))
        if node.right:queue.append((node.right,depth+1))
        if not node.left and not node.right:
            continue
    return depth

