#### Algorithm

* Open list:Nodes checking
* Closed list: Nodes already checked 
* g:  g(n) is the known cost of getting from the initial node to n，this value is tracked by the algorithm
* h:  h(n) is a heuristic estimate of the cost to get from n to any goal node. 
* f = g + h
* each nodes has the parent 

```
function A*(start,goal)
    closedset := the empty set    // The set of nodes already evaluated.
    openset := {start}    // The set of tentative nodes to be evaluated, initially containing the start node
    came_from := the empty map    // The map of navigated nodes.
 
    g_score[start] := 0    // Cost from start along best known path.
    // Estimated total cost from start to goal through y.
    f_score[start] := g_score[start] + heuristic_cost_estimate(start, goal)
     
    while openset is not empty
        current := the node in openset having the lowest f_score[] value
        if current = goal
            return reconstruct_path(came_from, goal)
         
        remove current from openset
        add current to closedset
        for each neighbor in neighbor_nodes(current)
            if neighbor in closedset
                continue
            tentative_g_score := g_score[current] + dist_between(current,neighbor)
 
            if neighbor not in openset or tentative_g_score < g_score[neighbor] 
                came_from[neighbor] := current
                g_score[neighbor] := tentative_g_score
                f_score[neighbor] := g_score[neighbor] + heuristic_cost_estimate(neighbor, goal)
                if neighbor not in openset
                    add neighbor to openset
 
    return failure

function reconstruct_path(came_from,current)
    total_path := [current]
    while current in came_from:
        current := came_from[current]
        total_path.append(current)
    return total_path
```

#### Reference
* Good Video: https://www.youtube.com/watch?v=KNXfSOx4eEE
* Wiki: https://en.wikipedia.org/wiki/A*_search_algorithm
