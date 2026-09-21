# Problem: Point to next higher value node in a linked list with an Arbitrary Pointer
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/point-to-next-higher-value-node-in-a-linked-list-with-an-arbitrary-pointer/

class Solution:
    def solve(self, nums):
        return sum(nums) if len(nums) > 1 else nums[0] if nums else 0

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))