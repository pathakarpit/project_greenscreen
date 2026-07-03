# Problem: Spiral Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/spiral-matrix/

class Solution:
    def solve(self, matrix):
        if not matrix or not matrix[0]:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        spiral_order = []
        
        while top <= bottom and left <= right:
            # Traverse from left to right.
            for col in range(left, right + 1):
                spiral_order.append(matrix[top][col])
            top += 1
            
            # Traverse downwards.
            for row in range(top, bottom + 1):
                spiral_order.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:
                # Traverse from right to left.
                for col in range(right, left - 1, -1):
                    spiral_order.append(matrix[bottom][col])
                bottom -= 1
                
            if left <= right:
                # Traverse upwards.
                for row in range(bottom, top - 1, -1):
                    spiral_order.append(matrix[row][left])
                left += 1
        
        return spiral_order

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))