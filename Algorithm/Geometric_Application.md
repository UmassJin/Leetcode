#### 1D range count
    * Insert key-value pair
    * Search for key k
    * Delete key k
    * Range search: find all keys between k1 and k2
    * Range count: number of keys between k1 and k2

* Use the BST 
    * keep the keys in BST, the keys could be the count that how many keys are less than this character
        * for example: 
        ![pic](https://cloud.githubusercontent.com/assets/9062406/8469463/0324385a-2030-11e5-8bcf-54bded3c43e6.png)    

#### Line Segment Intersection
      * Problem: Check all pairs of line segments for intersection
      * Resolution: sweep-line algorithm 

#### Intersection of two line segment 
      * Orientation:
         * –counterclockwise
         * –clockwise
         * –colinear
      * How to calculate Orientation
      
![pic](https://cloud.githubusercontent.com/assets/9062406/8470461/7eafea04-2040-11e5-9927-99e7dd26e65c.png)
![pic](https://cloud.githubusercontent.com/assets/9062406/8470767/3c8c8312-2045-11e5-8040-8a6be6aa488f.png)            

#### Implement


```python
'''
0: p, q and r are colinear
1: clockwise
2: counterclockwise
'''

class Point:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

def orientation(p, q, r):
    val = (q.y - p.y)*(r.x - q.x) - (q.x - p.x)*(r.y - q.y)
    if val == 0: return 0
    if val > 0:
        return 1 # clockwise
    else: return 2 # counterclockwise
    
def onSegment(p, q, r):
    if q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and \
            q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y):
                return True
    else:   
        return False
    
def checkIntersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    
    if (o1 != o2) and (o3 != o4):
        return True
    
    if ((o1 == 0 and onSegment(p1, p2, q1)) or\
        (o2 ==0 and onSegment(p1, q2, q1)) or\
        (o3 == 0 and onSegment(p2, p1, q2)) or\
        (o4 == 0 and onSegment(p2, q1, q2))):
                return True
    return False
    
```


#### Reference:
* http://www.geeksforgeeks.org/given-a-set-of-line-segments-find-if-any-two-segments-intersect/
* http://www.dcs.gla.ac.uk/~pat/52233/slides/Geometry1x1.pdf
* http://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
