# Problem: M Coloring Problem
# Difficulty: Medium
# Link: https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1

class Solution:
    def solve(self, graph):
        from collections import defaultdict
        
        # Function to check if it's safe to color vertex v with color c
        def is_safe(v, color, c):
            for i in graph[v]:
                if color[i] == c:
                    return False
            return True
        
        # Function to solve the coloring problem using backtracking
        def graph_coloring_util(color, v):
            if v == len(graph):
                return True
            
            for c in range(1, m + 1):
                if is_safe(v, color, c):
                    color[v] = c
                    if graph_coloring_util(color, v + 1):
                        return True
                    color[v] = 0
        
        # Main function to initialize and call the coloring utility
        def solve(graph, m):
            global n
            n = len(graph)
            color = [0] * n
            if not graph_coloring_util(color, 0):
                return False
            return True
        
        # Find the minimum number of colors required
        for i in range(1, m + 1):
            if solve(graph, i):
                return i
        
        return -1

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))