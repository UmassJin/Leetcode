##[Consistent Hashing](http://blog.csdn.net/sparkliang/article/details/5279393)
* Naive way to do: hash(k) % n
* four important keys
  * Balancing
  * Monotonicity
  * Spread
  * Load
* 解决的问题：The principle advantage of consistent hashing is that departure or arrival of a node only affects
              its immediate neighbors and other nodes remain unaffected 
* Steps:
  1. the output range of a hash function is treaded as a fixed circular space or "ring"
  2. each data item is assigned to a node by hashing the data to yield its position on the ring
  3. each node in the system is assigned a random value within this space which represents its "position" on the ring
  4. Map Object to Server：顺时针顺着object的key走遇到的第一个Server负责该object
  5. 分析
     * 移除Server
       Server B被移除后，只需要从B出发逆时针找到下一个Server之间的所有object，然后remap到Server B的下一个Server
     * 添加Server
       同样是从新的server逆时针出发到上一个server之间object归他管了
* 通过virtual node来提高balance
    * The number of virtual nodes that a node is responsible can decided based on its capacity, accounting for heterogeneity
      in the physical infrastructure.
* 正常hash就直接hash ip就行了 hash('192.168.1.1')， 如果是hash virtual node可以 hash('192.168.1.1#1')

## Dynamo Partition Scheme 
* Introduction 
    * 1. divides the hash space into Q equally sized partitions
    * 2. each node is assigned Q/S tokens where S is the number of nodes in the system.
    * 3. its tokens are randomly distributed to the remaining nodes such that these properties are preserved
    * 4. Load balancing efficiency is defined as the ratio of average number of requests served by each node to the maximum number of requests
served by the hottest node.

* Advantage 
    * Faster bootstrapping/recovery:
      * Since partition ranges are fixed, they can be stored in separate  files, meaning a partition can be relocated as a unit by simply
        transferring the file (avoiding random accesses needed to locate specific items). This simplifies the process of bootstrapping and
        recovery.
    * Ease of archival: 
     * Periodical archiving of the dataset is a mandatory requirement for most of Amazon storage services.
        Archiving the entire dataset stored by Dynamo is simpler in strategy 3 because the partition files can be archived separately. 
        By contrast, in Strategy 1,

* Disadvantage 
    * changing the node membership requires coordination in order to preserve the properties required of the assignment.
