* Introduction
  * There are many services on Amazon’s platform that only need
primary-key access to a data store. For many services, such as
those that provide best seller lists, shopping carts, customer
preferences, session management, sales rank, and product catalog,
the common pattern of using a relational database would lead to
inefficiencies and limit scale and availability.

* Design Consideration 
    * Dynamo is targeted mainly at applications that need an “always writeable” data store
      where no updates are rejected due to failures or concurrent writes.
    * Dynamo is built for an infrastructure within a single administrative domain where all
      nodes are assumed to be trusted. Third, applications that use
    * Dynamo do not require support for hierarchical namespaces (a norm in many file systems) or 
    complex relational schema (supported by traditional databases).
    * Fourth, Dynamo is built for latency sensitive applications that require at least 99.9% of read
      and write operations to be performed within a few hundred milliseconds.

* System Interfaces
    * get(key): The get(key) operation locates the object replicas associated with the key in the
                storage system and returns a single object or a list of objects with conflicting versions 
                along with a context.
    * The put(key, context, object) operation determines where the replicas of the object should be placed 
                based on the associated key, and writes the replicas to disk.
    
* Partition Algorithm
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
