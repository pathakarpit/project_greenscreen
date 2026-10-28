# Professor's Analysis: Segregate even and odd Elements in a Linked List

## Time Complexity Analysis
* The loop runs `N` times, where `N` is the number of nodes in the linked list.
* The dictionary lookup `if head.val % 2 == 0` takes `O(1)` time on average.
* Therefore, `N * O(1) = O(N)`.

## Space Complexity Analysis
* The Big O is `O(N)`.
* We use a dictionary/hash map to store at most `N` elements.

## Step-by-Step Reconstruction Logic
* Initialize two dummy nodes `even_head` and `odd_head` with value `0` and set them as the `next` pointer of `even` and `odd` respectively.
* Initialize `even` and `odd` as the current nodes for even and odd numbers.
* **Loop**:
	+ Check if the current node `head` is `None`.
	+ If `head.val % 2 == 0`, it's an even number, so:
		- Set `even.next` as `head` and move `even` to the next node.
	+ If `head.val % 2 != 0`, it's an odd number, so:
		- Set `odd.next` as `head` and move `odd` to the next node.
	+ Move `head` to the next node.
* After the loop, set `even.next` as `odd_head.next` to connect the even nodes to the odd nodes.
* Set `odd.next` as `None` to terminate the odd nodes.
* Return `even_head.next` as the new head of the merged list.
