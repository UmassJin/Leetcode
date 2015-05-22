#! /usr/bin/env python
'''
/**
 * http://blog.csdn.net/luckyxiaoqiang/article/details/7518888  轻松搞定面试中的二叉树题目 
 * http://www.cnblogs.com/Jax/archive/2009/12/28/1633691.html  算法大全（3） 二叉树 
 *  
 * TODO: 一定要能熟练地写出所有问题的递归和非递归做法！ 
 * 
 * 1. 前序遍历，中序遍历，后序遍历: preorderTraversalRec, preorderTraversal, inorderTraversalRec, postorderTraversalRec 
 * (https://en.wikipedia.org/wiki/Tree_traversal#Pre-order_2) 
 * 2. 分层遍历二叉树（按层次从上往下/从下往上，从左往右）: levelTraversal, levelTraversalRec（递归解法！） 
 * 3. 求最大最小二叉树的深度: getDepthRec（递归），getDepthRec, find MAX/MIN depth 
 * 4. 判断二叉树是不是二叉搜索树
 * 5. 给定一个数字n，可以写出多少相关的二叉搜索树, optimization: 列出所有的二叉树
 * 6. 判断二叉树是不是平衡二叉树：isAVLRec 
 * 7. 判断两个树是否互相镜像：isMirrorRec 
 * 8. 判断两棵二叉树是否相同的树：isSameRec, isSame 
 * 9. 计算二叉树从根节点到叶子节点的合
 * 10. 给定一个数字，判断是否存在路径的合，并别输出这个路径
 * 11 找出一个二叉搜索树中被颠倒的两个节点
 * 12 将一个二叉树变成flatten tree based on pre-order
 * 13 Convert the sorted array to the BST 
 * 14. 由前序遍历序列和中序遍历序列重建二叉树：rebuildBinaryTreeRec  
 * 15. 由后序遍历序列和中序遍历序列重建二叉树：rebuildBinaryTreeRec 
 * 16. 求二叉树中节点的最大距离：getMaxDistanceRec 
 * 17. 按照z字形输出树的节点
 * 18. 将二叉查找树变为有序的双向链表: convertBST2DLLRec, convertBST2DLL 
 * 19. 求二叉树第K层的节点个数：getNodeNumKthLevelRec, getNodeNumKthLevel 
 * 20. 求二叉树中叶子节点的个数：getNodeNumLeafRec, getNodeNumLeaf 
 * 21. 求二叉树中两个节点的最低公共祖先节点：getLastCommonParent, getLastCommonParentRec, getLastCommonParentRec2 
 * 22. 求二叉树的镜像（破坏和不破坏原来的树两种情况）：mirrorRec, mirrorCopyRec 
 * 23.判断二叉树是不是完全二叉树：isCompleteBinaryTree, isCompleteBinaryTreeRec 
 * 24. Populating Next Right Pointers in Each Node 
 * 25. Convert Sorted List to Binary Search Tree 
 */  
'''

class tree_node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def create_minimum_BST(datalist, start, end):
    if end < start:
        return None
    mid = (start + end) / 2
    n = tree_node(datalist[mid])
    n.left = create_minimum_BST(datalist, start, mid-1)
    n.right = create_minimum_BST(datalist, mid+1, end)
    return n

# DFS: use the stack to implement 
# BFS: use the queue to implement 
# 1) Inorder Recursive 
def in_order_traverse_rec(root):
    result = []
    in_order_rec(result,root)
    return result

def in_order_rec(result,root):
    if not root: return
    in_order_rec(result, root.left)
    result.append(root.val)
    in_order_rec(result, root.right)

# 2) Inorder Iterative (DFS)
def in_order_traverse_iter(root):
    stack = []; result = []
    node = root
    while True:
        while node:
            stack.append(node)
            node = node.left

        if not stack: break
        node = stack.pop()
        result.append(node.val)
        node = node.right
    return result

