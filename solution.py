# Problem: Segregate even and odd Elements in a Linked List
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

class Solution:
    class ListNode:
        def __init__(self, data=0, next=None):
            self.data = data
            self.next = next

    def solve(self, head):
        if not head:
            return head

        even_head = None
        even_tail = None
        odd_head = head
        odd_tail = head

        current = head.next
        while current:
            if current.data % 2 == 0:
                if not even_head:
                    even_head = current
                    even_tail = even_head
                else:
                    even_tail.next = current
                    even_tail = current
            else:
                odd_tail.next = current
                odd_tail = current
            current = current.next

        if even_head:
            even_tail.next = None
            head = even_head
            if odd_head:
                current = even_head
                while current.next:
                    current = current.next
                current.next = odd_head
        else:
            if odd_head:
                head = odd_head

        return head

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))