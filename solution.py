# Problem: Piar with given difference
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/find-a-pair-with-the-given-difference/

class Solution:
    def solve(self, arr, x):
        seen = set()
        for num in arr:
            if (x - num) in seen:
                return True
            seen.add(num)
        return False

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))