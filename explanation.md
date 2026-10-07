# Professor's Analysis: Segregate even and odd Elements in a Linked List

## Time Complexity Analysis

* The time complexity of this algorithm is O(N), where N is the number of nodes in the linked list.
* The loop runs N times, and the dictionary lookup `if x in dict` takes O(1) time on average.
* Therefore, N * O(1) = O(N).

## Space Complexity Analysis

* The space complexity of this algorithm is O(N), where N is the number of nodes in the linked list.
* We use a dictionary/hash map to store at most N elements.

## Step-by-Step Reconstruction Logic

### Initialize Variables

* Create two dummy nodes `even_head` and `odd_head` to serve as the head of the even and odd linked lists, respectively.
* Initialize `even` and `odd` pointers to `even_head` and `odd_head`, respectively.
* Initialize `current` pointer to `head`, which is the head of the input linked list.

### Loop Through the Linked List

* While `current` pointer is not `None`:
	+ Check if the value of the current node `current.val` is even.
		- If it is even:
			- Set `even.next` to `current`.
			- Move `even` pointer to the next node.
		- If it is odd:
			- Set `odd.next` to `current`.
			- Move `odd` pointer to the next node.
	+ Move `current` pointer to the next node.

### Terminate the Loop

* After the loop, `even.next` and `odd.next` are set to `None`, effectively terminating the even and odd linked lists.

### Return the Even and Odd Linked Lists

* Create `even_list` and `odd_list` by moving the `next` pointer of `even_head` and `odd_head` to the actual head of the even and odd linked lists, respectively.
* Return `even_list` and `odd_list`.

### Edge Case Handling

* If the input linked list is empty, return two empty lists.

Note: This solution assumes that the input linked list has at least one node. If the input linked list is empty, the function will return two empty lists as expected.
