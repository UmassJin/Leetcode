* Why we need Non_SQL
    * 1. Data Large and unstructred 
    * 2. Lots of random reads and writes
    * 3. Sometimes write-heavy, but Relational SQL is read-heavy
    * 4. Foreign keys rarely needed
    * 5. Joins infrequent

* Needs recently
    * Speed
    * Avoid Single point of Failure (SPoF)
    * Low TCO (Total cost of operation)
    * Fewer system adminstrators
    * Incremental Scalability
    * Scale out than scale up

* NoSQL = "Not Only SQL"
    * Necessary API operations:
      * get(key)
      * put(key, value)
    * Unstructured
    * No schema imposed, maybe missing columns or some Rows
    * No foreign keys, joins may not be supported 

* Column-Oriented Storage
    * RDBMS store an entire row together
    * NoSQL systems typically store a column together 
    * Why useful ?
        * Queries that touch only a few columns are faster than those in a row-oriented storage
        * It enables faster range searches using one column
        * It prevents the entire table from being read for a query 
        * example: get the blog_ids fromt he blog table, for the RDBMS, need to fetch
        all the table and get each row, but for NoSQL, we only need to fetch that column 
        do not need other column at all

* Cassandra
  * a distributed key-value store
     * Based on the Distributed Hash Table (DHT), each data center keep a ring store servers and keys
     * Coordinator could be per query/client/data center based 
     * Instead of using the finger table, Coordinator need to know all the keys store in which nodes
       (include the duplicate nodes), 
  
  * Replication Strategy (two options)
      * SimpleStrategy
      * NetworkTopologyStrategy
      * SimpleStrategy: uses the Partitioner, of which there are two kinds
         * 1. RandomPartitioner: Chord-like hash partitioning
         * 2. ByteOrderedPartitioner: Assigns ranges of keys to servers.
               * Easier for range queries (e.g., get me all twitter users starting with [a-b])
      * NetworkTopologyStrategy: for multi-DC deployments
         * Two replicas per DC
         * Three replicas per DC
         * Per DC
            * How to set the replicas in per DC
               * First replica placed according to Partitioner
               * Then go clockwise around ring until you hit a different rack
   * Snitches:
      * Maps IPs to racks and DCs,  Configured in cassandra.yaml config file
         * SimpleSnitch: Unaware of Topology (Rack-unaware)
         * RackInferring: Assumes topology of network by octet of server’s IP address
            * 101.201.301.401 = x.<DC octet>.<rackoctet>.<node octet>
         * PropertyFileSnitch: uses a config file
   
  * Writes (Check the slides, important !) 
      * Hinted Handoff mechanism 
          * If any replica is down, the coordinator writes to all other replicas, and keeps the write locally
until down replica comes back up.When all replicas are down, the Coordinator (front end) buffers writes (for up to a few hours).   
      * Election of coordinate per datacenter using ZooKeeper


* P2P Systems
    * A. Gnutella
      * little-endian format for the message structure and protocol 
      * To avoid duplicate transmissions, each peer maintains a list of recently received messages
      * Query forwarded to all neighbors except peer from which received
      * Each Query (identified by DescriptorID) forwarded only once
      * QueryHit routed back only to peer from which Query received with same DescriptorID
      * Duplicates with same DescriptorID and Payload descriptor (msg type) are dropped
      * QueryHit with DescriptorID for which Query not seen is dropped
      
    * Five main messages:
      * Query (search)
        * when the nodes receive the query message, it will first check the local whether hit the keyword
        * then flood the query messages to all the neighbors 
        * if receive the duplicate, will not send the msgs second time
      * QueryHit (response to query)
      * Ping (to probe network for other peers)
        * keep set of the neighbors are fresh 
      * Pong (reply to ping, contains address of another peer)
      * Push (used to initiate file transfer)
          * if there is the response behind the requestor, then we could use the push messages since it already connected
            to peers, which go through the query path
      
    * B. Chord
      * Distributed Hash Table
        A distributed hash table allows you to do the same in a distributed setting (objects=files)
        * Performance concerns:
          * Load balancing
          * Fault-tolerance
          * Efficiency of lookups and inserts
          * Locality
      * Chord:
        * Memory: O(logN)
        * Lookup Latency: O(logN)
        * Messages for a lookup: O(logN)
      * How we place the nodes(peers) in the ring ?
          * Uses Consistent Hashing on node’s (peer’s) address
          * SHA-1(ip_address,port) -> 160 bit string
          * Truncated to m bits
          * Called peer id (number between 0 and 2^m - 1)
          * Not unique but id conflicts very unlikely
          * Can then map peers to one of 2^m logical points on a circle
          * kinds of the peer pointers(types of neighbors): 
              * 1) successors 
              * 2) Predecessors
              * 2) Finger Table:
                  * for example: m = 7, the fingle table i from 0 to 6
                  * for each node id, let's say the peer with id 33, the first peer id is 
                   id >= n + 2^i (mod 2^m)
                  * details see the video, charpter 3.5 P2P
      * How we place the files?
         * SHA-1(filename) 160 bit string (key)
         * File is stored at first peer with id greater than its key (mod 2^m)
      * How the search works ?
         * At node n, send query for key k to largest successor/finger entry <= k
         * if none exist, send query to successor(n)
      
      * How we handle the failures ? 
         * we may not find the node which store the data 
            * Save r successors in table
            * Choose r = 2log(N) suffices to maintain lookup
         * if the node which save the data has failure 
            * duplicate the key in the Predecessors and successors
      
      * When the new node inserted
         * update the successor and predesessor
         * talks to neighbors to update finger table (Stablization protocol used by each node)
         * a new peer affects O(logN) other finger entries in the system 
         * Stabilization Protocol 
      
      * Virtual Nodes
         * ensure load balance
        
      
      
      
      
      
