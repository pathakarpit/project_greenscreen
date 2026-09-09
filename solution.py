# Problem: Linked List Cycle
# Difficulty: Easy
# Link: https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def solve(self, head):
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))