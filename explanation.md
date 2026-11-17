# Professor's Analysis: Segregate even and odd Elements in a Linked List

```
## Time Complexity Analysis
The loop runs N times, where N is the number of nodes in the linked list.
The dictionary lookup if x in dict takes O(1) time on average.
Therefore, N * O(1) = O(N).

## Space Complexity Analysis
The space complexity is O(N), where N is the number of nodes in the linked list.
We use a dictionary/hash map to store at most N elements.

## Step-by-Step Reconstruction Logic
### Step 1: Initialize variables
* Create two dummy nodes even_head and odd_head with next pointers set to None.
* Initialize two pointers even and odd to point to even_head and odd_head, respectively.
* Initialize a current pointer to point to the head of the linked list.

### Step 2: Loop through the linked list
* The loop will run N times, where N is the number of nodes in the linked list.
* Inside the loop:
	+ Check if the current node's value is even (current.val % 2 == 0).
	+ If the value is even:
		- Set even.next to point to the current node.
		- Move even pointer to point to the next node.
	+ If the value is odd:
		- Set odd.next to point to the current node.
		- Move odd pointer to point to the next node.
	+ Move current pointer to point to the next node.

### Step 3: Connect the even and odd lists
* After the loop, set even.next to point to odd_head.next (which is the head of the odd list).
* Set odd.next to None to prevent infinite loops.

### Step 4: Return the new head
* Return even_head.next, which is the new head of the merged list.
```
