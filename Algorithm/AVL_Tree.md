#### AVL Tree Introduction
* Self-balancing Binary Search Tree
* Search, Insert, Delete take O(logn) time

##### Balance Factor
* Keep track of a balance factor for each node in the tree 
* ```balanceFactor = height(leftSubTree) - height(rightSubTree)```
* left-heavy: if the balance factor is greater than 0
* right-heavy: if the balance factor is less than 0
* If the balance factor is zero then the tree is perfectly in balance. 

##### [AVL Tree Performance](http://interactivepython.org/runestone/static/pythonds/Trees/balanced.html#avl-tree-performance)
* h = 1.44logN, details check the link

-------------------------
#### [AVL Tree Implementation](http://interactivepython.org/runestone/static/pythonds/Trees/balanced.html#avl-tree-implementation)

* First insert the node and update the parent node
* Go through the load balance from the insert new node and recursive back to the parent node
* Since this is a recursive procedure let us examine the two base cases for updating balance factors:
  1. The recursive call has reached the root of the tree.
  2. The balance factor of the parent has been adjusted to zero. You should convince yourself that once a subtree has a balance factor of zero, then the balance of its ancestor nodes does not change.
```
def _put(self,key,val,currentNode):
    if key < currentNode.key:
        if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
        else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild)
    else:
        if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
        else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightChild)

def updateBalance(self,node):
    if node.balanceFactor > 1 or node.balanceFactor < -1:
        self.rebalance(node)
        return
    if node.parent != None:
        if node.isLeftChild():
                node.parent.balanceFactor += 1
        elif node.isRightChild():
                node.parent.balanceFactor -= 1

        if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

```

* rebalance(node), we use the rotations on the tree 

##### Rotations
* right-heavy: loadbalance < 0, left rotate 
* left-heavy: loadbalance > 0, right rotate 


##### Left Rotation:
To perform a left rotation we essentially do the following:

* Promote the right child (B) to be the root of the subtree.
* Move the old root (A) to be the left child of the new root.
* If new root (B) already had a left child then make it the right child of the new left child (A). Note: Since the new root (B) was the right child of A the right child of A is guaranteed to be empty at this point. This allows us to add a new node as the right child without any further consideration.

```
def rotateLeft(self,rotRoot):
    newRoot = rotRoot.rightChild
    rotRoot.rightChild = newRoot.leftChild
    if newRoot.leftChild != None:
        newRoot.leftChild.parent = rotRoot
    newRoot.parent = rotRoot.parent
    if rotRoot.isRoot():
        self.root = newRoot
    else:
        if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
        else:
            rotRoot.parent.rightChild = newRoot
    newRoot.leftChild = rotRoot
    rotRoot.parent = newRoot
    rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
    newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

```

##### Right Rotation:
To perform a right rotation we essentially do the following:

* Promote the left child (C) to be the root of the subtree.
* Move the old root (E) to be the right child of the new root.
* If the new root(C) already had a right child (D) then make it the left child of the new right child (E). Note: Since the new root (C) was the left child of E, the left child of E is guaranteed to be empty at this point. This allows us to add a new node as the left child without any further consideration.

##### Update the balance Factor:
* rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
* newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

```
newBalD = hb - he
oldBalD = hc - he

newBalD - oldBalD = (hb - he) - (hc - he) = hb - hc
hb = max(ha, hc) + 1 
newBalD - oldBalD = 1 + max(ha, hc) - hc = 1 + max(ha-hc, hc-hc) = 1 + max(hb, 0)
newBalD = oldBalD + 1 + max(hb, 0)
```

##### Left-Right rotate and Right-Left rotate
To correct this problem we must use the following set of rules:

* If a subtree needs a left rotation to bring it into balance, first check the balance factor of the right child. If the right child is left heavy then do a right rotation on right child, followed by the original left rotation.
* If a subtree needs a right rotation to bring it into balance, first check the balance factor of the left child. If the left child is right heavy then do a left rotation on the left child, followed by the original right rotation.

#####Good Reference 
* [AVL tree in Python](http://interactivepython.org/runestone/static/pythonds/Trees/balanced.html#tab-compare) Nice Introduction
* [G4G](http://www.geeksforgeeks.org/avl-tree-set-1-insertion/)