# 3) Preorder Recursive 
def preorder_traverse_rec(root):
    result = []
    pre_order_rec(result,root)
    return result

def pre_order_rec(result,root):
    if not root: return
    result.append(root.val)
    pre_order_rec(result, root.left)
    pre_order_rec(result, root.right)

# 4) Preorder Iterative (DFS)
def preorder_traverse_iter(root):
    stack = [root]; result = []
    while stack: # Use while ! 
        node = stack.pop()
        if node: # check if node !
            result.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return result

# 5) Postorder Recursive
def postorder_traverse_rec(root):
    result = []
    post_order_rec(result,root)
    return result

def post_order_rec(result,root):
    if not root: return
    post_order_rec(result, root.left)
    post_order_rec(result, root.right)
    result.append(root.val)

# 6) Postorder Iterative (DFS)
def postorder_traverse_iter(root):
    stack = [root]; result = []

    if not root: return result # Note: Check!
    while stack:
        node =stack.pop()
        result.insert(0,node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result

# 7) Level Traversal from top to bottom, recursion 
def levelOrder_rec(root):
    result = []
    level_order(root, 0, result)
    return result

def level_order(node, level, result):
    if node:                        # Note: here if check !
        if len(result) < level + 1: # Note: the condition here 
            result.append([])
        result[level].append(node.val)
        level_order(node.left, level+1, result)
        level_order(node.right, level+1, result)
  
# 8) Level Traversal from top to bottom, iteration  
def levelOrder_iter(root):
    result = [];queue=[root]
    if not root: return result

    while queue:
        sublist = []
        length = len(queue)
        for i in xrange(length):  # Note: here we need to iterate each element in queue
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            sublist.append(node.val)
        result.append(sublist)
    return result

# 9) Level Traversal from bottom to top, recursion 
def levelOrderBottom_rec(root):
    result = []
    if not root: return result  # Note: check the root = None !!
    level_bottom_rec(root, result, 0)
    return result

def level_bottom_rec(root, result, level):
    if root:
        if len(result) < level + 1:
            result.insert(0,[])
        result[len(result)-level-1].append(root.val)
        level_bottom_rec(root.left, result, level+1)
        level_bottom_rec(root.right, result, level+1)

# 10) Level Traversal from bottom to top, iteration  
def levelOrderBottom_iter(root):
    queue = [root]; result = []
    if not root: return result

    while queue:
        qlist = []
        length = len(queue)
        for i in xrange(length):
            node = queue.pop(0)
            qlist.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.insert(0, qlist)
    return result
    
# Use deque 
from collections import deque

def levelOrderBottom(self, root):
        if not root: return []
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            subresult = []
            for _ in xrange(len(queue)):
                node = queue.popleft()
                if node:
                    subresult.append(node.val)
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
            result.insert(0, subresult)
        return result 

# 11) Find the Minimum Depth of the tree, recursion
def minDepth_rec(root):
    if not root: return 0
    if (root.left and not root.right):
        return minDepth_rec(root.left)+1
    if (not root.left and root.right):
        return minDepth_rec(root.right)+1
    return min(minDepth_rec(root.left),minDepth_rec(root.right))+1

# 12) Find the Minimum Depth of the tree, iteration 
def minDepth_iter(root):
    queue = []; depth = 0
    if not root: return depth
    queue.append((root,1))

    while queue:
        node, depth = queue.pop(0)
        if node.left: queue.append((node.left,depth+1))
        if node.right:queue.append((node.right,depth+1))
        if not node.left and not node.right:
            return depth

# 13) Find the Maximum Depth of the tree, recursion
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# 注意这里find maxDepth recursion is different from find minDepth recursion, 
# 因为对于minDepth recursion, 我们需要考虑到，1, 2, None, 3, None, 所有节点都在
# 左子树或者右子树的情况，如果仅仅判断 min(minDepth(root.left), minDepth(root.right)) + 1
# 很容易出现最后depth为1，因为minDepth(root.right) always equal to 0, 但是求max不存在这个问题

# 14) Find the Maximum Depth of the tree, iteration
def maxDepth_iter(root):
    queue = []; depth = 0
    if not root: return depth
    queue.append((root,1))

    while queue:
        node, depth = queue.pop(0)
        if node.left: queue.append((node.left,depth+1))
        if node.right:queue.append((node.right,depth+1))
        if not node.left and not node.right:
            continue
    return depth

# 15) determine if the tree is a valid BST, recursion
def isValidBST_rec(root):
    return check_validBST(root,-(1<<31)-1,1<<31) 
    # Note: max:1<<31-1, min:-1<<31, but here each one need to +1

def check_validBST(root,min_val,max_val):
    if not root: return True  # Check here!
    if root.val <= min_val or root.val >= max_val: return False     
    return (check_validBST(root.left,min_val,root.val) and check_validBST(root.right,root.val,max_val))


# 16) determine if the tree is a valid BST, iteration
def isValidBST_iter(root):
    stack = []; pre= None;node = root
    while stack or node:
        while node:                
            stack.append(node)                
            node = node.left
        node = stack.pop()
        if pre and node.val <= pre.val: return False
        pre,node = node,node.right
    return True

# 17) Given n, how many unique BST ?
def numTrees(n):
    if n <= 1: return 1
    result = 0
    for i in xrange(1,n+1):
        result += numTrees(i-1)*numTrees(n-i)
    return result

# DP (46ms)    
def numTrees_dp(n):
    result = [0 for i in xrange(n+1)]
    result[0] = 1; result[1] = 1

    for i in xrange(2, n+1):
        for j in xrange(1, n+1):
            result[i] += result[j-1]*result[i-j]
    return result[n]

# 18) Given n, how many unique BST, display all of them.
def generateTrees(n):
    return dfs(1,n)

def dfs(start, end):
    if start > end: return [None]
    res = []
    for i in xrange(start, end+1):
        left = dfs(start, i-1)
        right = dfs(i+1, end)
        for l in left:
            for r in right:
                root = tree_node(i)
                root.left = l
                root.right = r
                res.append(root)
    return res

# 19) Determine if a binary tree is the height-balanced tree
def isBalanced(root):
       global result
       result = True
       getheight(root)
       return result

def getheight(root):
        global result
        if not root: return 0
        left = getheight(root.left)
        right = getheight(root.right)

        if abs(left-right) > 1:
            result = False
        return max(left,right) + 1

# 20) Determine if the tree is a mirror of itself 
# Recursion 
def isSymmetric_rec(root):
    if not root: return True # Note this check !
    return check_symmetric(root.left, root.right)

def check_symmetric(left, right):
    if not left and not right: return True    # Note this check !
    if not left or not right: return False
    return (left.val == right.val and check_symmetric(left.left, right.right) and \
            check_symmetric(left.right, right.left))

# Iteration 
def isSymmetric_iter(root):
    if not root: return True
    queue = [(root.left, root.right)]

    while queue:
        left, right = queue.pop(0)
        if not left and not right: continue
        if not left or not right: return False
        if left.val != right.val: return False
        queue.append((left.right,right.left))
        queue.append((left.left,right.right))
    return True

# 21) Same tree or not ?
def isSameTree(p, q):
    if not p and not q: return True
    if not q or not p: return False
    if p.val != q.val: return False
    return (isSameTree(p.left,q.left) and isSameTree(p.right,q.right))

def isSameTree(p,q):
    if not p and not q: return True
    if not q or not p: return False
    queue = [(p, q)]
    while queue:
        p, q = queue.pop(0)
        if not p and not q: continue
        if not p or not q: return False
        if p.val != q.val: return False
        queue.append((p.left,q.left))
        queue.append((p.right, q.right))
    return True

# 22) sum from root-to-leaf
def hasPathSum(root, sum):
    if not root: return False
    sum = sum - root.val
    if not root.left and not root.right:
        if sum == 0: return True
        else: return False
    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)

