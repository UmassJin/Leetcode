#### [Segment Tree](http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)

#### Scenario 1: Find sum and update the value in array in O(logn)
We have an array arr[0 . . . n-1]. We should be able to
    * 1 Find the sum of elements from index l to r where 0 <= l <= r <= n-1
    * 2 Change value of a specified element of the array arr[i] = x where 0 <= i <= n-1.

* A simple solution is to run a loop from l to r and calculate sum of elements in given range. To update a value, simply do arr[i] = x. The first operation takes O(n) time and second operation takes O(1) time.

* Another solution is to create another array and store sum from start to i at the ith index in this array. Sum of a given range can now be calculated in O(1) time, but update operation takes O(n) time now. This works well if the number of query operations are large and very few updates.

* What if the number of query and updates are equal? Can we perform both the operations in O(log n) time once given the array? We can use a Segment Tree to do both operations in O(Logn) time.

* Representation of Segment trees
    * 1. Leaf Nodes are the elements of the input array.
    * 2. Each internal node represents some merging of the leaf nodes. 
        The merging may be different for different problems. For this problem, merging is sum of leaves under a node.

* An array representation of tree is used to represent Segment Trees. For each node at index i, the left child is at index 2*i+1, right child at 2*i+2 and the parent is at st1.

####[Implement](http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)

```python
# Here we do not need to create a class TreeNode for the segment tree

def constructST(array):
    if not array:
        return None
    # leaf nodes is n, internal nodes is n-1 for full tree
    n = len(array)
    maxsize = 2 * n + 1
    segmentTree = [0 for i in xrange(maxsize)]
    # 注意这里，我们是将array的长度，0到n-1传递到function中
    constructST_helper(array, 0, n - 1, segmentTree, 0)
    print "seg:", segmentTree
    return segmentTree

# Here index always point to the segmentTree index, and start, end are the index 
# in the input array
def constructST_helper(array, start, end, segmentTree, index):
    if start == end:
        segmentTree[index] = array[start]
        return segmentTree[index]

    mid = (start + end) / 2
    segmentTree[index] = constructST_helper(array, start, mid, segmentTree, index*2+1) +\
                    constructST_helper(array, mid+1, end, segmentTree, index*2+2)
    return segmentTree[index]

def getsum(segmentTree, n, start, end):
    if start < 0 or end > n or start > end:
        return -1
    return getsum_helper(segmentTree, 0, n-1, start, end, 0)
    
def getsum_helper(segmentTree, arr_s, arr_e, qs, qe, index):
    # Note the changes here: 
    # only in the following scenario, we return the segmentTree[index]
    # [ qs, [arr_s, arr_e], qe]
    if arr_s >= qs and arr_e <= qe:
        return segmentTree[index]

    if (qs > arr_e) or (qe < arr_s):
        return 0

    mid = (arr_s + arr_e) / 2
    return getsum_helper(segmentTree, arr_s, mid, qs, qe, index*2+1) +\
            getsum_helper(segmentTree, mid+1, arr_e, qs, qe, index*2+2)

# update arr[index] = value
# Here we first update the arr[index] = value, calculate the diff 
# and then search in the segmenttree, note here we still pass the length of arrary 
# into the helper function 
def update(arr, segmentTree, index, value):
    if index < 0 or index > len(arr) - 1:
        return

    diff = value - arr[index]
    arr[index] = value

    update_helper(segmentTree, 0, len(arr)-1, index, diff, 0)

'''
@segmentTree: is the segmentTree after construct
@arr_s is the array start, not the segmentTree start
@arr_e is the array end, not the segmentTree end
@i is the index which get change
@ diff is the difference btw new value and old value
@ index is the index in segmentTree
'''
def update_helper(segmentTree, arr_s, arr_e, i, diff, index):
    if i < arr_s or i > arr_e:
        return
    segmentTree[index] += diff
    if arr_s != arr_e:
        mid = (arr_s + arr_e) / 2
        update_helper(segmentTree, arr_s, mid, i, diff, index*2 + 1)
        update_helper(segmentTree, mid+1, arr_e, i, diff, index*2 + 2)


test = [1,3,5,7,9,11]
segment = constructST(test)
print getsum(segment, len(test), 2, 4)
update(test, segment, 3, 8)
print getsum(segment, len(test), 2, 4)
```


#### Scenario 2: Range Minimum Query
##### We have an array arr[0 . . . n-1]. We should be able to efficiently find the minimum value from index qs (query start) to qe (query end) where 0 <= qs <= qe <= n-1. The array is static (elements are not deleted and inserted during the series of queries)

* Segment tree can be used to do preprocessing and query in moderate time. With segment tree, preprocessing time is O(n) and time to for range minimum query is O(Logn). The extra space required is O(n) to store the segment tree.

* Representation of Segment trees
      * 1. Leaf Nodes are the elements of the input array.
      * 2. Each internal node represents minimum of all leaves under it.

#### [Implement](http://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/)
```python
def constructST(array):
    if not array: return []
    n = len(array)
    maxsize = 2 * n + 1
    segmentTree = [(1<<31)-1 for i in xrange(maxsize)]
    constructST_helper(array, 0, n-1, segmentTree, 0)
    print "segmentTree: ", segmentTree
    return segmentTree

def constructST_helper(array, start, end, segmentTree, index):    
    if start == end:
        segmentTree[index] = array[start]
        return segmentTree[index]

    mid = (start + end)/2
    segmentTree[index] = min(constructST_helper(array, start, mid, segmentTree, index*2+1),
                constructST_helper(array, mid+1, end, segmentTree, index*2+2))
    return segmentTree[index]

def RMQ(segmentTree, n, start, end):
    if start < 0 or end > n-1 or start > end:
        return -1
    return RMQ_helper(segmentTree, 0, n-1, start, end, 0)

def RMQ_helper(segmentTree, arr_s, arr_e, qs, qe, index):
    if (arr_s >= qs) and (arr_e <= qe):
        return segmentTree[index]
    
    if qe < arr_s or qs > arr_e:
        return (1<<31)-1

    mid = (arr_s + arr_e) / 2
    return min(RMQ_helper(segmentTree, arr_s, mid, qs, qe, index*2 + 1),
            RMQ_helper(segmentTree, mid+1, arr_e, qs, qe, index*2 + 2))
    
test = [2,5,1,4,9,3]
seg = constructST(test)
print RMQ(seg, len(test), 3,5)

```


#### Reference:
* [G4G Set1](http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)
* [G4G Set2 Range Minimum Query](http://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/)
* [RMQ topcoder](https://www.topcoder.com/community/data-science/data-science-tutorials/range-minimum-query-and-lowest-common-ancestor/#Range_Minimum_Query_(RMQ))
