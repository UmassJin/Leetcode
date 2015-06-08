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
* LRU (Least Recently Used)
* Memory Allocation
* Consistent Hashing 

#### a) Big-O
* Most of memcache functionality (add, get, set, flush etc) are o(1)
* Cannot iterate over all your items inside memcache 

#### b) LRU Algorithm (Least Recently Used)
* Tell how much memory could used for memcache 
* Implement 
      * Internally, all objects have a “counter”. This counter holds a timestamp. Every time a new object is created, that counter will be set to the current time. 
      * When an object gets FETCHED, it will reset that counter to the current time as well. As soon as memcache needs to “evict” an object to make room for newer objects, it will find the lowest counter. 
      * That is the object that isn’t fetched or is fetched the longest time ago (and probably isn’t needed that much, otherwise the counter would be closed to the current timestamp).

#### c) Memory Allocation
* Could not use the same memory allocation way in C, like allocate some memory to create a string, do some things with it, and in the end, free up the memory that has been used.
* The reason is that malloc() and free() functions are not really optimized for such kind of programs. Memory gets fragmented easily which means a lot of memory will get spilled, just like you can spill a lot of diskspace when you write/delete a lot of files on your filesystem
* Memcache’s memory manager will allocate the maximum amount of memory from the operating system that you have set (for instance, 64Mb, but probably more) through one malloc() call. From that point on, it will use its own memory manager system called the slab allocator.

##### Sloab allocation
* partition the allocated memory into small parts: pages, each page is 1Mb large
* Each of those pages can be assigned to a slab-class, or can be unassigned (being a free page)
* Each page that is designated to a particular slab-class will be divided into smaller parts called chunks.
* There can be multiple pages for each slab-class, but as soon as a page is assigned a slab-class (and thus, split up in chunks), it cannot be changed to another slab-class.
* as soon as a complete page if full (all chunks in the page are filled) and we need to add another piece of data, it will fetch a new free page, assign it to the specified slab-class, partition it into chunks and gets the first available chunk to store the data. But as soon as there are no more pages left that we can designate to our slab-class, it will use the LRU-algorithm to evict one of the existing chunks to make room. This means that when we need a 128byte chunk, it will evict a 128byte chunk, even though there might be a 256byte chunk that is even older. Each slab-class has its own LRU.

* Notes:
      * a) 1 page (1 Mb) --> assign to one slab-class 
      * b) after assign one slab-class, will divided into chunks, each size of chunck is same, like 80 bytes each, 100 bytes each
      * c) There can be multiple pages for each slab-class, but as soon as a page is assigned a slab-class (and thus, split up in chunks), it cannot be changed to another slab-class.
      * d) The smallest chunk-size starts at 80 bytes and increases with a factor of 1.25 

#### Reference:
* [Memcache Internals](https://www.adayinthelifeof.nl/2011/02/06/memcache-internals/)
* [Scaling memcached at Facebook](https://www.facebook.com/note.php?note_id=39391378919)

