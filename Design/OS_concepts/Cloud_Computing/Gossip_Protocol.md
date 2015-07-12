* Multicast Protocol Problem
      * Fault Tolerance: packets may dropped or delayed by underlying network 
      * Scalability
      
* Centralized
      * one sender, multiple receivers, using UDP/TCP packets
      * problem: latency, the receivers that received the packets (average time) is O(n), size of the receivers 
      
* Tree Based topology 
      * Spanning tree protocol, IPmulticast, SRM, RMTP, TRAM, TMTP 
      * latency: O(logn)
      * problem: need to take time to repair the internal nodes (not the leaf nodes) if internal nodes are down
      * SRM (Scalable Reliable Multicast)
            * Use NAKs (Negative Acknowledgements) to repair multicast not received 
            * But adds random delays, and uses exponential backoff to avoid NAK storms
      * RMTP (Reliable Multicast Transport Protocol)
            * Use ACKs (positive acknowledgmetns)
            * But ACKs only sent to designated receivers, which then re-transmit missing multicasts 
            
* A third Approach 
    * Gossip is used in Multicast problem, and tree-based multicast protocols, as known as epidemics 
    * 1 multicast sender 
    * Periodically, sender random choose b targets and transmit the messages, use Gossip messages(UDP)
    * it maybe possible that the same nodes may be picked multiple times 
    * once the node received the Gossip messages, it will set the "infected" by the Gossip 
    * There may be one node received multiple multicast message
    * nodes are independent with other infected nodes in different gossip protocol 

* Push VS Pull
* So that was “Push” gossip
    * Once you have a multicast message, then become "infected" and start gossiping about it
    * Multiple messages? Gossip a random subset of them, or recently-received ones, or higher priority ones

* There’s also “Pull” gossip
    * Periodically poll a few randomly selected processes for new multicast messages that you haven’t received no
       matter you are "infected" or "non-infected"
    * Get those messages
    * pull gossip is faster than push gossip
    * Second half of pull gossip finishes in time O(log(log(N)) 
    
* Hybrid variant: Push-Pull
    * As the name suggests we could use push at beginning and then use pull to later round to get it out into everyone 
     in the system very quickly 
     
* Pull Gossip is faster than push gossip 
![pic](https://cloud.githubusercontent.com/assets/9062406/8636302/b194ff0a-280f-11e5-9b78-9a3c5065dccf.png)

* Gossip Protocol 
          * is lightweight in large groups
          * spreads a multicast quickly
          * fault tolerance 
          * low latency
          * reliability 

* Topology Analysis
          * In a datacenter topology with top of the rack switches talking to one core switch, there are 2 racks, each with N/2 nodes from the multicast group. The nodes execute push gossip. If each node picks a gossip target outside its rack with probability (1/N) and choose the local gossip is O(1-1/N), and gossip targets are selected uniformly at random from the target subgroup, the time to disseminate a gossip is O(logN)
![pic](https://cloud.githubusercontent.com/assets/9062406/8636303/c0e0f306-280f-11e5-814b-7b0ff0e1e7bb.png)

* Implementations
          * Cassandra key-value store (an others) use gossip for maintaining membership lists

