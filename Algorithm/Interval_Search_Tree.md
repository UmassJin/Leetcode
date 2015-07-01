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

#### The time complexity of Interval Search tree
![pic](https://cloud.githubusercontent.com/assets/9062406/8466850/fbc28afe-200b-11e5-88b6-1da15f90a0ec.png)


### Compare different tree

All these data structures are used for solving different problems:

##### Segment tree stores intervals
optimized for "which of these intervals contains a given point" queries.

##### Interval tree stores intervals as well
optimized for "which of these intervals overlap with a given interval" queries. It can also be used for point queries - similar to segment tree.

##### Range tree stores points
optimized for "which points fall within a given interval" queries.

##### Binary indexed tree stores items-count per index
for "how many items are there between index m and n" queries.


#### Performance / Space consumption for one dimension:

* Segment tree - O(n logn) preprocessing time, O(k+logn) query time, O(n logn) space
* Interval tree - O(n logn) preprocessing time, O(k+logn) query time, O(n) space
* Range tree - O(n logn) preprocessing time, O(k+logn) query time, O(n) space
* Binary Indexed tree - O(n logn) preprocessing time, O(logn) query time, O(n) space
(k is the number of reported results).

All data structures can be dynamic, in the sense that the usage scenario includes both data changes and queries:

* Segment tree - interval can be added/deleted in O(logn) time (see here)
* Interval tree - interval can be added/deleted in O(logn) time
* Range tree - new points can be added/deleted in O(logn) time (see here)
* Binary Indexed tree - the items-count per index can be increased in O(logn) time
Higher dimensions (d>1):

* Segment tree - O(n(logn)^d) preprocessing time, O(k+(logn)^d) query time, O(n(logn)^(d-1)) space
* Interval tree - O(n logn) preprocessing time, O(k+(logn)^d) query time, O(n logn) space
* Range tree - O(n(logn)^d) preprocessing time, O(k+(logn)^d) query time, O(n(logn)^(d-1))) space
* Binary Indexed tree - O(n(logn)^d) preprocessing time, O((logn)^d) query time, O(n(logn)^d) space



#### Implement 

```python
class Interval:
    def __init__(self, low = None, high = None):
        self.low = low
        self.high = high

class IntervalTree_Node:
    def __init__(self, low = None, high = None, imax = None):
        self.interval = Interval(low, high)
        self.imax = imax
        self.left = IntervalTree_Node()
        self.right = IntervalTree_Node()
        
class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, root, interval):
        if not root:
            return IntervalTree_Node(interval.low, interval.high, interval.high)

        rootlow = root.interval.low
        
        # Insert the interval into the Tree 
        if interval.low < rootlow:
            root.left = self.insert(root.left, interval)
        elif interval.low > rootlow:
            root.right = self.insert(root.right, interval)
            
        # Update the max in the Tree path
        if interval.high > root.imax:
            root.imax = interval.high

        return root
    
    def find_overlap(self, root, interval):
        if not root: return None
        if root.interval.low <= interval.high and root.interval.high >= interval.low:
            return root.interval
        if root.left and root.left.imax > interval.low:
            return self.find_overlap(root.left, interval)
        else:
            return self.find_overlap(root.right, interval)
```



#### Reference
* [Interval Tree G4G](http://www.geeksforgeeks.org/interval-tree/)
* [Video BST](https://www.youtube.com/watch?v=q0QOYtSsTg4)
* [Different between segment tree and interval tree](http://stackoverflow.com/questions/17466218/what-are-the-differences-between-segment-trees-interval-trees-binary-indexed-t)
