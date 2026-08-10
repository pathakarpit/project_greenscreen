# Problem: Make all Array Elements Equal
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/make-array-elements-equal-minimum-cost/

class Solution:
    def solve(self, a, b):
        # Function to perform binary GCD algorithm
        def gcd_binary(x, y):
            if x == 0:
                return y
            if y == 0:
                return x
            k = 0
            while ((x | y) & 1) == 0:
                x >>= 1
                y >>= 1
                k += 1
            while (x & 1) == 0:
                x >>= 1
            while (y & 1) == 0:
                y >>= 1
            while True:
                while (x & 1) == 0:
                    x >>= 1
                while (y & 1) == 0:
                    y >>= 1
                if x < y:
                    x, y = y, x
                x -= y
                if y == 0:
                    return x << k
        # Implementing the solve method to use gcd_binary function
        return gcd_binary(a, b)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))