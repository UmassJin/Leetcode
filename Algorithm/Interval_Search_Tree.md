#### Definition
assume no two intervals has the same left key

Every node of Interval Tree stores following information.
* a) i: An interval which is represented as a pair [low, high]
* b) max: Maximum high value in subtree rooted at this node.
* c) use left endpoint as BST key 


#### Interval Search Tree interface 
* Insert an interval (lo, hi)
* Search an interval (lo, hi)
* Delete an interval (lo, hi)
* Interval intersection query. given an interval (lo, hi), find all intervals in data structure overlapping (lo, hi)




#### Reference
* [Interval Tree G4G](http://www.geeksforgeeks.org/interval-tree/)
* [Video BST](https://www.youtube.com/watch?v=q0QOYtSsTg4)
