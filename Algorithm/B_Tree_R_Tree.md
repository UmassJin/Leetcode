#### B-Tree Definition
According to Knuth's definition, a B-tree of order m is a tree which satisfies the following properties:
* Every node has at most m children.(order to be maximum number of children)
* Every non-leaf node (except root) has at least ⌈m⁄2⌉ children.
* The root has at least two children if it is not a leaf node.
* A non-leaf node with k children contains k−1 keys.
* All leaves appear in the same level

#### R-Tree Definition
一棵R树满足如下的性质：

1.     除非它是根结点之外，所有叶子结点包含有m至M个记录索引（条目）。作为根结点的叶子结点所具有的记录个数可以少于m。通常，m=M/2。
2.     对于所有在叶子中存储的记录（条目），I是最小的可以在空间中完全覆盖这些记录所代表的点的矩形（注意：此处所说的“矩形”是可以扩展到高维空间的）。
3.     每一个非叶子结点拥有m至M个孩子结点，除非它是根结点。
4.     对于在非叶子结点上的每一个条目，i是最小的可以在空间上完全覆盖这些条目所代表的店的矩形（同性质2）。
5.     所有叶子结点都位于同一层，因此R树为平衡树。

#### Reference
* [B-Tree wiki](http://en.wikipedia.org/wiki/B-tree#Technical_description)
* [从头到尾详细解说B Tree](http://blog.csdn.net/v_july_v/article/details/6530142#t2)
* [R-Tree wiki](http://en.wikipedia.org/wiki/R-tree)
