'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

'''

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None: return None
        queue= []; map = {}   # Use the map to record which node is set or not!
        newnode = UndirectedGraphNode(node.label)
        queue.append(node)
        map[node] = newnode
        
        while queue:
            curr = queue.pop() # Here we use pop() or pop(0), either is fine, since we use the map{} to double check 
            for neighbor in curr.neighbors:
                if neighbor not in map:
                    copy = UndirectedGraphNode(neighbor.label)
                    map[curr].neighbors.append(copy)
                    queue.append(neighbor)
                    map[neighbor] = copy
                else:  
                    map[curr].neighbors.append(map[neighbor])  #Note here! we need to update!
        
        return newnode  
