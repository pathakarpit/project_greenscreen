# Problem: Segregate even and odd Elements in a Linked List
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

class Solution:
    def solve(self, head: ListNode) -> ListNode:
        even_head = ListNode(0)
        odd_head = ListNode(0)
        even_tail = even_head
        odd_tail = odd_head
        current = head
        
        while current:
            if current.value % 2 == 0:
                even_tail.next = current
                even_tail = even_tail.next
            else:
                odd_tail.next = current
                odd_tail = odd_tail.next
            current = current.next
        
        even_tail.next = odd_head.next
        odd_tail.next = None
        
        return even_head.next

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))