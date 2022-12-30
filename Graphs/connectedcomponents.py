"""
Connected components count
write a function , connectedComponentsCount, that takes in an adjacency list
of an undirected graph. the function should return the number of connected components
within the graph

Example
    input = {
            0:[8,1,5],
            1:[0],
            5:[0,8],
            8:[0,5],
            2:[3,4],
            3:[2,4],
            4:[3,2]

            }

            should return 2
"""


class Solution:
    # This method is for iterating through the nodes
    dict_traversed = []
    count = 0

    def connectedComponentsCount(self, graph):
        if graph is None or len(graph) < 1:
            return self.count
        for node in graph:
            if node not in self.dict_traversed:
                self.count += 1
                self.dict_traversed.append(node)
                self.traverse_Neighbours(graph, node)
        return self.count

    def traverse_Neighbours(self, graph, node):
        for nei in graph[node]:
            if nei not in self.dict_traversed:
                self.dict_traversed.append(nei)
                self.traverse_Neighbours(graph, nei)


sol = Solution()
input = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
    7: [6, 9],
    6: [],
    9: [],
    10: [12, 13],
    12: [],
    13: []

}
print(sol.connectedComponentsCount(graph=input))
