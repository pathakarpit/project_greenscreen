# Problem: Write a Function to get the Intersection Point of two Linked Lists
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/

class Solution:
    def solve(self, headA, headB):
        # Define a helper function to find the length of the linked list
        def get_length(head):
            length = 0
            while head:
                head = head.next
                length += 1
            return length
        
        lenA = get_length(headA)
        lenB = get_length(headB)
        
        # Move the longer list's pointer to match the starting point of the shorter list
        for _ in range(abs(lenA - lenB)):
            if lenA > lenB:
                headA = headA.next
            else:
                headB = headB.next
        
        # Now both pointers are at the same distance from the end of their lists
        while headA and headB:
            if headA == headB:
                return headA  # or headB, since they point to the same node
            headA = headA.next
            headB = headB.next
        
        return None  # No intersection found

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))