# Problem: Rearrange a given linked list in place
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/rearrange-a-given-linked-list-in-place/

class Solution:
    def solve(self, head):
        if not head or not head.next:
            return head
        
        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        # Step 3: Merge two halves
        first_half = head
        second_half = prev
        while second_half.next:
            temp1 = first_half.next
            first_half.next = second_half
            first_half = temp1
            
            temp2 = second_half.next
            second_half.next = temp2
            second_half = temp2

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))