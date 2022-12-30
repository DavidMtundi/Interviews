"""
longest connected components
write a function , connectedComponentsCount, that takes in an adjacency list
of an undirected graph. the function should return the maximum number of connected nodes
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

            should return 4
"""


class Solution:
    traversed_nodes = []
    max_length = 0

    def longestComponents(self, graph):
        # iterate through all the nodes in the graph
        for node in graph:
            count = 0
            if node not in self.traversed_nodes:
                self.traversed_nodes.append(node)
                count += self.traverse_Node(graph, node, 1)
                self.max_length = max(count, self.max_length)
        return self.max_length

    def traverse_Node(self, graph, node, count):
        # iterate through each of the node's neighbours
        for nei in graph[node]:
            if nei not in self.traversed_nodes:
                count += 1
                self.traversed_nodes.append(nei)
                count = self.traverse_Node(graph, nei, count)
        return count


input = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],


}
sol = Solution()
print(sol.longestComponents(input))
