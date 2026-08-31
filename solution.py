# Problem: Backtracking set-7 hamiltonian cycle
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/backtracking-set-7-hamiltonian-cycle/

class Solution:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.graph = {vertex: [] for vertex in V}
        for edge in E:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
    
    def dfs(self, u, v, visited):
        if u == v:
            return True
        for neighbor in self.graph[u]:
            if not visited[neighbor]:
                visited[neighbor] = True
                if self.dfs(neighbor, v, visited):
                    return True
                visited[neighbor] = False
        return False
    
    def solve(self, u, v):
        visited = {vertex: False for vertex in self.V}
        visited[u] = True
        return self.dfs(u, v, visited)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))