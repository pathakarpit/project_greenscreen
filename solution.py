# Problem: Find Shortest Safe Route in a Path with Landmines
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/find-shortest-safe-route-in-a-path-with-landmines/

class Solution:
    def solve(self, grid):
        n = len(grid)
        if n == 0: return "No safe route found"
        
        # Directions for moving in the grid (right and down only)
        directions = [(0, 1), (1, 0)]
        
        # Function to check if a move is valid
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n and grid[x][y] == 1
        
        # BFS initialization
        queue = [(0, 0, "")]
        visited = set((0, 0))
        
        while queue:
            x, y, path = queue.pop(0)
            if (x, y) == (n-1, n-1):
                return path + str(y) # Return the shortest path found
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y, path + str(y)))
                    visited.add((new_x, new_y))
        
        return "No safe route found"

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))