# Problem: Segregate even and odd Elements in a Linked List
# Difficulty: Medium
# Link: https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

# WARNING: Valid Class Definition Not Found
# Raw Output:
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def splitList(head):
    if head is None:
        return None, None

    slow = head
    fast = head

    # Find the midpoint of the circular linked list
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next

    # If the list has an even number of nodes, slow will be just before the midpoint
    # If the list has an odd number of nodes, slow will be the midpoint
    mid = slow.next

    # Split the list into two halves
    slow.next = head

    # Find the head of the second half
    head2 = mid
    while mid.next != head:
        mid = mid.next

    mid.next = head2

    # Return the heads of the two halves
    return head, head2

# Example usage:
# Define the circular linked list
# head = ListNode(10)
# head.next = ListNode(4)
# head.next.next = ListNode(9)
# head.next.next.next = head

# Split the circular linked list
# head1, head2 = splitList(head)

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))