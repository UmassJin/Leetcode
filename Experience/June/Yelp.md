* How is the load balancer works and how could we define the load balancer ?
* Leetcode: Search a 2D matrix 

* Why we need both the IP address and MAC address ? What's the MAC address used for ?
      * MAC addresses are used to send Ethernet frames between two stations in the same local area network. Each station has a unique MAC address that is used to identify who is the sender (source address) and who is the receiver (destination address). But Ethernet frames can't travel between networks. One computer in a local network never sees the MAC of a computer which is on another network.

      * IP addresses are used to send IP packets to another station over the Internet, which is a collection of networks (hence the name "inter networks", from where Internet is derived). Contrary to MAC addresses, IP frames aren't limited to the local network. While travelling around the world, IP packets pass through many smaller networks, many of them using Ethernet (like inside your home or office LAN). When it is the case, the network stack puts the IP packet inside an Ethernet frame, using the MAC address to send to the next stop (what we call 'next hop'). The gateway strips the Ethernet header, rocering the original IP packet, and forwards it over the next network, until it reaches the destination.

* How could we define the load balancer?
    * input: given the machine "A, B, C" and weights "9, 2, 3"
    * let's say the weights mean how much capacity the machine could have 
    * write a function to check how to load balance the input request ?

* The simple way we could do is use the random generater generate the value between 0 to 1, and then times the weight of the machine 
    
http://docs.oracle.com/cd/E23943_01/web.1111/e13709/load_balancing.htm#CLUST183


* topology sort 

* dictionary 问题
