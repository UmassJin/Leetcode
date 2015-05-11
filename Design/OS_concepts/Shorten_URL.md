#### Design a system that takes user-provided URLs and transforms them to shortened URLs that redirect back to original URLs.

##### Interface:
* short_url insert(long_url)
* long_url lookup(short_url)

##### Requirement:
* No two long_urls have the same short_url
* Multiple short_urls could map to one long_url

##### System Design的步骤
* 找出interface之后
* 在small scale里面解决问题
* 

#### Related OS concepts

##### [1. RAM和ROM的区别](http://product.pconline.com.cn/itbk/sjtx/sj/1305/3303309.html)

##### 2. CPU cache
##### 1) Replacement policies, LRU (Least Recently Used): 
* In order to make room for the new entry on a cache miss, the cache may have to evict one of the existing entries. The heuristic that it uses to choose the entry to evict is called the replacement policy. The fundamental problem with any replacement policy is that it must predict which existing cache entry is least likely to be used in the future. Predicting the future is difficult, so there is no perfect way to choose among the variety of replacement policies available.
* One popular replacement policy, least-recently used (LRU), replaces the least recently accessed entry.
* Marking some memory ranges as non-cacheable can improve performance, by avoiding caching of memory regions that are rarely re-accessed. This avoids the overhead of loading something into the cache without having any reuse.
Cache entries may also be disabled or locked depending on the context.
* Reference:
* [LRU wiki](http://en.wikipedia.org/wiki/Cache_algorithms)
* [CPU 缓存](http://zh.wikipedia.org/wiki/CPU%E7%BC%93%E5%AD%98)
* [LFU Least Frequently Used](http://en.wikipedia.org/wiki/Least_frequently_used)

##### [3. Locality of Reference](http://en.wikipedia.org/wiki/Locality_of_reference)
* In computer science, locality of reference, also known as the principle of locality, is a phenomenon describing the same value, or related storage locations, being frequently accessed. 
* There are two basic types of reference locality – temporal(时间局部性) and spatial locality(空间局部性). 
* Temporal locality refers to the reuse of specific data, and/or resources, within a relatively small time duration. 
* Spatial locality refers to the use of data elements within relatively close storage locations. Sequential locality, a special case of spatial locality, occurs when data elements are arranged and accessed linearly, such as, traversing the elements in a one-dimensional array.

