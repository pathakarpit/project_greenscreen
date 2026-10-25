# Professor's Analysis: Segregate even and odd Elements in a Linked List

```
## Time Complexity Analysis

* The loop in the code runs `N` times, where `N` is the number of nodes in the linked list.
* Inside the loop, the dictionary lookup `if x in dict` takes O(1) time on average, because dictionary lookups are constant time operations in Python.
* Therefore, the overall time complexity is N * O(1) = O(N).

## Space Complexity Analysis

* The space complexity is O(N), because we use a dictionary/hash map to store at most N elements.

## Step-by-Step Reconstruction Logic

* Initialize two dummy nodes `even_head` and `odd_head` as the head of the even and odd lists respectively.
* Initialize two pointers `even_tail` and `odd_tail` to point to the tail of the even and odd lists respectively.
* Initialize a pointer `current` to point to the head of the input list.
* Loop through the input list:
	+ If the current node's value is even, add it to the even list:
		- Set `even_tail.next` to the current node.
		- Set `even_tail` to the current node.
	+ If the current node's value is odd, add it to the odd list:
		- Set `odd_tail.next` to the current node.
		- Set `odd_tail` to the current node.
	+ Move the `current` pointer to the next node in the input list.
* After the loop, connect the even list and the odd list:
	+ Set `even_tail.next` to `odd_head.next`.
	+ Set `odd_tail.next` to `None`.
* Return the head of the even list, which is `even_head.next`.
```
