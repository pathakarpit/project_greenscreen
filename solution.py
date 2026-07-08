# Problem: Find a Common Element in all Rows of a Given Row-Wise Sorted Matrix
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/find-common-element-rows-row-wise-sorted-matrix/

class Solution:
    def solve(self, matrix):
        if not matrix or not matrix[0]:
            return -1
        
        rows = len(matrix)
        cols = len(matrix[0])
        common_elements = set(matrix[0])
        
        for i in range(1, rows):
            current_row_set = set()
            for j in range(cols):
                if matrix[i][j] in common_elements:
                    current_row_set.add(matrix[i][j])
            if not current_row_set:
                return -1
            common_elements = current_row_set
        
        result = min(common_elements) if common_elements else -1
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))