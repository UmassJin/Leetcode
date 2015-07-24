'''
Design an algorithm and write code to serialize and deserialize a binary tree. Writing the tree to a file is called 'serialization' and reading back from the file to reconstruct the exact same binary tree is 'deserialization'.

There is no limit of how you deserialize or serialize a binary tree, you only need to make sure you can serialize a binary tree to a string and deserialize this string to the original structure.

Have you met this question in a real interview? Yes
Example
An example of testdata: Binary tree {3,9,20,#,#,15,7}, denote the following structure:

  3
 / \
9  20
  /  \
 15   7
Our data serialization use bfs traversal. This is just for when you got wrong answer and want to debug the input.

You can use other method to do serializaiton and deserialization.
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:

    def __init__(self):
        self.index = 0
    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        result = []
        if not root: return 
        
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node != '#':
                result.append(str(node.val))
                
                if node.right:
                    stack.append(node.right)
                elif not node.right:
                    stack.append('#')
                    
                if node.left:
                    stack.append(node.left)
                elif not node.left:
                    stack.append('#')
            else:
                result.append(node)
        
        return result
        
    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        if not data: return None
        return self.deserialize_helper(data)

    def deserialize_helper(self, data):
        if data[self.index] == '#':
            return None

        value = int(data[self.index])
        node = TreeNode(value)
        self.index += 1
        node.left = self.deserialize_helper(data)
        self.index += 1
        node.right = self.deserialize_helper(data)
        return node


'''
# Google interview: http://www.1point3acres.com/bbs/thread-131485-1-1.html
49. given a full binary tree, please write a function to encode the shape of the tree. Using the result that you get from part I to reconstruct the tree. 
You should use as little space as you can to reconstrcut it.

Generall Tree serialization 
https://github.com/UmassJin/Leetcode/blob/master/LintCode/Binary%20Tree%20Serialization.py
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.index = 0

    def serization(self, root):
        if not root: return None
        ret = 0
        queue = [root]
        while queue:
            node = queue.pop()
            ret <<= 1
            if node.left and node.right:
                ret |= 1
                queue.append(node.left)
                queue.append(node.right)
        return ret

    def deserization(self, array):
        if not array: return None
        bit_array = []

        while array:
            digit = array & 1
            bit_array.insert(0,digit)
            array >>= 1
        root = TreeNode(0)
        queue = [root]
        for bit in bit_array:
            if bit == 1:
                node = queue.pop(0)
                node.left = TreeNode(0)
                node.right = TreeNode(0)
                queue.append(node.left)
                queue.append(node.right)
            elif bit == 0:
                queue.pop()
        return root            

#### Reference
# http://www.cs.usfca.edu/~brooks/S04classes/cs245/lectures/lecture11.pdf
# http://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
# http://articles.leetcode.com/2010/09/saving-binary-search-tree-to-file.html
# http://articles.leetcode.com/2010/09/serializationdeserialization-of-binary.html
        
        
        
        
        
