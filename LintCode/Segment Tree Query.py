'''
or an integer array (index from 0 to n-1, where n is the size of this array), in the corresponding SegmentTree, each node stores an extra attribute max to denote the maximum number in the interval of the array (index from start to end).

Design a query method with three parameters root, start and end, find the maximum number in the interval [start, end] by the given root of segment tree.

Have you met this question in a real interview? Yes
Example
For array [1, 4, 2, 3], the corresponding Segment Tree is:

                  [0, 3, max=4]
                 /             \
          [0,1,max=4]        [2,3,max=3]
          /         \        /         \
   [0,0,max=1] [1,1,max=4] [2,2,max=2], [3,3,max=3]
query(root, 1, 1), return 4

query(root, 1, 2), return 4

query(root, 2, 3), return 3

query(root, 0, 2), return 4
'''


"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        this.start, this.end, this.max = start, end, max
        this.left, this.right = None, None
"""
import sys 

class Solution:	
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The maximum number in the interval [start, end]
    def query(self, root, start, end):
        if start > end:
            return -sys.maxint
        
        if root.start >= start and root.end <= end:
            return root.max 
        
        imax = -sys.maxint
        
        if root.left:
            left = self.query(root.left, start, end)
            imax = max(imax, left)
        if root.right:
            right = self.query(root.right, start, end)
            imax = max(imax, right)
            
        return imax 


