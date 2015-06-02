#### Load Balancing:
* Load balancing is the process of spreading requests across multiple resources according to some metric (random, round-robin, random with weighting for machine capacity, etc) 
and their current status (available for requests, not responding, elevated error rate, etc).
* Smart Clients
* Hardware Load Balancers
* Software Load Balancers

#### Caching
##### Caching consists of: 
    * precalculating results (e.g. the number of visits from each referring domain for the previous day), 
    * pre-generating expensive indexes (e.g. suggested stories based on a user's click history), 
    * storing copies of frequently accessed data in a faster backend (e.g. Memcache instead of PostgreSQL)
    * Have two kinds:
      * Application Caching
      * Database Caching

##### Content Delivery/Distribution Network(CDN)


#### Reference:
* [HAproxy Introduction]http://www.oschina.net/question/17_8785
