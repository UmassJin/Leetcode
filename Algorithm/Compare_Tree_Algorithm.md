* B-tree when you're managing more than thousands of items and you're paging them from a disk or some slow storage medium.
* RB tree when you're doing fairly frequent inserts, deletes and retrievals on the tree.
* AVL tree when your inserts and deletes are infrequent relative to your retrievals.
* The AVL trees are more balanced compared to Red Black Trees, but they may cause more rotations during insertion and deletion. So if your application involves many frequent insertions and deletions, then Red Black trees should be preferred. And if the insertions and deletions are less frequent and search is more frequent operation, then AVL tree should be preferred over Red Black Tree.

| AVL Tree | Red-Black Tree |
| --- | --- |
| More load balanced | Less load balanced |
| Path from Root to Leaf at most 1.44log(n+2) | Path from Root to Leaf at most 2log(n+1) | 
| Insert/Delete more rotations | Less rotations in Insert/Delete |
| Use AVL Tree if less insert/delete ans more search |  Use RB Tree if more insert/delete | 
| language dictionaries (or program dictionaries, such as the opcodes of an assembler or interpreter) | usage: computational geometry, Completely Fair Scheduler used in current Linux kernels|


* A perfect binary tree is a binary tree in which all leaves have the same depth or same level.[19] (This is ambiguously also called a complete or full binary tree
* A full binary tree (sometimes referred to as a proper[citation needed] or plane binary tree)[17][18] is a tree in which every node in the tree has either 0 or 2 children.

![pic](https://cloud.githubusercontent.com/assets/9062406/8122459/f2d87036-106e-11e5-8eb5-44623b28d69d.png)
