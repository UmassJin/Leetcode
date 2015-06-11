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

#### Friend of Friend
1. Distributed Graph Search Service, use the prefix matching 
      * For some users which has the tiny friend, will seach the three degrees out
![pic](https://cloud.githubusercontent.com/assets/9062406/8112857/82a1e88c-101f-11e5-952a-62ba219dbce6.png)

#### Object of Friend
![pic](https://cloud.githubusercontent.com/assets/9062406/8112987/2a09e7a0-1020-11e5-8016-5c15164a2216.png)

#### Static status
* Around 936 million daily active users
* 1.44 billion monthly active users 
* at 2010, Fof: 7.7 billion edges and 400 million nodes, OoF: 1 billion nodes, 110 billion edges
* 
