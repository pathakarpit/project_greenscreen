# Problem: Flatten a linked list with next and child pointers
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/

class Solution:
    def solve(self, head):
        if not head:
            return None
        
        curr = head
        tail = head
        
        while curr:
            if curr.child:
                # Append the child list to the end of the current list
                temp_tail = curr.child
                while temp_tail.next:
                    temp_tail = temp_tail.next
                temp_tail.next = curr.next
                if curr.next:
                    curr.next.prev = temp_tail
                # Move the child list to be part of the main list
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            else:
                tail = curr
            curr = curr.next
        
        return head

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))