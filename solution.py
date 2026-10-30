# Problem: Segregate even and odd Elements in a Linked List
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

class Solution:
    def solve(self, head):
        if not head:
            return head
        
        even_dummy = ListNode(0)
        odd_dummy = ListNode(0)
        even_tail = even_dummy
        odd_tail = odd_dummy
        current = head
        
        while current:
            if current.val % 2 == 0:
                even_tail.next = current
                even_tail = even_tail.next
            else:
                odd_tail.next = current
                odd_tail = odd_tail.next
            current = current.next
        
        even_tail.next = odd_dummy.next
        odd_tail.next = None
        
        return even_dummy.next

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))