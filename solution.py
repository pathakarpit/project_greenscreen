# Problem: Delete nodes which have a greater value on right side
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/delete-nodes-which-have-a-greater-value-on-right-side/

class Solution:
    def solve(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            if current.next.val > current.next.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))