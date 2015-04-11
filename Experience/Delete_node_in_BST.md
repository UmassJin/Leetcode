实际上有好几种做法 1. replace current node with left maximum node
2. replace current node with right minimum node 
3. 整体移动，前提是这个node只能有一边的subtree

这里就直接选第一种作为解法 但是这种也有特殊情况 

1. No left child and No right child, leaf node

2. Only left child or only right child 

3. Have two children: left and right, find the minimum susuccessor node  

4. node is root of the tree (use dummy node)


```python
def delete_node(root, val):
    dummy_node = tree_node(0)
    dummy_node.left = root
    find_delete(dummy_node, root, val)
    return dummy_node.left

def find_delete(parent, node, val):
    if not node:
        return None
    if node.val == val:
        delete_node_in_BST(parent, node)
    if node.val < val:
        find_delete(node, node.right, val)
    elif node.val > val:
        find_delete(node, node.left, val)

# Case 1: the delete node has no left child and no right child 
# Case 2: the delete node has ONLY left child or right child 
# Case 3: the delete node has two children 
def delete_node_in_BST(parent, node):
    # Case 1
    if not node.left and not node.right:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None

    # Case 2
    elif not node.left:
        if parent.left == node:
            parent.left = node.right
        else:
            parent.right = node.right

    elif not node.right:
        if parent.left == node:
            parent.left = node.left
        else:
            parent.right = node.left

    # Case 3
    else:
        successor = get_successor(node)
        if parent.left == node:
            parent.left = successor
        else:
            parent.right = successor
        successor.left = node.left

def get_successor(delnode):
    successor_parent = delnode
    successor = delnode
    cur = delnode.right
    while cur:
        successor_parent = successor
        successor = cur
        cur = cur.left

    if successor != delnode.right:
        successor_parent.left = successor.right
        successor.right = delnode.right

    return successor

```
