### A program that performs a depth-first search algorithm on a graph that is implemented as an adjacency list.


# Example implementation of a weighted, undirected graph using an adjacency list.

# The key represents the node
# The first index is a boolean value that indicates if this node has been visited (True) or not (False).
# The second index is a list of the neighbours of that node.
# Each item in this list is a tuple where the first item is the actual node,
# and the second item is the cost to get to that node (from the current node).
graph = {
    '0': [('1', 1), ('2', 2)],
    '1': [('0', 1), ('2', 1)],
    '2': [('0', 2), ('1', 1), ('6', 4), ('7', 3)],
    '3': [('4', 1), ('9', 3)],
    '4': [('1', 2), ('3', 1), ('7', 4), ('8', 2)],
    '5': [('6', 3)],
    '6': [('2', 4), ('5', 3)],
    '7': [('2', 3), ('4', 4), ('8', 3)],
    '8': [('4', 2), ('7', 3)],
    '9': [('3', 3)],
}

def dfs(current_node, path=[], visited=[False for node in graph]):
    '''
    Performs the depth-first search algorithm.
    'current_node' is the node that the algorithm is currently on.
    'path' is a list that contains the nodes that the algorithm has taken to get to the current node (in order).
    'visited' is a list that contains boolean values representing the nodes that have been visited. The index of each item
    represents the node it refers to (e.g. the first item has index 0, so it indicated whether or not node '0' has been visited, and so on). 
    '''
    
    # Store the currently visited nodes in a local variable
    currently_visited = visited

    # If we are visiting a node that we have already visited, we backtrack to the previous node.
    if currently_visited[int(current_node)]: return
    
    # Otherwise, we have now visited this node so we set this to true.
    currently_visited[int(current_node)] = True

    # Store the current path in a local variable, then append the current node to it.
    current_path = path
    current_path.append(current_node)

    # A list of the neighbours of the current node.
    neighbours = graph[current_node]

    # Iterate through each neighbour and recursively call this function, passing in the actual node.
    for path in neighbours:
        dfs(path[0], current_path, currently_visited)

    return current_path, currently_visited

# Change this value to any other value (0-9 inclusive) 
start_node = '0'

# visited = [False for node in graph]
# print(visited)
path, visited = (dfs(start_node))

# Print out the path
print(f'Path taken: {path}')

# Verify that all nodes have been visited.
print('Verfication that each node has been visited:')
for node, is_visited in enumerate(visited):
    print(f'{node}: {is_visited}')