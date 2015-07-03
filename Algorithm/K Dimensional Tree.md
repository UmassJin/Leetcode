#### Problem
##### Range Search
* find all keys that lie in a 2d range

##### Range Count
* Number of keys that lie in a 2d range

##### Geometric Interpretation
* Keys are point in the plane 
* Find/count points in a given h-v rectangle 

##### Grid Implementation 
* Divide space into M-by-M grid of squares 
* Create list of points contained in each square
* Use 2d array to directly index relevant square
* Insert: add (x, y) to list for corresponding square
* Range search: examine only squares that intersect 2d range query 

* Space: M^2 + N (N is the number of points, M is the square, we create a 2d array)
* Time: 1+ N/M^2 per square examined, on average 

![pic](https://cloud.githubusercontent.com/assets/9062406/8482695/2859c7dc-20a0-11e5-8a2d-fcd9b4deb3c5.png)

#### The problem of Grid Implementation 
* Clustering 

![pic](https://cloud.githubusercontent.com/assets/9062406/8482718/40b153d6-20a0-11e5-859d-c424ee0bee32.png)

#### Implement 

```python
class Point:
    def __init__(self, x = 0, y = 0):
        self.coord = [x, y]

class Node:
    def __init__(self, x, y):
        self.point = Point(x, y)
        self.left = None
        self.right = None

class kDTree:
    def __init__(self):
        self.root = None

    def InsertKDTree(self, point):
        newNode = Node(point.coord[0], point.coord[1])
        depth = 0
        if not self.root:
            self.root = newNode
            return
        self.InsertKDTree(self.root, newNode, depth)
        
    def InsertKDTree(self, root, newNode, depth):
        if not root:
            root = newNode
            return
        # for the even line, if depth % 2 == 0: will use x-axis compare
        # for the odd line, if depth % 2 == 1: will use y-axis compare
        x_y_axis = depth % 2
        if newNode.point.coord[x_y_axis] < root.point.coord[x_y_axis]:
                self.InsertKDTree(root.left, newNode, depth + 1)
        else:   
                self.InsertKDTree(root.right, newNode, depth + 1)
                
    def searchKDTree(self, point):
        if not self.root:
            return False
        self.searchKDTree_helper(self.root, point, 0)
   def searchKDTree_helper(root, point, depth):
       if not root:
           return False

       if root.point.coord[0] == point.coord[0] and \
               root.point.coord[1] == point.coord[1]:
                   return True
       xy_axis = depth % 2
       if point.coord[xy_axis] < root.point.coord[xy_axis]:
           self.searchKDTree_helper(root.left, point, depth+1)
       else:
           self.searchKDTree_helper(root.right, point, depth+1)

```

#### Resolve Problem
* Range search in a 2d tree (check the video)
* Nearest neighbor search in a 2d tree (check the video)

#### Reference
* [Video Algorithm K-d tree](https://www.youtube.com/watch?v=EsY8KSXKe5k)
* [G4G](http://www.geeksforgeeks.org/k-dimensional-tree/)
