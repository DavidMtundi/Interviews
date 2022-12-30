"""
Shortest path length
write a function , smallestPathLength, that takes in a  list
of an undirected graph. the function should return the smallest path length between two nodes any component
within the graph

Example
    edges=[
        [w,x],
        [x,y],
        [z,y],
        [z,v],
        [w,v]
        ]

    startnode=w,endnode=y
    should return 2

"""


class Solution:
    # a list of traversed_nodes
    traversed_nodes = []
    shortest_path = 1000

    def ShortestLength(self, edges, start, end):
        graph = self.getGraph(edges)
        return self.traverse_Node(graph, start, end)

    def traverse_Node(self, graph, start, end):
        queue_selected = []
        traversed = []
        queue_selected.append([start, 0])
        traversed.append(start)

        while len(queue_selected) > 0:
            element = queue_selected.pop(0)
            print(element)
            [value, count] = element

            if value == end:
                return count
            for nei in graph[value]:
                if nei not in traversed:
                    queue_selected.append([nei, count + 1])
                    traversed.append(nei)
                print(traversed)
        return count

    def getGraph(self, edges):
        graph = {}
        for first, last in edges:
            if first not in graph:
                graph[first] = []
            if last not in graph:
                graph[last] = []
            if last not in graph[first]:
                graph[first].append(last)
            if last not in graph[last]:
                graph[last].append(first)
        print(graph)
        return graph


edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]
sol = Solution()
print(sol.ShortestLength(edges, 'w', 'w')
      )
