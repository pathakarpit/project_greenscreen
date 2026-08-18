# Problem: Backtracking Set 2 Rat in a Maze
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/

class Solution:
    def solve(self, maze):
        n = len(maze)
        if n == 0 or maze[0][0] == 0:
            return []
        
        directions = [('D', (1, 0)), ('R', (0, 1)), ('U', (-1, 0)), ('L', (0, -1))]
        visited = [[False] * n for _ in range(n)]
        paths = []
        
        def dfs(x, y, path):
            if x == n - 1 and y == n - 1:
                paths.append(path)
                return
            
            for move_name, (dx, dy) in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] == 1:
                    visited[nx][ny] = True
                    dfs(nx, ny, path + move_name)
                    visited[nx][ny] = False
        
        visited[0][0] = True
        dfs(0, 0, '')
        
        return sorted(paths) if paths else []

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))