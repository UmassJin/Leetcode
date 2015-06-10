### Introduction
  * There are many services on Amazon’s platform that only need
primary-key access to a data store. For many services, such as
those that provide best seller lists, shopping carts, customer
preferences, session management, sales rank, and product catalog,
the common pattern of using a relational database would lead to
inefficiencies and limit scale and availability.

### Design Consideration 
    * Dynamo is targeted mainly at applications that need an “always writeable” data store
      where no updates are rejected due to failures or concurrent writes.
    * Dynamo is built for an infrastructure within a single administrative domain where all
      nodes are assumed to be trusted. Third, applications that use
    * Dynamo do not require support for hierarchical namespaces (a norm in many file systems) or 
    complex relational schema (supported by traditional databases).
    * Fourth, Dynamo is built for latency sensitive applications that require at least 99.9% of read
      and write operations to be performed within a few hundred milliseconds.

### System Interfaces
    * get(key): The get(key) operation locates the object replicas associated with the key in the
                storage system and returns a single object or a list of objects with conflicting versions 
                along with a context.
    * The put(key, context, object) operation determines where the replicas of the object should be placed 
                based on the associated key, and writes the replicas to disk.

### Different Algorithm 
* Partition and Replication using consistent hashing
* consistency is facilitated by object versioning 
* The consistency among replicas during updates is maintained by a quorum-like technique and a
decentralized replica synchronization protocol.
 
#### Partition Algorithm
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

#### Replication Algorithm 
* for each data item, replicated at N hosts. Each key, k, assigned to a coordinator node.
* In addition to locally storing each key within its range, the coordinator replicates these keys at the N-1
clockwise successor nodes in the ring.
* The list of nodes that is responsible for storing a particular key is called the preference list.

#### Data Versioning (Consistency)
* Need to keep each version for the user's action 
* Use Vector clocks:
   * A vector clock is effectively a list of (node, counter) pairs.
   * One vector clock is associated with every version of every object.
   * One can determine whether two versions of an object are on parallel branches or have a causal ordering, by examine their vector clocks.
   * If the counters on the first object’s clock are less-than-or-equal to all of the nodes in the second clock, 
     then the first is an ancestor of the second and can be forgotten. Otherwise, the two changes are considered to be
     in conflict and require reconciliation

* Possible issue: 
   * the size of vector clocks may grow if many servers coordinate the writes to an object
   * resolve using the clock truncation scheme 
 
#### Consistency between Duplication
* quorum systems
  * R is the minimum number of nodes that must participate in a successful read operation. 
  * W is the minimum number of nodes that must participate in a successful write operation.
  * Procedure:
    * Upon receiving a put() request for a key, the coordinator generates the vector clock for the new version and writes the new version locally.
    * The coordinator then sends the new version (along with the new vector clock) to the N highest-ranked reachable nodes.
    * If at least W-1 nodes respond then the write is considered successful.

