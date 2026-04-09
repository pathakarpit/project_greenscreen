# Problem: Valid Anagram
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-anagram/

class Solution:
    def solve(self, s1, s2):
        if len(s1) != len(s2):
            return False
        count_s1 = [0] * 256
        count_s2 = [0] * 256
        for char in s1:
            count_s1[ord(char)] += 1
        for char in s2:
            count_s2[ord(char)] += 1
        return count_s1 == count_s2

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))