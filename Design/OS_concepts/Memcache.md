### Cache 
#### Different Type
##### 1) Global Cache
* A global cache is just as it sounds: all the nodes use the same single cache space. 

##### 2) Distributed Cache 
* Definition 
    * Typically the cache is divided up using a consistent hashing function, such that if a request node is looking for a certain piece of data it can quickly know where to look within the distributed cache to determine if that data is available.

* Advantage 
    * A distributed cache is the increased cache space that can be had just by adding nodes to the request pool.

* Disadvantage
    * A disadvantage of distributed caching is remedying a missing node. Some distributed caches get around this by storing multiple copies of the data on different nodes; however, you can imagine how this logic can get complicated quickly, especially when you add or remove nodes from the request layer.

### Memcached 
* Big-O
* LRU
* Memory Allocation
* Consistent Hashing 

#### a) Big-O




#### Reference:
* [Memcache Internals](https://www.adayinthelifeof.nl/2011/02/06/memcache-internals/)
* [Scaling memcached at Facebook](https://www.facebook.com/note.php?note_id=39391378919)

