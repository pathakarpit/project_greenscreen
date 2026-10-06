# Professor's Analysis: Segregate even and odd Elements in a Linked List

```markdown
## Time Complexity Analysis
* The Big O time complexity is O(N).
* The loop runs N times, where N is the number of nodes in the linked list.
* The dictionary lookup `if x in dict` takes O(1) time on average, as dictionary lookups are constant time operations in Python.
* Therefore, N * O(1) = O(N).

## Space Complexity Analysis
* The Big O space complexity is O(N).
* We use a dictionary/hash map to store at most N elements, where N is the number of nodes in the linked list.

## Step-by-Step Reconstruction Logic
### Step 1: Initialize Variables
* We initialize two pointers, `even_head` and `odd_head`, to `ListNode(0)`, which is a dummy node.
* We initialize two variables, `even` and `odd`, to point to `even_head` and `odd_head`, respectively.
* We initialize a variable `node` to point to the head of the linked list.

### Step 2: Loop through the Linked List
* We enter a while loop that continues until we reach the end of the linked list (`node` becomes `None`).
* Inside the loop, we check if the current node's value is even by using the modulo operator (`node.val % 2 == 0`).
* If the value is even, we link the current node to the `even` list by setting `even.next` to the current node and moving the `even` pointer to the next node.
* If the value is odd, we link the current node to the `odd` list by setting `odd.next` to the current node and moving the `odd` pointer to the next node.
* We move the `node` pointer to the next node in the linked list.

### Step 3: Link the Even and Odd Lists
* After the loop, we link the `even` list to the `odd` list by setting `even.next` to `odd_head.next`.
* We set `odd.next` to `None` to prevent linking the `odd` list to any other nodes.

### Step 4: Return the Result
* We return `even_head.next`, which is the head of the modified linked list.
```
