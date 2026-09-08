# Problem: Reverse Linked List
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-linked-list/

class Solution:
    class ListNode:
        def __init__(self, value=0, next=None):
            self.value = value
            self.next = next

    def solve(self, head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))