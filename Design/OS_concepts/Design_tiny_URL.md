#### Design a system that takes user-provided URLs and transforms them to shortened URLs that redirect back to original URLs.

##### Interface:
* short_url insert(long_url)
* long_url lookup(short_url)

##### Requirement:
* No two long_urls have the same short_url
* Multiple short_urls could map to one long_url

##### Improve the scalability:
###### More URLs: use multiple backend data-server: database sharding 

* Distribute long_urls to N data-servers by round-robin, and each data-server has it’s own range of short_url.
* Given short_url, find which data-server it belongs to, and send request only to that data-server.
* Each data-server get 1/N write and (approx.) 1/N read.
* How to deal with skewing? (有些URL read非常频繁，可能成为一个hotspot? 怎么解决)
* 对hotspot做进一步partition，把第二bit继续做partition

###### Query-per-second 越来越多?
* Problem: more queries per second => less CPU cycle/network bandwidth per
query
* Solution: Multiple front-end servers.

##### Followup question:
1. Inserting the same long_url multiple times, how to generate the same
short_url?

* we need lookup(long_url) now.

2. How to make short_urls look more random?

* a random number generator will do. (hash is a reasonable choice, if you also want to lookup(long_url))
* short_url = hash(long_url), store <short_url, long_url> pair.
* remember to detect collision.
* how to distribute? prefixing the hash value.

3. How to support user-suggested short_url?

* lookup(short_url), 如果已经有了，可以再suggest几个short_url给用户

4. How about short-time tiny-url?

* database with expiring entry.
* Gabage Collection: dynamic checking

5. Open question: how could tiny-url be exploited maliciously? how do you react?

6. Network-oriented question: how do you implement redirect? HTTP 301.

##### System Design的步骤
* 找出interface之后
* 在small scale里面解决问题
* Improve the scalability

##### Range Partition and Consistent Hashing 
* Range partitioning 
* Selects a partition by determining if the partitioning key is inside a certain range. An example could be a partition for all rows where the column zipcode has a value between 70000 and 79999.

