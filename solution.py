# Problem: Set Matrix Zeroes
# Difficulty: Medium
# Link: https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def solve(self, mat):
        n = len(mat)
        m = len(mat[0])
        rows_to_zero = set()
        cols_to_zero = set()
        
        # Identify the rows and columns that need to be zeroed
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)
        
        # Set the identified rows to zero
        for row in rows_to_zero:
            for j in range(m):
                mat[row][j] = 0
        
        # Set the identified columns to zero
        for col in cols_to_zero:
            for i in range(n):
                mat[i][col] = 0
        
        return mat

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))