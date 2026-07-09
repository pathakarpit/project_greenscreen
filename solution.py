# Problem: Maximum Size Rectangle of all 1s
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/

class Solution:
    def solve(self, mat):
        if not mat or not mat[0]:
            return 0
        
        rows = len(mat)
        cols = len(mat[0])
        
        # Create a histogram for each row considering all previous rows
        max_area = 0
        heights = [0] * cols
        
        for i in range(rows):
            for j in range(cols):
                # Update the height of the histogram based on current and previous rows
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0
            
            # Calculate max area using the largest rectangle in histogram method
            stack = [-1]
            for k in range(cols):
                while heights[k] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = k - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(k)
            
            # For remaining elements in the stack
            while len(stack) > 1:
                height = heights[stack.pop()]
                width = cols - stack[-1] - 1
                max_area = max(max_area, height * width)
        
        return max_area

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))