#### [1. Topology Sort] (http://en.wikipedia.org/wiki/Topological_sorting)
* ONLY used for the [Directed Acyclic Graph(DAG)](http://en.wikipedia.org/wiki/Directed_acyclic_graph)
* DAG means "A directed graph with no directed cycles", each edge connecting one vertex to another, such that there is no way to start at some vertex v and follow a sequence of edges that eventually loops back to v again.
* Useful: A collection of tasks that must be ordered into a sequence, subject to constraints that certain tasks must be performed earlier than others, may be represented as a DAG with a vertex for each task and an edge for each constraint.
* For example, we should finish the prerequisite class A and then take the class B, A is the prerequisite of the class B. 
* O(V) + O(E)

##### 2. Compare different Sort for graph
* BFS is useful for finding the shortest path
* DFS is useful for performing a topological sort
* Topology Sort of a DAG G=(V,E) is a liner ordering of all its vertices such that if G contains an edge (u,v) then u always appears before v in the ordering


##### 3. Algorithm 
For example, we have the following DAG, the following algorithm are from the Video, a little bit different in the G4G, since we check whether the graph is the DAG or not!!
![pic](http://www.geeksforgeeks.org/wp-content/uploads/graph.png)

```python
def topolopy_sort(root):
    stack = []
    for i in all_vertex:
        visited[i] = "White"
    for i in all_vertex:
        if visited[i] == "White":
            topology_help(i, visited, stack)
            
    for i in stack:
        print stack.pop() # Or we could use a queue here!

def topology_help(node, visited, stack):
    if visited[node] == "Gray":
        print "This is the cycle graph!"
    if visited[node] == 'White':
        visited[node] = 'Gray'
        for adjacent in node_adjacents:
            topology_help(adjacent, visited, stack)
        visited[node] = 'Black'
        stack.push() # Or we could use a queue here, queue.insert(0, node)
        
# Note the array graph in the video, so we could find the prerequest node
# put in the beginning of the array and the children node put in the end 
# of the node


# DFS for the Graph ! 
def dfs(root):
    for i in all_vertex:
        visited[i] = False
    for i in all_vertex:
        if visited == False:
            dfs_util(i, visited)

def dfs_util(node, visited):
    print node
    visited[node] = True
    
    for adjacent in node_adjacents:
        if not visited(adjacent):
            def_util(adjacent, visited)

```

##### 4. Example Interview Questions  
* [Find Order of Char in Sorted Dict](https://github.com/UmassJin/Leetcode/blob/master/Experience/Find_Order_of_Char_in_Sorted_Dict.md)
* [Course Schedule](https://github.com/UmassJin/Leetcode/blob/master/Array/Course_Schedule.py)


##### 5. Reference
* [Very Good Explaination Video 1&2](https://www.youtube.com/watch?v=PfiFnXg2G2I)
* [G4G Topological Sorting](http://www.geeksforgeeks.org/topological-sorting/)
* [G4G DFS](http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/)

##### 6. Questions using Topology Sort
        *[Course Schedule](./Array/Course_Schedule.py)
        *[Course Schedule2](./Array/Course_Schedule2.py)
