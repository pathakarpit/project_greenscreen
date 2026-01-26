# Problem: Kosaraju's Theorem
# Difficulty: Medium
# Link: https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1

class Solution:
    def __init__(self, graph):
        self.graph = graph
        self.stack = []
        self.visited = set()
        self.low = {}
        self.ids = {}
        self.id = 0
        self.scc_count = 0

    def dfs(self, at):
        self.visited.add(at)
        self.stack.append(at)
        self.ids[at] = self.low[at] = self.id
        self.id += 1

        for to in self.graph[at]:
            if to not in self.visited:
                self.dfs(to)
                self.low[at] = min(self.low[at], self.low[to])
            elif to in self.stack:
                self.low[at] = min(self.low[at], self.ids[to])

        if self.low[at] == self.ids[at]:
            while self.stack and self.stack[-1] != at:
                node = self.stack.pop()
                self.visited.remove(node)
            self.stack.pop()
            self.scc_count += 1

    def solve(self):
        for i in range(len(self.graph)):
            if i not in self.visited:
                self.dfs(i)
        return list(set(range(len(self.graph))) - set(self.ids.keys()))

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))