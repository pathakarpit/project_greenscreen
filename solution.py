# Problem: Segregate even and odd Elements in a Linked List
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

class Solution:
    def solve(self, head):
        if not head or not head.next:
            return head
        
        even_head = ListNode(0)
        odd_head = ListNode(0)
        even = even_head
        odd = odd_head
        node = head
        
        while node:
            if node.val % 2 == 0:
                even.next = node
                even = even.next
            else:
                odd.next = node
                odd = odd.next
            node = node.next
        
        even.next = odd_head.next
        odd.next = None
        return even_head.next


my best complete final answer to the task.

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))