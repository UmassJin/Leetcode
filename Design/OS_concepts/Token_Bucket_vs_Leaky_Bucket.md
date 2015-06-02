#### Congestion Control 

##### Definition  
* When one part of the subnet (e.g. one or more routers in an area) becomes overloaded, congestion results. 
* Because routers are receiving packets faster than they can forward them, one of two things must happen: 
    * The subnet must prevent additional packets from entering the congested region until those already present can be processed. 
    * The congested routers can discard queued packets to make room for those that are arriving. 

##### Factors that Cause Congestion
* Packet arrival rate exceeds the outgoing link capacity.
* Insufficient memory to store arriving packets
* Bursty traffic
* Slow processor

##### Congestion Control vs Flow Control 
* Congestion control is a global issue – involves every router and host within the subnet
* Flow control – scope is point-to-point; involves just sender and receiver.

##### Congestion Control method 
* Congestion Control is concerned with efficiently using a network at high load.
* Several techniques can be employed. These include:
    * Warning bit
    * Choke packets
    * Load shedding
    * Random early discard
    * Traffic shaping
* The first 3 deal with congestion detection and recovery. The last  2 deal with congestion avoidance.

###### Warning bit
* A special bit in the packet header is set by the router to warn the source when congestion is detected.
* The bit is copied and piggy-backed on the ACK and sent to the sender.
* The sender monitors the number of ACK packets it receives with the warning bit set and adjusts its transmission rate accordingly.

###### Choke Packet 
* A more direct way of telling the source to slow down.
* A choke packet is a control packet generated at a congested node and transmitted to restrict traffic flow.
* The source, on receiving the choke packet must reduce its transmission rate by a certain percentage.
* An example of a choke packet is the ICMP Source Quench Packet.

##### Hop-by-Hope Choke Packet 
* Over long distances or at high speeds choke packets are not very effective. 
* A more efficient method is to send to choke packets hop-by-hop.
* This requires each hop to reduce its transmission even before the choke packet arrive at the source.

##### Loading Shedding
* When buffers become full, routers simply discard packets.
* Which packet is chosen to be the victim depends on the application and on the error strategy used in the data link layer. 
* For a file transfer, for, e.g. cannot discard older packets since this will cause a gap in the received data.
* For real-time voice or video it is probably better to
	throw away old data and keep new packets. 
* Get the application to mark packets with discard priority.


##### Random Early Discard(RED)
* This is a proactive approach in which the router discards one or more packets before the buffer becomes completely full.
* Each time  a packet arrives, the RED algorithm computes the average queue length, avg.
* If avg is lower than some lower threshold, congestion is assumed to be minimal or non-existent and the packet is queued
* If avg is greater than some upper threshold, congestion is assumed to be serious and the packet is discarded.
* If avg is between the two thresholds, this might indicate the onset of congestion. The probability of congestion is then calculated.

##### Traffic Shaping
* Another method of congestion control is to “shape” the traffic before it enters the network.
* Traffic shaping controls the rate at which packets are sent (not just how many). Used in ATM and Integrated Services networks. 
* At connection set-up time, the sender and carrier negotiate a traffic pattern (shape).
* Two traffic shaping algorithms are:
    * Leaky Bucket
    * Token Bucket

#### [PPT for leaky Bucket & Tocken Bucket](http://www.slideshare.net/vimal25792/leaky-bucket-tocken-buckettraffic-shaping)

