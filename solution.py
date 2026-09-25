# Problem: Quicksort on singly-linked list
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/quicksort-on-singly-linked-list/

class Solution:
    def solve(self, head):
        if not head or not head.next:
            return head
        
        # Helper function to partition and sort the linked list using Quick Sort
        def quick_sort(start, end):
            if start == end or start.next == end:
                return
            
            pivot = start
            current = start.next
            left = start
            right = end
            
            while current != end:
                if current.val < pivot.val:
                    left = left.next
                    left.val, current.val = current.val, left.val
                current = current.next
            
            left.val, pivot.val = pivot.val, left.val
            quick_sort(start, left)
            quick_sort(left.next, end)
        
        # Convert the linked list to a list for sorting and back again
        node_list = []
        current = head
        while current:
            node_list.append(current)
            current = current.next
        
        quick_sort(node_list[0], None)
        
        # Rebuild the linked list from the sorted list
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        node_list[-1].next = None
        
        return head

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))