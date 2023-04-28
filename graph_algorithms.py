def bfs(graph, start_node, search_node=None):
    # graph: a dictionary representing the graph to be traversed.
    # start_node: a string representing the starting node of the traversal.
    # search_node: an optional string representing the node being searched for in the graph.
    # Note: If the given start_node belongs to one strongly connected component then the other nodes belong to that
           # particular component can only be traversed. But the nodes belonging to other components must not be traversed
           # if those nodes were not reachable from the given start_node.

    #The output depends on whether the search_node is provided or not:
        #1. If search_node is provided, the function returns 1 if the node is found during the search and 0 otherwise.
        #2. If search_node is not provided, the function returns a list containing the order in which the nodes were visited during the search.

    
    queue = [start_node]
    
    visited = set([start_node])
   
    visitedinorder = []
    while len(queue) > 0:
        
        current_node = queue.pop()
        visitedinorder.append(current_node)
        
        if search_node is not None and current_node == search_node:
            return 1
        
        for neighbor, weight in graph[current_node].items():
            
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                
                

    
    if search_node is not None:
        return 0
    
    else:
        return visitedinorder



def dfs(graph, start_node, visited=None, path=None, search_node=None):
    # graph: a dictionary representing the graph
    # start_node: the starting node for the search
    # visited: a set of visited nodes (optional, default is None)
    # path: a list of nodes in the current path (optional, default is None)
    # search_node: the node to search for (optional, default is None)

    # Note1: The optional parameters “visited” and “path” are initially not required to be passed as inputs but needs to be
            # updated recursively during the search implementation. If not required for your implementation purposes they can
            # be ignored and can be removed from the parameters.

    # Note2: If the given start_node belongs to one strongly connected component then the other nodes belong to that
           # particular component can only be traversed. But the nodes belonging to other components must not be traversed
           # if those nodes were not reachable from the given start_node.

    # The function returns:
        # 1. If search_node is provided, the function returns 1 if the node is found and 0 if it is not found.
        # 2. If search_node is not provided, the function returns a list containing the order in which the nodes were visited during the search.

     
    if visited is None:
        visited = {}
    if path is None:
        path = []

    
    visited[start_node] = True
    path.append(start_node)

    
    if search_node is not None and start_node == search_node:
        return 1

    
    for neighbor in graph[start_node]:
        
        if neighbor not in visited:
            result = dfs(graph, neighbor, visited, path, search_node)
            
            if search_node is not None and result == 1:
                return 1

    if search_node is None and path is None:
        return list(visited.keys())

    elif search_node is None and path is not None:
        path_list = []
        for node in path:
            path_list.append(node)
        return path_list

    else:
        return 0


#import heapq
#def dijkstra(graph, start_node, end_node):
#    # graph: a dictionary representing the graph where the keys are the nodes and the values
#            # are dictionaries representing the edges and their weights.
#    # start_node: the starting node to begin the search.
#    # end_node: the node that we want to reach.

#    # Outputs:
#        #1. If the end_node is not reachable from the start_node, the function returns 0.

#        #2. If the end_node is reachable from the start_node, the function returns a list containing three elements:
#                #2.1 The first element is a list representing the shortest path from start_node to end_node.
#                     #[list of nconst values in the visited order]
#                #2.2 The second element is the total distance of the shortest path.
#                     #(summation of the distances or edge weights between minimum visited nodes)
#                #2.3 The third element is Hop Count between start_node and end_node.

#    # Return the shortest path and distances
#        # initialize distance and visited dictionaries, and priority queue
#    distance = {}
#    visited = {}
#    pq = []
#    predecessor = {node: None for node in graph}

#    # initialize distance and visited dictionaries with default values
#    #for node in graph:
#    #    distance[node] = float('inf')
#    #    visited[node] = False
#    distance, visited = {node: float('inf') for node in graph}, {node: False for node in graph}

#    # set distance of start node to 0 and push it onto the priority queue
#    distance[start_node] = 0
#    heapq.heappush(pq, (0, start_node))

#    while pq:
#        # get the node with the smallest distance from the priority queue
#        current_distance, current_node = heapq.heappop(pq)

#        # if the current node is the end node, break out of the loop
#        if current_node == end_node:
#            break

#        # mark the current node as visited
#        visited[current_node] = True

#        if current_distance > distance[current_node]:
#            continue

#        # iterate over the neighbors of the current node
#        for neighbor, weight in graph[current_node].items():
#            # if the neighbor has not been visited, update its distance and push it onto the priority queue
#            if not visited[neighbor]:
#                new_distance = distance[current_node] + weight
#                if new_distance < distance[neighbor]:
#                    distance[neighbor] = new_distance
#                    predecessor[neighbor] = current_node
#                    heapq.heappush(pq, (new_distance, neighbor))

