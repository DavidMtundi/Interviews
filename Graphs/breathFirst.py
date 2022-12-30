graph = {
    'A': ['C', 'B'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print(visited)


queue_updated = []


def bfsUpdated(visited_Nodes, graph_Provided, node):
    visited_Nodes.append(node)
    queue_updated.append(node)

    while len(queue_updated) > 0:
        s = queue_updated.pop(0)
        print(s)
        for nei in graph_Provided[s]:
            if nei not in visited_Nodes:
                queue_updated.append(nei)
                visited_Nodes.append(nei)


bfsUpdated(visited, graph, 'C')

# bfs(visited, graph, 'A')
