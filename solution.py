# Problem: Given a Matrix of ‘O’ and ‘X’, Replace ‘O’ with ‘X’ if Surrounded by ‘X’
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/given-matrix-o-x-replace-o-x-surrounded-x/

class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                dfs(i + dx, j + dy)
        
        # Step 1: Mark all 'O's connected to the boundary with 'T'
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)
        
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m - 1][j] == 'O':
                dfs(m - 1, j)
        
        # Step 2: Convert all remaining 'O's to 'X' and revert 'T' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))