# 这道题容易做错的几点: 
# 1) sum < 0: 不一定false，因为节点数字可能<0
# 2) 必须在 root.left 和 root.right 全部为 None 的时候，才可以判断sum为0时候为True
#    因为有可能在中间节点的时候，sum 为0
# 面试时候碰到这个题目，可以提问几点
# 每个节点的node为positive的数字还是negative的？

    
# 23) sum from root-to-leaf, print out all the path
def pathSum(root, sum):
    result = []
    path_sum(root, sum, result, [])
    return result

def path_sum(root, sum, result, res_list):
    if not root: return 
    if not root.left and not root.right:
        if sum == root.val:
            res_list.append(root.val)
            result.append(res_list[:]) # Note: here we should give the res_list[:] not the res_list!!!
            res_list.pop()
    path_sum(root.left, sum - root.val, result, res_list+[root.val])
    path_sum(root.right, sum - root.val, result, res_list+[root.val])

# 注意，我们在将res_list append到result的时候，如果不用res_list[:]，我们其实没有make a copy,
# 此时 result[0] 的地址和res_list的地址是一样的，所以之后将res_list.pop()，result[0]里面的也被pop
# 出来了，所以如果直接append会有如下的结果，会发现sublist和result[0]的地址是一样的
'''
[JINZH2-M-20GQ: ~/Desktop/Python_training/Leetcode]: python path_sum2.py
sublist:  [1]
result:  [[1]]
id: result:  4375484248
id: result[0]:  4375560560
id: sublist:  4375560560
out result id:  4375484248
[[]]
'''

