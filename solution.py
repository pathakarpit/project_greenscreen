# Problem: Linked list in zig-zag fashion
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/linked-list-in-zig-zag-fashion/

class Solution:
    def solve(self, head):
        if not head or not head.next:
            return head
        
        current = head
        while current and current.next:
            # If the next node should be greater (for increasing order)
            if current.val < current.next.val:
                # Swap values
                current.val, current.next.val = current.next.val, current.val
            
            # Move to the next pair of nodes
            current = current.next.next
        
        return head

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))