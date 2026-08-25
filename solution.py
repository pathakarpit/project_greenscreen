# Problem: Knight Tour
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/

class Solution:
    def __init__(self):
        self.moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        self.board_size = 8
        self.solution = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]
    
    def is_valid(self, x, y):
        return 0 <= x < self.board_size and 0 <= y < self.board_size and self.solution[x][y] == -1
    
    def solve(self):
        if not self.solve_util(0, 0, 0):
            print("No solution exists")
            return False
        else:
            self.print_solution()
            return True
    
    def solve_util(self, x, y, move_count):
        if move_count == self.board_size * self.board_size:
            return True
        
        for i in range(8):
            next_x, next_y = x + self.moves[i][0], y + self.moves[i][1]
            if self.is_valid(next_x, next_y):
                self.solution[next_x][next_y] = move_count
                if self.solve_util(next_x, next_y, move_count + 1):
                    return True
                self.solution[next_x][next_y] = -1
        return False
    
    def print_solution(self):
        for row in self.solution:
            print(row)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))