# Professor's Analysis: Segregate even and odd Elements in a Linked List

## Time Complexity Analysis

*   The Big O time complexity is O(N), where N is the number of nodes in the linked list.
*   The loop runs N times, as it iterates through each node in the linked list.
*   The dictionary lookup `if x in dict` takes O(1) time on average.
*   Therefore, N * O(1) = O(N).

## Space Complexity Analysis

*   The Big O space complexity is O(N), where N is the number of nodes in the linked list.
*   We use a dictionary/hash map to store at most N elements.

## Step-by-Step Reconstruction Logic

*   **Initialization**: We initialize four pointers: `even_head`, `even_tail`, `odd_head`, and `odd_tail`. These pointers will be used to keep track of the head and tail of the even and odd nodes.
*   **Initialization of pointers**: We also initialize a pointer `current` to point to the head of the linked list.
*   **Loop Condition**: The loop condition is `current`, which will run N times, where N is the number of nodes in the linked list.
*   **Inside the Loop**:
    *   We check if the current node's value is even by using the modulo operator (`current.val % 2 == 0`).
    *   If the current node's value is even, we check if the `even_head` is `None`. If it is, we set `even_head` to the current node and `even_tail` to the current node. If it's not `None`, we set the next pointer of `even_tail` to the current node and update `even_tail` to the current node.
    *   If the current node's value is odd, we check if the `odd_head` is `None`. If it is, we set `odd_head` to the current node and `odd_tail` to the current node. If it's not `None`, we set the next pointer of `odd_tail` to the current node and update `odd_tail` to the current node.
    *   We update the `current` pointer to point to the next node in the linked list.
*   **After the Loop**: After the loop finishes, we check if the `even_tail` is not `None`. If it's not `None`, we set the next pointer of `even_tail` to `None`. We do the same for the `odd_tail` pointer.
*   **Return Statement**: Finally, we return the `even_head` and `odd_head` pointers, which point to the head of the even and odd nodes, respectively.
