# Problem: Zigzag (or diagonal) Traversal of Matrix
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/

class Solution:
    def solve(self, mat):
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        for d in range(m + n - 1):
            temp = []
            r, c = d if d < n else n - 1, 0 if d < n else d - (n - 1)
            while r >= 0 and c < n:
                temp.append(mat[r][c])
                r -= 1
                c += 1
            result.extend(temp if d % 2 == 0 else reversed(temp))
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))