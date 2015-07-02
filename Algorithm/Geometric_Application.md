* 1D range count
    * Insert key-value pair
    * Search for key k
    * Delete key k
    * Range search: find all keys between k1 and k2
    * Range count: number of keys between k1 and k2

* Use the BST 
    * keep the keys in BST, the keys could be the count that how many keys are less than this character
        * for example: 
        ![pic](https://cloud.githubusercontent.com/assets/9062406/8469463/0324385a-2030-11e5-8bcf-54bded3c43e6.png)    

* Line Segment Intersection
      * Problem: Check all pairs of line segments for intersection
      * Resolution: sweep-line algorithm 

* Intersection of two line segment 
      * Orientation:
         * –counterclockwise
         * –clockwise
         * –colinear
      * How to calculate Orientation
      ![pic](https://cloud.githubusercontent.com/assets/9062406/8470461/7eafea04-2040-11e5-9927-99e7dd26e65c.png)
      
      * Reference:
      * http://www.dcs.gla.ac.uk/~pat/52233/slides/Geometry1x1.pdf
      * http://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
      
      

#### Reference:
* http://www.geeksforgeeks.org/given-a-set-of-line-segments-find-if-any-two-segments-intersect/
