# Problem: Word Search
# Difficulty: Medium
# Link: https://leetcode.com/problems/word-search/

class Solution:
    def solve(self, matrix, word):
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c, index):
            if index == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] != word[index] or visited[r][c]:
                return False
            
            visited[r][c] = True
            found = (dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1) or
                     dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1))
            visited[r][c] = False
            return found
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))