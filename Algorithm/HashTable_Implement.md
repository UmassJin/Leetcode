#### HashTable vs BST
##### HashTable
* Search (O(1))
* Insert (O(1))
* Delete (O(1))

##### BST
* Search (O(logn))
* Insert (O(logn))
* Delete (O(logn))


1) Hash tables are only O(1) when there is a reasonably good hashing algorithm.  Perhaps the data
is such that it's difficult to write a algorithm that has predictably good performance.  Hash table
performance can degrade to o(n), where balanced trees are always O(log n).

2) Unless the maximum size of the hash table is known and established at the time the table is created, the
table will periodically resize itself (as items are added) which can lead to performance "hiccups".  This
is not a problem with trees.

3) A traversal of the hash table has to process more than n entries due to empty hash table entries.  Also,
the traversal processes the elements in a not particularly useful order.  This is not a problem with trees.

1)  We can get all keys in sorted order by just doing Inorder Traversal of BST. This is not a natural operation in Hash Tables and requires extra efforts.
2)  Doing order statistics, finding closest lower and greater elements, doing range queries are easy to do with BSTs. Like sorting, these operations are not a natural operation with Hash Tables.
3)  BSTs are easy to implement compared to hashing, we can easily implement our own customized BST. To implement Hashing, we generally rely on libraries provided by programming languages.
4)  With BSTs, all operations are guaranteed to work in O(Logn) time. But with Hashing, Θ(1) is average time and some particular operations may be costly, especially when table resizing happens.

##### Reference
* http://comscigate.com/HW/cs31/hashingVbst.htm
* [G4G](http://www.geeksforgeeks.org/advantages-of-bst-over-hash-table/)
* http://stackoverflow.com/questions/4128546/advantages-of-binary-search-trees-over-hash-tables