#    # if the end node was not reached, return 0
#    if distance[end_node] == float('inf'):
#        return 0

#    # build the shortest path list and calculate the total distance and hop count
#    shortest_path = [end_node]
#    total_distance = distance[end_node]
#    hop_count = 0
#    while shortest_path[-1] != start_node:
#        current_node = shortest_path[-1]
#        shortest_path.append(predecessor[current_node])
#        hop_count += 1

#    # reverse the shortest path list to get the correct order
#    shortest_path.reverse()

#    # return the shortest path list, total distance, and hop count
#    return [shortest_path, total_distance, hop_count]

import heapq

def dijkstra(graph, start_node, end_node):
    # graph: a dictionary representing the graph where the keys are the nodes and the values
            # are dictionaries representing the edges and their weights.
    # start_node: the starting node to begin the search.
    # end_node: the node that we want to reach.

    # Outputs:
        #1. If the end_node is not reachable from the start_node, the function returns 0.

        #2. If the end_node is reachable from the start_node, the function returns a list containing three elements:
                #2.1 The first element is a list representing the shortest path from start_node to end_node.
                     #[list of nconst values in the visited order]
                #2.2 The second element is the total distance of the shortest path.
                     #(summation of the distances or edge weights between minimum visited nodes)
                #2.3 The third element is Hop Count between start_node and end_node.

    def initialize_dicts():
        return {node: float('inf') for node in graph}, {node: False for node in graph}

    def update_neighbor_distances(node, dist, vis, pred, queue):
        for neighbor, weight in graph[node].items():
            if not vis[neighbor]:
                new_distance = dist[node] + weight
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    pred[neighbor] = node
                    heapq.heappush(queue, (new_distance, neighbor))

    def build_shortest_path(start, end, pred):
        path = [end]
        hop_count = 0
        while path[-1] != start:
            path.append(pred[path[-1]])
            hop_count += 1
        path.reverse()
        return path, hop_count

    distance, visited = initialize_dicts()
    pq = []
    predecessor = {node: None for node in graph}

    distance[start_node] = 0
    heapq.heappush(pq, (0, start_node))

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_node == end_node:
            break
        visited[curr_node] = True

        if curr_dist > distance[curr_node]:
            continue

        update_neighbor_distances(curr_node, distance, visited, predecessor, pq)

    if distance[end_node] == float('inf'):
        return 0

    shortest_path, hop_count = build_shortest_path(start_node, end_node, predecessor)

    return [shortest_path, distance[end_node], hop_count]



# (strongly connected components)
def kosaraju(graph):
     # graph: a dictionary representing the graph where the keys are the nodes and the values
            # are dictionaries representing the edges and their weights.
    #Note: Here you need to call dfs function multiple times so you can Implement seperate
         # kosaraju_dfs function if required.

    #The output:
        #list of strongly connected components in the graph,
          #where each component is a list of nodes. each component:[nconst2, nconst3, nconst8,...] -> list of nconst id's.
    def first_pass(graph, visited_set, node_stack):
        for v in graph:
            if v not in visited_set:
                perform_dfs(graph, v, visited_set, node_stack)

    def perform_dfs(graph, v, visited_set, node_stack):
        visited_set.add(v)
        for neighbor in graph.get(v, {}):
            if neighbor not in visited_set:
                perform_dfs(graph, neighbor, visited_set, node_stack)
        node_stack.append(v)

    def reverse_graph(graph):
        reversed_graph = {vertex: {} for vertex in graph}
        for vertex in graph:
            for neighbor in graph.get(vertex, {}):
                reversed_graph.setdefault(neighbor, {})[vertex] = graph[vertex][neighbor]
        return reversed_graph

    def second_pass(graph, visited_set, node_stack):
        scc_list = []
        while node_stack:
            curr_vertex = node_stack.pop()
            if curr_vertex not in visited_set:
                curr_component = []
                perform_dfs_reverse(graph, curr_vertex, visited_set, curr_component)
                scc_list.append(curr_component)
        return scc_list

    def perform_dfs_reverse(graph, v, visited_set, component):
        visited_set.add(v)
        component.append(v)
        for neighbor in graph.get(v, {}):
            if neighbor not in visited_set:
                perform_dfs_reverse(graph, neighbor, visited_set, component)

    visited = set()
    stack = []
    first_pass(graph, visited, stack)

    reversed_adj_list = reverse_graph(graph)

    visited = set()
    scc = second_pass(reversed_adj_list, visited, stack)

    return scc



