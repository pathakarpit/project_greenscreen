# Problem: Mo's Algorithm
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/mos-algorithm-query-square-root-decomposition-set-1-introduction/

class Solution:
    def solve(self, A):
        n = len(A)
        if n == 0:
            return []
        
        # Calculate prefix sums
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + A[i]
        
        result = []
        max_prefix_sum = float('-inf')
        
        # Find the maximum subarray sum (using Kadane's algorithm)
        for i in range(n):
            current_max = 0
            for j in range(i, n):
                current_max += A[j]
                if current_max >= max_prefix_sum:
                    result.append([i, j])
                    max_prefix_sum = current_max
        
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))