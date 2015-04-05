#! /usr/bin/env python

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
 * 19. 求二叉树中的节点个数: getNodeNumRec（递归），getNodeNum（迭代） 
 * 20. 求二叉树第K层的节点个数：getNodeNumKthLevelRec, getNodeNumKthLevel 
 * 21. 求二叉树中叶子节点的个数：getNodeNumLeafRec, getNodeNumLeaf 
 * 22. 求二叉树中两个节点的最低公共祖先节点：getLastCommonParent, getLastCommonParentRec, getLastCommonParentRec2 
 * 23. 求二叉树的镜像（破坏和不破坏原来的树两种情况）：mirrorRec, mirrorCopyRec 
 * 24.判断二叉树是不是完全二叉树：isCompleteBinaryTree, isCompleteBinaryTreeRec 
 */  


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
def maxDepth_rec(root):
    if root == None:
        return 0
    if (root.left != None and root.right == None):
        return maxDepth_rec(root.left) + 1
    if (root.left == None and root.right != None):
        return maxDepth_rec(root.right) + 1
    return max(maxDepth_rec(root.left), maxDepth_rec(root.right))+1

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
