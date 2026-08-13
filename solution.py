# Problem: Median of Two Sorted Array with Different Size
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/

class Solution:
    def solve(self, m, n):
        # Function to calculate Fibonacci number using memoization
        def fibonacci(k):
            if k <= 1:
                return k
            a, b = 0, 1
            for _ in range(2, k + 1):
                a, b = b, a + b
            return b
        
        # Calculate the mth and nth Fibonacci numbers
        fib_m = fibonacci(m)
        fib_n = fibonacci(n)
        
        # Return the sum of the mth and nth Fibonacci numbers
        return fib_m + fib_n

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))