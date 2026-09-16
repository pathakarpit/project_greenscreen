# Problem: Detect and remove loop in a linked list
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/

class Solution:
    def solve(self, head):
        if not head or not head.next:
            return head
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if not fast or not fast.next:
            return head
        
        slow = head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))