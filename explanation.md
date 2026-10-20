# Professor's Analysis: Segregate even and odd Elements in a Linked List

## Time Complexity Analysis

*   The Big O of this solution is O(N).
*   The loop runs N times, where N is the number of nodes in the linked list.
*   Inside the loop, we use a dictionary lookup `if current.val % 2 == 0` which takes O(1) time on average.
*   Therefore, the total time complexity is N \* O(1) = O(N).

## Space Complexity Analysis

*   The Big O of this solution is O(N).
*   We use a dictionary/hash map to store at most N elements, but in this case, we are using a constant amount of extra space to store the `even_head`, `odd_head`, `even_tail`, and `odd_tail` pointers.

## Step-by-Step Reconstruction Logic

*   Initialize the following variables:
    *   `even_head`: a `ListNode` with value 0, which will be the head of the even-numbered nodes
    *   `odd_head`: a `ListNode` with value 0, which will be the head of the odd-numbered nodes
    *   `even_tail`: the `even_head` node, which will keep track of the last even-numbered node
    *   `odd_tail`: the `odd_head` node, which will keep track of the last odd-numbered node
    *   `current`: the current node being processed, initialized to the head of the linked list
*   Loop through the linked list until we reach the end (i.e., `current` is `None`):
    *   Inside the loop:
        1.  Check if the current node's value is even by using the modulo operator (`current.val % 2 == 0`).
        2.  If the current node's value is even, add it to the end of the even-numbered nodes list by setting `even_tail.next` to the current node and updating `even_tail` to the current node.
        3.  If the current node's value is odd, add it to the end of the odd-numbered nodes list by setting `odd_tail.next` to the current node and updating `odd_tail` to the current node.
        4.  Move to the next node in the linked list by setting `current` to `current.next`.
*   After the loop, set the `next` pointer of the last even-numbered node to `None` to indicate the end of the even-numbered nodes list.
*   Set the `next` pointer of the last odd-numbered node to the `next` pointer of the first even-numbered node (`even_head.next`) to link the odd-numbered nodes list to the even-numbered nodes list.
*   Return the `next` pointer of the `odd_head` node, which is the head of the modified linked list.
