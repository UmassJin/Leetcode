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
    
