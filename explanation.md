# Professor's Analysis: Segregate even and odd Elements in a Linked List

```
## Time Complexity Analysis
* The Big O notation for this solution is O(N), where N is the number of nodes in the linked list.
* The loop runs N times, as we are traversing the entire list.
* The dictionary lookup `if current.val % 2 == 0` takes O(1) time on average, as dictionary lookups are constant time operations in Python.
* Therefore, N * O(1) = O(N).

## Space Complexity Analysis
* The Big O notation for this solution is O(N), where N is the number of nodes in the linked list.
* We use a dictionary/hash map to store at most N elements, which is the number of nodes in the linked list.

## Step-by-Step Reconstruction Logic
* We initialize two dummy nodes `even_head` and `odd_head` to serve as the heads of the even and odd lists, respectively.
* We initialize two pointers `even_tail` and `odd_tail` to keep track of the last node in the even and odd lists, respectively.
* We initialize a pointer `current` to point to the head of the linked list.
* The loop condition is `while current`, which will continue until we reach the end of the linked list.
* Inside the loop, we check if the current node's value is even by using the modulo operator (`current.val % 2 == 0`).
* If the current node's value is even, we add it to the even list by updating the `even_tail` pointer.
* If the current node's value is odd, we add it to the odd list by updating the `odd_tail` pointer.
* After the loop, we update the `even_tail` and `odd_tail` pointers to point to the last nodes in the even and odd lists, respectively.
* We update the `even_tail` pointer to point to the `odd_head.next` node, effectively connecting the even list to the odd list.
* We set the `odd_tail` pointer to `None`, effectively terminating the odd list.
* Finally, we return the `even_head.next` node, which is the head of the resulting linked list.
```
