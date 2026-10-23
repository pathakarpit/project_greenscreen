# Problem: Segregate even and odd Elements in a Linked List
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

class Solution:
    def solve(self, A, B, C):
        # Sort the numbers to easily find the median
        numbers = sorted([A, B, C])
        return numbers[1]

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))