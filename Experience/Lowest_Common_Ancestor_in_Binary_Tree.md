### Lowest Common Ancestor in a Binary Tree
#### Bottom-up Approach (O(n))  
* Assume both the node1 and node2 are exist in the Binary Tree 
* Here if the input tree node does not exist, may cause the issue 
* we do not know whether input p, q, 
* 1) q does not exist 
* 2) q is the children of p 

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

* Maybe input tree node does not exist in the Binary Tree O(n)
```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        if (not A and not B ) or not root: return None 
        global v1
        global v2
        v1 = False; v2 = False 
        
        result = self.find_LCA(root, A, B)
        if v1 and v2:
            return result
        else:
            return None 
    
    def find_LCA(self, root, A, B):
        global v1
        global v2
        
        if not root: return None
        if root.val == A.val and root.val == B.val:
            v1 = v2 = True 
            return root 
        
        left = self.find_LCA(root.left, A, B)
        right = self.find_LCA(root.right, A, B)
        
        if left and right:
            return root
        elif root.val == A.val:
            v1 = True 
            return root
        elif root.val == B.val:
            v2 = True 
            return root 
        elif left:
            return left
        else:
            return right 

```

#### Method 2 (O(n))
* By Storing root to n1 and root to n2 paths):
* Find path from root to n1 and store it in a vector or array.
* Find path from root to n2 and store it in another vector or array.
* Traverse both paths till the values in arrays are same. Return the common element just before the mismatch.

```python
def findLCA(root, node1, node2):
    path1 = []
    path2 = []

    if ((not findpath(root, path1, node1)) or (not findpath(root, path2, node2))):
        return -1

    length = min (len(path1), len(path2))
    for i in range(length):
        if path1[i] != path2[i]:
            break
    return path1[i-1]

# Finds the path from root node to given root of the tree, Stores the
# path in a vector path[], returns true if path exists otherwise false
def findpath(root, path, node):
    if not root: return False
    path.append(root.val)
    
    # Check if the root value is same as node value
    if root.val == node.val:
        return True
    # Check if k is found in left or right sub-tree
    if ((root.left and findpath(root.left, path, node)) or
            (root.right and findpath(root.right, path, node))):
        return True

    path.pop()
    return False

```

### Lowest Common Ancestor in a Binary Search Tree 
* Analysis: We can solve this problem using BST properties. We can recursively traverse the BST from root. The main idea of the solution is, while traversing from top to bottom, the first node n we encounter with value between n1 and n2, i.e., n1 < n < n2 or same as one of the n1 or n2, is LCA of n1 and n2 (assuming that n1 < n2). So just recursively traverse the BST in, if node's value is greater than both n1 and n2 then our LCA lies in left side of the node, if it's is smaller than both n1 and n2, then LCA lies on right side. Otherwise root is LCA (assuming that both n1 and n2 are present in BST)
* O(h), h is the height of the tree 
* Four cases need to consider:
* a) Both nodes are to the left of the tree.
* b) Both nodes are to the right of the tree.
* c) One node is on the left while the other is on the right.
* d) When the current node equals to either of the two nodes, this node must be the LCA too.


```python
def findLCA_BST(root, node1, node2):
    if not root or not node1 or not node2:
        return None
    if (max(node1.val, node2.val) < root.val):
        return findLCA_BST(root.left, node1, node2)  # Note: here we need to return !!
    elif (min(node1.val, node2.val) > root.val):
        return findLCA_BST(root.right, node1, node2)
    else:
        return root

```

### [Lowest Common Ancestor in a Binary Tree II] (http://articles.leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-tree-part-ii.html)
* Given a binary tree, find the lowest common ancestor of two given nodes in the tree. Each node contains a parent pointer which links to its parent.


### Follow up questions:
* Find the path between any nodes in the tree 

### Reference:
* [GeeksforGeeks] (http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/)
* [Leetcode Articals] (http://articles.leetcode.com/2011/07/lowest-common-ancestor-of-a-binary-tree-part-i.html)
* [Topcoder] (https://www.topcoder.com/community/data-science/data-science-tutorials/range-minimum-query-and-lowest-common-ancestor/)
