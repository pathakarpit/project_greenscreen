# Problem: Maximum Product Subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def solve(self, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == mid + 1:
                left = mid + 1
            else:
                right = mid - 1
        return left + 1

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))