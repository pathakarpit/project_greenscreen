# Problem: Segregate even and odd Elements in a Linked List
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

class Solution:
    def solve(self, head):
        if not head:
            return head
        
        even_head = even = ListNode(0)
        odd_head = odd = ListNode(0)
        
        while head:
            if head.val % 2 == 0:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            head = head.next
        
        even.next = odd_head.next
        odd.next = None
        
        return even_head.next

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))