# Problem: Segregate even and odd Elements in a Linked List
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def solve(self, head):
        if not head or not head.next:
            return head

        even_head = None
        even_tail = None
        odd_head = head
        odd_tail = head

        while odd_tail and odd_tail.next:
            if even_head is None:
                even_head = odd_tail.next
                even_tail = even_head
            else:
                even_tail.next = odd_tail.next
                even_tail = even_tail.next

            odd_tail.next = odd_tail.next.next
            if odd_tail.next:
                odd_tail = odd_tail.next

        if even_tail:
            even_tail.next = None

        odd_tail.next = even_head

        return head

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))