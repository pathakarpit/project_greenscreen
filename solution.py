# Problem: Merge sort for linked list
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/merge-sort-for-linked-list/

class Solution:
    def merge_sort(self, head):
        if not head or not head.next:
            return head
        
        # Split the list into two halves
        mid = self.find_middle(head)
        left = head
        right = mid.next
        mid.next = None
        
        # Recursively sort both halves
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        
        # Merge the sorted halves
        return self.merge(left, right)
    
    def find_middle(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, left, right):
        dummy = ListNode()
        tail = dummy
        
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        
        if left:
            tail.next = left
        if right:
            tail.next = right
        
        return dummy.next
    
    def solve(self, head):
        return self.merge_sort(head)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))