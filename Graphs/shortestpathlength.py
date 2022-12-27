"""
Connected maximum nodes =
write a function , smallestPathLength, that takes in an adjacency list
of an undirected graph. the function should return the smallest path length between two nodes any component
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
    def smallestPathLength(self, graph, A, B):
        traversed_nodes = {}
        minimum_count = 1000
        all_results = []
        for nodes in graph[A]:
            if nodes not in traversed_nodes:
                result = self.traverseNode(graph, nodes, traversed_nodes, B, 1, all_results)

        if len(all_results) > 0:
            print(all_results)
            print(min(all_results))

        else:
            print("Not Found")

    def traverseNode(self, graph, node, traversed_nodes, B, totalcount, all_results):
        count = 0
        count += 1
        if node in traversed_nodes:
            return [0, False, all_results]
        traversed_nodes[node] = node
        if node == B:
            return [totalcount, True, all_results]
        for nei in graph[node]:
            totalcount += 1
            result = self.traverseNode(graph, nei, traversed_nodes, B, totalcount, all_results)
            if result[1]:
                all_results.append(result[0])

        return [totalcount, False, all_results]


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
sol.smallestPathLength(graph=input, A=5, B=1)
