#####Print BST Keys in the Give Range

Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree. 

Print all the keys of tree in range k1 to k2. i.e. 
print all x such that k1<=x<=k2 and x is a key of given BST. Print all the keys in increasing order.

[G4G Solution](http://www.geeksforgeeks.org/print-bst-keys-in-the-given-range/)

* 注意这里的思路：
* 一开始的思路是判断 ```if root.val > k2, then go to root.left, if root.val < k1, then go to root. right， if root.val in between the k1 and k2, will add the root.val， ```但是这个思路输出的结果不是按照 ```increasing order``` 输出的
* 所以这里的思路是，比较 ```root.val > k1, then go to the left, until find one node is None or < k1, then check if recent root.val between k1 and k2, if so, print out the root.val, which gurantee the increasing value, then check if root.val < k2, if so, go to the right``` 

```python
def search_a_range(root, k1, k2):
    if not root:
        return

    if root.val > k1:
        search_a_range(root.left, k1, k2)

    if k1< root.val < k2:
        print root.val

    if root.val < k2:
        search_a_range(root.right, k1, k2)

```
