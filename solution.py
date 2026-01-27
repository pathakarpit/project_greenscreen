# Problem: Contains Duplicate
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate/

class Solution:
    def solve(self, arr):
        seen = set()
        for num in arr:
            if num in seen:
                return True
            seen.add(num)
        return False

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))