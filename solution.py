# Problem: Find Duplicates in O(n) Time and O(1) Extra Space
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

class Solution:
    def solve(self, nums, target):
        pairs = []
        seen = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                pairs.append([seen[complement], i])
            seen[nums[i]] = i
        
        return pairs

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))