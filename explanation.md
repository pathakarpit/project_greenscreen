# Professor's Analysis: Segregate even and odd Elements in a Linked List

```
## Time Complexity Analysis
* The Big O notation for this solution is O(N), where N is the number of nodes in the linked list.
* The loop runs N times, as it iterates through each node in the linked list.
* The dictionary lookup `if current.val % 2 == 0` takes O(1) time on average, as dictionary lookups are constant time operations.
* Therefore, N * O(1) = O(N).

## Space Complexity Analysis
* The Big O notation for this solution is O(N), as we use a dictionary/hash map to store at most N elements.

## Step-by-Step Reconstruction Logic
### Initialize Variables
* `even_head` and `odd_head` are initialized as dummy nodes to simplify the code.
* `even_tail` and `odd_tail` are initialized as pointers to the last nodes in the even and odd linked lists, respectively.
* `current` is initialized as a pointer to the head of the linked list.

### Loop Through the Linked List
* The loop iterates through each node in the linked list.
* For each node:
	+ If the node's value is even (`current.val % 2 == 0`), we add it to the even linked list.
	+ If the node's value is odd, we add it to the odd linked list.

### Connect the Even and Odd Linked Lists
* After the loop, we connect the even and odd linked lists together by setting `even_tail.next` to `odd_head.next`.
* We set `odd_tail.next` to `None` to terminate the odd linked list.

### Return the Head of the Modified Linked List
* Finally, we return the head of the modified linked list, which is `even_head.next`.
```
