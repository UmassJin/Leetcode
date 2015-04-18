#### [Topology Sort] (http://en.wikipedia.org/wiki/Topological_sorting)
* ONLY used for the [Directed Acyclic Graph(DAG)](http://en.wikipedia.org/wiki/Directed_acyclic_graph)
* DAG means "A directed graph with no directed cycles", each edge connecting one vertex to another, such that there is no way to start at some vertex v and follow a sequence of edges that eventually loops back to v again.
* Useful: A collection of tasks that must be ordered into a sequence, subject to constraints that certain tasks must be performed earlier than others, may be represented as a DAG with a vertex for each task and an edge for each constraint.

##### Compare different Sort for graph
* BFS is useful for finding the shortest path
* DFS is useful for performing a topological sort
* Topology Sort of a DAG G=(V,E) is a liner ordering of all its vertices such that if G contains an edge (u,v) then u always appears before v in the ordering
* Topology Sort only for DAG 


