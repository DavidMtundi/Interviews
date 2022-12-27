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
    def connectedComponentsCount(self, graph):
        traversed_nodes = {}
        count = 0
        for node in graph:
            if self.traverseNode(graph, node, traversed_nodes):
                count += 1
        print(count)

    def traverseNode(self, graph, node, traverse_nodes):
        if node in traverse_nodes:
            return False
        traverse_nodes[node] = node
        for sub_node in graph[node]:
            self.traverseNode(graph, sub_node, traverse_nodes)
        return True


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
sol.connectedComponentsCount(graph=input)