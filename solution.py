# Problem: Rotate Image
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-image/

class Solution:
    def solve(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        rotated_matrix = [[0] * m for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                rotated_matrix[j][m - 1 - i] = matrix[i][j]
        
        return rotated_matrix

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))