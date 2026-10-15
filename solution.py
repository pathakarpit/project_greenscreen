# Problem: Segregate even and odd Elements in a Linked List
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def solve(self, head: ListNode):
        if not head:
            return None, None

        even_head = None
        even_tail = None
        odd_head = None
        odd_tail = None

        current = head
        while current:
            if current.val % 2 == 0:
                if not even_head:
                    even_head = current
                    even_tail = even_head
                else:
                    even_tail.next = current
                    even_tail = current
            else:
                if not odd_head:
                    odd_head = current
                    odd_tail = odd_head
                else:
                    odd_tail.next = current
                    odd_tail = current
            current = current.next

        if even_tail:
            even_tail.next = None
        if odd_tail:
            odd_tail.next = None

        return even_head, odd_head

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))