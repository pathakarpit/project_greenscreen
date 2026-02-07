# Problem: Product of Array Except Self
# Difficulty: Medium
# Link: https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def solve(self, arr):
        n = len(arr)
        if n == 0:
            return []
        
        # Create two arrays to store the product of elements to the left and right of each index
        left_products = [1] * n
        right_products = [1] * n
        
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * arr[i - 1]
        
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * arr[i + 1]
        
        # The result is the product of left and right products at each index
        return [left_products[i] * right_products[i] for i in range(n)]

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))