# The other method 
def pathSum_1(root, sum):
    def getpath(node,cursum,curlist):
        if not node.left and not node.right:
            if cursum == sum: return result.append(curlist)
        if node.left:
            getpath(node.left,cursum+node.left.val,curlist+[node.left.val])
        if node.right:
            getpath(node.right,cursum+node.right.val,curlist+[node.right.val])

    if not root: return []
    result = [];curlist = [root.val]
    getpath(root,root.val,curlist)

# 24) Zigzag Level Order Traversal
def zigzagLevelOrder_rec(root):
    result = []
    zig_order(root, result, 0)
    return result

def zig_order(root, result, level):
    if root:
        if len(result) < level + 1:
            result.append([])
        if level % 2 == 0:
            result[level].append(root.val)
        else:
            result[level].insert(0, root.val)
        zig_order(root.left, result, level +1)
        zig_order(root.right, result, level +1)

# Zigzag level Order Iteration 
def zigzagLevelOrder_iter(root):
    queue = [root]
    result = []
    if not root: return result

    while queue:
        res_list = []
        for i in xrange(len(queue)):
            q = queue.pop(0)
            res_list.append(q.val)
            if q.left: queue.append(q.left)
            if q.right: queue.append(q.right)

        if len(result) %2 == 0:
            result.append(res_list)
        else:
            result.append(res_list[::-1])
    return result

# 25) Find the total sum of all root-to-leaf numbers
# Recursion:
def sumNumbers_rec(root):
    return addsum(root,0)

def addsum(root, sumvalue):
    if not root: return 0
    sumvalue = sumvalue*10 + root.val # Good pointer is here !! 
    if not root.left and not root.right: return sumvalue
    return addsum(root.left, sumvalue) + addsum(root.right, sumvalue)

# Iteration:
def sumNumbers_iter(root):
    if not root: return 0
    queue = [root.val]; nodelist = [root]; result = 0 
    while nodelist:
            node = nodelist.pop()  # Note: here we use two queue!!!
            tmpval = queue.pop()
            
            if node.left:
                nodelist.append(node.left)
                queue.append(tmpval*10+node.left.val)
                
            if node.right:
                nodelist.append(node.right) 
                queue.append(tmpval*10+node.right.val)
            
            if not node.left and not node.right:
                result = result + tmpval

    return result 

