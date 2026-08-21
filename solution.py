# Problem: Longest Possible Route in a Matrix with Hurdles
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/longest-possible-route-in-a-matrix-with-hurdles/

class Solution:
    def solve(self, mat, xs, ys, xd, yd):
        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1
        
        n = len(mat)
        m = len(mat[0])
        visited = [[False] * m for _ in range(n)]
        memo = [[-1] * m for _ in range(n)]
        
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or mat[x][y] == 0:
                return -float('inf')
            if (x, y) == (xd, yd):
                return 0
            if visited[x][y]:
                return memo[x][y]
            
            visited[x][y] = True
            max_depth = -float('inf')
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                depth = dfs(new_x, new_y)
                if depth != -float('inf'):
                    max_depth = max(max_depth, 1 + depth)
            
            visited[x][y] = False
            memo[x][y] = max_depth
            return max_depth
        
        result = dfs(xs, ys)
        return -1 if result == -float('inf') else result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))