### Lowest Common Ancestor in a Binary Tree
#### Bottom-up Approach (O(n))  
* Assume both the node1 and node2 are exist in the Binary Tree 
```python
def common_ancestry(root, node1, node2):
    if not node1 and not node2:
        return None
    return get_LCA(root, node1, node2)

def get_LCA(root, node1, node2):
    if not root: 
        return None
    # If either n1 or n2 matches with root's key, report
    # the presence by returning root (Note that if a key is
    # ancestor of other, then the ancestor key becomes LCA
    # Note: here we compare the root.val 
    if node1.val == root.val or node2.val == root.val:
        return root
    # Look for keys in left and right subtrees
    left = get_LCA(root.left, node1, node2)
    right = get_LCA(root.right, node1, node2)
   
    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left and right: 
        return root
    # Otherwise check if left subtree or right subtree is LCA
    if left:
        return left
    elif right:
        return right
    else:
        return None
```

* If maybe one of the tree node does not exist in the Binary Tree
```python




```


#### Method 2



### Lowest Common Ancestor in a Binary Tree II
* Given a binary tree, find the lowest common ancestor of two given nodes in the tree. Each node contains a parent pointer which links to its parent.


### Reference:
* [GeeksforGeeks] (http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/)
* [Leetcode Articals] (http://articles.leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-tree-part-i.html)
* [Topcoder] (https://www.topcoder.com/community/data-science/data-science-tutorials/range-minimum-query-and-lowest-common-ancestor/)
