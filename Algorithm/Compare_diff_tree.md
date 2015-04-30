* B-tree when you're managing more than thousands of items and you're paging them from a disk or some slow storage medium.
* RB tree when you're doing fairly frequent inserts, deletes and retrievals on the tree.
* AVL tree when your inserts and deletes are infrequent relative to your retrievals.
* The AVL trees are more balanced compared to Red Black Trees, but they may cause more rotations during insertion and deletion. So if your application involves many frequent insertions and deletions, then Red Black trees should be preferred. And if the insertions and deletions are less frequent and search is more frequent operation, then AVL tree should be preferred over Red Black Tree.
