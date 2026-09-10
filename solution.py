# Problem: Merge Two Sorted Lists
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def solve(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))