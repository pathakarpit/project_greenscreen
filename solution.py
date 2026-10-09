# Problem: Segregate even and odd Elements in a Linked List
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

class Solution:
    def solve(self, head):
        if not head:
            return head

        odd_head = odd = Node(0)
        even_head = even = Node(0)

        current = head
        while current:
            if current.value % 2 == 0:
                even.next = current
                even = even.next
            else:
                odd.next = current
                odd = odd.next
            current = current.next

        even.next = odd_head.next
        odd.next = None

        return even_head.next

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))