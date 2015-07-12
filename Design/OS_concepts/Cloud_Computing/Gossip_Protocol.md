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
    * Once you have a multicast message, you start  gossiping about it
    * Multiple messages? Gossip a random subset of them, or recently-received ones, or higher priority ones
* There’s also “Pull” gossip
    * Periodically poll a few randomly selected processes for new multicast messages that you haven’t received
    * Get those messages
* Hybrid variant: Push-Pull
    * As the name suggests
* Pull Gossip is faster than push gossip 

* Group Membership List 
    * mean time to failure (MTTF) of the 120 server is 1 month, and 12,000 servers is 7.2 hours
    * failure detector program (distributed) and automatically detects failures 
    
