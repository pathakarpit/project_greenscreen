# Problem: Segregate even and odd Elements in a Linked List
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

class Solution:
    def solve(self, head: ListNode) -> ListNode:
        if not head:
            return head

        even_head = ListNode(0)
        odd_head = ListNode(0)
        even_tail = even_head
        odd_tail = odd_head
        current = head

        while current:
            if current.val % 2 == 0:
                even_tail.next = current
                even_tail = even_tail.next
            else:
                odd_tail.next = current
                odd_tail = odd_tail.next
            current = current.next

        even_tail.next = None
        odd_tail.next = even_head.next

        return odd_head.next

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))