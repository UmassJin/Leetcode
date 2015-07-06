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
* http://www.cs.princeton.edu/~rs/AlgsDS07/10Hashing.pdf


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
      * x + 1^2, x + 2^2, x + 3^2,...
      * the other problem for this method is cause the secondary clustering, the linear probing called the primary clustering 
    * double hashing 
      * For the above issue, The solution is to hash the key a second time, using a different hash function, and use the result as the step size. 
      * Experience has shown that this secondary hash function must have certain
characteristics:
         * It must not be the same as the primary hash function. 
         * It must never output a 0 (otherwise, there would be no step; every probe would land on the same cell, and the algorithm would go into an endless loop).
         ```java
         public void insert(int key, DataItem item)
         // (assumes table not full)
         {
            int hashVal = hashFunc1(key); // hash the key
            int stepSize = hashFunc2(key); // get step size
            // until empty cell or -1
            while(hashArray[hashVal] != null && hashArray[hashVal].getKey() != -1)
            {
               hashVal += stepSize; // add the step
               hashVal %= arraySize; // for wraparound
            }
            hashArray[hashVal] = item; // insert item
         } // end insert()
         ```
      * Double hashing requires that the size of the hash table is a prime number. To see
why, imagine a situation in which the table size is not a prime number. For example,
suppose the array size is 15 (indices from 0 to 14), and that a particular key hashes to
an initial index of 0 and a step size of 5. The probe sequence will be 0, 5, 10, 0, 5,
10, and so on, repeating endlessly. Only these three cells are ever examined, so the
algorithm will never find the empty cells that might be waiting at 1, 2, 3, and so on.
The algorithm will crash and burn.  
      
* Seperate Chaining 
    * A second approach (mentioned earlier) is to create an array that consists of linked
lists of words instead of the words themselves. Then, when a collision occurs, the
new item is simply inserted in the list at that index. This is called separate chaining.
    * load factor 
         * The load factor (the ratio of the number of items in a hash table to its size) is typically
different in separate chaining than in open addressing. In separate chaining it’s
normal to put N or more items into an N cell array; thus, the load factor can be 1 or
greater.
      * With separate chaining, making the table size a prime number is not as important as
it is with quadratic probes and double hashing.

#### Open Addressing Versus Separate Chaining
* If open addressing is to be used, double hashing seems to be the preferred system by
a small margin over quadratic probing. The exception is the situation in which
plenty of memory is available and the data won’t expand after the table is created; in
this case linear probing is somewhat simpler to implement and, if load factors below
0.5 are used, causes little performance penalty.

* If the number of items that will be inserted in a hash table isn’t known when the
table is created, separate chaining is preferable to open addressing. Increasing the
load factor causes major performance penalties in open addressing, but performance
degrades only linearly in separate chaining.

* When in doubt, use separate chaining. Its drawback is the need for a linked list class,
but the payoff is that adding more data than you anticipated won’t cause performance
to slow to a crawl.

#### Summary 
A hash table is based on an array.

• The range of key values is usually greater than the size of the array.

• A key value is hashed to an array index by a hash function.

• An English-language dictionary is a typical example of a database that can be
efficiently handled with a hash table.

• The hashing of a key to an already-filled array cell is called a collision.

• Collisions can be handled in two major ways: open addressing and separate
chaining.

• In open addressing, data items that hash to a full array cell are placed in
another cell in the array.

• In separate chaining, each array element consists of a linked list. All data items
hashing to a given array index are inserted in that list.

• We discussed three kinds of open addressing: linear probing, quadratic probing,
and double hashing.

• In linear probing the step size is always 1, so if x is the array index calculated
by the hash function, the probe goes to x, x+1, x+2, x+3, and so on.

• The number of such steps required to find a specified item is called the probe
length.

• In linear probing, contiguous sequences of filled cells appear. They are called
primary clusters, and they reduce performance.

• In quadratic probing the offset from x is the square of the step number, so the
probe goes to x, x+1, x+4, x+9, x+16, and so on.

• Quadratic probing eliminates primary clustering but suffers from the less severe
secondary clustering.

• Secondary clustering occurs because all the keys that hash to the same value
follow the same sequence of steps during a probe.

• All keys that hash to the same value follow the same probe sequence because
the step size does not depend on the key, but only on the hash value.

• In double hashing the step size depends on the key and is obtained from a
secondary hash function.

• If the secondary hash function returns a value s in double hashing, the probe
goes to x, x+s, x+2s, x+3s, x+4s, and so on, where s depends on the key but
remains constant during the probe.

• The load factor is the ratio of data items in a hash table to the array size.

• The maximum load factor in open addressing should be around 0.5. For double
hashing at this load factor, searches will have an average probe length of 2.

• Search times go to infinity as load factors approach 1.0 in open addressing.

• It’s crucial that an open-addressing hash table does not become too full.

• A load factor of 1.0 is appropriate for separate chaining.

• At this load factor a successful search has an average probe length of 1.5, and
an unsuccessful search, 2.0.

• Probe lengths in separate chaining increase linearly with load factor.

• A string can be hashed by multiplying each character by a different power of a
constant, adding the products, and using the modulo operator (%) to reduce
the result to the size of the hash table.

• To avoid overflow, we can apply the modulo operator at each step in the
process, if the polynomial is expressed using Horner’s method.

• Hash table sizes should generally be prime numbers. This is especially
important in quadratic probing and separate chaining.

• Hash tables can be used for external storage. One way to do this is to have the
elements in the hash table contain disk-file block numbers.

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

