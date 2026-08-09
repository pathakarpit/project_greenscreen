# Problem: Product of Array except itself
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/a-product-array-puzzle/

class Solution:
    def solve(self, arr):
        n = len(arr)
        result = []
        
        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= arr[j]
            result.append(product)
        
        return result

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))