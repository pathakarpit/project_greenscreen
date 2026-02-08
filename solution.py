# Problem: Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def solve(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))