#### [Definition](http://en.wikipedia.org/wiki/Cartesian_tree)
a Cartesian tree is a binary tree derived from a sequence of numbers; it can be uniquely defined from the 
properties that it is heap-ordered and that a symmetric (in-order) traversal of the tree returns the original sequence. 

#### Attribute 
1. The Cartesian tree for a sequence has one node for each number in the sequence. Each node is associated with a single sequence value.
2. A symmetric (in-order) traversal of the tree results in the original sequence. That is, the left subtree consists of the values earlier than the root in the sequence order, while the right subtree consists of the values later than the root, and a similar ordering constraint holds at each lower node of the tree.
3. The tree has the heap property: the parent of any non-root node has a smaller value than the node itself.[1]

#### Algorithm
An alternative linear-time construction algorithm is based on the all nearest smaller values problem. 
In the input sequence, one may define the left neighbor of a value x to be the value that occurs prior to x, 
is smaller than x, and is closer in position to x than any other smaller value. The right neighbor is defined symmetrically. 
The sequence of left neighbors may be found by an algorithm that maintains a stack containing a subsequence of the input. 
For each new sequence value x, the stack is popped until it is empty or its top element is smaller than x, and then x is
pushed onto the stack. The left neighbor of x is the top element at the time x is pushed. The right neighbors may be found 
by applying the same stack algorithm to the reverse of the sequence. The parent of x in the Cartesian tree is either the 
left neighbor of x or the right neighbor of x, whichever exists and has a larger value. The left and right neighbors may 
also be constructed efficiently by parallel algorithms, so this formulation may be used to develop efficient parallel 
algorithms for Cartesian tree construction

#### Example
##### [Max Tree](https://github.com/UmassJin/Leetcode/blob/master/LintCode/Max_Tree.py)
