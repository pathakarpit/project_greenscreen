# Problem: Remove nth node from end of list
# Difficulty: Medium
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution:
    def solve(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move the first pointer n steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        second.next = second.next.next
        
        return dummy.next

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))