# Problem: Printing all solutions in N-Queen Problem
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/

class Solution:
    def solve(self, n):
        if n == 1:
            return [[0]]
        
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col or abs(board[i] - col) == abs(i - row):
                    return False
            return True
        
        def backtrack(board, row, n, result):
            if row == n:
                result.append(board[:])
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(board, row + 1, n, result)
                    board[row] = -1
        
        board = [-1] * n
        result = []
        backtrack(board, 0, n, result)
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))