# 26) Construct Binary Tree from Preorder and Inorder Traversal 
def buildTree(preorder, inorder):
    return buildfunc(0,preorder,0,len(inorder)-1,inorder)

def buildfunc(prestart,preorder,instart,inend,inorder):
    if instart > inend or prestart > len(preorder)-1: return None
    node = TreeNode(preorder[prestart])
    index = inorder.index(preorder[prestart])
    node.left = buildfunc(prestart+1,preorder,instart,index-1,inorder)
    node.right = buildfunc(prestart+index-instart+1,preorder,index+1,inend,inorder) # index important!!!
    return node

# 27) Construct Binary Tree from Inorder and Postorder Traversal 
def buildTree_in_post(inorder, postorder):
    if len(inorder) == 0 and len(postorder) ==0: return None
    return buildfunc_in_post(0,len(inorder)-1,inorder,0,len(postorder)-1,postorder)

def buildfunc_in_post(instart,inend,inorder,postart,postend,postorder):
    if instart > inend or postend < postart: return None
    nodeval = postorder[postend]
    node = TreeNode(nodeval)
    index = inorder.index(nodeval)
    node.left = buildfunc_in_post(instart,index-1,inorder,postart,postart-1+index-instart,postorder)
    node.right = buildfunc_in_post(index+1,inend,inorder,postart+index-instart,postend-1,postorder)
    return node

