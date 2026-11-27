# Professor's Analysis: Segregate even and odd Elements in a Linked List

```
## Time Complexity Analysis
The time complexity of this algorithm is O(N), where N is the number of nodes in the linked list.

* The while loop runs N times because it iterates over each node in the list.
* Inside the loop, the dictionary lookup `if current.val % 2 == 0` takes O(1) time on average, as dictionary lookups are constant time operations.
* Therefore, N * O(1) = O(N).

## Space Complexity Analysis
The space complexity of this algorithm is O(N), where N is the number of nodes in the linked list.

* We use a dictionary/hash map to store at most N elements, which is the number of nodes we are iterating over.

## Step-by-Step Reconstruction Logic
### Initialize Variables
* `even_head` and `odd_head` are initialized as dummy nodes to serve as the head of the even and odd linked lists, respectively.
* `even_tail` and `odd_tail` are initialized as the tail of the even and odd linked lists, respectively.
* `current` is initialized as the head of the original linked list.

### Loop Condition
* The while loop continues as long as `current` is not `None`, which means there are still nodes to process in the linked list.

### Math to Find Complement
* Inside the loop, we use the modulo operator (`current.val % 2 == 0`) to check if the current node's value is even or odd.

### If/Else Logic
* If the current node's value is even, we append it to the even linked list:
	+ `even_tail.next = current`
	+ `even_tail = even_tail.next` to move the tail pointer to the next node
* If the current node's value is odd, we append it to the odd linked list:
	+ `odd_tail.next = current`
	+ `odd_tail = odd_tail.next` to move the tail pointer to the next node
* We then move to the next node in the linked list: `current = current.next`

### Handling Edge Cases
* If the linked list has less than two nodes, we simply return the head of the original linked list.

### Returning the Result
* After processing all nodes, we append the odd linked list to the even linked list by setting `even_tail.next = odd_head.next`.
* We then set `odd_tail.next = None` to ensure the odd linked list is properly terminated.
* Finally, we return the `even_head.next` node, which is the head of the resulting linked list with even and odd nodes separated.
```
