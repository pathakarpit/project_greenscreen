# Problem: Remove duplicates from an unsorted linked list
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/

class Solution:
    def solve(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))