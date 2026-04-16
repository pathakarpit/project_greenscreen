# Problem: Longest Substring without Repeating Characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def solve(self, heights):
        total_height = sum(heights)
        num_students = len(heights)
        average_height = total_height / num_students
        return round(average_height, 2)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))