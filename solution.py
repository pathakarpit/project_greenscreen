# Problem: ceiling in a sorted array
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/

class Solution:
    def solve(self, arr, x):
        n = len(arr)
        if x > arr[-1]:
            return -1
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return left

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))