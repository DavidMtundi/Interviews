"""
You are given a list of nodes, you are tasked to check whether the two nodes provided, A and B  are connected or not
"""


class Solution:
    traversed_list = []
    traversed_list_BFS=[]
    queue_list = []

    def traverse_QueueBFS(self, A, B, graph):
        self.queue_list.append(A)
        self.traversed_list_BFS.append(A)
        while len(self.queue_list) > 0:
            element = self.queue_list.pop(0)
            if element == B:
                return True
            for nei in graph[element]:
                if nei not in self.traversed_list_BFS:
                    self.queue_list.append(nei)
                    self.traversed_list_BFS.append(nei)

        return False

    # Traversing the graph using depth First Search
    def traverse_queueDFS(self, A, B, graph):
        self.traversed_list.append(A)
        if A == B:
            return True

        for nei in graph[A]:
            if nei not in self.traversed_list:
                if self.traverse_queueDFS(nei, B, graph):
                    return True

        return False


input = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]

}
sol = Solution()
print("DFS")
print(sol.traverse_queueDFS(0, 2, input))
print("BFS")
print(sol.traverse_QueueBFS(0, 2, input))
