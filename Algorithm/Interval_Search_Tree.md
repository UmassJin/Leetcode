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

#### Insert an interval (lo, hi)
* Use the lo as the key, and same like the BST insert 
* Update max in each node on serach path 


#### Search a intersects (lo, hi)
* if interval in node intersects query interval, return it
* elif left subtree is None, go right
* elif max end point in left subtree is less than lo, go right
* else go left 

### The time complexity of Interval Search tree
![pic](https://cloud.githubusercontent.com/assets/9062406/8466850/fbc28afe-200b-11e5-88b6-1da15f90a0ec.png)

#### Reference
* [Interval Tree G4G](http://www.geeksforgeeks.org/interval-tree/)
* [Video BST](https://www.youtube.com/watch?v=q0QOYtSsTg4)
