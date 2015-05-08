'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        graph = {}
        self.result = True
        for course in xrange(numCourses):
            graph[course] = ["white",[]]
        
        for prerequest in prerequisites:
            graph[prerequest[0]][1].append(prerequest[1])
        
        self.topology_sort(graph)    
        return self.result
    
    def topology_sort(self, graph):    
        queue = []
        for node in graph:
            self.topology_util(graph, node, queue)
    
    def topology_util(self, graph, node, queue):
        if graph[node][0] == 'gray':
            self.result = False
        if graph[node][0] == 'white':
            graph[node][0] = 'gray'
            for adj in graph[node][1]:
                self.topology_util(graph, adj, queue)
            graph[node][0] = 'black'
            queue.insert(0,node)
