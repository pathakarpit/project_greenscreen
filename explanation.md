# Professor's Analysis: Segregate even and odd Elements in a Linked List

## Time Complexity Analysis

### O(N) where N is the number of nodes in the linked list

The loop runs N times, as we are iterating through each node in the linked list. The dictionary lookup `if x in dict` is not present in this code, but if it were, it would take O(1) time on average. Therefore, N * O(1) = O(N).

## Space Complexity Analysis

### O(N)

We use a dictionary/hash map to store at most N elements (in this case, we don't use any dictionaries, but we are storing references to nodes in the even and odd lists, so the space complexity is O(N) for storing at most N elements).

## Step-by-Step Reconstruction Logic

### Initialize Variables

* `even_head` and `even_tail` are initialized to `None` to store the head and tail of the even list, respectively.
* `odd_head` and `odd_tail` are initialized to `None` to store the head and tail of the odd list, respectively.
* `current` is initialized to `head` to keep track of the current node.

### Loop Condition

* The loop continues as long as `current` is not `None`.

### Inside the Loop

* If the current node's value is even (`current.val % 2 == 0`):
	+ If `even_head` is `None`, set `even_head` to the current node and `even_tail` to the current node.
	+ Otherwise, set `even_tail.next` to the current node and `even_tail` to the current node.
* If the current node's value is odd:
	+ If `odd_head` is `None`, set `odd_head` to the current node and `odd_tail` to the current node.
	+ Otherwise, set `odd_tail.next` to the current node and `odd_tail` to the current node.
* Move to the next node: `current = current.next`

### After the Loop

* If the even tail is not `None`, set `even_tail.next` to `odd_head`.
* If the odd tail is not `None`, set `odd_tail.next` to `None`.

### Return Statement

* If `even_head` is not `None`, return `even_head` (meaning there are at least one even node).
* Otherwise, return `odd_head` (meaning there are only odd nodes).
