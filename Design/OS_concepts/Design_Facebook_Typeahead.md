### Introduction 

    * user --> Browser --> Web Cluster:first-dedegreee.php; typeahead.php
                       --> Typeahead Cluster:aggregator

#### Facebook Sacial Graph: 
1. The graph of the friendship among the people, edges are directed(two sides) between friends.
2. Also other interesting stings which user likes, will have the edges point to other application.
    

### Procedure 
1. When the user clicks the search box, the backend search the home page and 
         fetch the first degree graph which has the connections for the user.
2. When the user type the letter "B", let's say, immediately render the first directly friend, like "Bob"
3. FoF, "friend of friend", "object of friend"
4. The right engles in the graph are services for the significant chunk machines
      * Server first come in the aggregator, and then the aggregator point to the three parts: 
        friend of friend, obj-of-friend, global and memcache parallelly, these three parts are not depend on each other 
![pic](https://cloud.githubusercontent.com/assets/9062406/8112672/39228802-101e-11e5-8ab6-3039fb48d09d.png)

#### A. Friend of Friend
1. Distributed Graph Search Service, use the prefix matching 
      * For some users which has the tiny friend, will seach the three degrees out
![pic](https://cloud.githubusercontent.com/assets/9062406/8112857/82a1e88c-101f-11e5-952a-62ba219dbce6.png)

#### B. Object of Friend
![pic](https://cloud.githubusercontent.com/assets/9062406/8112987/2a09e7a0-1020-11e5-8016-5c15164a2216.png)

#### Static status
* Around 936 million daily active users
* 1.44 billion monthly active users 
* at 2010, Fof: 7.7 billion edges and 400 million nodes, OoF: 1 billion nodes, 110 billion edges

#### Big Graphs for Prefix Search 
#### Three way tradeoff 
* Memory Consumption 
* Cache Bandwidth
* Compute
      * like MD5 sum

#### Option1: Trie<Name, ID>
* prefix-matching is straightforward, but wastes space, thrashes cache
      * pointers are huge: 8 bytes * million/billions nodes 
      * pointers point to random places 

#### Option2: Sorted Vector of name, ID
* binary search finds range of prefix matches 
* but scales badly as we index more terms, O(n) insertion, move half of them 
* Since the memory use is users * id

#### Option3: Brute Force
* Adjacency list for a graph 
* every node has adjacency list coming out that nodes 
* disadvantage: 1) duplicate save information, 2) if find any information, need to go through each user's friend, and check each
  chunk, cache bandwidth are too big, CPU hot 

#### Option4: Filtered Force 
* Tiny Bloom Filter
* reject of most prefix mismatches
* nicer cache behavior and can trade space for CPU 
![pic](https://cloud.githubusercontent.com/assets/9062406/8119424/3c014e60-104a-11e5-82d1-628d84bd2fec.png)
* 1. Let's say, first find the direct friend "Chuck" in my graph, and try to find the letter 'B' in my FoF
* 2. For the each user, it has the bloom filter, like Chuck, it has two friends "boris" and "zifha", then we just hash the "b" and "z" and set the bloom filter as '1', so when we check 'b', first hash 'b', then check if h('b') set in the bloom filter or not, then filter. 
* 3. In the facebook, for the FoF, use one bloom filter and one hashfunction, for the OoF, use two bloom filter and two hashfunction, one bloom filter for the name, one for the diagram. 

#### C. Global and memcache 
* Merging, Ranking, Returning 
* Fetch per-result rendering information from  memcache 


### Good reference
* [Facebook Typeahead Video](https://www.facebook.com/video/video.php?v=432864835468)
* [How the bloom filter usage?](http://www.quora.com/What-are-the-best-applications-of-Bloom-filters)
* [Linkedin typeahead usage](https://engineering.linkedin.com/open-source/cleo-open-source-technology-behind-linkedins-typeahead-search)
