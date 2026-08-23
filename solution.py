# Problem: Solve the Sudoku
# Difficulty: Medium
# Link: https://practice.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1

class Solution:
    def solve(self, grid):
        def is_valid(row, col, num):
            for x in range(9):
                if grid[row][x] == num or grid[x][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if grid[i][j] == num:
                        return False
            return True
        
        def solve_sudoku():
            for i in range(9):
                for j in range(9):
                    if grid[i][j] == 0:
                        for num in range(1, 10):
                            if is_valid(i, j, num):
                                grid[i][j] = num
                                if solve_sudoku():
                                    return True
                                grid[i][j] = 0
                        return False
            return True
        
        solve_sudoku()
        return grid

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))