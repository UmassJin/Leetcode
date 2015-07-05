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



#### Advantage and Disadvantage
* Advantage: 0(1) for insert, search and delete
* Disadvantate: 
    * 1) based on arrays, difficult to expand 
    * 2) can not visit the items in a hash table in any kind of order
    * 3) collisions

#### Collision
* Open addressing
    * One approach, when a collision occurs, is to search
the array in some systematic way for an empty cell and insert the new item there,
instead of at the index specified by the hash function. This approach is called open
addressing.
    * linear probing 
      *  在实现 linear probing的时候，注意delete的function的实现，不是简单的空为1，要取一个特殊值，否则find func会出问题
    * quadratic probing
    * double hashing 

* Seperate Chaining 
    * A second approach (mentioned earlier) is to create an array that consists of linked
lists of words instead of the words themselves. Then, when a collision occurs, the
new item is simply inserted in the list at that index. This is called separate chaining.

#### Implement 
##### Linear Probing 

```python
# hashtable: linear probing 
class HashTable:
    def __init__(self, n):
        self.hasharray = [None for _ in xrange(n)]
        self.size = n

    def insert(self, item):
        hashvalue = item % self.size
        while self.hasharray[hashvalue] and self.hasharray[hashvalue] != -1:
                    hashvalue += 1
                    hashvalue = hashvalue % self.size
        self.hasharray[hashvalue] = item

    def delete(self, item):
        hashvalue = item % self.size
        while self.hasharray[hashvalue]:
            if self.hasharray[hashvalue] == item:
                temp = self.hasharray[hashvalue]
                self.hasharray[hashvalue] = -1
                return temp
            hashvalue += 1
            hashvalue %= self.size
        return None

    def find(self, item):
        hashvalue = item % self.size
        while self.hasharray[hashvalue]:
            if self.hasharray[hashvalue] == item:
                return True
            hashvalue += 1
            hashvalue %= self.size
        return False

test = HashTable(5)
test.insert(2)
test.insert(6)
test.insert(1)
test.insert(3)
print test.hasharray
print test.find(6)

# Output:
[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python hashtable.py
[None, 6, 2, 1, 3]
True
```

