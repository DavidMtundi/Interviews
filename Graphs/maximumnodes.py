"""
Connected maximum nodes =
write a function , maximumnodesconnected, that takes in an adjacency list
of an undirected graph. the function should return the maximum number of connected nodes in any component
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
    def maximumNodesConnected(self, graph):
        maximum = 0
        count = 0
        traversed_nodes = {}
        for node in graph:
            count = self.traverseNode(graph, node, traversed_nodes)
            maximum = max(maximum, count)
        print(maximum)

    def traverseNode(self, graph, node, traversed_nodes):

        if node in traversed_nodes:
            return 0
        count = 0

        traversed_nodes[node] = node
        count += 1
        for sub_node in graph[node]:
            count += self.traverseNode(graph, sub_node, traversed_nodes)

        return count


sol = Solution()
input = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]

}
sol.maximumNodesConnected(graph=input)
