# Problem: Sort Biotonic Doubly Linked Lists
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/sort-biotonic-doubly-linked-list/

class Solution:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None
    
    def solve(head):
        if not head or not head.next:
            return head
        
        # Find the pivot point where the list changes from increasing to decreasing
        current = head
        while current.next and current.value <= current.next.value:
            current = current.next
        if current.next is None:  # Already sorted
            return head
        
        # Split the list into two parts, reverse the second part
        pivot = current
        tail_second_part = pivot.next
        while tail_second_part.next:
            tail_second_part = tail_second_part.next
        
        # Reverse the second half
        prev = None
        current = pivot.next
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        
        tail_second_part.next = None
        head_second_part = prev
        
        # Merge the two sorted halves
        dummy = Node(0)
        current = dummy
        while head and head_second_part:
            if head.value < head_second_part.value:
                current.next = head
                head.prev = current
                head = head.next
            else:
                current.next = head_second_part
                head_second_part.prev = current
                head_second_part = head_second_part.next
            current = current.next
        
        if head:
            current.next = head
            head.prev = current
        else:
            current.next = head_second_part
            if head_second_part:
                head_second_part.prev = current
        
        return dummy.next

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))