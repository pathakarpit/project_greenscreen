# Problem: Remove Consecutive Characters
# Difficulty: Easy
# Link: https://practice.geeksforgeeks.org/problems/consecutive-elements2306/1

class Solution:
    def solve(self, s):
        result = []
        for char in s:
            if not result or result[-1] != char:
                result.append(char)
        return ''.join(result)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))