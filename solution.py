# Problem: Find the Number of Islands | Set 1 (Using DFS)
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/find-number-of-islands/

class Solution:
    def solve(self, grid):
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 'W' or visited[i][j]:
                return
            visited[i][j] = True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for di, dj in directions:
                dfs(i + di, j + dj)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'L' and not visited[i][j]:
                    dfs(i, j)
                    count += 1
        return count

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))