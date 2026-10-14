# Problem: Segregate even and odd Elements in a Linked List
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

class Solution:
    def solve(self, nums):
        even_nums = [num for num in nums if num % 2 == 0]
        return even_nums

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))