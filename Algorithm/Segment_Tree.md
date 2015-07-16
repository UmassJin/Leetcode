#### [Segment Tree](http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)

#### Scenario 1: Find sum and update the value in array in O(logn)
We have an array arr[0 . . . n-1]. We should be able to

1)  Find the sum of elements from index l to r where 0 <= l <= r <= n-1

2)  Change value of a specified element of the array arr[i] = x where 0 <= i <= n-1.

* A simple solution is to run a loop from l to r and calculate sum of elements in given range. To update a value, simply do arr[i] = x. The first operation takes O(n) time and second operation takes O(1) time.

* Another solution is to create another array and store sum from start to i at the ith index in this array. Sum of a given range can now be calculated in O(1) time, but update operation takes O(n) time now. This works well if the number of query operations are large and very few updates.

* What if the number of query and updates are equal? Can we perform both the operations in O(log n) time once given the array? We can use a Segment Tree to do both operations in O(Logn) time.

* Representation of Segment trees
    * 1. Leaf Nodes are the elements of the input array.
    * 2. Each internal node represents some merging of the leaf nodes. 
        The merging may be different for different problems. For this problem, merging is sum of leaves under a node.

* An array representation of tree is used to represent Segment Trees. For each node at index i, the left child is at index 2*i+1, right child at 2*i+2 and the parent is at st1.

* One optimization:
    * 只存和，会导致每次加数的时候都要更新 到叶子节点，速度太慢，这是必须要避免的。
本题树节点结构：
```c
struct CNode
{
int L ,R; //区间起点和终点
CNode * pLeft, * pRight;
long long nSum; //原来的和
long long Inc; //增量c的累加
}; //本节点区间的和实际上是nSum+Inc*(R-L+1)
```
    * 在增加时，如果要加的区间正好覆盖一个节点，则增加其节点的Inc值，不再往下走 ，否则要更新nSum,再将增量往下传
    * 在查询时，如果待查区间不是正好覆盖一个节点，就将节点的Inc往下带，然后将Inc代表的所有增量累加到nSum上后将Inc清0，接下来再往下查询。

####[Implement](http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)

```python
# Here we do not need to create a class TreeNode for the segment tree
# Time complexity: O(n)
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

# Time complexity: O(logn)
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

# Time complexity: O(logn)
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

#### Scenario 3: interview question, recover the array

```python
'''
55. 给定一个数字数组 ,其中每个元素是从末端数小于原数组中该元素的个数。求原数组。
原数组中元素是一个[1,n]的随机排列。

For example:
Count array: [3, 0, 1, 0]
Original array: [4, 1, 3, 2]

Can you give an O(nlogn) solution?
original question: http://www.mitbbs.com/article_t/JobHunting/32856675.html

分析：
Count array 就是一个rank
表示当前数字在还存在的[1..n]中的第几个

count array 
i  C[3,0,1,0]   N[1,2,3,4] 
0 C[0] = 3     N中第3个,N[3] = 4,在N里面删除4, N=[1,2,3]
1 C[1] = 0     N中第0个,N[0] = 1,在N里面删除1, N=[2,3]
2 C[2] = 1     N中第1个,N[1] = 3,在N里面删除3, N=[2]
3 C[3] = 0     N中第0个,N[0] = 2

所以答案是4 1 3 2

# 思路
1. 先简历一个segmenttree, 从[0, n-1]
2. find_kth function, which find tree 中 the kth �小的数字
3. delete that node, then find next one 
'''


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = 0
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, irange):
        self.root = self.build_tree(0, irange-1)

    def build_tree(self, left, right):
        if left > right: return None
        newnode = Node(left, right)
        if left == right:
            newnode.count = 1
            return newnode

        mid = (left + right) / 2
        newnode.left = self.build_tree(left, mid)
        newnode.right = self.build_tree(mid+1, right)
        newnode.count = newnode.left.count + newnode.right.count
        return newnode

    def get_kth(self, k):
        cur = self.root
        while cur:
            if cur.start == cur.end:
                return cur.start
            left_cover = 0
            if cur.left:
                left_cover = cur.left.count
            if k < left_cover:
                cur = cur.left
            else:
                k -= left_cover
                cur = cur.right
        return -1

    def remove_leaf(self, val):
        self.remove_helper(self.root, val)

    def remove_helper(self, cur, val):
        if not cur: return
        cur.count -= 1
        if cur.left and cur.left.start == val and cur.left.end == val:
            cur.left = None

        if cur.right and cur.right.start == val and cur.right.end == val:
            cur.right = None
        mid = (cur.start + cur.end)/2
        if val <= mid:
            self.remove_helper(cur.left, val)
        else:
            self.remove_helper(cur.right, val)

if __name__ == "__main__":
    array = [3, 0, 1, 0]
    test = SegmentTree(4)
    result = []
    for i in array:
        print "i: ", i
        kth = test.get_kth(i)
        print "kth: ", kth
        result.append(kth + 1)
        test.remove_leaf(kth)
    print result
```


#### Reference:
* [G4G Set1](http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/)
* [G4G Set2 Range Minimum Query](http://www.geeksforgeeks.org/segment-tree-set-1-range-minimum-query/)
* [RMQ topcoder](https://www.topcoder.com/community/data-science/data-science-tutorials/range-minimum-query-and-lowest-common-ancestor/#Range_Minimum_Query_(RMQ))
