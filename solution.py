# Problem: Wildcard String Matching
# Difficulty: Medium
# Link: https://practice.geeksforgeeks.org/problems/wildcard-string-matching1126/1

class Solution:
    def solve(self, text, pattern):
        memo = {}
        
        def is_match(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(pattern):
                return i == len(text)
            first_match = i < len(text) and pattern[j] in {text[i], '?'}
            if pattern[j] == '*':
                ans = is_match(i, j + 1) or (first_match and is_match(i + 1, j))
            else:
                ans = first_match and is_match(i + 1, j + 1)
            memo[(i, j)] = ans
            return ans
        
        return is_match(0, 0)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))