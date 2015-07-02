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


#### Reference
* [Video Algorithm K-d tree](https://www.youtube.com/watch?v=EsY8KSXKe5k)
* [G4G](http://www.geeksforgeeks.org/k-dimensional-tree/)
