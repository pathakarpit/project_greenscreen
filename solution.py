# Problem: Soduko
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/backtracking-set-7-suduku/

class Solution:
    def solve(self, board):
        def is_valid(row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True
        
        def solve_sudoku():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == 0:
                        for num in range(1, 10):
                            if is_valid(row, col, num):
                                board[row][col] = num
                                if solve_sudoku():
                                    return True
                                board[row][col] = 0
                        return False
            return True
        
        solve_sudoku()

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))