# Professor's Analysis: Segregate even and odd Elements in a Linked List

My final answer is: 

## Time Complexity Analysis
* The Big O is O(N), where N is the number of nodes in the linked list.
* The loop runs N times, and the dictionary lookup `if x in dict` takes O(1) time on average.
* Therefore, N * O(1) = O(N).

## Space Complexity Analysis
* The Big O is O(N), where N is the number of nodes in the linked list.
* We use a dictionary/hash map to store at most N elements.

## Step-by-Step Reconstruction Logic
### Step 1: Initialize Variables
* Initialize two dummy nodes, `even_head` and `odd_head`, to serve as the head of the even and odd linked lists, respectively.
* Initialize two pointers, `even` and `odd`, to point to the current even and odd nodes, respectively.
* Initialize a pointer `head` to point to the current node being processed.

### Step 2: Process Nodes
* The loop runs until all nodes in the linked list have been processed.
* In each iteration, check if the current node's value is even or odd.
* If the current node's value is even, set `even.next` to point to the current node, and move the `even` pointer to the next even node.
* If the current node's value is odd, set `odd.next` to point to the current node, and move the `odd` pointer to the next odd node.
* Move the `head` pointer to the next node.

### Step 3: Connect Even and Odd Linked Lists
* Set `even.next` to point to the `odd_head.next` node, effectively connecting the even and odd linked lists.

### Step 4: Terminate Odd Linked List
* Set `odd.next` to `None`, effectively terminating the odd linked list.

### Step 5: Return Result
* Return `even_head.next`, which points to the head of the merged linked list.
