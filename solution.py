# Problem: Maximum-Subarray
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-subarray/

class Solution:
    def solve(self, nums):
        max_sum = float('-inf')
        current_sum = 0
        
        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        
        return max_sum

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))