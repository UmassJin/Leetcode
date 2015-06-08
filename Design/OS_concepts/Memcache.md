### Cache 
#### Why use the Cache ?
* To reduce the number or retrieval queries made to a database
* To reduce the number of requests made to external services
* To reduce the time spent computing data
* To reduce filesystem access

#### Type of Cache
* File system
* Database
* Shared memory
* RAM disk
* Object cache (memcached and APC)
* Opcode cache (APC)

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
#### Introduction
* Distributed memory object caching
* Acts as a simple key/value dictionary
* Runs as a daemon
* Has a simple protocol for client access over TCP and UDP
* Can be run in a pool, but individual daemons are not aware of the pool
* Clients/applications manage the pool
* Not an opcode cache

#### Limitation 
* Key size has a 250 byte limit
* Value can not be larger than 1 MB
* Memory limits for 32bit/64bit systems
* Replication not built-in; dependent on the client

* Fast asynchronous network I/O
* Not a persistent data store
* It does not provide redundancy
* Data is not replicated across the cluster
* It doesn’t handle failover
* Daemons are not aware of each other
* It does not provide authentication•Works great on a small and local-area network
* A single value cannot contain more than 1MB of data
* Keys are strings limited to 250 characters

#### Internal Design 
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

##### Slab allocation
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

##### [Consistent hashing](https://www.adayinthelifeof.nl/2011/02/06/memcache-internals/)
* hash the key and the server 
* it's like the clock, 头尾相连

### Facebook Cache 
* $GLOBALS
      * Avoids unnecessary APC and Memcached requests
      * Automatic via abstraction
      * But still has function call cost overhead
      
* APC (Alternative PHP Cache)
      * Non-user specific data
      * Network/School information
      * Database information
      * Useragent strings
      * Hot application data
      * Site variables
      * Languange Strings
      
* Memcached
      * Distributed object cache
      * Facebook currently utilizes > 400 memcached hosts
      * With > 5TB in memory cache
      * Facebook contributions:
         * UDP Support
         * Performance Enhancements
      * Many choices in opensource clients
      * What to cached ?
         * User Specific Data
         * Long profile
         * Short profile
         * Friends
         * Applications

* Database
* Browser Cache
* Third Party CDN

#### Memcache vs APC
##### when use memcache
* when requests aren’t guaranteed to always go to the same machine
* Data is specific or targeted to a user
* User sessions

##### when use APC
* Application settings•Configuration
* Data that is the same for each user
* Requests are guaranteed to go to the same machine (i.e. sticky sessions)
* File upload progress & sessions (if using sticky sessions)

##### Use both
* Create a caching adapter for a uniform caching interface and decide where to store at the app level or even dynamically at runtime
* Use APC for things it’s good at and memcached for things it’s good at

#### Reference:
* [Memcache Internals](https://www.adayinthelifeof.nl/2011/02/06/memcache-internals/)
* [Scaling memcached at Facebook](https://www.facebook.com/note.php?note_id=39391378919)
* [Facebook Cache](http://download.docslide.net/uploads/check_up03/192015/54647671b4af9f6e568b4899.pdf)
* [Memcache and APC](http://docslide.us/technology/caching-with-memcached-and-apc.html)
