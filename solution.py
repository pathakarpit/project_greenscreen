# Problem: Find Minimum Number of Merge Operations to Make an Array Palindrome
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/find-minimum-number-of-merge-operations-to-make-an-array-palindrome/

class Solution:
    def solve(self, arr):
        n = len(arr)
        operations = 0
        
        for i in range(n // 2):
            if arr[i] != arr[n - i - 1]:
                operations += abs(arr[i] - arr[n - i - 1])
        
        return operations

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))