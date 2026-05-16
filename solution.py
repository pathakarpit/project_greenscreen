# Problem: Longest Prefix Suffix
# Difficulty: Medium
# Link: https://practice.geeksforgeeks.org/problems/longest-prefix-suffix2527/1

class Solution:
    def solve(self, s):
        n = len(s)
        for i in range(n // 2, -1, -1):
            if s[:i] == s[-i:]:
                return s[:i]
        return ""

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))