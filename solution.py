# Problem: Find paths from corner cell to middle cell in maze
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/find-paths-from-corner-cell-to-middle-cell-in-maze/

class Solution:
    def solve(self, n, maze):
        if not maze or not maze[0]:
            return []
        
        start = (0, 0)
        end = (n // 2, n // 2)
        directions = [(1, 0, 'D'), (-1, 0, 'U'), (0, 1, 'R'), (0, -1, 'L')]
        
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n and maze[x][y] == 0
        
        def backtrack(path, x, y):
            if (x, y) == end:
                result.append(path)
                return
            
            for dx, dy, direction in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    maze[nx][ny] = 1  # Mark as visited
                    backtrack(path + direction, nx, ny)
                    maze[nx][ny] = 0  # Backtrack
        
        result = []
        maze[0][0] = 1  # Mark the starting cell as visited
        backtrack('', 0, 0)
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))