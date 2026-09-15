# Problem: Reorder List
# Difficulty: Medium
# Link: https://leetcode.com/problems/reorder-list/

class Solution:
    def solve(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        
        # Find the middle of the list using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list into two halves
        second_half = slow.next
        slow.next = None
        
        # Reverse the second half of the list
        prev, curr = None, second_half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Merge two halves
        first_half = head
        second_half = prev
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half = temp1
            second_half = temp2

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))