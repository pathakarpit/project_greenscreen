# Problem: Sort a linked list of 0s-1s-or-2s
# Difficulty: Easy
# Link: https://www.geeksforgeeks.org/sort-a-linked-list-of-0s-1s-or-2s/

class Solution:
    def solve(self, head):
        count = [0, 0, 0]  # To store count of 0s, 1s, and 2s
        current = head
        
        # Count the number of 0s, 1s, and 2s in the linked list
        while current:
            if current.val == 0:
                count[0] += 1
            elif current.val == 1:
                count[1] += 1
            elif current.val == 2:
                count[2] += 1
            current = current.next
        
        # Reconstruct the linked list with sorted values
        current = head
        while current:
            if count[0] > 0:
                current.val = 0
                count[0] -= 1
            elif count[1] > 0:
                current.val = 1
                count[1] -= 1
            elif count[2] > 0:
                current.val = 2
                count[2] -= 1
            current = current.next
        
        return head

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))