# Problem: Create a Matrix with Alternating Rectangles of O and X
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/create-a-matrix-with-alternating-rectangles-of-0-and-x/

class Solution:
    def solve(self, m, n):
        matrix = [['' for _ in range(n)] for _ in range(m)]
        layer = 0
        while 2 * layer < min(m, n):
            # Fill the top and bottom rows of the current layer
            for i in range(layer, n - layer):
                matrix[layer][i] = 'X' if (layer + i) % 2 == 0 else '0'
            for i in range(layer, m - layer):
                matrix[m - layer - 1][i] = 'X' if (layer + i) % 2 == 0 else '0'
            # Fill the left and right columns of the current layer
            for j in range(layer, m - layer):
                matrix[j][layer] = 'X' if (layer + j) % 2 == 0 else '0'
            for j in range(layer, n - layer):
                matrix[j][n - layer - 1] = 'X' if (layer + j) % 2 == 0 else '0'
            layer += 1
        return matrix

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))