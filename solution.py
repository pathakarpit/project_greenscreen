# Problem: Space Optimization Using Bit Manipulations
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/space-optimization-using-bit-manipulations/

class Solution:
    def solve(self, a, b):
        multiples = []
        for num in range(a, b + 1):
            if num % 2 == 0 or num % 5 == 0:
                multiples.append(num)
        return ' '.join(map(str, multiples))

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))