* [Consistent Hashing](http://blog.csdn.net/sparkliang/article/details/5279393)

### Related OS concepts
#### [1. RAM和ROM的区别](http://product.pconline.com.cn/itbk/sjtx/sj/1305/3303309.html)

#### 2. CPU cache

##### 1) Replacement policies, LRU (Least Recently Used) LFU (Least Frequently Used): 
* In order to make room for the new entry on a cache miss, the cache may have to evict one of the existing entries. The heuristic that it uses to choose the entry to evict is called the replacement policy. The fundamental problem with any replacement policy is that it must predict which existing cache entry is least likely to be used in the future. Predicting the future is difficult, so there is no perfect way to choose among the variety of replacement policies available.
* One popular replacement policy, least-recently used (LRU), replaces the least recently accessed entry.
* Marking some memory ranges as non-cacheable can improve performance, by avoiding caching of memory regions that are rarely re-accessed. This avoids the overhead of loading something into the cache without having any reuse.
Cache entries may also be disabled or locked depending on the context.
* Reference:
* [LRU wiki](http://en.wikipedia.org/wiki/Cache_algorithms)
* [CPU 缓存](http://zh.wikipedia.org/wiki/CPU%E7%BC%93%E5%AD%98)
* [LFU Least Frequently Used](http://en.wikipedia.org/wiki/Least_frequently_used)

##### 2) [Write Policy] (http://www.cs.cornell.edu/courses/cs3410/2013sp/lecture/18-caches3-w.pdf)


#### [3. Locality of Reference](http://en.wikipedia.org/wiki/Locality_of_reference)
* In computer science, locality of reference, also known as the principle of locality, is a phenomenon describing the same value, or related storage locations, being frequently accessed. 
* There are two basic types of reference locality – temporal(时间局部性) and spatial locality(空间局部性). 
* Temporal locality refers to the reuse of specific data, and/or resources, within a relatively small time duration. 
* Spatial locality refers to the use of data elements within relatively close storage locations. Sequential locality, a special case of spatial locality, occurs when data elements are arranged and accessed linearly, such as, traversing the elements in a one-dimensional array.


### [System Design example: shorten URL](http://www.hiredintech.com/system-design/the-system-design-process/)
#### 1. Use Cases
1. Shortening: take a URL => return a much shorter URL
2. Redirection: take a short URL => redirect to the original URL 
3. Custom URL
4. High availability of the system 

  Our of scope 
   4. Analytics
   5. Automatic link expiration
   6. Manural link removal 
   7. UI vs API 

#### 2. Constraints
1. Amount of the traffic the system should handle 
2. Amount of the data the system should work with

  Should ask the following questions: 
   1. How many requests per sec should be handle ?
   2. How many new URLs each sec should be handle ?

* 15 Billion new tweets
* All shortened URLs per month: 1.5BN
* We: 100 Million URLs each month 

Math:
* 1. New URLs per month: 100 Million (shortening requests)
* 2. 1 Billion requests per month 
* 3. 10% from shortening and 90% from redirection 
* 4. Requests per second: 400+ requests per sec (40 shortens, 360: redirects)
* 5. Total URLs: 5 years x 12 months x 100 million/month = 6 billion URLs in 5 years
* 6. 500 bytes per URL, URL is case sensitive !
* 7. 6 bytes per hash 
* 8. 3 TBs for all urls, 36 GB for all hashes (over 5 years)
* 9. New data written per second: 40 * (500+6): 20K
* 10. Data read per second: 360 * 506 bytes: 180 K

* All shortened URLs per Month: 1.5 Billion 
* Sites below the top3: 300 M per month 

#### static numbers:
##### [Facebook](http://newsroom.fb.com/company-info/)
* 1.44 billion monthly active users as of March 31, 2015
* 1.25 billion mobile monthly active users as of March 31, 2015

##### [Twitter](https://about.twitter.com/company)
* 302 million monthly active users
* 500 million Tweets are sent per day
 
#### 3. Abstract Design
##### 1. Application service layer (serves the requests)
* Shortening service: 
    * a) Generate the hash, checking if it is in the database, if already used, will keep generating until one unused is find
    * b) For the customer URL, check if it is in the data store
* Rediction service 

##### 2. Data storage layer (keeps track of the hash => URL mapping)

* Acts like a big hash table: stores new mappings, and retrieves a value given a key.\
    * 1) hashed_url = convert_to_base_62(md5(original_url + random_salt))[:6]
    * 2) Base 62 是一种short ulr的encoding, encode之后只有62种字符0-9 a-z A-Z
    * 3) The MD5 message-digest algorithm is a widely used cryptographic hash function producing a 128-bit (16-byte) hash value, typically expressed in text format as a 32 digit hexadecimal number.  

##### 3. Understanding Bottlenecks
    * 1. Traffic - not going to be very hard
    * 2. Lots of data - more interesting
  

##### 4. Scaling your abstract design 
   1. Application Service Layer
      * Start with one machine
      * Measure how far it take us(load tests)
      * Add a load balancer + a cluster of machines over time
        1. to deal with spiky traffice
        2. Also avoid single failure and increase the availability
   2. Data Storage Layer
      1. What's data?
         * Billions of objects
         * Each object is fairly small(<1k)
         * There are no relationship between the objects
         * Reads are 9x more frequent thant writes(360 reads, 40 writes per second)
         * 3TBs of urls, 36GB of hashes
      2. NoSQL vs Relation SQL
         * MySQL:
           * Widely used
           * Mature technology
           * Clear Scaling Paradimgs(sharding, master/slave replication, master/master replication)
           * Used by Facebook, Twitter, Google etc
           * Index lookups are very fast
         * Mappings
           * hash: varchar(6)
           * original_url: varchar(512)
      3. Create a unique index on the hash(36GB+). We want to hold it in memory to speed up lookups.
         1. Vertical Scaling of the MySQL machine (memory is cheap) (vertical for a while)
         2. Partition the data: 5 partitions, 600GB of data, 8GB of indexes (Eventually partiion)
            * We can add more shards in the future. Easier for backup and replicate
            * Default idea of this is: get the first char from the ```hash % num_of_partition```
      4. Master/Slave replication(reading from the slave replicas, writes to the master)(如果有一天read/write不balance了的话) Master/Master
