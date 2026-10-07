# Problem: Segregate even and odd Elements in a Linked List
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

class Solution:
    def solve(self, head):
        if not head:
            return [], []
        
        even_head = even = ListNode(0)
        odd_head = odd = ListNode(0)
        
        current = head
        while current:
            if current.val % 2 == 0:
                even.next = current
                even = even.next
            else:
                odd.next = current
                odd = odd.next
            current = current.next
        
        even.next = None
        odd.next = None
        
        even_list = even_head.next
        odd_list = odd_head.next
        
        return even_list, odd_list

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))