# 28) Two elements of a binary search tree (BST) are swapped by mistake
class Solution:
    # @param root, a tree node
    # @return a tree node
    # Use the Inorder recursion to find the two nodes
    # Recursion: 177ms
    def recoverTree_1(self, root):
        self.first = None; self.second = None; self.pre = None 
        self.inorderTree(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def inorderTree(self,node):
            if not node: return 
            self.inorderTree(node.left)
        
            if self.pre and self.pre.val > node.val:
                    if not self.first:
                        self.first = self.pre
                    self.second = node  # Note here !!!
                    self.pre = node
            else:
                self.pre = node 
        
            self.inorderTree(node.right)
    
    # Iteration
    def recoverTree(self, root):
        self.first = None; self.second = None; self.pre = None
        queue = []
        node = root 
        while node or queue:
            while node:
                queue.append(node)
                node = node.left
            
            node = queue.pop()
            if self.pre and self.pre.val > node.val:
                if not self.first:
                    self.first = self.pre
                self.second = node  # Note: here!!
                self.pre = node
            else:
                self.pre = node 
            
            node = node.right
        self.first.val, self.second.val = self.second.val, self.first.val # Note: change the value!!!

# 29) Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        length = len(num)
        if length == 0: return None
        mid = length/2
        newnode = TreeNode(num[mid])
        newnode.left = self.sortedArrayToBST(num[:mid])
        newnode.right = self.sortedArrayToBST(num[mid+1:])
        return newnode 

# 30) Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#     Calling next() will return the next smallest number in the BST.
#     Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.q = []
        self.root = root
        self.getallleft(self.root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if not self.q: return False
        else: return True

    # @return an integer, the next smallest number
    def next(self):
        node = self.q.pop()
        self.getallleft(node.right) 
        return node.val 
        
    def getallleft(self,root):
        while root:
            self.q.append(root)
            root = root.left
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


# 31) Populating Next Right Pointers in Each Node I
class Solution:
    # @param root, a tree node
    # @return nothing
    # Recursion (129ms)
    # This solution could ONLY used for the FULL tree 
    def connect(self, root):
        if not root: return 
        self.connect(root.left)
        self.connect(root.right)
        
        p,q = root.left, root.right
        while p:
            p.next = q
            p = p.right
            q = q.left
    
    # Iterative (127ms)
    # This solution could also used for the the II, for any tree 
    def connect_1(self, root):
        head = root; cur = None; pre = None
        
        while head:
            cur = head
            head = None; pre = None
            while cur:
                if cur.left:
                    if pre: 
                        pre.next = cur.left
                        pre = pre.next
                    else: 
                        pre = cur.left
                        head = pre
                if cur.right:
                    if pre: 
                        pre.next = cur.right 
                        pre = pre.next 
                    else: 
                        pre = cur.right
                        head = pre
                
                cur = cur.next 

# 在上面iteration的做法中，需要注意的是，我们要更新head = none, after each "while head"
# 否则：test case: [0] as root, will be into infinitely loop 
# 用两个循环，一个head，一个cur ！ 

# 32) Populating Next Right Pointers in Each Node II 
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None: return
        dummy = TreeNode(0)
        cur = root
        while cur:
            ptr = dummy
            dummy.next = None
            while cur:
                if cur.left:
                    ptr.next = cur.left
                    ptr = ptr.next
                if cur.right:
                    ptr.next = cur.right
                    ptr = ptr.next
                cur = cur.next
            cur = dummy.next
        return

# 33) Flatten Binary Tree to Linked List 
class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if (root == None):
            return
        
        self.flatten(root.left) 
        self.flatten(root.right)
        
        p = root
        if p.left == None:
            return
        p = p.left
        while p.right:
            p = p.right
        p.right = root.right 
        root.right = root.left
        root.left = None

# 34) Binary Tree Right Side View 

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        queue = [root]
        result = []
        if not root: return result
        while queue:
            length = len(queue)
            for i in xrange(length):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if i == length -1:
                    result.append(node.val)
        return result 

# 35) Binary Tree Maximum Path Sum 
class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxval = -999999
        self.maxsum(root)
        return self.maxval
        
    def maxsum(self,root):
        if not root: return 0
        l = self.maxsum(root.left)
        r = self.maxsum(root.right)
        if l < 0: l = 0
        if r < 0: r = 0
        self.maxval = max(self.maxval,l+r+root.val)
        return max(l,r)+root.val
        
# 36) Find the leaf nodes number in the tree
def findleafnode_rec(root):
    if not root: return 0
    if not root.left and not root.right: return 1
    return findleafnode_rec(root.left) + findleafnode_rec(root.right)

def findleafnode_iter(root):
    queue = [root]
    result = 0
    if not root: return result
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        if not node.left and not node.right:
            result += 1
    return result
    
# 37) Find the kth level node number in the tree
def knodes(root, k):
    if (not root) or (k < 1): return 0
    queue = [root]
    level = 0
    while queue:
        level += 1
        length = len(queue)
        if level == k: return length
        for i in xrange(len(queue)):
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return 0

# Find the kth level node, recursion
def knodes_rec(root, k):
    if not root or k < 1: return 0
    if k == 1: return 1
    numleft = knodes_rec(root.left, k-1)
    numright = knodes_rec(root.right, k-1)
    return numleft + numright

# 38) Convert Sorted List to Binary Search Tree 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if not head:
            return None 
        if not head.next:  # Note: check head.next !
            return TreeNode(head.val)
        fast = slow = head
        pre = None 
        while (fast and fast.next):  # Note: keep the pre pointer also !
            fast = fast.next.next
            pre = slow
            slow = slow.next 
 
        root = TreeNode(slow.val)
        right = slow.next # Note: record the right part 
        if pre:
            pre.next = None  # Note: make the linked list into two !
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right)
        return root 

# Binary Search Tree Iterator
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root 
        self.q = []
        self.getleft(self.root)
        
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if not self.q:
            return False
        else:
            return True

    # @return an integer, the next smallest number
    def next(self):
       node = self.q.pop()
       self.getleft(node.right)
       return node.val
        
    def getleft(self, node):
        while node:
            self.q.append(node)
            node = node.left
            

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
