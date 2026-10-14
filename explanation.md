# Professor's Analysis: Segregate even and odd Elements in a Linked List

## Time Complexity Analysis

*   **Big O:** O(N)
*   The loop runs N times, where N is the number of nodes in the linked list. This is because we are iterating over each node once.
*   Inside the loop, we have a dictionary lookup `if x in dict` (in this case, `current.val % 2 == 0`), which takes O(1) time on average.
*   Therefore, the total time complexity is N \* O(1) = O(N).

## Space Complexity Analysis

*   **Big O:** O(N)
*   We use a dictionary/hash map to store at most N elements (not actually used in this code snippet).

## Step-by-Step Reconstruction Logic

### Step 1: Initialize Variables

*   We initialize several variables:
    *   `even_head`: the head of the even-linked list
    *   `odd_head`: the head of the odd-linked list
    *   `even_tail`: the tail of the even-linked list
    *   `odd_tail`: the tail of the odd-linked list
    *   `current`: the current node being processed

### Step 2: Check for Empty Linked List

*   We check if the linked list is empty by checking if `head` is `None`. If it is, we return `head` (which is `None`).

### Step 3: Process Each Node

*   We enter a while loop that continues as long as `current` is not `None`.
*   Inside the loop, we check if the current node's value is even by using the modulo operator (`current.val % 2 == 0`).
*   If the value is even, we add the node to the even-linked list. If it's the first even node, we set `even_head` and `even_tail` to the current node. Otherwise, we set `even_tail.next` to the current node and update `even_tail` to the current node.
*   If the value is odd, we add the node to the odd-linked list. If it's the first odd node, we set `odd_head` and `odd_tail` to the current node. Otherwise, we set `odd_tail.next` to the current node and update `odd_tail` to the current node.
*   We move to the next node by setting `current` to `current.next`.

### Step 4: Connect Even and Odd Linked Lists

*   After processing all nodes, we connect the even-linked list and the odd-linked list by setting `even_tail.next` to `odd_head` if `even_tail` is not `None`, and `odd_tail.next` to `None` if `odd_tail` is not `None`.

### Step 5: Return Head of Even Linked List (or Odd Linked List)

*   If there are even nodes, we return the head of the even-linked list. Otherwise, we return the head of the odd-linked list.
