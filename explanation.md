# Professor's Analysis: Segregate even and odd Elements in a Linked List

```
## Time Complexity Analysis
### Big O Notation:
The time complexity of the given Python solution is O(N), where N is the number of nodes in the linked list.

### Explanation:
* The loop runs N times because it iterates over each node in the linked list.
* Inside the loop, the dictionary lookup `if current.val % 2 == 0` takes O(1) time on average because dictionary lookups are constant time operations in Python.
* Therefore, the total time complexity is N * O(1) = O(N).

## Space Complexity Analysis
### Big O Notation:
The space complexity of the given Python solution is O(N).

### Explanation:
* We use a dictionary/hash map to store at most N elements, which are the nodes in the linked list.

## Step-by-Step Reconstruction Logic
### Initialize Variables:
* `even_head` and `odd_head` are initialized as dummy nodes to serve as the head of the even and odd linked lists, respectively.
* `even_tail` and `odd_tail` are initialized as the tail of the even and odd linked lists, respectively.
* `current` is initialized as the head of the input linked list.

### Loop Condition:
* The loop continues as long as `current` is not `None`.

### Loop Body:
* Inside the loop, we check if the value of the current node is even or odd using the modulo operator `%`.
* If the value is even, we add the current node to the even linked list by updating `even_tail.next` and incrementing `even_tail`.
* If the value is odd, we add the current node to the odd linked list by updating `odd_tail.next` and incrementing `odd_tail`.
* We then move on to the next node in the linked list by updating `current` to `current.next`.

### If/Else Logic:
* If the complement (i.e., the node with the value that is not the current node's value) is found in the other linked list, we update the `next` pointer of the tail of the even linked list to point to the head of the odd linked list.
* If the complement is not found, we simply move on to the next node in the linked list.

### Return Statement:
* If no pair is found, we return the `next` node of the `even_head`, which is the head of the even linked list.
```
