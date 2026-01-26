# Problem: Maximum and Minimum Element in an Array
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

class Solution:
    def solve(self, arr):
        if not arr:
            return None, None  # Return None for both min and max if array is empty
        
        minimum = float('inf')
        maximum = float('-inf')
        
        for num in arr:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num
        
        return minimum, maximum

########################################
# if __name__ == '__main__':
#     s = Solution()