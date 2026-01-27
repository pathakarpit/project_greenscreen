# Problem: Chocolate Distribution Problem
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/chocolate-distribution-problem/

class Solution:
    def solve(self, arr, m):
        if m == 0 or len(arr) < m:
            return -1
        
        # Sort the array to easily find the minimum difference between packets
        arr.sort()
        
        # Initialize min_diff to a large number
        min_diff = float('inf')
        
        # Iterate through the sorted array and find the minimum difference
        for i in range(len(arr) - m + 1):
            current_diff = arr[i + m - 1] - arr[i]
            if current_diff < min_diff:
                min_diff = current_diff
        
        return min_diff

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))